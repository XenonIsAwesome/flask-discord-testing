class ApplicationCommandType:
    CHAT_INPUT = 1  # Slash commands; a text-based command that shows up when a user types /
    USER = 2  # A UI-based command that shows up when you right-click or tap on a user
    MESSAGE = 3  # A UI-based command that shows up when you right-click or tap on a message


class ChannelType:
    GUILD_TEXT = 0  # a text channel within a server
    DM = 1  # a direct message between users
    GUILD_VOICE = 2  # a voice channel within a server
    GROUP_DM = 3  # a direct message between multiple users
    GUILD_CATEGORY = 4  # an organizational category that contains up to 50 channels
    GUILD_ANNOUNCEMENT = 5  # a channel that users can follow and cross post into
                            # their own server (formerly news channels)

    ANNOUNCEMENT_THREAD = 6  # a temporary sub-channel within a GUILD_ANNOUNCEMENT channel
    PUBLIC_THREAD = 7  # a temporary sub-channel within a GUILD_TEXT or GUILD_FORUM channel

    PRIVATE_THREAD = 8  # a temporary sub-channel within a GUILD_TEXT channel that is only
                        # viewable by those invited and those with the MANAGE_THREADS permission

    GUILD_STAGE_VOICE = 9  # a voice channel for hosting events with an audience
    GUILD_DIRECTORY = 10  # the channel in a hub containing the listed servers
    GUILD_FORUM = 11  # Channel that can only contain threads


class ComponentType:
    ACTION_ROW = 1  # Container for other components
    BUTTON = 2  # Button object
    STRING_SELECT = 3  # Select menu for picking from defined text options
    TEXT_INPUT = 4  # Text input object
    USER_INPUT = 5  # Select menu for users
    ROLE_SELECT = 6  # Select menu for roles
    MENTIONABLE_SELECT = 7  # Select menu for mentionables (users and roles)
    CHANNEL_SELECT = 8  # Select menu for channels


class TextInputStyle:
    SHORT = 1  # Single-line input
    PARAGRAPH = 2  # Multi-line input


class SelectMenuType:
    TEXT = 3  # Select menu for picking from defined text options
    USER = 5  # Select menu for users
    ROLE = 6  # Select menu for roles
    MENTIONABLE = 7  # Select menu for mentionables (users and roles)
    CHANNELS = 8  # Select menu for channels
