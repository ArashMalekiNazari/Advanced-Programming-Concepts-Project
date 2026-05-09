from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player


class Item(ABC):
    """
    The Item class represents an abstract item in the game.

    Items can be collected, carried in the inventory, and used by the player
    to interact with the game world.
    """

    def __init__(self, name: str, description: str):
        """
        Constructs an Item with a name and description.

        :param name: the name of the item
        :param description: a textual description of the item
        """
        self._name = name
        self._description = description

    @abstractmethod
    def use(self, player: "Player") -> bool:
        """
        Uses the item.

        The effect of using the item depends on the specific item type
        and is implemented by subclasses.

        :param player: the player using the item
        :return: True if the item had an effect, False otherwise
        """
        pass

    # Getters
    def get_name(self) -> str:
        """Returns the name of the item."""
        return self._name

    def get_description(self) -> str:
        """Returns the description of the item."""
        return self._description

    def __str__(self) -> str:
        return self._name
