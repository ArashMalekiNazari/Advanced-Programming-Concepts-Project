from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class InventoryCommand(Command):
    """Displays the contents of the player's inventory."""

    COST: int = 0

    def execute(self, player: Player, game: Game) -> None:
        inventory = player.get_inventory()
        items = inventory.get_items()

        print("\n======= INVENTORY =======")
        print(f"Capacity: {len(items)} / {inventory.get_capacity()}")
        print("--------------------------")

        if not items:
            print("Your inventory is empty.")
        else:
            for item in items:
                print(f"• {item.get_name()}")

        print("==========================\n")

        game.handle_action_cost(self.COST)