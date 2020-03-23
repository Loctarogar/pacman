import pygame as pg
from game_settings import *

class Map(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # list of rects for map
        map_list = [
                 (350, 200, 100, 20),
                 (175, 100, 50, 20),
                 ]
        self.image = pg.Surface((10, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()