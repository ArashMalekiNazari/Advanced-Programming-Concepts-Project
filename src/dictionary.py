from __future__ import annotations
from typing import TYPE_CHECKING

from item import Item
from language import Language

if TYPE_CHECKING:
    from player import Player


class Dictionary(Item):
    """
    The Dictionary class represents an item that allows communication
    between the player and French-speaking characters.

    When used, the dictionary enables a French-speaking NPC in the current
    location to understand English.
    """

    def __init__(self):
        super().__init__(
            "Dictionary",
            "A French to English dictionary. You can talk to any French person."
        )

    def use(self, player: Player) -> bool:
        """
        Uses the dictionary in the player's current location.

        If a French-speaking NPC is present, the NPC learns English and
        can understand the player from that point onward.

        :param player: the player using the dictionary
        :return: True if a French-speaking NPC learned English,
                 False if no applicable NPC was found
        """
        for npc in player.get_current_location().get_characters():
            if npc.can_speak(Language.FRENCH):
                npc.add_language(Language.ENGLISH)
                print(f"'{npc.get_name()}' can understand English now!")
                return True

        print("No one here speaks French to use the dictionary!")
        return False