from typing import Optional

from utils.serializable import Serializable


class EmbedProvider(Serializable):
    def __init__(self, name: Optional[str] = None, url: Optional[str] = None):
        self.name: Optional[str] = name
        self.url: Optional[str] = url
