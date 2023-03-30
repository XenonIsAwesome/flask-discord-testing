from typing import Union, Dict

from bot.custom_commands.test import TestCommand
from bot.custom_commands.message_translate import TranslateMessageCommand
from discord_types.interactions.requests.commands.command import Command

CommandsDict = Dict[str, Command]


def CommandFactory(name: str) -> Union[CommandsDict, Command]:
    commands = {
        TestCommand.name: TestCommand(),
        TranslateMessageCommand.name: TranslateMessageCommand()
    }

    if name == '*':
        return commands

    return commands.get(name)
