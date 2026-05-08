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
    by the player along with the inventory capacity.
    """

    # The action cost associated with executing this command
    COST: int = 0

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the inventory command.

        Retrieves the player's inventory and prints all items currently
        being carried. If the inventory is empty, an appropriate message
        is displayed.
        """
        inventory = player.get_inventory()
        items = inventory.get_items()

        print("\n======= INVENTORY =======")
        print("Capacity: " + str(len(items)) + " / " + str(inventory.get_capacity()))
        print("--------------------------")

        if len(items) == 0:
            print("Your inventory is empty.")
        else:
            for item in items:
                print("• " + item.get_name())

        print("==========================\n")

        game.handle_action_cost(InventoryCommand.COST)
