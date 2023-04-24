from django.db import models
import math, random

from .interfaces import Collidable
from .constants import TERRAIN_WIDTH, MAX_TERRAIN_HEIGHT, MIN_TERRAIN_HEIGHT


class Terrain(Collidable):
    heights = models.JSONField()

    @classmethod
    # Terrain을 생성하는 코드 추가
    def create_terrain(cls):
        position = 0
        heights = []
        for _ in range(TERRAIN_WIDTH):
            heights.append(random.uniform(MIN_TERRAIN_HEIGHT, MAX_TERRAIN_HEIGHT))
        terrain = cls.objects.create(heights=heights, position=position)
        return terrain

    def check_collision(self, projectile):
        if projectile.position[1] <= self.heights[math.floor(projectile.position[0])]:
            return True
        else:
            return False