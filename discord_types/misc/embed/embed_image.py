from typing import Optional

from utils.serializable import Serializable


class EmbedImage(Serializable):
    def __init__(
            self, url: Optional[str] = None, proxy_url: Optional[str] = None,
            height: Optional[int] = None, width: Optional[int] = None
    ):
        self.url: Optional[str] = url
        self.proxy_url: Optional[str] = proxy_url
        self.height: Optional[int] = height
        self.width: Optional[int] = width
