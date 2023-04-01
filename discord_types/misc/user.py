from typing import Optional

from utils import Serializable
from utils.discord_utils.types import Snowflake


class User(Serializable):
    def __init__(
            self, _id: Snowflake, username: str, discriminator: str,
            avatar: Optional[str], accent_color: Optional[int], bot: Optional[bool] = None,
            system: Optional[bool] = None, mfa_enabled: Optional[bool] = None,
            banner: Optional[str] = None, locale: Optional[str] = None,
            verified: Optional[bool] = None, email: Optional[str] = None, flags: Optional[int] = None,
            premium_type: Optional[int] = None, public_flags: Optional[int] = None,
    ):
        # Requires "identify" OAUTH2 scope
        self.id: Snowflake = _id
        self.username: str = username
        self.discriminator: str = discriminator
        self.avatar: Optional[str] = avatar  # the user's avatar hash
        self.bot: Optional[bool] = bot
        self.system: Optional[bool] = system
        self.mfa_enabled: Optional[bool] = mfa_enabled
        self.banner: Optional[str] = banner  # the user's banner hash
        self.accent_color: Optional[int] = accent_color
        self.locale: Optional[str] = locale

        # Requires "email" OAUTH2 scope
        self.verified: Optional[bool] = verified  # whether the email on this account has been verified
        self.email: Optional[str] = email

        # Requires "identify" OAUTH2 scope
        self.flags: Optional[int] = flags
        self.premium_type: Optional[int] = premium_type
        self.public_flags: Optional[int] = public_flags
