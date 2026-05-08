from location import Location


class CafeCoach(Location):
    """
    The CafeCoach class represents a specific type of location in the game.

    This coach functions as a cafe area that the player can access.
    It is neither locked nor dark when the game starts.
    """

    def __init__(self):
        """
        Constructs the Cafe Coach location with a predefined name,
        description, and initial state.
        The cafe coach is initialized as unlocked and not dark.
        """
        super().__init__(
            "Cafe Coach",
            "This is the cafe coach.",
            False,   # locked?
            False    # dark?
        )
