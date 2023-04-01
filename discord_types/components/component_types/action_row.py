from typing import Optional, List

from discord_types.components.component import Component
from utils.discord_utils.enums import ComponentType


class ActionRow(Component):
    def __init__(self, components: Optional[List[Component]] = None):
        super().__init__(ComponentType.ACTION_ROW)

        self.components: Optional[List[Component]] = components
