import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, colour):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.colour = colour

    
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, SHOT_RADIUS, 2)


    def update(self,dt):
        self.position += self.velocity * dt

        