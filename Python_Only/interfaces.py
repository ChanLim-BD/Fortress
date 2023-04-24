from abc import ABC, abstractmethod

class GameObject:
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

class Collidable(GameObject, ABC):
    @abstractmethod
    def check_collision(self, obj):
        pass

class Fireable(GameObject, ABC):
    @abstractmethod
    def fire_projectile(self, angle, power):
        pass

class Movable(GameObject, ABC):
    @abstractmethod
    def update_position(self, time):
        pass