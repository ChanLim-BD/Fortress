from django.db import models
import math

from .interfaces import Movable
from .constants import GRAVITY

class Projectile(Movable):
    angle = models.FloatField()
    power = models.FloatField()
    size = models.IntegerField(default=3)  # 기본값 설정
    velocity = models.JSONField(null=False)

    @classmethod
    def create_projectile(cls, position, angle, power, size=None, velocity=None):
        if size is None:
            size = cls._meta.get_field('size').default  # 기본값 가져오기
        if velocity is None:
            velocity = [power * math.cos(math.radians(angle)), power * math.sin(math.radians(angle))]
        projectile = cls.objects.create(
            position=position,
            angle=angle,
            power=power,
            size=size,
            velocity=velocity
        )
        return projectile
    
    def update_pos(self, time):
        x = self.position[0] + self.velocity[0] * time 
        y = self.position[1] + self.velocity[1] * time
        self.velocity[1] -= GRAVITY * time
        self.position = [x, y]