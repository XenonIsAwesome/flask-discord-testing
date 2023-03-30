from typing import List

from discord_interactions import InteractionType

from discord_types.interactions.components.component import Component
from discord_types.interactions.components.component_factory import ComponentFactory
from discord_types.interactions.components.component_types.action_row import ActionRow
from discord_types.interactions.discord_interaction import DiscordInteraction
from utils.discord_utils.discord_enums import DiscordComponentTypes


class ModalSubmit(DiscordInteraction):
    def __init__(self, custom_id: str, components: List[Component]):
        super().__init__(InteractionType.MODAL_SUBMIT)

        self.custom_id: str = custom_id
        self.components: List[Component] = components

    def _parse_answers(self, components: list) -> dict:
        values = {}
        for comp in components:
            if comp['type'] == DiscordComponentTypes.ACTION_ROW:
                values.update(ModalSubmit._parse_answers(comp['components']))
                continue

            values[comp['custom_id'].replace(f'{self.custom_id}_', '')] = comp['value']

        return values

    @staticmethod
    def _parse_components(components):
        parsed_components = []
        for comp in components:
            if comp['type'] == DiscordComponentTypes.ACTION_ROW:
                parsed_data = ActionRow(ModalSubmit._parse_components(comp['components']))
            else:
                parsed_data = ComponentFactory(comp)

            parsed_components.append(parsed_data)
        return parsed_components

    def json(self, keep_nulls: bool = False):
        data = super().json(keep_nulls)
        del data['type']

        return data
