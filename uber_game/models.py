from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sprite, wrap_position

UP = Vector2(0,-1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self,surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)
    
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

class Rider(GameObject):
    MANEUVERABILITY = 2
    ACCELERATION = 0.1

    def __init__(self, position):
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("rider"), Vector2(0))

    def rotate(self, clockwise = True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        computed =  self.velocity + self.direction * self.ACCELERATION

        
        if computed[1] < -2:
            computed[1] = -2
        elif computed[1] > 2:
            computed[1] = 2

        if computed[0] < -2:
            computed[0] = -2
        elif computed[0] > 2:
            computed[0] = 2

        
        self.velocity =computed
        

    def deccelerate(self):
        computed =  self.velocity - self.direction * self.ACCELERATION
        if computed[1] < -1:
            computed[1] = -1
        elif computed[1] > 1:
            computed[1] = 1

        if computed[0] < -1:
            computed[0] = -1
        elif computed[0] > 1:
            computed[0] = 1
        self.velocity = computed