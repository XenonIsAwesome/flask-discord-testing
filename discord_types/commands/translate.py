from dataclasses import dataclass

from discord_interactions import InteractionResponseType

from discord_types.commands.command import Command
from discord_types.modals.translate_request import TranslateRequest
from utils.discord_utils.discord_enums import ApplicationCommandTypes


@dataclass
class TranslateCommand(Command):
    name: str = 'Translate'
    description: str = ""
    type: ApplicationCommandTypes = ApplicationCommandTypes.MESSAGE

    @staticmethod
    def execute(data, *args, **kwargs) -> dict:
        first_key = list(data['resolved']['messages'].keys())[0]
        message_content = data['resolved']['messages'][first_key]['content']

        return {
            'type': InteractionResponseType.MODAL,
            'data': TranslateRequest(message_content).json()
        }
