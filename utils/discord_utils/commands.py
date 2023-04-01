import os
from typing import Dict, Optional
import requests as requests

from bot.custom_commands.command_factory import CommandFactory


def construct_base_url():
    url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/"
    if os.getenv('GUILD_ID'):
        url += f"guilds/{os.getenv('GUILD_ID')}/"
    url += "commands"

    return url


def register_commands() -> Dict[str, dict]:
    responses: Dict[str, dict] = {}

    headers = {
        "User-Agent": "DiscordBot (Xenon, 0.1)",
        "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
    }

    for name, cmd in CommandFactory('*').items():
        response = requests.post(construct_base_url(), headers=headers, json=cmd.json())
        responses[name] = response.json()

    return responses


def remove_commands() -> Dict[str, bool]:
    responses: Dict[str, bool] = {}

    headers = {
        "User-Agent": "DiscordBot (Xenon, 0.1)",
        "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
    }

    commands = get_commands()
    for cmd_name, cmd_json in commands.items():
        if not cmd_name:
            continue

        response = requests.delete(f"{construct_base_url()}/{cmd_json.get('id')}", headers=headers)
        responses[cmd_name] = response.status_code == 200

    return responses


def get_commands() -> Dict[str, Optional[dict]]:
    headers = {
        "User-Agent": "DiscordBot (Xenon, 0.1)",
        "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
    }

    response = requests.get(construct_base_url(), headers=headers)

    return {
        cmd_json.get('name'): cmd_json
        for cmd_json in response.json()
        if cmd_json and type(cmd_json) is dict
    }

