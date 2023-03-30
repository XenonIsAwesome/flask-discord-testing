from abc import ABC

from discord_types.interactions.requests.commands.command import Command
from utils.discord_utils.discord_enums import ApplicationCommandType


class SlashCommand(Command, ABC):
    def __init__(self, name: str, description: str = None):
        super().__init__(
            _type=ApplicationCommandType.CHAT_INPUT,
            name=name,
            description=description,
        )
