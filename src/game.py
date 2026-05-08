from __future__ import annotations

from access_card import AccessCard
from cafe_coach import CafeCoach
from candle import Candle
from command import Command
from command_parser import CommandParser
from conductor import Conductor
from dictionary import Dictionary
from direction import Direction
from economy_coach import EconomyCoach
from engine_coach import EngineCoach
from explain_command import ExplainCommand
from family_coach import FamilyCoach
from game_state import GameState
from help_command import HelpCommand
from mechanic import Mechanic
from old_man import OldMan
from player import Player
from service_coach import ServiceCoach
from win_condition import WinCondition
from wrench import Wrench


class Game:
    """
    The Game class represents the main controller of the game.

    It is responsible for initializing the game world, handling the game loop,
    processing player commands, and managing win/lose conditions.
    """

    def __init__(self):
        """
        Constructs a new Game instance and initializes the game world.
        """
        self._player: Player = None
        self._win_condition: WinCondition = None
        self.setup_world()  # initialize the locations, items, characters and player
        self._command_parser: CommandParser = CommandParser(self)
        self._game_state: GameState = GameState.PLAYING

    def start_game(self) -> None:
        """
        Starts the game by displaying the introduction and entering
        the game loop.
        """
        # Game introduction
        print("Welcome to the Subway Survival Game!")
        print("Press enter to continue...")
        input()
        # explain the game
        explain_command = ExplainCommand()
        explain_command.execute(self._player, self)
        # Commands introduction
        print("Press enter to see the valid commands...")
        input()
        help_command = HelpCommand()
        help_command.execute(self._player, self)
        # going to gameLoop to actually play the game
        self.game_loop()

    def game_loop(self) -> None:
        """
        Runs the main game loop.

        The loop continues while the game state is PLAYING.
        Player commands are read, executed, and checked for win or loss
        conditions.
        """
        while self._game_state == GameState.PLAYING:
            print("================================")
            string_command = input()
            command = self.process_command(string_command)
            command.execute(self._player, self)
            self.check_win()
            self.check_lose()

        if self._game_state == GameState.WON:
            print("You Won!")
        elif self._game_state == GameState.LOST:
            print("You Lost!\nTime is over!")
        elif self._game_state == GameState.QUIT:
            print("You Quit!\nDo you want to try again?")

    def setup_world(self) -> None:
        """
        Sets up the game world.

        This includes creating locations, connecting them,
        placing items and characters, and initializing the player.
        """
        # Create locations
        economy_coach = EconomyCoach()
        family_coach = FamilyCoach()
        cafe_coach = CafeCoach()
        service_coach = ServiceCoach()
        engine_coach = EngineCoach()

        # Connect exits
        # cafe-economy-family-service-engine
        cafe_coach.set_exit(Direction.NORTH, economy_coach)
        economy_coach.set_exit(Direction.SOUTH, cafe_coach)
        economy_coach.set_exit(Direction.NORTH, family_coach)
        family_coach.set_exit(Direction.SOUTH, economy_coach)
        family_coach.set_exit(Direction.NORTH, service_coach)
        service_coach.set_exit(Direction.SOUTH, family_coach)
        service_coach.set_exit(Direction.NORTH, engine_coach)
        engine_coach.set_exit(Direction.SOUTH, service_coach)

        # Items
        # Cafe
        cafe_coach.add_item(AccessCard())
        # Economy
        economy_coach.add_item(Candle())
        # Family
        family_coach.add_item(Dictionary())
        # Service
        service_coach.add_item(Wrench())

        # Characters
        # Economy
        economy_coach.add_npc(OldMan())
        # Service
        service_coach.add_npc(Conductor())
        # Engine
        engine_coach.add_npc(Mechanic())

        # Player setup
        self._player = Player(economy_coach)  # starting point
        # game changer location
        self._win_condition = engine_coach  # since the player will win here

    # for quitting to set the state into QUIT
    def set_game_state(self, game_state: GameState) -> None:
        """
        Sets the current state of the game.

        :param game_state: the new game state
        """
        self._game_state = game_state

    def process_command(self, string_command: str) -> Command:
        """
        Processes a raw command string entered by the player.

        :param string_command: the raw command input
        :return: the parsed Command object
        """
        return self._command_parser.parse(string_command)

    # update time according to the actions
    def handle_action_cost(self, cost: int) -> None:
        """
        Updates the player's remaining time based on an action cost.

        :param cost: the time cost of the action
        """
        self._player.set_time_remaining(self._player.get_time_remaining() - cost)

    def check_win(self) -> None:
        """
        Checks whether the win condition has been satisfied.
        If so, the game state is set to WON.
        """
        win = self._win_condition.is_satisfied()
        if win:
            self._game_state = GameState.WON

    def check_lose(self) -> None:
        """
        Checks whether the player has lost the game.

        The player loses if the remaining time is zero or less.
        """
        if self._player.is_out_of_time():
            self._game_state = GameState.LOST
