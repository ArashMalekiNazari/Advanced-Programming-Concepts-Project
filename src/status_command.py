from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class StatusCommand(Command):
    """Displays the player's current location, time, and known languages."""

    COST: int = 0

    def execute(self, player: Player, game: Game) -> None:
        loc = player.get_current_location()
        languages = player.get_languages()

        print("\n===== PLAYER STATUS =====")
        print(f"Current Location: {loc.get_name()}")
        print(f"Time Remaining: {player.get_time_remaining()}")

        if not languages:
            print("Languages you can communicate with: (none)")
        else:
            langs = " ".join(str(lang) for lang in languages)
            print(f"Languages you can communicate with: [ {langs} ]")

        print("==========================")
        game.handle_action_cost(self.COST)