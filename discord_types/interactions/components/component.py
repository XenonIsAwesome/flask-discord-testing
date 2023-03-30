from discord_interactions import InteractionType

from discord_types.interactions.discord_interaction import DiscordInteraction
from utils.discord_utils.discord_enums import DiscordComponentTypes


class Component(DiscordInteraction):
    def __init__(self, _type: DiscordComponentTypes):
        super().__init__(
            InteractionType.MESSAGE_COMPONENT
        )

        self.type: DiscordComponentTypes = _type


