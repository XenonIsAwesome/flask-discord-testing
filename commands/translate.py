from dataclasses import dataclass

from discord_interactions import InteractionResponseType, InteractionResponseFlags

from commands.command import Command
from utils.discord_enums import ApplicationCommandTypes


@dataclass
class TranslateCommand(Command):
    name: str = 'translate'
    description: str = ""
    type: ApplicationCommandTypes = ApplicationCommandTypes.MESSAGE

    @staticmethod
    def execute(data, *args, **kwargs) -> dict:
        first_key = list(data['resolved']['messages'].keys())[0]

        return {
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': "This asshole said: " + data['resolved']['messages'][first_key]['content'],
                'flags': InteractionResponseFlags.EPHEMERAL
            }
        }
