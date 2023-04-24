from interfaces import Collidable
from constants import TERRAIN_WIDTH, MAX_TERRAIN_HEIGHT , MIN_TERRAIN_HEIGHT
import math, random


class Terrain(Collidable):
    """발사체가 충돌할 수 있는 지형을 나타냅니다."""
    def __init__(self):
        super().__init__(TERRAIN_WIDTH)
        self.heights = [random.uniform(MIN_TERRAIN_HEIGHT, MAX_TERRAIN_HEIGHT) for _ in range(TERRAIN_WIDTH)]

    def check_collision(self, projectile):
        """발사체가 지형과 충돌하는지 확인합니다."""
        return projectile.get_position()[1] <= self.heights[math.floor(projectile.get_position()[0])]

    def out_of_terrain(self, projectile):
        """발사체가 지형을 벗어난 지 여부를 반환합니다."""
        return projectile.get_position()[0] > TERRAIN_WIDTH
