from __future__ import annotations
from typing import TYPE_CHECKING

from item import Item
from direction import Direction

if TYPE_CHECKING:
    from player import Player


class AccessCard(Item):
    """
    The AccessCard class represents a reusable access card that allows
    the player to temporarily unlock locked coaches.

    Using the access card unlocks an adjacent locked coach, moves the
    player into it immediately, and grants access for a single traversal.
    Once the player exits the coach, it becomes locked again.
    At just 0.5 kg it is the lightest item in the game.
    """

    def __init__(self):
        """
        Constructs an AccessCard with a predefined name, description,
        and physical weight of 0.5 kg.
        """
        super().__init__(
            "AccessCard",
            "You can enter locked coaches by this card.\n"
            "if you use it you can unlock it forever.",
            0.5
        )

    def use(self, player: "Player") -> bool:
        """
        Uses the access card to temporarily unlock a nearby locked coach.

        The card can only be used when the player is not already inside
        a locked coach. If a locked adjacent coach exists, it is unlocked
        temporarily and the player is moved into it immediately.

        :param player: the player using the access card
        :return: True if a locked coach was successfully unlocked
                 and entered, False otherwise
        """
        current = player.get_current_location()

        # Cannot unlock from inside a locked coach
        if current.is_locked():
            print("You are already inside this coach.")
            return False

        for direction in Direction:
            next_loc = current.get_exit(direction)

            if next_loc is not None and next_loc.is_locked():
                next_loc.temporarily_unlock()
                player.move_to(next_loc)

                print("You swipe the Access Card...")
                print("The door unlocks temporarily.")
                print("You enter: " + next_loc.get_name())
                print(next_loc.get_description())

                return True

        print("There is no locked coach here to unlock.")
        return False