from __future__ import annotations
from typing import TYPE_CHECKING

from npc import NPC
from language import Language

if TYPE_CHECKING:
    from player import Player


class Mechanic(NPC):
    """
    The Mechanic class represents a non-player character (NPC)
    responsible for repairing the train engine.

    The mechanic provides information about the broken engine
    and guides the player toward the required solution.
    """

    def __init__(self):
        """
        Constructs a Mechanic character with a predefined name.
        The mechanic initially speaks French.
        """
        super().__init__("Mechanic")
        self.add_language(Language.FRENCH)

    def talk(self, player: "Player") -> str:
        """
        Returns the dialogue spoken by the mechanic when the player
        interacts with them.

        :param player: the player interacting with the mechanic
        :return: a message explaining the engine problem
        """
        return "The engine is broken! If you have a wrench, you can fix it."
