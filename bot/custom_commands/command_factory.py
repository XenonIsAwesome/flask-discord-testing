from typing import Union, Dict

from bot.custom_commands.test import TestCommand
from bot.custom_commands.translate import TranslateCommand
from discord_types.interactions.requests.commands.command import Command

CommandsDict = Dict[str, Command]


def CommandFactory(name: str) -> Union[CommandsDict, Command]:
    commands = {
        TestCommand.name: TestCommand(),
        TranslateCommand.name: TranslateCommand()
    }

    if name == '*':
        return commands

    return commands.get(name)
