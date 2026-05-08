from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command
from game_state import GameState

if TYPE_CHECKING:
    from player import Player
    from game import Game


class QuitCommand(Command):
    """
    The QuitCommand class represents a command that allows the player
    to exit the game.

    When executed, this command changes the game state to QUIT,
    causing the game loop to terminate.
    """

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the quit command.

        Updates the game state to indicate that the player has chosen to quit.
        """
        game.set_game_state(GameState.QUIT)
