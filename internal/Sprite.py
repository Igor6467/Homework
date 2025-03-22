"""
Модуль создания основного класса, от которого будут наследоваться другие
"""

import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(
        self, image_path, pos_x, pos_y, speed, size_x, size_y, health
    ):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (size_x, size_y)
        )
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
        self.health = health

    def reset(self, window: pygame.transform.scale):
        """
        Эта функция отвечает за отрисовку персонажа и обновление нахождения:

        self.rect.x - координата x
        self.rect.y - координата y
        self.image - отрисовка и обновление
        """
        window.blit(self.image, (self.rect.x, self.rect.y))
