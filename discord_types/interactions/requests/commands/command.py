from abc import ABC, abstractmethod
from typing import Union

from discord_interactions import InteractionType

from discord_types.interactions.requests.interaction_request import DiscordRequest
from discord_types.interactions.responses.response_data.response_data import ResponseData
from utils.discord_utils.decorators import discord_response
from utils.discord_utils.discord_enums import ApplicationCommandType


ApplicationCommands = Union[InteractionType, ApplicationCommandType]


class Command(DiscordRequest, ABC):
    def __init__(self, _type, name, description):
        super().__init__(InteractionType.APPLICATION_COMMAND)

        self.type: ApplicationCommands = _type
        self.name: str = name
        self.description: str = description

    @staticmethod
    @abstractmethod
    @discord_response
    def execute(*args, **kwargs) -> ResponseData:
        raise NotImplemented
