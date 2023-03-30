from typing import List

from discord_interactions import InteractionResponseType

from discord_types.components.component import Component
from discord_types.interactions.responses.response_data.response_data import ResponseData


class Modal(ResponseData):
    def __init__(self, custom_id: str, title: str, components: List[Component]):
        super().__init__(InteractionResponseType.MODAL)

        self.custom_id: str = custom_id
        self.title: str = title
        self.components: List[Component] = components

    def json(self, keep_nulls: bool = False):
        data = super().json(keep_nulls)
        del data['type']

        return data
