from typing import Union, List, Optional

from discord_types.components.component import Component
from discord_types.components.component_types.select_menu_types.select_option import SelectOption
from utils.discord_utils.discord_enums import SelectMenuType, ComponentType

SelectComponent = Union[ComponentType, SelectMenuType]


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




