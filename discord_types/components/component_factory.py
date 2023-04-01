from discord_types.components.component_types.action_row import ActionRow
from discord_types.components.component_types.select_menu_types.select_menu import SelectMenu
from discord_types.components.component_types.select_menu_types.string_select import StringSelect
from discord_types.components.component_types.text_input import TextInput
from utils.discord_utils.enums import ComponentType


def ComponentFactory(component_data):
    components = {
        ComponentType.ACTION_ROW: ActionRow,
        # DiscordComponentTypes.BUTTON: None,
        ComponentType.STRING_SELECT: StringSelect,
        ComponentType.TEXT_INPUT: TextInput,
        ComponentType.USER_INPUT: SelectMenu,
        ComponentType.ROLE_SELECT: SelectMenu,
        ComponentType.MENTIONABLE_SELECT: SelectMenu,
        ComponentType.CHANNEL_SELECT: SelectMenu,
    }

    # fixed_data = component_data
    # fixed_data['_type'] = component_data['type']
    # del fixed_data['type']

    component = components[component_data['type']]
    del component_data['type']
    return component(**component_data) if component else None

