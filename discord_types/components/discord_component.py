from dataclasses import dataclass

from utils.discord_utils.discord_enums import DiscordComponentTypes
from utils.serializeable import Serializable


@dataclass
class Component(Serializable):
    type: DiscordComponentTypes


