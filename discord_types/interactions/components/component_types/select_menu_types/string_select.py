from typing import List, Optional

from discord_types.interactions.components.component_types.select_menu_types.select_menu import SelectMenu, SelectOption
from utils.discord_utils.discord_enums import SelectMenuTypes, DiscordComponentTypes


class StringSelect(SelectMenu):
    def __init__(
        self, custom_id: str, options: List[SelectOption],
        placeholder: Optional[str] = None, min_values: Optional[int] = None,
        max_values: Optional[int] = None, disabled: Optional[bool] = None
    ):
        super().__init__(
            DiscordComponentTypes.STRING_SELECT, custom_id, options,
            None, placeholder, min_values, max_values, disabled
        )

        self.type: SelectMenuTypes = SelectMenuTypes.TEXT
        self.options: List[SelectOption] = options
