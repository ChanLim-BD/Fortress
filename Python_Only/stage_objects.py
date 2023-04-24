from target import Target
from terrain import Terrain
from tank import Tank
from constants import MAX_NUM_TARGET, MIN_NUM_TARGET, MAX_TARGET_POSITION_X, MIN_TARGET_POSITION_X, MAX_TANK_POSITION_X, MIN_TANK_POSITION_X, MAX_TARGET_SIZE, MIN_TARGET_SIZE

import random

class StageObjects:
    """이 코드는 게임 스테이지 안의 객체를 생성하고 관리하는 클래스를 정의합니다.
    게임의 상황을 관리하고 게임의 룰을 구현하는데 사용됩니다."""
    def __init__(self):
        self.terrain = Terrain()
        self.targets = self._create_targets()
        self.tank = self._create_tank()

    def _create_targets(self):
        """(Private) 목표물을 생성합니다."""
        targets = []
        num_targets = random.randint(MIN_NUM_TARGET, MAX_NUM_TARGET)
        for _ in range(num_targets):
            target_x = random.randint(MIN_TARGET_POSITION_X, MAX_TARGET_POSITION_X)
            target_y = self.terrain.heights[target_x]
            target_size = random.randint(MIN_TARGET_SIZE, MAX_TARGET_SIZE)
            targets.append(Target(target_size, (target_x, target_y)))
        return targets

    def _create_tank(self):
        """(Private) 탱크를 생성합니다."""
        tank_x = random.randint(MIN_TANK_POSITION_X, MAX_TANK_POSITION_X)
        tank_y = self.terrain.heights[tank_x]
        return Tank((tank_x, tank_y))

    def get_tank(self):
        """현재 스테이지의 탱크를 반환합니다."""
        return self.tank

    def get_targets(self):
        """현재 스테이지의 목표물을 반환합니다."""
        return self.targets
    
    def get_terrain(self):
        """현재 스테이지의 지형을 반환합니다."""
        return self.terrain
    
    def get_tank_position(self):
        """현재 스테이지의 탱크의 위치를 반환합니다."""
        return self.tank.get_position()
    
    def get_target_positions(self):
        """현재 스테이지의 목표물의 위치들을 반환합니다."""
        return [target.get_position() for target in self.targets]
    
    def remove_target(self, index):
        """현재 스테이지의 발사체와 충돌한 목표물을 제거합니다."""
        del self.targets[index]

    def get_targets_num(self):
        """현재 스테이지의 목표물의 갯수 반환합니다."""
        return len(self.targets)

