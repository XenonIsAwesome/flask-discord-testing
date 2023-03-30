from discord_interactions import InteractionResponseFlags
from discord_types.interactions.requests.commands.command import Command
from discord_types.interactions.responses.response_data.messages.message_types.channel_message_with_source import ChannelMessageWithSource
from utils.discord_utils.decorators import discord_response
from utils.discord_utils.discord_enums import ApplicationCommandType


class TestCommand(Command):
    name: str = 'test'
    description: str = 'test command'

    def __init__(self):
        super().__init__(
            ApplicationCommandType.CHAT_INPUT,
            TestCommand.name, TestCommand.description
        )

    @staticmethod
    @discord_response
    def execute(*args, **kwargs):
        return ChannelMessageWithSource(
            content='hello world! (from python)',
            flags=InteractionResponseFlags.EPHEMERAL
        )


