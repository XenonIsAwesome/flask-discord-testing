from discord_types.interactions.components.component_types.action_row import ActionRow
from discord_types.interactions.components.component_types.select_menu_types.select_menu import SelectMenu
from discord_types.interactions.components.component_types.select_menu_types.string_select import StringSelect
from discord_types.interactions.components.component_types.text_input import TextInput
from utils.discord_utils.discord_enums import DiscordComponentTypes


def ComponentFactory(component_data):
    components = {
        DiscordComponentTypes.ACTION_ROW: ActionRow,
        # DiscordComponentTypes.BUTTON: None,
        DiscordComponentTypes.STRING_SELECT: StringSelect,
        DiscordComponentTypes.TEXT_INPUT: TextInput,
        DiscordComponentTypes.USER_INPUT: SelectMenu,
        DiscordComponentTypes.ROLE_SELECT: SelectMenu,
        DiscordComponentTypes.MENTIONABLE_SELECT: SelectMenu,
        DiscordComponentTypes.CHANNEL_SELECT: SelectMenu,
    }

    # fixed_data = component_data
    # fixed_data['_type'] = component_data['type']
    # del fixed_data['type']

    component = components[component_data['type']]
    del component_data['type']
    return component(**component_data) if component else None

