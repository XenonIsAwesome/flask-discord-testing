from typing import List, Optional

from discord_types.components.component_types.select_menu_types.select_menu import SelectMenu
from discord_types.components.component_types.select_menu_types.select_option import SelectOption
from utils.discord_utils.discord_enums import SelectMenuType, ComponentType


class StringSelect(SelectMenu):
    def __init__(
        self, custom_id: str, options: List[SelectOption],
        placeholder: Optional[str] = None, min_values: Optional[int] = None,
        max_values: Optional[int] = None, disabled: Optional[bool] = None
    ):
        super().__init__(
            ComponentType.STRING_SELECT, custom_id, options,
            None, placeholder, min_values, max_values, disabled
        )

        self.type: SelectMenuType = SelectMenuType.TEXT
        self.options: List[SelectOption] = options
