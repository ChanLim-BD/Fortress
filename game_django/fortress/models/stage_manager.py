from django.db import models
import random
from .stage import Stage
from .terrain import Terrain
from .target import Target
from .tank import Tank
from .constants import MAX_STAGE_NUM, MAX_NUM_TARGET, MIN_NUM_TARGET

class StageManager(models.Model):
    current_stage = models.IntegerField(default=0)

    def create_stages(self):
        num_stages = MAX_STAGE_NUM
        stages = [Stage.create_stage(random.randint(MIN_NUM_TARGET, MAX_NUM_TARGET)) for _ in range(num_stages)]
        for i, stage in enumerate(stages):
            stage_info = StageInfo.objects.create(
                stage_manager=self,
                number=i,
                terrain=stage.terrain,
                tank=stage.tank,
            )
            stage_info.targets.set(stage.targets.all())
    
    def get_current_stage(self):
        return self.current_stage

    def next_stage(self):
        self.current_stage = self.current_stage + 1
        self.save()

    def get_tank(self):
        return self.stages.all()[self.current_stage].tank
    
    def get_targets(self):
        return self.stages.all()[self.current_stage].targets.all()

    def get_target_positions(self):
        stage = self.stages.all()[self.current_stage]
        return [(target.position[0], target.position[1]) for target in stage.targets.all()]

    def get_terrain(self):
        return self.stages.all()[self.current_stage].terrain
    

class StageInfo(models.Model):
    stage_manager = models.ForeignKey(StageManager, on_delete=models.CASCADE, related_name='stages')
    number = models.IntegerField()
    terrain = models.OneToOneField(Terrain, on_delete=models.CASCADE)
    targets = models.ManyToManyField(Target)
    tank = models.OneToOneField(Tank, on_delete=models.CASCADE)