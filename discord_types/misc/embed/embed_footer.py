from typing import Optional

from utils.serializable import Serializable


class EmbedFooter(Serializable):
    def __init__(
            self, text: Optional[str] = None, icon_url: Optional[str] = None,
            proxy_icon_url: Optional[str] = None
    ):
        self.text: Optional[str] = text
        self.icon_url: Optional[str] = icon_url
        self.proxy_icon_url: Optional[str] = proxy_icon_url
