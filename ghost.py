import pygame as pg
from game_settings import *

class Ghost(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (275, 200)
        
    def can_move(self):
        return True
    
    def move(self, direction):
        if direction == 'UP' and self.can_move():
            self.rect.y -= 2
        elif direction == 'DOWN' and self.can_move():
            self.rect.y += 2
        elif direction == 'LEFT' and self.can_move():
            self.rect.x -= 2
        elif direction == 'RIGTH' and self.can_move():
            self.rect.x += 2