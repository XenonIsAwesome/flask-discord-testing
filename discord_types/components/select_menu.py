from dataclasses import dataclass
from typing import Union, List, Optional, Dict

from discord_types.components.discord_component import Component
from utils.discord_utils.discord_enums import SelectMenuTypes

SelectOption = Union[Dict]


@dataclass
class SelectMenu(Component):
    type: SelectMenuTypes
    custom_id: str

    options: Optional[List[SelectOption]]
    channel_types: Optional[List[int]]

    placeholder: Optional[str]
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]


# @dataclass
class StringSelect(SelectMenu):
    options: List[SelectOption]
    type: SelectMenuTypes = SelectMenuTypes.TEXT
    channel_types = None



