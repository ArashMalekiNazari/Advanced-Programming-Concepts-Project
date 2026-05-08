from __future__ import annotations
from typing import TYPE_CHECKING

from npc import NPC
from language import Language

if TYPE_CHECKING:
    from player import Player


class OldMan(NPC):
    """
    The OldMan class represents a non-player character (NPC)
    who provides helpful information to the player.

    The old man speaks Spanish and gives hints about the
    location of the engine coach.
    """

    def __init__(self):
        """
        Constructs an OldMan character with a predefined name.
        The old man initially speaks Spanish.
        """
        super().__init__("OldMan")
        self.add_language(Language.SPANISH)

    def talk(self, player: "Player") -> str:
        """
        Returns the dialogue spoken by the old man when the player
        interacts with him.

        :param player: the player interacting with the old man
        :return: a hint about the location of the engine coach
        """
        return "The engine coach is at the end of the train"
