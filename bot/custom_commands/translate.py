from discord_types.interactions.commands.command import Command
from bot.custom_modals.translate_request import TranslateRequest
from discord_types.responses.response_data.response_data import ResponseData
from utils.discord_utils.decorators import discord_response
from utils.discord_utils.discord_enums import ApplicationCommandTypes


class TranslateCommand(Command):
    name: str = 'Translate'
    description: str = ''

    def __init__(self):
        super().__init__(
            ApplicationCommandTypes.MESSAGE,
            TranslateCommand.name, TranslateCommand.description
        )

    @staticmethod
    @discord_response
    def execute(data, *args, **kwargs) -> ResponseData:
        first_key = list(data['resolved']['messages'].keys())[0]
        message_content = data['resolved']['messages'][first_key]['content']

        return TranslateRequest(message_content)
