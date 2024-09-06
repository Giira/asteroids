import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerups import SpeedUp, Shield
from menus import draw_start_menu, draw_pause_menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    game_state = "start_menu"
      
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    SpeedUp.containers = (updateable, drawable, powerups)
    Shield.containers = (updateable, drawable, powerups)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    score = 0
    
    while True:
        if game_state != "game":
            dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if game_state == "start_menu":
                draw_start_menu(screen)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    rect = pygame.Rect(892, 640, 136, 71)
                    if rect.collidepoint(event.pos):
                        game_state = "game"

            if game_state == "pause_menu":
                draw_pause_menu(screen)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    rect = pygame.Rect(812, 640, 296, 86)
                    if rect.collidepoint(event.pos):
                        game_state = "game"
                        clock = pygame.time.Clock()


            if game_state == "game_over":
                pass
                
                
        if game_state == "game":
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                game_state = "pause_menu"

            for object in updateable:
                object.update(dt)
            
            for asteroid in asteroids:
                if asteroid.collision_check(player):
                    if player.shield_on:
                        asteroid.kill()
                        player.shield_on = False
                    else:
                        print("Game Over!")
                        print(f"Score: {score}")
                        sys.exit()
                for shot in shots:
                    if shot.collision_check(asteroid):
                        shot.kill()
                        asteroid.split()
                        score += 1
            
            for powerup in powerups:
                if powerup.collision_check(player):
                    powerup.kill()
                    if powerup.powerup == "speedup":
                        player.speed_boost()
                    if powerup.powerup == "shield":
                        player.shield_powerup()
            
            screen.fill("black")

            for object in drawable:
                object.draw(screen)

            pygame.display.flip()
            

            dt = clock.tick(60) / 1000
            



if __name__ == "__main__":
    main()