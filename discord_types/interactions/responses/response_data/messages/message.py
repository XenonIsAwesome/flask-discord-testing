from typing import Optional, List

from discord_interactions import InteractionResponseFlags
from discord_types.components.component import Component
from discord_types.interactions.responses.response_data.response_data import ResponseData
from discord_types.misc.allowed_mentions import AllowedMentions
from discord_types.misc.attachment import Attachment
from discord_types.misc.embed import Embed
from utils.discord_utils.enums import MessageType


class Message(ResponseData):
    def __init__(
        self, _type: MessageType, tts: Optional[bool] = None,
        content: Optional[str] = None, embeds: Optional[List[Embed]] = None,
        allowed_mentions: Optional[AllowedMentions] = None, flags: Optional[InteractionResponseFlags] = None,
        components: Optional[List[Component]] = None, attachments: Optional[List[Attachment]] = None
    ):
        super().__init__(_type)

        self.tts: Optional[bool] = tts
        self.content: Optional[str] = content
        self.embeds: Optional[List[Embed]] = embeds

        # TODO: make AllowedMentions object
        self.allowed_mentions: Optional[AllowedMentions] = allowed_mentions

        self.flags: Optional[InteractionResponseFlags] = flags
        self.components: Optional[List[Component]] = components
        self.attachments: Optional[List[Attachment]] = attachments
