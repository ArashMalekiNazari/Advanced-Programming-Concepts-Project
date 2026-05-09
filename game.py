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
        self._player, self._win_condition = self._setup_world()
        self._command_parser = CommandParser(self)
        self._game_state = GameState.PLAYING

    def start_game(self) -> None:
        """
        Starts the game by displaying the introduction and entering
        the game loop.
        """
        print("Welcome to the Subway Survival Game!")
        input("Press enter to continue...")

        ExplainCommand().execute(self._player, self)

        input("Press enter to see the valid commands...")

        HelpCommand().execute(self._player, self)

        self._game_loop()

    def _game_loop(self) -> None:
        """
        Runs the main game loop.

        The loop continues while the game state is PLAYING.
        Player commands are read, executed, and checked for win or loss
        conditions after each action.
        """
        while self._game_state == GameState.PLAYING:
            print("================================")
            command = self._command_parser.parse(input())
            command.execute(self._player, self)
            self._check_win()
            self._check_lose()

        if self._game_state == GameState.WON:
            print("You Won!")
        elif self._game_state == GameState.LOST:
            print("You Lost!\nTime is over!")
        elif self._game_state == GameState.QUIT:
            print("You Quit!\nDo you want to try again?")

    def _setup_world(self) -> tuple[Player, WinCondition]:
        """
        Sets up the game world.

        Creates all locations, connects their exits, places items and
        characters, and returns the player and win condition.

        return: a tuple of (Player, WinCondition)
        """
        # Create locations
        economy_coach = EconomyCoach()
        family_coach  = FamilyCoach()
        cafe_coach    = CafeCoach()
        service_coach = ServiceCoach()
        engine_coach  = EngineCoach()

        # Connect exits: cafe - economy - family - service - engine
        cafe_coach.set_exit(Direction.NORTH,    economy_coach)
        economy_coach.set_exit(Direction.SOUTH, cafe_coach)
        economy_coach.set_exit(Direction.NORTH, family_coach)
        family_coach.set_exit(Direction.SOUTH,  economy_coach)
        family_coach.set_exit(Direction.NORTH,  service_coach)
        service_coach.set_exit(Direction.SOUTH, family_coach)
        service_coach.set_exit(Direction.NORTH, engine_coach)
        engine_coach.set_exit(Direction.SOUTH,  service_coach)

        # Place items in locations
        cafe_coach.add_item(AccessCard())
        economy_coach.add_item(Candle())
        family_coach.add_item(Dictionary())
        service_coach.add_item(Wrench())

        # Place NPCs in locations
        economy_coach.add_npc(OldMan())
        service_coach.add_npc(Conductor())
        engine_coach.add_npc(Mechanic())

        return Player(economy_coach), engine_coach

    def set_game_state(self, game_state: GameState) -> None:
        """
        Sets the current state of the game.

        param game_state: the new game state
        """
        self._game_state = game_state

    def handle_action_cost(self, cost: int) -> None:
        """
        Deducts the action cost from the player's remaining time.

        param cost: the time cost of the action
        """
        self._player.set_time_remaining(self._player.get_time_remaining() - cost)

    def _check_win(self) -> None:
        """Sets game state to WON if the win condition is satisfied."""
        if self._win_condition.is_satisfied():
            self._game_state = GameState.WON

    def _check_lose(self) -> None:
        """Sets game state to LOST if the player has run out of time."""
        if self._player.is_out_of_time():
            self._game_state = GameState.LOST