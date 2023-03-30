from abc import ABC

from discord_interactions import InteractionResponseType

from discord_types.responses.response_data.response_data import ResponseData
from utils.serializeable import Serializable


class DiscordResponse(Serializable):
    def __init__(self, data: ResponseData):
        self.type: InteractionResponseType = data.type
        self.data: ResponseData = data
