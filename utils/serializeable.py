class Serializable:
    @staticmethod
    def __serialize(dir_data: dict):
        for key, value in dir_data.items():
            if '__' in key:
                continue

            if type(value) is list:
                dir_data[key] = [
                    Serializable.__serialize(x)
                    if type(x) is Serializable else x
                    for x in value
                ]
                continue

            if type(value) is dict:
                dir_data[key] = {
                    k: Serializable.__serialize(v)
                    if type(v) is Serializable else v
                    for k, v in value.items()
                }
                continue

            if type(value) not in [int, str, float, bool]:
                continue

            dir_data[key] = value

        return dir_data

    def json(self):
        return self.__serialize({attr: getattr(self, attr) for attr in dir(self)})
