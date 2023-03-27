from abc import ABC
from dataclasses import dataclass

from discord_interactions import InteractionType
from utils.serializeable import Serializable


@dataclass
class DiscordInteraction(Serializable, ABC):
    type: InteractionType
