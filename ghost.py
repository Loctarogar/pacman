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
        self.direction = UP
        
    def can_move(self):
        return True
    
    def move(self):
        if self.direction == 'UP' and self.can_move():
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if not hits:
                self.rect.y -= 2
        elif self.direction == 'DOWN' and self.can_move():
            self.rect.y += 2
        elif self.direction == 'LEFT' and self.can_move():
            self.rect.x -= 2
        elif self.direction == 'RIGTH' and self.can_move():
            self.rect.x += 2