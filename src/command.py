from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player
    from game import Game


class Command(ABC):
    """
    The Command interface represents an executable action in the game.

    Every command in the game must implement this interface so that it can
    be executed by the game engine. Commands define actions that affect
    the player or the game state.
    """

    # all the commands need to be executed (activated) so that the game goes on
    @abstractmethod
    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the command. Defines the behavior of the command when it is
        triggered during gameplay.

        param player: the player performing the command
        param game: the game instance in which the command is executed
        """
        pass
