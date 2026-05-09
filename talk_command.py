from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class TalkCommand(Command):
    """Talks to an NPC in the current location if a shared language exists."""

    COST: int = 1

    def __init__(self, character_name: str):
        self._character_name = character_name

    def execute(self, player: Player, game: Game) -> None:
        location = player.get_current_location()

        #https://stackoverflow.com/questions/50573100/using-next-on-generator-function
        target = next(
            (c for c in location.get_characters() # generator: loop through all characters
             if c.get_name().lower() == self._character_name.lower()), # filter: name must match
            None # return None if no match found
        )

        if target is None:
            print(f"There is no one named '{self._character_name}' here.")
            game.handle_action_cost(self.COST)
            return

        can_communicate = any(player.can_understand(lang) for lang in target.get_languages())

        if not can_communicate:
            print(f"{target.get_name()} speaks: {target.get_languages()}")
            print(f"You understand: {player.get_languages()}")
            game.handle_action_cost(self.COST)
            return

        print(target.talk(player))
        game.handle_action_cost(self.COST)