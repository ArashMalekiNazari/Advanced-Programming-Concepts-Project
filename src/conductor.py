from __future__ import annotations
from typing import TYPE_CHECKING

from npc import NPC
from language import Language

if TYPE_CHECKING:
    from player import Player


class Conductor(NPC):
    """
    The Conductor class represents a specific non-player character (NPC)
    in the game.

    The conductor can communicate with the player and provides guidance
    about the location of other characters in the train.
    """

    def __init__(self):
        """
        Constructs a Conductor character with a predefined name.
        The conductor is able to speak French.
        """
        super().__init__("Conductor")
        self.add_language(Language.FRENCH)

    def talk(self, player: "Player") -> str:
        """
        Returns the dialogue spoken by the conductor when the player talks
        to them.

        :param player: the player interacting with the conductor
        :return: a message guiding the player further into the game
        """
        return "Welcome. The mechanic is ahead in the engine coach."
