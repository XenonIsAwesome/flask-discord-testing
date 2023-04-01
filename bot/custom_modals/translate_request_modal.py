from discord_types.components.component_types.action_row import ActionRow
from discord_types.components.component_types.select_menu_types.select_option import SelectOption
from discord_types.components.component_types.select_menu_types.string_select import StringSelect
from discord_types.components.component_types.text_input import TextInput
from discord_types.interactions.responses.response_data.modals.modal import Modal
from discord_types.misc.emoji import Emoji
from utils.discord_utils.enums import TextInputStyle


class TranslateRequestModal(Modal):
    custom_id: str = 'translate_modal'

    def __init__(self, message_content):
        self.__target_language: ActionRow = ActionRow([
            TextInput(
                custom_id=f'{self.custom_id}_target_language',
                style=TextInputStyle.SHORT,
                label='Target Language'
            )
        ])

        self.__lang_select: ActionRow = ActionRow([
            StringSelect(
                custom_id=f'{self.custom_id}_lang_select',

                options=[
                    SelectOption(
                        label="English",
                        value="en",
                        description="English",
                        emoji=Emoji(
                            name="flag_us",
                            _id="1089638579359195227"
                        )
                    ), SelectOption(
                        label="French",
                        value="fr",
                        description="Français",
                        emoji=Emoji(
                            name="flag_fr",
                            _id="1089638579359195227"
                        )
                    )
                ],

                placeholder=':earth_americas: Language',
            )]
        )

        self.__translate_textbox: ActionRow = ActionRow([
            TextInput(
                custom_id=f'{self.custom_id}_translate_textbox',
                style=TextInputStyle.PARAGRAPH,
                label='Translate',

                value=message_content
            )]
        )

        super().__init__(
            custom_id=TranslateRequestModal.custom_id,
            title='Translate',
            components=[
                self.__target_language,
                self.__translate_textbox
            ]
        )
