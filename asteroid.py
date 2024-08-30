import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, colour="white"):
        super().__init__(x, y, radius)
        self.colour = colour
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vectors = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for vector in vectors:
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = vector * 1.2
