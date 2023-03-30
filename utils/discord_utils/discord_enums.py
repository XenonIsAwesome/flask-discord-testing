class ApplicationCommandTypes:
    CHAT_INPUT = 1  # Slash commands; a text-based command that shows up when a user types /
    USER = 2  # A UI-based command that shows up when you right click or tap on a user
    MESSAGE = 3  # A UI-based command that shows up when you right click or tap on a message


class DiscordComponentTypes:
    ACTION_ROW = 1  # Container for other components
    BUTTON = 2  # Button object
    STRING_SELECT = 3  # Select menu for picking from defined text options
    TEXT_INPUT = 4  # Text input object
    USER_INPUT = 5  # Select menu for users
    ROLE_SELECT = 6  # Select menu for roles
    MENTIONABLE_SELECT = 7  # Select menu for mentionables (users and roles)
    CHANNEL_SELECT = 8  # Select menu for channels


class TextInputStyles:
    SHORT = 1  # Single-line input
    PARAGRAPH = 2  # Multi-line input


class SelectMenuTypes:
    TEXT = 3  # Select menu for picking from defined text options
    USER = 5  # Select menu for users
    ROLE = 6  # Select menu for roles
    MENTIONABLE = 7  # Select menu for mentionables (users and roles)
    CHANNELS = 8  # Select menu for channels
