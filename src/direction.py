from __future__ import annotations
from enum import Enum


class Direction(Enum):
    """
    The Direction enum represents the possible movement directions
    available in the game.

    Each direction is associated with a lowercase string value
    that corresponds to user input.
    """
    NORTH = "north"
    SOUTH = "south"
    EAST  = "east"    # wall
    WEST  = "west"    # wall

    @staticmethod
    def from_string(name: str) -> Direction | None:
        """
        Converts a string into a corresponding Direction value.

        :param name: the string representation of a direction
        :return: the matching Direction, or None if no match is found
        """
        try:
            return Direction(name.strip().lower())
        except ValueError:
            return None