from __future__ import annotations
from typing import TYPE_CHECKING

from item import Item

if TYPE_CHECKING:
    from player import Player


class Wrench(Item):
    """A tool used to fix the engine in the Engine Coach."""

    def __init__(self):
        super().__init__(
            "Wrench",
            "A sturdy tool used to tighten bolts and repair machinery."
        )

    def use(self, player: Player) -> bool:
        from engine_coach import EngineCoach

        location = player.get_current_location()

        if isinstance(location, EngineCoach):
            location.fix_engine()
            print("You tighten the bolts carefully with the wrench...")
            print("The engine rumbles back to life! You fixed it!")
            return True

        print("There is nothing here that you can fix with a wrench.")
        return False