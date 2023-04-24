from django.db import models
import math, random

from .interfaces import Fireable
from .projectile import Projectile

class Tank(Fireable):
    angle = models.FloatField()
    power = models.FloatField()

    @classmethod
    def create_tank(cls, terrain):
        # Tank를 생성하는 코드 추가
        x = random.randint(10, 100)
        y = terrain.heights[x]
        tank = cls.objects.create(angle=45, power=45, position = (x,y))
        return tank

    def fire_projectile(self, angle, power):
        size = Projectile._meta.get_field('size').get_default()  # 기본값 가져오기
        velocity = [power * math.cos(math.radians(angle)), power * math.sin(math.radians(angle))]
        return Projectile.objects.create(position=self.position, angle=angle, power=power, size=size, velocity=velocity)