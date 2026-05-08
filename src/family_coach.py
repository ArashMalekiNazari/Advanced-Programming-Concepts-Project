from location import Location


class FamilyCoach(Location):
    """
    The FamilyCoach class represents the family coach location in the game.

    This coach is accessible to the player and is neither locked nor dark
    when the game begins.
    """

    def __init__(self):
        """
        Constructs the Family Coach location with a predefined name,
        description, and initial state.
        The family coach is initialized as unlocked and well-lit.
        """
        super().__init__(
            "Family Coach",
            "This is the family coach.",
            False,   # locked?
            False    # dark?
        )
