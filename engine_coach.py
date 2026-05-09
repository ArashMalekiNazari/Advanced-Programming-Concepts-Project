from location import Location
from win_condition import WinCondition


class EngineCoach(Location, WinCondition):
    """
    The EngineCoach class represents the engine coach location in the game.

    This location starts as dark and contains the main objective required
    to satisfy the game's win condition.
    """

    def __init__(self):
        """
        Constructs the Engine Coach location with a predefined name,
        description, and initial state.
        The engine coach starts unlocked but dark.
        """
        super().__init__(
            "Engine Coach",
            "This is the engine coach. Help the mechanic fix the engine!",
            False,   # locked?
            True     # dark?
        )
        # Indicates whether the engine has been fixed.
        # Since the player will win at this coach we implement WinCondition.
        self._fixed = False

    def fix_engine(self) -> None:
        """Marks the engine as fixed."""
        self._fixed = True

    def is_satisfied(self) -> bool:
        """
        Checks whether the win condition associated with this location
        has been satisfied.

        :return: True if the engine has been fixed, False otherwise
        """
        return self._fixed
