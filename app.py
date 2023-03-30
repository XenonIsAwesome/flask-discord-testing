import json
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

from discord_types.responses.interaction_response import DiscordResponse
from utils.discord_utils.command_utils import register_command, remove_command, CommandFactory, get_command

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return 'I\'m alive!'


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(os.getenv('PUBLIC_KEY'))
def interactions_router():
    print('request:', json.dumps(request.json, indent=4))
    # SLASH COMMAND CASE
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        cmd = CommandFactory(request.json['data']['name'])
        discord_response = cmd.execute(request.json['data'])
        print('response:', json.dumps(discord_response, indent=4))

        return jsonify(discord_response)

    # MODAL SUBMIT CASE
    if request.json['type'] == InteractionType.MODAL_SUBMIT:
        pass

    # MESSAGE COMPONENT CASE
    if request.json['type'] == InteractionType.MESSAGE_COMPONENT:
        pass

    # PONG CASE (default)
    return jsonify({'type': InteractionResponseType.PONG})


@app.route('/register/<string:name>')
def register(name):
    response = ""
    for n, j in register_command(name).items():
        response += f"<p>{n}: {json.dumps(j, indent=4)}</p><br/>"

    return response


@app.route('/remove/<string:name>')
def remove(name):
    response = ""
    for n, s in remove_command(name).items():
        response += f"<p>{n}: {s}</p><br/>"

    return response


@app.route('/command/<string:name>')
def command(name):
    response = ""
    for n, j in get_command(name).items():
        response += f"<p>{n}: {json.dumps(j, indent=4)}</p><br/>"

    return response


if __name__ == '__main__':
    app.run()
