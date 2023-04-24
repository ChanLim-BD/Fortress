from game_ import Game
from user_input import UserInput

import time
import sys
from constants import GAME_CLEAR


class GameController:
    """Game과 UserInput 클래스를 활용하여 게임을 제어하고, 게임을 시작하고 업데이트하며, 게임을 종료하는 기능"""
    
    def __init__(self):
        self.game = Game()
        self.user_input = UserInput()

    def start_game(self):
        """유저의 데이터를 전달하여 게임을 시작합니다."""
        angle, power = self.user_input.receive_input()
        self.game.set_data_for_fire(angle, power)
        
    def update_game(self):
        """게임을 업데이트합니다."""
        if self.game.update_game() == GAME_CLEAR:
            return GAME_CLEAR
            
    def end_game(self):
        """전체 게임 종료"""
        print("Game Clear!")
        time.sleep(10)
        sys.exit()