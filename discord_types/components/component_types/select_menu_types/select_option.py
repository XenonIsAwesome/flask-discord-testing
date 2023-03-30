from typing import Optional

from discord_types.misc.emoji import Emoji
from utils.serializable import Serializable


class SelectOption(Serializable):
    def __init__(
        self, label, value, description: Optional[str] = None,
        emoji: Optional[Emoji] = None, default: Optional[bool] = None
    ):
        self.label: str = label
        self.value: str = value
        self.description: Optional[str] = description
        self.emoji: Optional[Emoji] = emoji
        self.default: Optional[bool] = default
