from __future__ import annotations
from typing import TYPE_CHECKING

from item import Item

if TYPE_CHECKING:
    from player import Player


class Candle(Item):
    """
    The Candle class represents an item that can be used to remove darkness
    from dark coaches.

    When used, the candle is removed from the player's inventory, placed
    in the current location, and may illuminate the coach if it is dark.
    At 1.0 kg it is light enough to carry alongside heavier tools.
    """

    def __init__(self):
        """
        Constructs a Candle item with a predefined name, description,
        and physical weight of 1.0 kg.
        """
        super().__init__(
            "Candle",
            "A candle that helps you see in dark coaches.",
            1.0
        )

    def use(self, player: "Player") -> bool:
        """
        Uses the candle in the player's current location.

        The candle is removed from the player's inventory and added to the
        current location. If the location is dark, it is illuminated and
        the location description is displayed.

        :param player: the player using the candle
        :return: True if the location was dark and successfully illuminated,
                 False if the location was not dark
        """
        location = player.get_current_location()
        # after using candle, the candle is not in inventory
        player.get_inventory().remove_item(self)
        # candle is a ground item in that location
        location.add_item(self)
        # the effect of using candle
        if location.is_dark():
            location.enlighten()
            print("You turned on the Candle. The darkness fades away...")
            print(location.get_description())
            return True  # meaningful action performed

        print("That coach was not dark!")
        return False  # no effect