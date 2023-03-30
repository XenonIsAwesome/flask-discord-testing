from abc import ABC

from discord_types.interactions.requests.commands.command import Command
from utils.discord_utils.discord_enums import ApplicationCommandType


class UserCommand(Command, ABC):
    def __init__(self, name: str, description: str = ""):
        super().__init__(
            _type=ApplicationCommandType.USER,
            name=name,
            description=description,
        )
