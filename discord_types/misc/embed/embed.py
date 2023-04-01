from typing import Optional, List

from discord_types.misc.embed.embed_author import EmbedAuthor
from discord_types.misc.embed.embed_field import EmbedField
from discord_types.misc.embed.embed_footer import EmbedFooter
from discord_types.misc.embed.embed_image import EmbedImage
from discord_types.misc.embed.embed_provider import EmbedProvider
from discord_types.misc.embed.embed_thumbnail import EmbedThumbnail
from discord_types.misc.embed.embed_video import EmbedVideo
from utils.discord_utils.types import ISO8601Timestamp
from utils.serializable import Serializable


class Embed(Serializable):
    def __init__(
            self, title: Optional[str] = None, _type: Optional[str] = None, description: Optional[str] = None,
            url: Optional[str] = None, timestamp: Optional[ISO8601Timestamp] = None,
            color: Optional[int] = None, footer: Optional[EmbedFooter] = None,
            image: Optional[EmbedImage] = None, thumbnail: Optional[EmbedThumbnail] = None,
            video: Optional[EmbedVideo] = None, provider: Optional[EmbedProvider] = None,
            author: Optional[EmbedAuthor] = None, fields: Optional[List[EmbedField]] = None
    ):
        self.title: Optional[str] = title
        self.type: Optional[str] = _type
        self.description: Optional[str] = description
        self.url: Optional[str] = url
        self.timestamp: Optional[ISO8601Timestamp] = timestamp
        self.color: Optional[int] = color
        self.footer: Optional[EmbedFooter] = footer
        self.image: Optional[EmbedImage] = image
        self.thumbnail: Optional[EmbedThumbnail] = thumbnail
        self.video: Optional[EmbedVideo] = video
        self.provider: Optional[EmbedProvider] = provider
        self.author: Optional[EmbedAuthor] = author
        self.fields: Optional[List[EmbedField]] = fields
