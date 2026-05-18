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

    COST: int = 0

    def __init__(self, item_name: str):
        """
        Constructs a DropCommand for a specific item.

        param item_name: the name of the item to drop
        """
        self._item_name = item_name

    def execute(self, player: Player, game: Game) -> None:
        """
        Executes the drop command.

        Attempts to locate the specified item in the player's
        inventory, remove it, and add it to the current location.
        """
        inventory = player.get_inventory()
        target_item = inventory.get_item_by_name(self._item_name)

        if target_item is None:
            print(f"You don't have '{self._item_name}' in your inventory.")
            game.handle_action_cost(DropCommand.COST)
            return

        inventory.remove_item(target_item)
        player.get_current_location().add_item(target_item)
        print(f"You dropped the {target_item.get_name()}.")
        game.handle_action_cost(DropCommand.COST)