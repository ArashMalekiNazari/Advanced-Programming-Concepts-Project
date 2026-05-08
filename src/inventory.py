from __future__ import annotations
from typing import List, Optional

from item import Item


class Inventory:
    """
    The Inventory class represents the collection of items carried by the player.

    The inventory has a fixed capacity and prevents duplicate items
    based on item names.
    """

    # The maximum number of items the inventory can hold
    CAPACITY: int = 3

    def __init__(self):
        """
        Constructs an empty inventory with a fixed capacity.
        """
        # the items will always reference this list, the list itself will not
        # change but its components will
        self._items: List[Item] = []

    def add_item(self, item: Item) -> bool:
        """
        Adds an item to the inventory if there is available space
        and the item is not already present.

        :param item: the item to add
        :return: True if the item was successfully added, False otherwise
        """
        if len(self._items) >= Inventory.CAPACITY:
            print("you can't have more than " + str(Inventory.CAPACITY) + " items")
            return False
        if self.has_item_by_name(item.get_name()):
            print("You already have this item!")
            return False

        self._items.append(item)
        return True

    # remove Item by an object of that item not by its name
    def remove_item(self, item: Item) -> bool:
        """
        Removes an item from the inventory using the item object.

        :param item: the item to remove
        :return: True if the item was removed,
                 False if the item was not found
        """
        if not self.has_item_by_name(item.get_name()):
            print("You don't have this item!")
            return False

        for i in range(len(self._items)):
            current = self._items[i]
            if current.get_name().lower() == item.get_name().lower():
                self._items.pop(i)
                return True
        return False

    # Getters by name
    def get_item_by_name(self, item_name: str) -> Optional[Item]:
        """
        Returns an item from the inventory by its name.

        :param item_name: the name of the item
        :return: the matching item, or None if not found
        """
        for item in self._items:
            if item.get_name().lower() == item_name.lower():
                return item
        return None

    # Since the identifier of items is their names
    def has_item_by_name(self, name: str) -> bool:
        """
        Checks whether the inventory contains an item with the given name.

        :param name: the name of the item
        :return: True if the item exists in the inventory, False otherwise
        """
        return self.get_item_by_name(name) is not None

    # =================================================
    # get copy of the field(s)
    # does not return the actual list but a copy for encapsulation
    def get_items(self) -> List[Item]:
        """
        Returns a copy of the list of items in the inventory.
        This prevents external modification of the internal list.

        :return: a copy of the inventory items
        """
        return list(self._items)

    def get_capacity(self) -> int:
        """
        Returns the maximum capacity of the inventory.

        :return: the inventory capacity
        """
        return Inventory.CAPACITY
