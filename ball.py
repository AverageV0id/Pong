import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))  # визуал
        self.image.fill(pg.Color(color))
        self.rect = self.image.get_rect(center=(x, y))  # хитбокс
