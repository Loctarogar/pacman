import pygame as pg
from game_settings import *

class Ghost(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (275, 200)