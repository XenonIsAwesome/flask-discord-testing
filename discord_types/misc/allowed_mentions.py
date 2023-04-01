from typing import List

from utils import Serializable
from utils.discord_utils.enums import AllowedMentionType
from utils.discord_utils.types import Snowflake


class AllowedMentions(Serializable):
    def __init__(
        self, parse: List[AllowedMentionType], roles: List[Snowflake],
        users: List[Snowflake], replied_user: bool
    ):
        self.parse = parse
        self.roles = roles
        self.users = users
        self.replied_user = replied_user
