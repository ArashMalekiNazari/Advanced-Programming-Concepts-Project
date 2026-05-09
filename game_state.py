from enum import Enum


class GameState(Enum):
    """
    The GameState enum represents the possible states of the game.
    The game transitions between these states based on player actions
    and game conditions.
    """
    PLAYING = "PLAYING"   # The game is currently running
    QUIT = "QUIT"         # The player has chosen to quit
    WON = "WON"           # The player has successfully completed the win condition
    LOST = "LOST"         # The player has failed to complete the game in time
