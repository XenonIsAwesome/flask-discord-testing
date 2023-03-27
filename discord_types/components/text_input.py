from typing import Optional

from discord_types.components.discord_component import Component
from utils.discord_utils.discord_enums import DiscordComponentTypes, TextInputStyles


# @dataclass
class TextInput(Component):
    def __init__(
        self, custom_id: str, style: TextInputStyles,
        label: str, min_length: int = None,
        max_length: int = None, required: bool = None,
        value: str = None, placeholder: str = None
    ):
        self.type: DiscordComponentTypes = DiscordComponentTypes.TEXT_INPUT

        self.custom_id: str = custom_id
        self.style: TextInputStyles = style
        self.label: str = label

        self.min_length: Optional[int] = min_length
        self.max_length: Optional[int] = max_length
        self.required: Optional[bool] = required
        self.value: Optional[str] = value
        self.placeholder: Optional[str] = placeholder

