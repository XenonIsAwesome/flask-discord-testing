from typing import Optional, List

from discord_types.interactions.components.component import Component
from utils.discord_utils.discord_enums import DiscordComponentTypes


class ActionRow(Component):
    def __init__(self, components: Optional[List[Component]] = None):
        super().__init__(DiscordComponentTypes.ACTION_ROW)

        self.components: Optional[List[Component]] = components
