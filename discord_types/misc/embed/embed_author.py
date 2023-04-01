from typing import Optional

from discord_types.misc.user import User
from utils.serializable import Serializable


class EmbedAuthor(Serializable):
    def __init__(
            self, name: Optional[str] = None, url: Optional[str] = None,
            icon_url: Optional[str] = None, proxy_icon_url: Optional[str] = None
    ):
        self.name: Optional[str] = name
        self.url: Optional[str] = url
        self.icon_url: Optional[str] = icon_url
        self.proxy_icon_url: Optional[str] = proxy_icon_url

    @classmethod
    def from_user(cls, user: User) -> 'EmbedAuthor':
        return cls(
            name=user.username,
            icon_url=user.avatar,
        )
