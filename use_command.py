from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class UseCommand(Command):
    """
    The UseCommand class represents a command that allows the player
    to use an item from their inventory.

    The effect of using an item depends on the specific item type.
    Executing this command consumes time.
    """

    # The action cost associated with executing this command
    COST: int = 1

    def __init__(self, item_name: str):
        """
        Constructs a UseCommand for a specific item.

        :param item_name: the name of the item to use
        """
        self._item_name = item_name

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the use command.

        Attempts to locate the specified item in the player's
        inventory and applies its effect. If the item cannot be used or
        does not exist, appropriate feedback is shown to the player.
        """
        # find the item by its name
        item = player.get_inventory().get_item_by_name(self._item_name)
        game.handle_action_cost(UseCommand.COST)
        # after applying the cost now we actually use the item
        if item is None:
            print("You don't have a/an " + self._item_name + ".")
            return

        success = item.use(player)

        if not success:
            print("You successfully WASTED your time!\nNothing happened!")
