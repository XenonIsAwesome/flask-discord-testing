from discord_types.interactions.components.component_types.action_row import ActionRow
from discord_types.interactions.components.component_types.select_menu_types.string_select import StringSelect
from discord_types.interactions.components.component_types.text_input import TextInput
from discord_types.responses.response_data.modals.modal import Modal
from utils.discord_utils.discord_enums import TextInputStyles, SelectMenuTypes


class TranslateRequest(Modal):
    custom_id: str = 'translate_modal'

    def __init__(self, message_content):
        self.__target_language: ActionRow = ActionRow([
            TextInput(
                custom_id=f'{self.custom_id}_target_language',
                style=TextInputStyles.SHORT,
                label='Target Language'
            )
        ])

        self.__lang_select: ActionRow = ActionRow([
            StringSelect(
                custom_id=f'{self.custom_id}_lang_select',

                # TODO: make SelectOption
                options=[{
                    "label": "English",
                    "value": "en",
                    "description": "English",
                    "emoji": {
                        "name": "flag_us",
                        "id": 1089638579359195227
                    }
                }, {
                    "label": "French",
                    "value": "fr",
                    "description": "Français",
                    "emoji": {
                        "name": "flag_fr",
                        "id": 1089638579359195227
                    }
                }],

                placeholder=':earth_americas: Language',
            )]
        )

        self.__translate_textbox: ActionRow = ActionRow([
            TextInput(
                custom_id=f'{self.custom_id}_translate_textbox',
                style=TextInputStyles.PARAGRAPH,
                label='Translate',

                value=message_content
            )]
        )

        super().__init__(
            custom_id=TranslateRequest.custom_id,
            title='Translate',
            components=[
                self.__target_language,
                self.__translate_textbox
            ]
        )
