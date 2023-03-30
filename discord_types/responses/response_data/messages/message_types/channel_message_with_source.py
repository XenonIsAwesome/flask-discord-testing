from typing import Optional, List

from discord_interactions import InteractionResponseType, InteractionResponseFlags

from discord_types.interactions.components.component import Component
from discord_types.responses.response_data.messages.message import Message


class ChannelMessageWithSource(Message):
    def __init__(
        self, tts: Optional[bool] = None, content: Optional[str] = None,
        embeds: Optional[List['Embed']] = None, allowed_mentions: Optional['AllowedMentions'] = None,
        flags: Optional[InteractionResponseFlags] = None, components: Optional[List[Component]] = None,
        attachments: Optional[List['Attachment']] = None
    ):
        super().__init__(
            InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,

            tts, content, embeds, allowed_mentions,
            flags, components, attachments
        )
