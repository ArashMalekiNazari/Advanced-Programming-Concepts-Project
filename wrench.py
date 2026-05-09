from __future__ import annotations
from typing import TYPE_CHECKING

from item import Item

if TYPE_CHECKING:
    from player import Player


class Wrench(Item):
    """
    The Wrench class represents an item that can be used to repair machinery.

    This item is specifically required to fix the engine in the Engine Coach,
    which is necessary to satisfy the game's win condition.
    """

    def __init__(self):
        """
        Constructs a Wrench item with a predefined name and description.
        """
        super().__init__(
            "Wrench",
            "A sturdy tool used to tighten bolts and repair machinery."
        )

    def use(self, player: "Player") -> bool:
        """
        Uses the wrench in the player's current location.

        The wrench can only be used effectively in the Engine Coach.
        If used there, it fixes the engine and progresses the game
        toward completion.

        :param player: the player using the wrench
        :return: True if the engine was successfully fixed,
                 False if the wrench had no effect
        """
        # Local import to avoid circular import at module load
        from engine_coach import EngineCoach

        location = player.get_current_location()

        # Only works in Engine Coach
        if isinstance(location, EngineCoach):
            # Fix the engine
            location.fix_engine()
            print("You tighten the bolts carefully with the wrench...")
            print("The engine rumbles back to life! You fixed it!")
            return True

        print("There is nothing here that you can fix with a wrench.")
        return False
