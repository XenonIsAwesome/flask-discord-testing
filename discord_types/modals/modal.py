from dataclasses import dataclass
from typing import List

from discord_types.components.discord_component import Component
from utils.serializeable import Serializable


@dataclass
class Modal(Serializable):
    custom_id: str
    title: str
    components: List[Component]
