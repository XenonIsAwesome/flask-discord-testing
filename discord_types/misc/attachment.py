from typing import Optional

from utils import Serializable
from utils.discord_utils.types import Snowflake


class Attachment(Serializable):
    def __init__(
            self, _id: Snowflake, filename: str, size: int, url: str, proxy_url: str,
            description: Optional[str] = None, content_type: Optional[str] = None,
            height: Optional[int] = None, width: Optional[int] = None,
            ephemeral: Optional[bool] = None
    ):
        self.id: Snowflake = _id
        self.filename: str = filename
        self.description: Optional[str] = description
        self.content_type: Optional[str] = content_type
        self.size: int = size
        self.url: str = url
        self.proxy_url: str = proxy_url
        self.height: Optional[int] = height
        self.width: Optional[int] = width
        self.ephemeral: Optional[bool] = ephemeral
