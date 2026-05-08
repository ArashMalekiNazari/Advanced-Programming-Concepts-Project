from __future__ import annotations
from abc import ABC #for abstract class
from item import Item
from npc import NPC


class Location(ABC):# this means we cannot make instance from this class

    """
    The Location class represents a place in the game world.

    A location can contain items on the ground, non-player characters (NPCs),
    exits to other locations, and properties such as being dark or locked.
    """

    def __init__(self, name: str, description: str, locked: bool, dark: bool):
        """
        Constructs a Location with the given properties.

        param name: the name of the location
        param description: the description of the location
        param locked: whether the location is locked
        param dark: whether the location is dark
        """
        #private attributes, we should not touch them outside this class
        self._name = name
        self._description = description
        self._exits: dict[Direction, Location] = {}
        self._ground_items: list[Item] = []
        self._npcs: list[NPC] = []
        self._dark = dark
        self._locked = locked
        # A temporarily unlocked location will be re-locked automatically
        # once the player leaves it.
        self._temporarily_unlocked = False
        # Indicates whether the location currently has a light source
        self._light = False  # if there is something like flashlight or candle

    # Core actions

    def add_item(self, item: Item) -> None:
        """
        Adds an item to the ground of this location.

        param item: the item to add
        """
        self._ground_items.append(item)


    # since the output of input() is a str, it is better to remove the item by its name not object
    def remove_item_by_name(self, item_name: str) -> None:
        """
        Removes an item from the ground by its name.

        param item_name: the name of the item to remove
        """
        target = self.get_item_by_name(item_name)
        if target is not None:
            self._ground_items.remove(target)




    # avoid searching by the instance's address and instead search by the name
    # of the item (item is equal to another item if they have the same name)
    def get_item_by_name(self, item_name: str) -> Item | None:
        """
        Returns an item from the ground by its name.

        param item_name: the name of the item
        return: the matching item, or None if not found
        """
        for item in self._ground_items:
            if item.get_name().lower() == item_name.lower():
                return item
        return None

    def add_npc(self, npc: NPC) -> None:
        """
        Adds a non-player character to this location.

        :param npc: the NPC to add
        """
        self._npcs.append(npc)

    def enlighten(self) -> None:
        """Illuminates the location by enabling a light source."""
        self._light = True

    # player can see whether the coach is not dark or at least has a light
    def can_see(self) -> bool:
        """
        Checks whether the player can see in this location.

        The player can see if the location is not dark or if a light source
        is present.

        :return: True if the player can see, False otherwise
        """
        return (not self._dark) or self._light

    def unlock(self) -> None:
        """Unlocks the location."""
        self._locked = False

    def temporarily_unlock(self) -> None:
        """
        Temporarily unlocks the location.

        This method unlocks the location for a single traversal.
        Once the player leaves the location, it will be locked again.
        """
        self._temporarily_unlocked = True
        self._locked = False

    def relock(self) -> None:
        """
        Re-locks the location after a temporary unlock.

        This is typically triggered when the player exits
        a temporarily unlocked location.
        """
        self._locked = True
        self._temporarily_unlocked = False

    def is_temporarily_unlocked(self) -> bool:
        """
        Checks whether the location is currently temporarily unlocked.

        :return: True if the location was unlocked temporarily,
                 False otherwise
        """
        return self._temporarily_unlocked

    # for connecting locations
    def set_exit(self, direction: Direction, location: Location) -> None: #since we are in Location class location: Location would cause error
        """
        Sets an exit from this location in a given direction.

        param direction: the direction of the exit
        param location: the destination location
        """
        self._exits[direction] = location

    # Getters

    def get_name(self) -> str:
        """Returns the name of the location."""
        return self._name

    def get_description(self) -> str:
        """Returns the description of the location."""
        return self._description

    def get_exit(self, direction: Direction) -> Optional["Location"]:
        """
        Returns the exit in a given direction.

        :param direction: the direction to move
        :return: the connected location, or None if no exit exists
        """
        return self._exits.get(direction)

    def get_ground_items(self) -> List[Item]:
        """
        Returns a copy of the list of items on the ground.

        :return: a list of ground items
        """
        return list(self._ground_items)  # return copy

    def get_characters(self) -> List[NPC]:
        """
        Returns a copy of the list of characters in this location.

        :return: a list of NPCs
        """
        return list(self._npcs)  # return copy

    def is_locked(self) -> bool:
        """Indicates whether the location is locked."""
        return self._locked

    def is_dark(self) -> bool:
        """Indicates whether the location is dark."""
        return self._dark

    # Display helpers

    def show_ground_items(self) -> str:
        """
        Returns a formatted string listing all items on the ground.

        :return: a string containing ground item names
        """
        ans = ""
        for item in self._ground_items:
            ans += item.get_name() + "\n"
        return ans

    def show_characters(self) -> str:
        """
        Returns a formatted string listing all characters in the location.

        :return: a string containing character names
        """
        ans = ""
        for npc in self._npcs:
            ans += npc.get_name() + "\n"
        return ans

    def show_exits(self) -> str:
        """
        Returns a formatted string listing all exits from this location.

        :return: a string containing exits and their destinations
        """
        ans = ""
        for direction, dest in self._exits.items():
            ans += direction.name + " -> " + dest.get_name() + "\n"
        return ans
