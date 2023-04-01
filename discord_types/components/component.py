from discord_interactions import InteractionType

from discord_types.interactions.requests.interaction_request import DiscordRequest
from utils.discord_utils.enums import ComponentType


class Component(DiscordRequest):
    def __init__(self, _type: ComponentType):
        super().__init__(
            InteractionType.MESSAGE_COMPONENT
        )

        self.type: ComponentType = _type


