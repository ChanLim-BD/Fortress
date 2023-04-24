from interfaces import Movable
from constants import GRAVITY, PROJECTILE_SIZE
import math

class Projectile(Movable):
    """발사체"""
    def __init__(self, position, angle, power):
        super().__init__(position=position)
        self.angle = angle
        self.power = power
        self.size = PROJECTILE_SIZE
        self.velocity = [power * math.cos(math.radians(self.angle)), power * math.sin(math.radians(self.angle))]

    def update_position(self, time):
        """위치 업데이트"""
        x = self.position[0] + self.velocity[0] * time 
        y = self.position[1] + self.velocity[1] * time
        self.velocity[1] -= GRAVITY * time
        self.position = (x, y)