from __future__ import annotations
from typing import List, Optional

from item import Item


class Inventory:
    """
    The Inventory class represents the collection of items carried by the player.

    The inventory is weight-based: each item has a weight attribute, and the
    total carried weight cannot exceed MAX_WEIGHT. Duplicate items (by name)
    are also prevented.
    """

    # Maximum total weight the inventory can hold
    MAX_WEIGHT: float = 10.0

    def __init__(self):
        """
        Constructs an empty, weight-limited inventory.
        """
        # The items list is mutated in-place; references to it remain valid.
        self._items: List[Item] = []

    # ------------------------------------------------------------------
    # Weight helpers
    # ------------------------------------------------------------------

    def get_current_weight(self) -> float:
        """
        Returns the total weight of all items currently in the inventory.

        :return: sum of weights of carried items
        """
        return sum(item.get_weight() for item in self._items)

    def get_remaining_weight(self) -> float:
        """
        Returns how much more weight the inventory can still hold.

        :return: MAX_WEIGHT minus current weight
        """
        return Inventory.MAX_WEIGHT - self.get_current_weight()

    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------

    def add_item(self, item: Item) -> bool:
        """
        Adds an item to the inventory if the weight limit allows
        and the item is not already present.

        :param item: the item to add
        :return: True if the item was successfully added, False otherwise
        """
        if self.has_item_by_name(item.get_name()):
            print("You already have this item!")
            return False

        if self.get_current_weight() + item.get_weight() > Inventory.MAX_WEIGHT:
            print(
                f"Too heavy! '{item.get_name()}' weighs {item.get_weight()} kg. "
                f"You can only carry {self.get_remaining_weight():.1f} kg more."
            )
            return False

        self._items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        """
        Removes an item from the inventory by matching its name.

        :param item: the item to remove
        :return: True if the item was removed, False if it was not found
        """
        if not self.has_item_by_name(item.get_name()):
            print("You don't have this item!")
            return False

        for i in range(len(self._items)):
            if self._items[i].get_name().lower() == item.get_name().lower():
                self._items.pop(i)
                return True
        return False

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get_item_by_name(self, item_name: str) -> Optional[Item]:
        """
        Returns an item from the inventory by its name (case-insensitive).

        Uses filter() to locate the matching item, returning None if not found.

        :param item_name: the name of the item to look up
        :return: the matching Item, or None if not found
        """
        return next(
            filter(lambda item: item.get_name().lower() == item_name.lower(), self._items),
            None
        )

    def has_item_by_name(self, name: str) -> bool:
        """
        Checks whether the inventory contains an item with the given name.

        :param name: the name of the item
        :return: True if the item exists in the inventory, False otherwise
        """
        return self.get_item_by_name(name) is not None

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------

    def get_items(self) -> List[Item]:
        """
        Returns a copy of the inventory item list.

        Uses a list comprehension to ensure the internal list cannot be
        modified through the returned reference.

        :return: a shallow copy of the inventory items
        """
        return [item for item in self._items]

    def get_capacity(self) -> float:
        """
        Returns the maximum weight this inventory can hold.

        :return: MAX_WEIGHT
        """
        return Inventory.MAX_WEIGHT