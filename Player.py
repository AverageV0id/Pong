import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pg.Surface((width, height))  # визуал
        self.image.fill(pg.Color(color))
        self.rect = self.image.get_rect(topleft=(x, y))  # хитбокс
