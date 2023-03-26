from dataclasses import dataclass
from typing import List

from discord_types.components.discord_component import DiscordComponent
from discord_types.discord_serializeable import DiscordSerializable


@dataclass
class DiscordModal(DiscordSerializable):
    custom_id: str
    title: str
    components: List[DiscordComponent]
