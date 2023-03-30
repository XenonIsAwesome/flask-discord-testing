from abc import ABC

from discord_interactions import InteractionType
from utils.serializable import Serializable


class DiscordRequest(Serializable, ABC):
    def __init__(self, _type: InteractionType):
        self.type: InteractionType = _type
