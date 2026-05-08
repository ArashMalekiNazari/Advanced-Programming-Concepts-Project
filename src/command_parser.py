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

    # VALID COMMANDS
    VALID = {
        "go", "look", "inventory", "help", "take",
        "drop", "talk", "use", "quit", "status", "explain"
    }

    # constructor
    def __init__(self, game: "Game"):
        """
        Constructs a CommandParser with a reference to the game.

        :param game: the current game instance
        """
        self._game = game

    # Parse a full input line (example: "go north")
    # Always returns a Command — even if it's an UnknownCommand.
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
        # if the input was space or enter only with no actual character
        if input_str is None or input_str.strip() == "":
            return UnknownCommand()

        # to delete the redundant spaces from the beginning and last
        input_str = input_str.strip().lower()

        # split the input into parts by space(s) e.g: "go north" or "go      north"
        # -> parts[0] = go, parts[1] = north
        parts = input_str.split()
        verb = parts[0]

        # check if the first part is valid
        if verb not in CommandParser.VALID:
            return UnknownCommand()

        # commands with only one part and no need of object
        if verb == "look":
            return LookCommand()
        if verb == "inventory":
            return InventoryCommand()
        if verb == "help":
            return HelpCommand()
        if verb == "status":
            return StatusCommand()
        if verb == "quit":
            return QuitCommand()
        if verb == "explain":
            return ExplainCommand()

        # commands with two parts like go north, take Wrench
        if verb == "go":
            if len(parts) < 2:
                return UnknownCommand()
            # fromString("north") -> Direction.NORTH
            direction = Direction.from_string(parts[1])
            # if dir was not direction but also not null, fromString gives None
            if direction is None:
                return UnknownCommand()
            return MoveCommand(direction)

        if verb == "take":
            if len(parts) < 2:
                return UnknownCommand()
            return TakeCommand(parts[1])

        if verb == "use":
            if len(parts) < 2:
                return UnknownCommand()
            return UseCommand(parts[1])

        if verb == "talk":
            if len(parts) < 2:
                return UnknownCommand()
            return TalkCommand(parts[1])

        if verb == "drop":
            if len(parts) < 2:
                return UnknownCommand()
            return DropCommand(parts[1])

        # fallback
        return UnknownCommand()
