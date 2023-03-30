import json

from discord_types.interactions.modal_submit.modal_submit import ModalSubmit
from discord_types.responses.response_data.messages.message_types.channel_message_with_source import \
    ChannelMessageWithSource
from utils.discord_utils.decorators import discord_response


class TranslateModalSubmit(ModalSubmit):
    custom_id: str = 'translate_modal'

    def __init__(self, custom_id: str, components: list):
        super().__init__(custom_id, components)
        self.__raw_components = components

    @discord_response
    def execute(self, *args, **kwargs):
        return ChannelMessageWithSource(
            content=f"```json\n{json.dumps(self._parse_answers(self.__raw_components), indent=4)}\n```"
        )

