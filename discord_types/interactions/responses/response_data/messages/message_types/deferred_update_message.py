from typing import Optional, List

from discord_interactions import InteractionResponseFlags
from discord_types.components.component import Component
from discord_types.interactions.responses.response_data.messages.message import Message
from discord_types.misc.allowed_mentions import AllowedMentions
from discord_types.misc.attachment import Attachment
from discord_types.misc.embed import Embed
from utils.discord_utils.enums import MessageType


class DeferredUpdateMessage(Message):
    def __init__(
        self, tts: Optional[bool] = None, content: Optional[str] = None,
        embeds: Optional[List[Embed]] = None, allowed_mentions: Optional[AllowedMentions] = None,
        flags: Optional[InteractionResponseFlags] = None, components: Optional[List[Component]] = None,
        attachments: Optional[List[Attachment]] = None
    ):
        super().__init__(
            MessageType.DEFERRED_UPDATE_MESSAGE,

            tts, content, embeds, allowed_mentions,
            flags, components, attachments
        )
