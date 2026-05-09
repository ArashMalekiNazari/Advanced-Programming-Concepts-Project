from abc import ABC, abstractmethod


class WinCondition(ABC):
    """
    The WinCondition interface represents a condition that determines
    whether the player has won the game.

    Classes implementing this interface define their own logic
    for deciding when the game is considered successfully completed.
    """

    @abstractmethod
    def is_satisfied(self) -> bool:
        """
        Checks whether the win condition has been satisfied.

        :return: True if the win condition is met, False otherwise
        """
        pass
