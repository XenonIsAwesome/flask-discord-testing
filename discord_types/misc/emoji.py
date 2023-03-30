from typing import List, Optional

from utils.discord_utils.general_utils import Snowflake
from utils.serializable import Serializable


class Emoji(Serializable):
    def __init__(
        self, _id: Optional[Snowflake], name: Optional[str],
        roles: Optional[List[Snowflake]] = None,
        user: Optional['User'] = None, require_colons: Optional[bool] = None,
        managed: Optional[bool] = None, animated: Optional[bool] = None,
        available: Optional[bool] = None
    ):
        self.id: Optional[Snowflake] = _id
        self.name: Optional[str] = name
        self.roles: Optional[List[Snowflake]] = roles

        # TODO: make User object
        self.user: Optional['User'] = user

        self.require_colons: Optional[bool] = require_colons
        self.managed: Optional[bool] = managed
        self.animated: Optional[bool] = animated
        self.available: Optional[bool] = available
        pass
    # {
    #     "id": "41771983429993937",
    #     "name": "LUL",
    #     "roles": ["41771983429993000", "41771983429993111"],
    #     "user": {
    #         "username": "Luigi",
    #         "discriminator": "0002",
    #         "id": "96008815106887111",
    #         "avatar": "5500909a3274e1812beb4e8de6631111",
    #         "public_flags": 131328
    #     },
    #     "require_colons": true,
    #     "managed": false,
    #     "animated": false
    # }
