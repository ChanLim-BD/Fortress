from django.db import models

from .terrain import Terrain
from .target import Target
from .tank import Tank

class Stage(models.Model):
    terrain = models.OneToOneField(Terrain, on_delete=models.CASCADE)
    target_x = models.IntegerField()
    target_y = models.IntegerField()
    tank_x = models.IntegerField()
    tank_y = models.IntegerField()
    targets = models.ManyToManyField(Target)
    tank = models.OneToOneField(Tank, on_delete=models.CASCADE)

    @classmethod
    def create_stage(cls, num_targets):
        terrain = Terrain.create_terrain()
        targets = Target.create_targets(terrain, num_targets)
        tank = Tank.create_tank(terrain)
        stage = cls.objects.create(
            terrain=terrain,
            target_x=targets[0].position[0],
            target_y=targets[0].position[1],
            tank_x=tank.position[0],
            tank_y=tank.position[1],
            tank=tank
        )
        stage.targets.set(targets)
        return stage

