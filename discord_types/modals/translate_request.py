from typing import List

from discord_types.components.discord_component import DiscordComponent
from discord_types.components.select_menu import StringSelect
from discord_types.components.text_input import TextInput
from discord_types.modals.modal import DiscordModal
from utils.discord_enums import TextInputStyles, SelectMenuTypes


class TranslateRequest(DiscordModal):
    def __init__(self, message_content):
        self.custom_id: str = 'translate_modal'
        self.title: str = 'Translate'
        self.components: List[DiscordComponent] = [
            StringSelect(
                type=SelectMenuTypes.TEXT,
                custom_id='translate_modal_lang_select',

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

                channel_types=None,
                placeholder=':earth_americas: Language',
                min_values=None,
                max_values=None,
                disabled=None
            ),
            TextInput(
                custom_id='translate_modal_translate_textbox',
                style=TextInputStyles.PARAGRAPH,
                label='Translate',

                min_length=None,
                max_length=None,
                required=None,
                value=message_content,
                placeholder=None
            )
        ]
