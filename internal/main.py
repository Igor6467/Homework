"""
Основной модуль для игры
"""

import pygame
from helper import resource_path
from Player import Player

pygame.init()

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
background = pygame.image.load(resource_path("assets/fon.png"))
pygame.display.set_caption("Моя игра")

p = resource_path("assets/men.png")

player = Player(p, 400, 300, 7, 100, 150, 100, 15)
timer = pygame.time.Clock()
game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    player.reset(window)

    if keys[pygame.K_d]:
        player.step_right()
    if keys[pygame.K_a]:
        player.step_left()
    if keys[pygame.K_w]:
        player.step_up()
    if keys[pygame.K_s]:
        player.step_down()

    timer.tick(60)
    pygame.display.update()
