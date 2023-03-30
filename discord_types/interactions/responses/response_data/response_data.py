from discord_interactions import InteractionResponseType

from utils.serializable import Serializable


class ResponseData(Serializable):
    def __init__(self, _type):
        self.type: InteractionResponseType = _type
