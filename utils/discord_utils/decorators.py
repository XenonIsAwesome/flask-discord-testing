from typing import Callable

from discord_types.interactions.responses.interaction_response import DiscordResponse
from discord_types.interactions.responses.response_data.response_data import ResponseData


def discord_response(func: Callable[[dict], ResponseData]):
    def inner(*args, **kwargs):
        rdata = func(*args, **kwargs)
        return DiscordResponse(rdata).json()
    return inner
