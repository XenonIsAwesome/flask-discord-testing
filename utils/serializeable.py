class Serializable:
    @staticmethod
    def __serialize_data(data):
        if type(data) is list:
            return [Serializable.__serialize_data(x) for x in data]

        if type(data) is dict:
            return {
                k: Serializable.__serialize_data(v)
                for k, v in data.items()
            }

        if hasattr(data, 'json') and 'method' in str(type(getattr(data, 'json'))):
            return data.json()

        if type(data) in [int, str, float, bool]:
            return data

        return None

    def json(self, keep_nulls: bool = False):
        json_data = {}
        for k, v in self.__dict__.items():
            if not keep_nulls and v is None:
                continue

            if k.startswith('_') or k.endswith('_'):
                continue

            serialized_data = Serializable.__serialize_data(v)
            if not keep_nulls and serialized_data is None:
                continue

            json_data[k] = serialized_data

        return json_data
