"""
Модуль с классом игрока
"""

from Sprite import GameSprite


class Player(GameSprite):
    def __init__(
        self,
        image_path,
        pos_x,
        pos_y,
        speed,
        size_x,
        size_y,
        health,
        cartridges,
    ):
        super().__init__(
            image_path, pos_x, pos_y, speed, size_x, size_y, health
        )
        self.cartridges = cartridges

    def step_right(self):
        """
        Эта функция отвечает за передвижение вправо:

        self.rect.x - координата x
        self.speed - шаг игрока(скорость)
        """
        self.rect.x += self.speed

    def step_left(self):
        """
        Эта функция отвечает за передвижение влево:

        self.rect.x - координата x
        self.speed - шаг игрока(скорость)
        """
        self.rect.x -= self.speed

    def step_up(self):
        """
        Эта функция отвечает за передвижение вверх:

        self.rect.y - координата y
        self.speed - шаг игрока(скорость)
        """
        self.rect.y -= self.speed

    def step_down(self):
        """
        Эта функция отвечает за передвижение вниз:

        self.rect.y - координата y
        self.speed - шаг игрока(скорость)
        """
        self.rect.y += self.speed
