from interfaces import Fireable
from projectile import Projectile
from constants import INIT_ANGLE, INIT_POWER

class Tank(Fireable):
    """플레이어가 제어하는 탱크를 나타냅니다."""
    def __init__(self, position):
        super().__init__(position=position)
        self.angle = INIT_ANGLE
        self.power = INIT_POWER

    def set_angle_power(self, angle, power):
        """탱크에게 플레이어로부터 입력받은 각도와 강도를 설정합니다."""
        self.angle = angle
        self.power = power

    def fire_projectile(self):
        """탱크에서 발사체 발사."""
        return Projectile(self.position, self.angle, self.power)