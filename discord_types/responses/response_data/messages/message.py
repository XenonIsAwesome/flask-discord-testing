# from typing import Union
from typing import Optional, List

from discord_interactions import InteractionResponseType, InteractionResponseFlags
from discord_types.interactions.components.component import Component
from discord_types.responses.response_data.response_data import ResponseData

# MessageType = Union[
#     InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
#     InteractionResponseType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE,
#     InteractionResponseType.DEFERRED_UPDATE_MESSAGE,
#     InteractionResponseType.UPDATE_MESSAGE
# ]


class Message(ResponseData):
    def __init__(
        self, _type: InteractionResponseType, tts: Optional[bool] = None,
        content: Optional[str] = None, embeds: Optional[List['Embed']] = None,
        allowed_mentions: Optional['AllowedMentions'] = None, flags: Optional[InteractionResponseFlags] = None,
        components: Optional[List[Component]] = None, attachments: Optional[List['Attachment']] = None
    ):
        super().__init__(_type)

        self.tts: Optional[bool] = tts
        self.content: Optional[str] = content

        # TODO: make Embed object
        self.embeds: Optional[List['Embed']] = embeds

        # TODO: make AllowedMentions object
        self.allowed_mentions: Optional['AllowedMentions'] = allowed_mentions

        self.flags: Optional[InteractionResponseFlags] = flags
        self.components: Optional[List[Component]] = components

        # TODO: make Attachment object
        self.attachments: Optional[List['Attachment']] = attachments
