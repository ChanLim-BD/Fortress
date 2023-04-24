from django.db import models
import math, random

from .interfaces import Collidable
from .constants import MAX_TARGET_POSITION_X, MIN_TARGET_POSITION_X

class Target(Collidable):
    size = models.IntegerField()

    @classmethod
    def create_targets(cls, terrain, num):
        targets = []
        for i in range(num):
            x = random.randint(MIN_TARGET_POSITION_X, MAX_TARGET_POSITION_X)
            y = terrain.heights[x]
            target = cls.objects.create(size=10, position=(x, y))
            targets.append(target)
        return targets
    
    def get_position(self):
        return (self.position["x"], self.position["y"])

    def check_collision(self, projectile):
        x, y = self.position
        r = self.size / 2
        dist = math.sqrt((projectile.position[0] - x)**2 + (projectile.position[1] - y)**2)
        if dist <= r/2 + projectile.size/2:
            return True
        else:
            return False