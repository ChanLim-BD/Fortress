from django.db import models

class ProjectileManager(models.Model):
    projectiles = models.JSONField(default=list)
    last_location = models.JSONField(default=list)  
    position = models.JSONField(default=list)  

    def fire_projectile(self, tank, angle, power):
        projectile = tank.fire_projectile(angle, power)
        self.projectiles.append(projectile)
        self.position.append(projectile.position)

    def update_projectiles(self, time, targets, terrain):
        while True:
            projectile = self.projectiles[0]
            projectile.update_pos(time)
            self.position[self.projectiles.index(projectile)] = projectile.position

            if (projectile.position[1] <= 0) or (terrain.check_collision(projectile)):
                self.last_location.clear()
                self.last_location.append(projectile.position)
                self.projectiles.remove(projectile)
                return False
            else:
                for target in targets:
                    if target.check_collision(projectile):
                        self.last_location.clear()
                        self.projectiles.remove(projectile)
                        return True
    
    def get_last_location(self):
        return self.last_location