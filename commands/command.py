from abc import abstractmethod, ABC
from dataclasses import dataclass

from discord_interactions import InteractionType

from utils.discord_enums import ApplicationCommandTypes


@dataclass
class Command(ABC):
    name: str
    description: str
    type: ApplicationCommandTypes

    @staticmethod
    @abstractmethod
    def execute(*args, **kwargs) -> dict:
        raise NotImplemented

    def json(self):
        json_data = {}

        for attr_key in dir(self):
            attr_val = getattr(self, attr_key)

            if '__' in attr_key:
                continue

            if type(attr_val) not in [int, str, float, bool]:
                continue

            json_data[attr_key] = attr_val

        return json_data

