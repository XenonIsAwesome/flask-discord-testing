from dataclasses import dataclass

from discord_interactions import InteractionResponseType, InteractionResponseFlags
from discord_types.commands.command import Command
from utils.discord_utils.discord_enums import ApplicationCommandTypes


@dataclass
class TestCommand(Command):
    name: str = 'test'
    description: str = 'test command'
    type: ApplicationCommandTypes = ApplicationCommandTypes.CHAT_INPUT

    @staticmethod
    def execute(*args, **kwargs):
        return {
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': 'hello world! (from python)',
                'flags': InteractionResponseFlags.EPHEMERAL
            }
        }


