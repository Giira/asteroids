import pygame
from constants import *

def draw_start_menu(screen):
    screen.fill("black")
    font = pygame.font.SysFont("elephant", 120)
    small_font = pygame.font.SysFont("roboto", 60)
    title = font.render('Asteroids', True, "white")
    start_button = small_font.render('Start', True, 'white')
    screen.blit(title, ((960 - (title.get_width() / 2)), 440))
    width, height = start_button.get_width() * 1.2, start_button.get_height() * 1.2
    rect = (pygame.Rect((960 - width / 2), 640, width, height))
    pygame.draw.rect(screen, "green", rect, 2, 15)
    screen.blit(start_button, (960 - (start_button.get_width() / 2), 645))
    pygame.display.update()


def draw_pause_menu(screen):
    font = pygame.font.SysFont("elephant", 120)
    small_font = pygame.font.SysFont("roboto", 60)
    title = font.render('Paused', True, "white")
    start_button = small_font.render('Continue', True, 'white')
    screen.blit(title, ((960 - (title.get_width() / 2)), 440))
    width, height = start_button.get_width() * 1.2, start_button.get_height() * 1.2
    rect = (pygame.Rect((960 - width / 2), 640, width, height))
    pygame.draw.rect(screen, "green", rect, 2, 15)
    screen.blit(start_button, (960 - (start_button.get_width() / 2), 645))
    pygame.display.update()