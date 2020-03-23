import pygame as pg
from settings import *

class Map(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((10, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        