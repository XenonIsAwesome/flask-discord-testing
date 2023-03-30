from discord_types.interactions.components.component_types.select_menu_types.string_select import StringSelect
from discord_types.interactions.components.component_types.text_input import TextInput
from discord_types.responses.response_data.modals.modal import Modal
from utils.discord_utils.discord_enums import TextInputStyles, SelectMenuTypes


class TranslateRequest(Modal):
    def __init__(self, message_content):
        self.custom_id = 'translate_modal'

        self.__lang_select: StringSelect = StringSelect(
            custom_id=f'{self.custom_id}_lang_select',

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
        )

        self.__translate_textbox = TextInput(
            custom_id=f'{self.custom_id}_translate_textbox',
            style=TextInputStyles.PARAGRAPH,
            label='Translate',

            value=message_content,
        )

        super().__init__(
            custom_id=self.custom_id,
            title='Translate',
            components=[
                {
                    'type': 1,
                    'components': [
                        self.__translate_textbox
                    ]
                }
                # self.__lang_select,
                # self.__translate_textbox
            ]
        )
