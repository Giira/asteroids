import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.rate_limit = 0
        self.weapon = 0
        self.burst = 5
        self.speed = PLAYER_SPEED
        self.boost_limit = 0
        self.boost_on = False
        self.lives = PLAYER_LIVES
        self.colour = "white"
        self.shield_on = False

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)
        if self.shield_on:
            pygame.draw.circle(screen, "turquoise", self.position, self.radius + 10, 3)

    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def update(self, dt):
        self.rate_limit -= dt
        if self.boost_limit > 0:
            self.boost_limit -= dt
        else:
            self.speed = PLAYER_SPEED
            self.boost_on = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.rate_limit <= 0:
                if self.weapon == 0:
                    self.shoot()
                elif self.weapon == 1:
                    self.arc_shoot()
                elif self.weapon == 2:
                    self.burst_shoot()
        
        if keys[pygame.K_1]:
            self.weapon = 0
        
        if keys[pygame.K_2]:
            self.weapon = 1

        if keys[pygame.K_3]:
            self.weapon = 2

    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, "green")
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.rate_limit = PLAYER_SHOOT_COOLDOWN

    
    def arc_shoot(self):
        angle = -30
        for i in range(5):
            shot = Shot(self.position.x, self.position.y, "red")
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation + angle) * PLAYER_SHOOT_SPEED
            angle += 15
        self.rate_limit = 3 * PLAYER_SHOOT_COOLDOWN

    
    def burst_shoot(self):
        if self.burst > 0:
            shot = Shot(self.position.x, self.position.y, "blue")
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.burst -= 1
        else:    
            self.rate_limit = 2 * PLAYER_SHOOT_COOLDOWN
            self.burst = 5


    def speed_boost(self):
        if not self.boost_on:
            self.boost_limit = 5
            self.speed *= 2.5
            self.boost_on = True


    def shield_powerup(self):
        if not self.shield_on:
            self.shield_on = True


    def lose_life(self):
        self.lives -= 1
        
    