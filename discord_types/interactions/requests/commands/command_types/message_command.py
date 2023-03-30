from abc import ABC

from discord_types.interactions.requests.commands.command import Command
from utils.discord_utils.discord_enums import ApplicationCommandType


class MessageCommand(Command, ABC):
    def __init__(self, name: str, description: str = ""):
        super().__init__(
            _type=ApplicationCommandType.MESSAGE,
            name=name,
            description=description,
        )
