from bot.custom_modals.translate_request_modal import TranslateRequestModal
from discord_types.interactions.requests.commands.command_types.message_command import MessageCommand
from discord_types.interactions.responses.response_data.response_data import ResponseData
from utils.discord_utils.decorators import discord_response


class TranslateMessageCommand(MessageCommand):
    name: str = 'Translate message'

    def __init__(self):
        super().__init__(TranslateMessageCommand.name)

    @staticmethod
    @discord_response
    def execute(data, *args, **kwargs) -> ResponseData:
        first_key = list(data['resolved']['messages'].keys())[0]
        message_content = data['resolved']['messages'][first_key]['content']

        return TranslateRequestModal(message_content)
