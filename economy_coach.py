from location import Location


class EconomyCoach(Location):
    """
    The EconomyCoach class represents the economy coach location in the game.

    This location is accessible to the player and is neither locked nor dark
    when the game starts.
    """

    def __init__(self):
        """
        Constructs the Economy Coach location with a predefined name,
        description, and initial state.
        The economy coach is initialized as unlocked and well-lit.
        """
        super().__init__(
            "Economy Coach",
            "This is the economy coach.",
            False,   # locked?
            False    # dark?
        )
