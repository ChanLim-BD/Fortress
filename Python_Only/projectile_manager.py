from constants import HIT_TARGET, HIT_TERRAIN, OUT_OF_TERRAIN, MOVING
import logging


class ProjectileManager:
    """게임의 발사체 생성, 이동, 충돌 여부를 관리합니다."""
    def __init__(self):
        self.projectile = None
        self.last_location = None
        self.target_index = None
            
    def _check_projectile_target_collision(self, targets):
        """(Private) 발사체와 목표물 간 충돌 여부를 업데이트합니다."""
        for idx, target in enumerate(targets):
            if target.check_collision(self.projectile):
                self.last_location = None
                self.projectile = None
                self.target_index = idx
                return HIT_TARGET
        return None

    def _check_projectile_terrain_collision(self, terrain):
        """(Private) 발사체와 지형 간 충돌 여부를 업데이트합니다."""
        if terrain.check_collision(self.projectile):
            self.last_location = self.projectile.get_position()
            self.projectile = None
            return OUT_OF_TERRAIN
        return None
    
    def _check_out_of_terrain(self, terrain):
        """(Private) 발사체가 지형 외부로 나갔는지 여부를 업데이트합니다."""
        if terrain.out_of_terrain(self.projectile):
            self.last_location = self.projectile.get_position()
            self.projectile = None
            return HIT_TERRAIN
        return None
    
    def fire_projectile(self, tank, angle, power):
        """탱크에서 발사체를 발사합니다."""
        logging.info("발사!")
        print("발사!")
        tank.set_angle_power(angle, power)
        projectile = tank.fire_projectile()
        self.projectile = projectile

    def update_projectiles(self, time):
        """발사체의 위치를 업데이트합니다."""
        self.projectile.update_position(time)

    def check_projectile(self, targets, terrain):
        """발사체의 상태를 확인합니다."""
        # 발사체가 목표물과 충돌하는가?
        target_collision_result = self._check_projectile_target_collision(targets)
        if target_collision_result is not None:
            return target_collision_result
        # 발사체가 지형 밖으로 나갔는가?
        out_of_terrain_result = self._check_out_of_terrain(terrain)
        if out_of_terrain_result is not None:
            return out_of_terrain_result
        # 발사체가 지형과 충돌하는가?
        terrain_collision_result = self._check_projectile_terrain_collision(terrain)
        if terrain_collision_result is not None:
            return terrain_collision_result
        return MOVING
        
    def get_last_location(self):
        """발사체의 마지막 위치 반환"""
        return self.last_location
    
    def get_target_index(self):
        """충돌한 목표물의 인덱스 반환"""
        return self.target_index