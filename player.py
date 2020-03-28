import pygame as pg
from game_settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (215, 200)
    
    def move_up(self):
        pass
    
    def move_down(self):
        pass
    
    def move_left(self):
        pass
    
    def move_rigth(self):
        pass