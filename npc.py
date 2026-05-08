from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Set, TYPE_CHECKING

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

    # Constructor
    def __init__(self, name: str):
        """
        Constructs an NPC with a given name.

        :param name: the name of the NPC
        """
        self._name = name
        # The set of languages the NPC can speak
        self._languages: Set[Language] = set()

    # Abstract method(s)
    @abstractmethod
    def talk(self, player: "Player") -> str:
        """
        Defines how the NPC talks to the player.
        This behavior must be implemented by subclasses.

        :param player: the player interacting with the NPC
        :return: a dialogue string spoken by the NPC
        """
        pass

    # Getters
    def get_name(self) -> str:
        """Returns the name of the NPC."""
        return self._name

    def can_speak(self, lang: Language) -> bool:
        """
        Checks whether the NPC can speak a given language.

        :param lang: the language to check
        :return: True if the NPC can speak the language, False otherwise
        """
        return lang in self._languages

    def get_languages(self) -> List[Language]:
        """
        Returns a list of languages spoken by the NPC.

        :return: a list of languages
        """
        return list(self._languages)

    # Learn language (after using dictionary)
    def add_language(self, lang: Language) -> None:
        """
        Adds a new language to the NPC's known languages.

        This is typically used when the player enables communication
        using a dictionary or similar item.

        :param lang: the language to add
        """
        self._languages.add(lang)
