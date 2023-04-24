from interfaces import Collidable

class Target(Collidable):
    """플레이어가 쳐야 할 목표물을 나타냅니다."""
    def __init__(self, radius, position):
        super().__init__(position=position)
        self.radius = radius

    def check_collision(self, projectile):
        """발사체가 목표물과 충돌하는지 확인합니다."""
        dx = projectile.position[0] - self.position[0]
        dy = projectile.position[1] - self.position[1]
        distance_squared = pow(dx, 2) + pow(dy, 2)
        return distance_squared <= pow(self.radius/2 + projectile.size/2, 2)
    
    def get_position(self):
        """원의 중심 위치를 반환합니다."""
        return self.position