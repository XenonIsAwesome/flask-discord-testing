from typing import Optional

from discord_types.interactions.components.component import Component
from utils.discord_utils.discord_enums import DiscordComponentTypes, TextInputStyles


class TextInput(Component):
    def __init__(
        self, custom_id: str, style: TextInputStyles, label: str,
        min_length: int = None, max_length: int = None, required: bool = None,
        value: str = None, placeholder: str = None
    ):
        super().__init__(DiscordComponentTypes.TEXT_INPUT)

        self.custom_id: str = custom_id
        self.style: TextInputStyles = style
        self.label: str = label

        self.min_length: Optional[int] = min_length
        self.max_length: Optional[int] = max_length
        self.required: Optional[bool] = required
        self.value: Optional[str] = value
        self.placeholder: Optional[str] = placeholder
