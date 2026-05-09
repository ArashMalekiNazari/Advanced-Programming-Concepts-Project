from __future__ import annotations
from typing import Optional

from item import Item


class Inventory:
    """Collection of items carried by the player, with a fixed capacity."""

    CAPACITY: int = 3

    def __init__(self):
        self._items: list[Item] = []

    def add_item(self, item: Item) -> bool:
        if len(self._items) >= self.CAPACITY:
            print(f"You can't carry more than {self.CAPACITY} items.")
            return False
        if self.has_item_by_name(item.get_name()):
            print("You already have this item!")
            return False
        self._items.append(item)
        return True

    def remove_item(self, item: Item) -> bool:
        found = self.get_item_by_name(item.get_name())
        if found is None:
            print("You don't have this item!")
            return False
        self._items.remove(found)
        return True

    def get_item_by_name(self, name: str) -> Optional[Item]:
        return next(
            (item for item in self._items if item.get_name().lower() == name.lower()),
            None
        )

    def has_item_by_name(self, name: str) -> bool:
        return self.get_item_by_name(name) is not None

    def get_items(self) -> list[Item]:
        return list(self._items)

    def get_capacity(self) -> int:
        return self.CAPACITY