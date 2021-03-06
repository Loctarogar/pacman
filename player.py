import pygame as pg
from game_settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (215, 200)

    def move_up(self):
        self.rect.y -= 2
        hits = pg.sprite.spritecollide(self.game.player, self.game.map_sprite, False)
        if hits:
            self.rect.y += 2

    def move_down(self):
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self.game.player, self.game.map_sprite, False)
        if hits:
            self.rect.y -= 2

    def move_left(self):
        self.rect.x -= 2
        hits = pg.sprite.spritecollide(self.game.player, self.game.map_sprite, False)
        if hits:
            self.rect.x += 2
    
    def move_right(self):
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self.game.player, self.game.map_sprite, False)
        if hits:
            self.rect.x -= 2