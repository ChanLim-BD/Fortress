from stage_objects import StageObjects
from projectile_manager import ProjectileManager
from constants import HIT_TARGET, HIT_TERRAIN,OUT_OF_TERRAIN , STAGE_CLEAR, REMAIN_TARGET, DT

# 전반적인 게임을 진행하는 클래스이기도 하다.

class Stage:
    """스테이지의 상태를 업데이트하고, 탱크에서 발사체를 발사하며, 발사체가 목표물이나 지형과 충돌했는지 확인하고, 충돌 결과에 따라 처리합니다. 
    현재 스테이지의 탱크와 목표물 위치를 반환하고, 마지막으로 발사체의 위치를 반환합니다."""
    def __init__(self):
        self.stageObjects = StageObjects()
        self.projectile_manager = ProjectileManager()

    def _update_projectile_position(self, dt):
        """(Private) 발사체의 위치를 업데이트합니다."""
        self.projectile_manager.update_projectiles(dt)

    def _check_projectile(self):
        """(Private) 발사체가 목표물이나 지형과 충돌했는지 확인합니다."""
        result =  self.projectile_manager.check_projectile(self.stageObjects.get_targets(), self.stageObjects.get_terrain())
        if result == HIT_TARGET:
            return result
        elif result == HIT_TERRAIN:
            return result
        elif result == OUT_OF_TERRAIN:
            return result
        # else:
        #     pass
    
    def _handle_collision(self, collision_result):
        """(Private) 발사체의 충돌 결과에 따라 핸들링합니다."""
        if collision_result == HIT_TERRAIN:
            # 지형과 충돌한 경우
            return HIT_TERRAIN
        elif collision_result == HIT_TARGET:
            # 목표물과 충돌한 경우, 충돌한 목표물을 제거합니다.
            target_index = self.projectile_manager.get_target_index()
            self.stageObjects.remove_target(target_index)
    
            # 남은 목표물이 없으면 스테이지를 클리어한 것이므로 `STAGE_CLEAR`을 반환합니다.
            if not self.stageObjects.get_targets_num():
                return STAGE_CLEAR
            # 목표물이 남아있으면 `REMAIN_TARGET`을 반환합니다.
            else:
                return REMAIN_TARGET
        elif collision_result == OUT_OF_TERRAIN:
            # 발사체가 지형에서 벗어난 경우.
            return OUT_OF_TERRAIN
        else:
            # 발사체가 아직 충돌하지 않음. (== MOVING)
            return False
        
    def fire_projectile(self, angle, power):  
        """현 스테이지의 탱크에서 발사체를 발사합니다."""
        self.projectile_manager.fire_projectile(self.stageObjects.get_tank(), angle, power)
    
    def update_stage(self):
        """현 스테이지의 상태를 업데이트 합니다."""
        while True:
            self._update_projectile_position(DT)
            collision_result = self._check_projectile()
            stage_result = self._handle_collision(collision_result)
            if stage_result:
                return stage_result
     
    def get_tank_position(self):
        """현재 스테이지의 탱크의 위치를 반환합니다."""
        return self.stageObjects.get_tank_position()
    
    def get_target_positions(self):
        """현재 스테이지의 목표물의 위치를 반환합니다."""
        return self.stageObjects.get_target_positions()

    def get_last_location(self):
        """발사체의 마지막 위치를 반환합니다."""
        return self.projectile_manager.get_last_location()