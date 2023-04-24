from django.db import models
import uuid

from .stage_manager import StageManager
from .projectile_manager import ProjectileManager

def generate_unique_id():
    return str(uuid.uuid4().hex)

class Game(models.Model):
    game_id = models.CharField(max_length=32, unique=True, default=generate_unique_id)
    stage_manager = models.OneToOneField(StageManager, on_delete=models.CASCADE)
    projectile_manager = models.OneToOneField(ProjectileManager, on_delete=models.CASCADE)
    is_game_over = models.BooleanField(default=False, null=True)

    @classmethod
    def create_game(cls):
        stage_manager = StageManager.objects.create(current_stage=0)
        stage_manager.create_stages()
        projectile_manager = ProjectileManager.objects.create()
        game_id = generate_unique_id()
        game = cls.objects.create(game_id=game_id, stage_manager=stage_manager, projectile_manager=projectile_manager)
        game.save()
        return game


    def fire_projectile(self, angle, power):
        self.projectile_manager.fire_projectile(self.stage_manager.get_tank(), angle, power)

    def update_projectiles(self, time):
        if self.projectile_manager.update_projectiles(time, self.stage_manager.get_targets(), self.stage_manager.get_terrain()):
            return True
        else:
            return False
        
    def current_stage(self):
        return self.stage_manager.get_current_stage()

    def next_stage(self):
        self.stage_manager.next_stage()
    
    def notice_target(self):
        return self.stage_manager.get_target_positions()

    def notice_last_location(self):
        return self.projectile_manager.get_last_location()