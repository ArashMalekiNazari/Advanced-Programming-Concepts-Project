from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player


class Item(ABC):
    """
    The Item class represents an abstract item in the game.

    Items can be collected, carried in the inventory, and used by the player
    to interact with the game world. Every item has a physical weight that
    contributes to the player's total carry load.
    """

    def __init__(self, name: str, description: str, weight: float):
        """
        Constructs an Item with a name, description, and physical weight.

        :param name: the name of the item
        :param description: a textual description of the item
        :param weight: the physical weight of the item in kilograms
        """
        self._name = name
        self._description = description
        self._weight = weight

    @abstractmethod
    def use(self, player: Player) -> bool:
        """
        Uses the item.

        The effect of using the item depends on the specific item type
        and is implemented by subclasses.

        :param player: the player using the item
        :return: True if the item had an effect, False otherwise
        """

    # Note: explicit getters are more common in Java.
    # In Python, @property is preferred. They are kept here intentionally
    # to enforce encapsulation in the style of this project.

    def get_name(self) -> str:
        """Returns the name of the item."""
        return self._name

    def get_description(self) -> str:
        """Returns the description of the item."""
        return self._description

    def get_weight(self) -> float:
        """
        Returns the physical weight of the item in kilograms.

        :return: the item's weight
        """
        return self._weight

    def __str__(self) -> str:
        return self._name