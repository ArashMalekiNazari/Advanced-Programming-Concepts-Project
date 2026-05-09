from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command
from direction import Direction
from drop_command import DropCommand
from explain_command import ExplainCommand
from help_command import HelpCommand
from inventory_command import InventoryCommand
from look_command import LookCommand
from move_command import MoveCommand
from quit_command import QuitCommand
from status_command import StatusCommand
from take_command import TakeCommand
from talk_command import TalkCommand
from unknown_command import UnknownCommand
from use_command import UseCommand

if TYPE_CHECKING:
    from game import Game


class CommandParser:
    """
    The CommandParser class is responsible for parsing raw user input
    and converting it into executable Command objects.

    It validates commands, extracts command keywords and arguments,
    and returns the appropriate Command instance. If the input is invalid
    or unrecognized, an UnknownCommand is returned.
    """
    # Belong to class
    # single-word commands that require no argument
    NO_ARG_COMMANDS: dict[str, type[Command]] = {
        "look":      LookCommand,
        "inventory": InventoryCommand,
        "help":      HelpCommand,
        "status":    StatusCommand,
        "quit":      QuitCommand,
        "explain":   ExplainCommand,
    }

    # two-word commands that require one argument (e.g. "take wrench") everything but "go"
    ONE_ARG_COMMANDS: dict[str, type[Command]] = {
        "take": TakeCommand,
        "use":  UseCommand,
        "talk": TalkCommand,
        "drop": DropCommand
    }

    def __init__(self, game: Game):
        """
        Constructs a CommandParser with a reference to the game.

        :param game: the current game instance
        """
        self._game = game

    def parse(self, input_str: str) -> Command:
        """
        Parses a full input line entered by the player.

        The input is trimmed, converted to lowercase, and split into parts.
        The first part is treated as the command verb, while subsequent parts
        may act as arguments depending on the command.

        This method always returns a Command object. If the input is invalid,
        empty, or unrecognized, an UnknownCommand is returned.

        :param input_str: the raw input string entered by the player
        :return: a Command corresponding to the parsed input
        """
        # empty or whitespace-only input
        if input_str.strip() == "":
            return UnknownCommand()

        #remove surrounding spaces, split by any whitespace
        # e.g. "go      north" -> parts = ["go", "north"]
        parts = input_str.strip().lower().split()
        verb = parts[0]

        # single-word commands: look, inventory, help, status, quit, explain
        if verb in self.NO_ARG_COMMANDS:
            return self.NO_ARG_COMMANDS[verb]() #creates a new instance each time

        # two-word commands: take, use, talk, drop
        elif verb in self.ONE_ARG_COMMANDS:
            if len(parts) < 2:
                return UnknownCommand()
            return self.ONE_ARG_COMMANDS[verb](parts[1]) #creates a new instance each time with the argument

        # movement: "go <direction>" — separate because argument needs
        # converting from string to Direction enum before passing to MoveCommand
        elif verb == "go":
            if len(parts) < 2:
                return UnknownCommand()
            direction = Direction.from_string(parts[1])
            if direction is None:
                return UnknownCommand()
            return MoveCommand(direction)

        else:
            return UnknownCommand()