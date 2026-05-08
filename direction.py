from enum import Enum


class Direction(Enum):
    """
    The Direction enum represents the possible movement directions
    available in the game.

    Each direction is associated with a lowercase string name that
    corresponds to user input.
    """
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"   # wall
    WEST = "west"   # wall

    @staticmethod
    def from_string(name):
        """
        Converts a string into a corresponding Direction value.
        The input string is trimmed and converted to lowercase before comparison.

        :param name: the string representation of a direction
        :return: the matching Direction, or None if no match is found
        """
        if name is None:
            return None
        name = name.strip().lower()
        for d in Direction:
            if d.value == name:
                return d
        return None
