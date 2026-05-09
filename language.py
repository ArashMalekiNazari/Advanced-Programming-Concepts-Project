from enum import Enum


class Language(Enum):
    """
    The Language enum represents the languages that characters
    in the game can speak and understand.

    Languages are used to control communication between the player
    and non-player characters.
    """
    ENGLISH = "ENGLISH"
    FRENCH = "FRENCH"
    SPANISH = "SPANISH"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
