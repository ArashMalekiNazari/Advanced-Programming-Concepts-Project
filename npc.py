from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from language import Language

if TYPE_CHECKING:
    from player import Player


class NPC(ABC):
    """
    The NPC class represents a non-player character in the game.

    NPCs can interact with the player through dialogue and may
    speak one or more languages. This class serves as a base class
    for all specific NPC types.
    """

    def __init__(self, name: str):
        """
        Constructs an NPC with a given name.

        param name: the name of the NPC
        """
        self._name = name
        self._languages: set[Language] = set()

    @abstractmethod
    def talk(self, player: Player) -> str:
        """
        Defines how the NPC talks to the player.
        Must be implemented by subclasses.

        param player: the player interacting with the NPC
        return: a dialogue string spoken by the NPC
        """

    # Note: explicit getters are more common in Java.
    #They are kept here intentionally
    # to enforce encapsulation in the style of this project.

    def get_name(self) -> str:
        """Returns the name of the NPC."""
        return self._name

    def get_languages(self) -> list[Language]:
        """
        Returns a copy of the languages spoken by the NPC.

        return: a list of languages
        """
        return list(self._languages)

    def can_speak(self, lang: Language) -> bool:
        """
        Checks whether the NPC can speak a given language.

        param lang: the language to check
        return: True if the NPC can speak the language, False otherwise
        """
        return lang in self._languages

    def add_language(self, lang: Language) -> None:
        """
        Adds a new language to the NPC's known languages.
        Typically called when the player uses the Dictionary item.

        param lang: the language to add
        """
        self._languages.add(lang)