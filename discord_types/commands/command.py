from abc import abstractmethod, ABC
from dataclasses import dataclass

from discord_interactions import InteractionType
from utils.discord_enums import ApplicationCommandTypes
from discord_types.discord_request import DiscordInteraction


# @dataclass
class Command(DiscordInteraction):
    name: str
    description: str
    type: ApplicationCommandTypes = InteractionType.APPLICATION_COMMAND

    @staticmethod
    # @abstractmethod
    def execute(*args, **kwargs) -> dict:
        raise NotImplemented
