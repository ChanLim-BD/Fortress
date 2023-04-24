from django.db import models
from django.utils import timezone

class GameObject(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.JSONField(default=dict)

class Collidable(GameObject):
    class Meta:
        abstract = True

    def check_collision(self, obj):
        pass

class Fireable(GameObject):
    class Meta:
        abstract = True

    def fire_projectile(self, angle, power):
        pass

class Movable(GameObject):
    class Meta:
        abstract = True

    def update_pos(self, time):
        pass