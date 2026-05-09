from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class TakeCommand(Command):
    """Picks up an item from the current location into the player's inventory."""

    COST: int = 1

    def __init__(self, item_name: str):
        self._item_name = item_name

    def execute(self, player: Player, game: Game) -> None:
        location = player.get_current_location()
        target_item = location.get_item_by_name(self._item_name)

        if target_item is None:
            print(f"There is no item '{self._item_name}' in this location.")
            game.handle_action_cost(self.COST)
            return

        if not player.get_inventory().add_item(target_item):
            print(f"Your inventory is full. You cannot take '{target_item.get_name()}'.")
            game.handle_action_cost(self.COST)
            return

        location.remove_item_by_name(self._item_name)
        print(f"You picked up the {target_item.get_name()}.")
        game.handle_action_cost(self.COST)