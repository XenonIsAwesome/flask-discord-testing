class DiscordSerializable:
    def json(self):
        # TODO: FIXXXXXXXXXXX
        json_data = {}

        for attr_key in dir(self):
            attr_val = getattr(self, attr_key)

            if '__' in attr_key:
                continue
            if type(attr_val) == list:
                json_data[attr_key] = [x.json() if getattr(x, 'json') else x for x in attr_val]
                continue
            if type(attr_val) == dict:
                json_data[attr_key] = {k: v.json() if getattr(v, 'json') else v for k, v in attr_val.items()}
                continue
            if type(attr_val) not in [int, str, float, bool]:
                continue

            json_data[attr_key] = attr_val

        return json_data
