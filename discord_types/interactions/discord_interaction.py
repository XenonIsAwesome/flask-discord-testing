from abc import ABC

from discord_interactions import InteractionType
from utils.serializeable import Serializable


class DiscordInteraction(Serializable, ABC):
    def __init__(self, _type: InteractionType):
        self.type: InteractionType = _type
