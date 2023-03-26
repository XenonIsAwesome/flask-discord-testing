from dataclasses import dataclass

from utils.discord_enums import DiscordComponentTypes
from discord_types.discord_serializeable import DiscordSerializable


@dataclass
class DiscordComponent(DiscordSerializable):
    type: DiscordComponentTypes


