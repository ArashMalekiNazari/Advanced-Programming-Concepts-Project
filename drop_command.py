from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class DropCommand(Command):
    """
    The DropCommand class represents a command that allows the player
    to drop an item from their inventory into the current location.

    This command safely removes the specified item from the player's
    inventory and places it in the current location.
    """

    # The action cost associated with executing this command
    COST: int = 0

    def __init__(self, item_name: str):
        """
        Constructs a DropCommand for a specific item.

        :param item_name: the name of the item to drop
        """
        self._item_name = item_name

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the drop command.

        Attempts to locate the specified item in the player's
        inventory, remove it, and add it to the current location.
        """
        location = player.get_current_location()

        # Find item safely using Inventory API
        target_item = player.get_inventory().get_item_by_name(self._item_name)

        if target_item is None:
            print("There is no item '" + self._item_name + "' in this location.")
            game.handle_action_cost(DropCommand.COST)
            return

        # Try removing from inventory
        dropped = player.get_inventory().remove_item(target_item)
        if not dropped:
            print("Item is still in your inventory, try again")
            game.handle_action_cost(DropCommand.COST)
            return

        # Return item SAFELY using Location API (not list returned by getter!)
        location.add_item(target_item)

        print("You dropped the " + target_item.get_name() + ".")
        game.handle_action_cost(DropCommand.COST)
