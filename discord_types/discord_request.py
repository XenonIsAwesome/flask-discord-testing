from abc import abstractmethod, ABC
from dataclasses import dataclass

from discord_interactions import InteractionType

from discord_types.discord_serializeable import DiscordSerializable


@dataclass
class DiscordInteraction(DiscordSerializable, ABC):
    type: InteractionType
