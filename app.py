import json
import os

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType, \
    InteractionResponseFlags
from dotenv import load_dotenv
from flask import Flask, request, jsonify

from bot.custom_commands.command_factory import CommandFactory
from discord_types.interactions.responses.interaction_response import DiscordResponse
from discord_types.interactions.responses.response_data.messages.message_types.channel_message_with_source import \
    ChannelMessageWithSource
from utils.discord_utils.command_utils import register_commands, remove_commands, get_commands
from utils.discord_utils.general_utils import format_dict_message, parse_answers

load_dotenv()
app = Flask(__name__)


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(os.getenv('PUBLIC_KEY'))
def interactions_router():
    # IMPORTANT: SLASH COMMAND CASE
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        cmd = CommandFactory(request.json['data']['name'])
        discord_response = cmd.execute(request.json['data'])

        return jsonify(discord_response)

    # TODO: MODAL SUBMIT CASE, add factory
    if request.json['type'] == InteractionType.MODAL_SUBMIT:
        # IMPORTANT: Blank modal submit response example
        # return jsonify({'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE})

        if request.json['data']['custom_id'] == 'translate_modal':
            pass

        # TODO: remove debug modal response
        comp_values = parse_answers(
            request.json['data']['custom_id'],
            request.json['data']['components']
        )

        return jsonify(DiscordResponse(ChannelMessageWithSource(
            content="**Temporary modal submit response:**\n" + format_dict_message(comp_values),
            flags=InteractionResponseFlags.EPHEMERAL
        )).json())

    # TODO: MESSAGE COMPONENT CASE, add factory
    if request.json['type'] == InteractionType.MESSAGE_COMPONENT:
        pass

    # IMPORTANT: PONG CASE (default)
    return jsonify({'type': InteractionResponseType.PONG})


@app.route('/')
def index():
    return 'I\'m alive!'


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
