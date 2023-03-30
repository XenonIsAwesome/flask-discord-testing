import json

from utils.discord_utils.discord_enums import ComponentType

Snowflake = str


def parse_answers(custom_id, components: list) -> dict:
    values = {}
    for comp in components:
        if comp['type'] == ComponentType.ACTION_ROW:
            values.update(parse_answers(custom_id, comp['components']))
            continue

        values[comp['custom_id'].replace(f'{custom_id}_', '')] = comp['value']

    return values


def format_code_message(language, code):
    return f"```{language}\n{code}\n```"


def format_dict_message(json_data: dict):
    return format_code_message('json', json.dumps(json_data, indent=4))
