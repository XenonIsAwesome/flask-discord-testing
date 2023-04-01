from typing import Optional

from utils.serializable import Serializable


class EmbedField(Serializable):
    def __init__(
            self, name: Optional[str] = None, value: Optional[str] = None,
            inline: Optional[bool] = None
    ):
        self.name: Optional[str] = name
        self.value: Optional[str] = value
        self.inline: Optional[bool] = inline
