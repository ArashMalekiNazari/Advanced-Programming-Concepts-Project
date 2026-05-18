from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class InventoryCommand(Command):
    """
    The InventoryCommand class represents a command that displays
    the contents of the player's inventory.

    When executed, this command shows the current items carried
    by the player, their individual weights, and the remaining
    carry capacity.
    """

    # The action cost associated with executing this command
    COST: int = 0

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the inventory command.

        Retrieves the player's inventory and prints all items currently
        being carried alongside their weights. Also displays the total
        weight used versus the maximum carry limit.
        """
        inventory = player.get_inventory()
        items = inventory.get_items()

        print("\n======= INVENTORY =======")
        print(f"Weight: {inventory.get_current_weight():.1f} / {inventory.MAX_WEIGHT:.1f} kg  "
              f"(space left: {inventory.get_remaining_weight():.1f} kg)")
        print("--------------------------")

        if len(items) == 0:
            print("Your inventory is empty.")
        else:
            for item in items:
                print(f"• {item.get_name():<14} {item.get_weight():.1f} kg")

        print("==========================\n")

        game.handle_action_cost(InventoryCommand.COST)