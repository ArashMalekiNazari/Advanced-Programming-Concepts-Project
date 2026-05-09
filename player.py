from __future__ import annotations


from inventory import Inventory
from language import Language
from location import Location


class Player:
    """
    The Player class represents the player character in the game.

    The player has a current location, limited time, an inventory,
    and a set of languages they can understand.
    """

    def __init__(self, start_location: Location):
        """
        Constructs a Player with a starting location.

        The player starts with a fixed amount of time and
        understands English and Spanish by default.

        param start_location: the starting location of the player
        """
        self._current_location: Location = start_location
        self._time_remaining: int = 30 

        # player can only interact with people knowing English and Spanish
        self._languages: set[Language] = set()
        self._languages: set[Language] = {Language.ENGLISH, Language.SPANISH}

        self._inventory: Inventory = Inventory()

    # Time management
    def is_out_of_time(self) -> bool:
        """
        Checks whether the player has run out of time.

        :return: True if no time remains, False otherwise
        """
        return self._time_remaining <= 0

    # Movement (used by MoveCommand)
    def move_to(self, next_location: Location) -> None:
        """
        Moves the player to a new location.

        If the player leaves a location that was unlocked temporarily,
        that location will be re-locked automatically.

        param next_location: the next location to move to
        """
        # If leaving a temporarily unlocked location, re-lock it
        if self._current_location.is_temporarily_unlocked():
            self._current_location.relock()
            print("The door locks behind you.")

        self._current_location = next_location

    # Language Management
    def can_understand(self, language: Language) -> bool:
        """
        Checks whether the player can understand a given language.

        param language: the language to check
        return: True if the player understands the language, False otherwise
        """
        return language in self._languages



    # Note: explicit getters and setters are more common in Java.
    # However, they are kept here intentionally to enforce encapsulation.

    # Getters

    def get_current_location(self) -> Location:
        """Returns the player's current location."""
        return self._current_location

    def get_time_remaining(self) -> int:
        """Returns the player's remaining time."""
        return self._time_remaining

    def get_languages(self) -> set[Language]:
        """
        Returns a copy of the languages the player understands.

        :return: a set of languages
        """
        return set(self._languages)  # return copy

    def get_inventory(self) -> Inventory:
        """Returns the player's inventory."""
        return self._inventory

    # Setters
    def set_time_remaining(self, time_remaining: int) -> None:
        """
        Sets the player's remaining time.

        param time_remaining: the new remaining time
        """
        self._time_remaining = time_remaining
