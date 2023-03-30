from typing import Union, List, Optional, Dict

from discord_types.interactions.components.component import Component
from utils.discord_utils.discord_enums import SelectMenuTypes, DiscordComponentTypes

SelectOption = Union[Dict]
SelectComponent = Union[DiscordComponentTypes, SelectMenuTypes]


class SelectMenu(Component):
    def __init__(
        self, _type: SelectComponent, custom_id: str, options: Optional[List[SelectOption]] = None,
        channel_types: Optional[List[int]] = None, placeholder: Optional[str] = None, min_values: Optional[int] = None,
        max_values: Optional[int] = None, disabled: Optional[bool] = None
    ):
        super().__init__(_type)

        self.custom_id: str = custom_id

        self.options: Optional[List[SelectOption]] = options
        self.channel_types: Optional[List[int]] = channel_types

        self.placeholder: Optional[str] = placeholder
        self.min_values: Optional[int] = min_values
        self.max_values: Optional[int] = max_values
        self.disabled: Optional[bool] = disabled




