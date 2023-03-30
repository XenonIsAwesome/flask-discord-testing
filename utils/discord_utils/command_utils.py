import os
from typing import Dict, Union, Optional
import requests as requests

from discord_types.interactions.commands.command import Command
from bot.custom_commands.test import TestCommand
from bot.custom_commands.translate import TranslateCommand

CommandsDict = Dict[str, Command]


def CommandFactory(name: str) -> Union[CommandsDict, Command]:
    commands = {
        TestCommand.name: TestCommand(),
        TranslateCommand.name: TranslateCommand()
    }

    if name == '*':
        return commands

    return commands.get(name)


def register_command(name: str) -> Dict[str, dict]:
    def register_one(command: Command) -> dict:
        url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/"
        if os.getenv('GUILD_ID'):
            url += f"guilds/{os.getenv('GUILD_ID')}/"
        url += "commands"

        print(url)

        headers = {
            "User-Agent": "DiscordBot (Xenon, 0.1)",
            "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
        }

        body = command.json()

        response = requests.post(url, headers=headers, json=body)
        return response.json()

    cmd = CommandFactory(name)

    if type(cmd) is dict:
        responses = {}
        for k, v in cmd.items():
            responses[k] = register_one(v)
        return responses
    elif type(cmd) is Command:
        return {name: register_one(cmd)}
    return {name: False}


def remove_command(name: str) -> Dict[str, bool]:
    # TODO FIX
    def remove_one(command: Command) -> bool:
        url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/"
        if os.getenv('GUILD_ID'):
            url += f"guilds/{os.getenv('GUILD_ID')}/"
        url += "commands"

        headers = {
            "User-Agent": "DiscordBot (Xenon, 0.1)",
            "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
        }

        response = requests.get(url, headers=headers)
        cmd_json = None

        for cmd_json in response.json():
            if type(cmd_json) == dict and  cmd_json.get('name') == command.name:
                break
            cmd_json = None

        if not cmd_json:
            return False

        response = requests.delete(f"{url}/{cmd_json['id']}", headers=headers)
        return response.status_code == 200

    cmd = CommandFactory(name)
    if type(cmd) is dict:
        responses = {}
        for k, v in cmd.items():
            responses[k] = remove_one(v)
        return responses
    elif type(cmd) is Command:
        return {name: remove_one(cmd)}
    return {name: False}


def get_command(name: str) -> Dict[str, Optional[dict]]:
    def get_one(command: Command) -> Optional[dict]:
        url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/"
        if os.getenv('GUILD_ID'):
            url += f"guilds/{os.getenv('GUILD_ID')}/"
        url += "commands"

        headers = {
            "User-Agent": "DiscordBot (Xenon, 0.1)",
            "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
        }

        response = requests.get(url, headers=headers)

        for cmd_json in response.json():
            if type(cmd_json) == dict and cmd_json.get('name') == command.name:
                return cmd_json
        return None

    cmd = CommandFactory(name)
    if type(cmd) is dict:
        responses = {}
        for k, v in cmd.items():
            responses[k] = get_one(v)
        return responses
    elif type(cmd) is Command:
        return {name: get_one(cmd)}
