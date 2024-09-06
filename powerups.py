import pygame
from constants import *
from circleshape import CircleShape

class SpeedUp(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt


class Shield(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def shield_shape(self):
        pass

    
    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", )
