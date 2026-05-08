from location import Location


class ServiceCoach(Location):
    """
    The ServiceCoach class represents the service coach location in the game.

    This coach starts locked and contains useful tools that can help
    the player progress in the game.
    """

    def __init__(self):
        """
        Constructs the Service Coach location with a predefined name,
        description, and initial state.
        The service coach is initialized as locked but not dark.
        """
        super().__init__(
            "Service Coach",
            "This is the service coach.\nYou can find some tools here!",
            True,    # locked?
            False    # dark?
        )
