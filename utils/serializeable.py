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

    def json(self):
        json_data = {}
        for k, v in self.__dict__.items():
            if '_' in k:
                continue
            json_data[k] = Serializable.__serialize_data(v)

        return json_data
