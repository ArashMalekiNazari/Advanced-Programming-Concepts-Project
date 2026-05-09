from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command
from direction import Direction

if TYPE_CHECKING:
    from player import Player
    from game import Game


class MoveCommand(Command):
    """Moves the player in a given direction, consuming one action."""

    COST: int = 1

    def __init__(self, direction: Direction):
        self._direction = direction

    def execute(self, player: Player, game: Game) -> None:
        game.handle_action_cost(self.COST)

        if self._direction in (Direction.EAST, Direction.WEST):
            print("There is a wall. You can't go that way.")
            return

        current = player.get_current_location()
        next_loc = current.get_exit(self._direction)

        if next_loc is None:
            print("You can't move in that direction.")
            return

        if next_loc.is_locked():
            print("This coach is locked. You need an Access Card to enter.")
            return

        player.move_to(next_loc)
        print(f"You moved {self._direction.name} and arrive at: {next_loc.get_name()}")
        print(next_loc.get_description())