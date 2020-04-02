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
        
    def move_up(self):
        self.rect.y -= 1
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.rect.y += 1
            return True
        print ('up false')
        return False
    
    def move_down(self):
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.rect.y -= 2
            return True
        return False
    
    def move_left(self):
        self.rect.x -= 2
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.rect.x += 2
            return True
        return False
    
    def move_right(self):
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.rect.x -= 2
            return True
        return False