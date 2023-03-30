import json
import os

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType, \
    InteractionResponseFlags
from dotenv import load_dotenv
from flask import Flask, request, jsonify

from bot.custom_commands.command_factory import CommandFactory
from utils.discord_utils.command_utils import register_commands, remove_commands, get_commands
from utils.discord_utils.general_utils import format_json_message, parse_answers

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return 'I\'m alive!'


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(os.getenv('PUBLIC_KEY'))
def interactions_router():
    # SLASH COMMAND CASE
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        cmd = CommandFactory(request.json['data']['name'])
        discord_response = cmd.execute(request.json['data'])

        return jsonify(discord_response)

    # MODAL SUBMIT CASE
    if request.json['type'] == InteractionType.MODAL_SUBMIT:
        if request.json['data']['custom_id'] == 'translate_modal':
            comp_values = parse_answers(
                request.json['data']['custom_id'],
                request.json['data']['components']
            )

            return jsonify({
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": f"{format_json_message(comp_values)}\n{format_json_message(request.json['data'])}",
                    "flags": InteractionResponseFlags.EPHEMERAL
                }
            })

    # MESSAGE COMPONENT CASE
    if request.json['type'] == InteractionType.MESSAGE_COMPONENT:
        pass

    # PONG CASE (default)
    return jsonify({'type': InteractionResponseType.PONG})


@app.route('/register')
def register_all():
    response = ""
    for n, j in register_commands().items():
        response += f"<p>{n}: {json.dumps(j, indent=4)}</p><br/>"

    return response


@app.route('/remove')
def remove_all():
    response = ""
    for n, s in remove_commands().items():
        response += f"<p>{n}: {s}</p><br/>"

    return response


@app.route('/commands')
def commands():
    response = ""
    for n, j in get_commands().items():
        response += f"<p>{n}: {json.dumps(j, indent=4)}</p><br/>"

    return response


if __name__ == '__main__':
    app.run()
