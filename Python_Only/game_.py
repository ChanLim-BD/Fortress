from stage_manager import StageManager 
from constants import GAME_CLEAR

class Game:
    """ StageManager 클래스를 사용하여 포트리스 게임의 핵심 기능을 구현하는 Game 클래스를 정의"""

    def __init__(self):
        self.stage_manager = StageManager()
        
    def set_data_for_fire(self, angle, power):
        """입력받은 데이터를 현 스테이지에 전달합니다."""
        self.stage_manager.set_data_for_fire(angle, power)

    def update_game(self):
        """ StageManager 클래스를 업데이트하고, 현재 스테이지가 클리어 되었는지를 체크합니다."""
        if self.stage_manager.update_game() == GAME_CLEAR:
            return GAME_CLEAR