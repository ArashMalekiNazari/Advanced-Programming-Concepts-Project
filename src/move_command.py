from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command
from direction import Direction

if TYPE_CHECKING:
    from player import Player
    from game import Game


class MoveCommand(Command):
    """
    The MoveCommand class represents a command that allows the player
    to move from one location to another.

    Movement is restricted by walls, locked locations, and available exits.
    Executing this command consumes time.
    """

    # The action cost associated with moving
    COST: int = 1

    def __init__(self, direction: Direction):
        """
        Constructs a MoveCommand with a specified direction.

        :param direction: the direction to move
        """
        self._direction = direction

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the move command.

        Checks for walls, valid exits, and locked locations
        before moving the player to the next location.
        """
        game.handle_action_cost(MoveCommand.COST)

        # Wall directions
        if self._direction == Direction.EAST or self._direction == Direction.WEST:
            print("There is a wall. You can't go that way.")
            return

        current = player.get_current_location()
        next_loc = current.get_exit(self._direction)

        # No exit
        if next_loc is None:
            print("You can't move in that direction.")
            return

        # if the next coach is locked
        if next_loc.is_locked():
            print("This coach is locked. You need Access Card to enter")
            return

        # Successful movement
        player.move_to(next_loc)
        print("You moved " + self._direction.name + " and arrive at: " + next_loc.get_name())
        print(next_loc.get_description())
