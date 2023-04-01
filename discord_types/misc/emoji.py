from typing import List, Optional

from discord_types.misc.user import User
from utils.discord_utils.types import Snowflake
from utils.serializable import Serializable


class Emoji(Serializable):
    def __init__(
        self, _id: Optional[Snowflake], name: Optional[str],
        roles: Optional[List[Snowflake]] = None,
        user: Optional[User] = None, require_colons: Optional[bool] = None,
        managed: Optional[bool] = None, animated: Optional[bool] = None,
        available: Optional[bool] = None
    ):
        self.id: Optional[Snowflake] = _id
        self.name: Optional[str] = name
        self.roles: Optional[List[Snowflake]] = roles
        self.user: Optional[User] = user
        self.require_colons: Optional[bool] = require_colons
        self.managed: Optional[bool] = managed
        self.animated: Optional[bool] = animated
        self.available: Optional[bool] = available

