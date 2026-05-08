from __future__ import annotations
from typing import TYPE_CHECKING

from command import Command

if TYPE_CHECKING:
    from player import Player
    from game import Game


class TalkCommand(Command):
    """
    The TalkCommand class represents a command that allows the player
    to talk to a non-player character (NPC) in the current location.

    Communication is only successful if the player understands at least
    one language spoken by the target character.
    """

    # The action cost associated with executing this command
    COST: int = 1

    def __init__(self, character_name: str):
        """
        Constructs a TalkCommand for a specific character.

        :param character_name: the name of the character to talk to
        """
        self._character_name = character_name

    def execute(self, player: "Player", game: "Game") -> None:
        """
        Executes the talk command.

        Searches for a character in the current location,
        checks whether communication is possible based on shared languages,
        and displays the character's dialogue if successful.
        """
        location = player.get_current_location()

        # Find the target character
        target = None
        for c in location.get_characters():
            if c.get_name().lower() == self._character_name.lower():
                target = c
                break

        if target is None:
            print("There is no one named '" + self._character_name + "' here.")
            game.handle_action_cost(TalkCommand.COST)
            return

        # Check if player understands ANY language the character can speak
        can_communicate = False
        for lang in target.get_languages():
            if player.can_understand(lang):
                can_communicate = True
                break

        if not can_communicate:
            print(target.get_name() + " speaks these languages: " + str(target.get_languages()))
            print("You can understand these languages: " + str(player.get_languages()))
            game.handle_action_cost(TalkCommand.COST)
            return

        # Successful communication
        print(target.talk(player))
        game.handle_action_cost(TalkCommand.COST)
