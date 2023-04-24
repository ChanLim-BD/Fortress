from stage import Stage
from stage_notice import StageNotice
from constants import STAGE_CLEAR, REMAIN_TARGET, HIT_TERRAIN, OUT_OF_TERRAIN, MAX_STAGE_NUM, GAME_CLEAR, CONTINUE

class StageManager:
    """게임 스테이지들을 관리합니다."""

    def __init__(self):
        """여러 개의 Stage 객체를 생성하고 이를 관리하며, 각 스테이지에서 발사체를 발사하고 업데이트합니다.
        게임이 진행되는 동안 필요한 다양한 함수들을 제공하며, 각 스테이지의 클리어 상황, 탱크와 목표물의 위치 등을 출력합니다."""
        self.stages = {}
        self.current_stage = 1
        self._create_stage(self.current_stage)
        # 현재 스테이지의 탱크와 목표물 위치를 안내합니다.
        StageNotice.tank_position(self.stages[self.current_stage])
        StageNotice.target_positions(self.stages[self.current_stage])

    def _create_stage(self, stage_num):
        """(Private) 새로운 스테이지를 생성합니다."""
        self.stages[stage_num] = Stage()    
    
    def _remove_stage(self, stage_num):
        """(Private) 지정 스테이지를 삭제합니다."""
        del self.stages[stage_num]

    def _next_stage(self):
        """(Private) 다음 단계로 진행합니다."""
        self.current_stage += 1

    def _notice_stage_clear(self):
        """(Private) 스테이지 클리어 안내합니다."""
        StageNotice.stage_clear(self.current_stage)

    def _notice_last_location(self):
        """(Private) 원활한 게임 진행을 위한 현 스테이지의 발사체 마지막 위치를 알립니다."""
        StageNotice.last_location(self.stages[self.current_stage])

    def _notice_tank(self):
        """(Private) 원활한 게임 진행을 위한 현 스테이지의 탱크 위치를 알립니다."""
        StageNotice.tank_position(self.stages[self.current_stage])

    def _notice_target(self):
        """(Private) 원활한 게임 진행을 위한 현 스테이지의 목표물 위치를 알립니다."""
        StageNotice.target_positions(self.stages[self.current_stage])

    def _check_game_end(self):
        """(Private) N단계 클리어 이후라면 종료합니다."""
        if self.current_stage > MAX_STAGE_NUM:
            return GAME_CLEAR
        else:
            return CONTINUE
        
    def _handle_stage_clear(self):
        """(Private) 스테이지 클리어 처리를 합니다."""
        self._notice_stage_clear()
        self._remove_stage(self.current_stage)
        self._next_stage()
        
        if self._check_game_end():
            return GAME_CLEAR
        else:
            self._create_stage(self.current_stage)
            self._notice_tank()
            self._notice_target()

    def _handle_remaining_targets(self):
        """(Private) 남은 목표물를 안내합니다."""
        self._notice_target()

    def _handle_terrain(self):
        """(Private) 지형 충돌 또는 지형 벗어난 상황의 처리를 합니다."""
        self._notice_last_location()
        self._notice_target()    

    def set_data_for_fire(self, angle, power):
        """현 스테이지에서 발사체의 초기 조건을 설정합니다. (angle, power)"""
        self.stages[self.current_stage].fire_projectile(angle, power)

    def update_game(self):
        """게임을 업데이트 합니다."""
        result = self.stages[self.current_stage].update_stage()

        if result == STAGE_CLEAR:
            return self._handle_stage_clear()
        elif result == REMAIN_TARGET:
            self._handle_remaining_targets()
        elif result == HIT_TERRAIN:
            self._handle_terrain()
        elif result == OUT_OF_TERRAIN:
            self._handle_terrain()
