import pygame as pg
import random
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
        
    def change_direction(self):
        directions = [UP, DOWN, LEFT, RIGHT]
        directions.remove(self.direction)
        self.direction = directions[random.randint(0, int(len(directions) - 1))]
    
    def move(self):
        if self.direction == UP:
            self.change_direction()
            self.rect.y -= 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.y += 1
                self.change_direction()
                self.move()
                
        elif self.direction == DOWN:
            self.change_direction()
            self.rect.y += 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.y -= 1
                self.change_direction()
                self.move()
        elif self.direction == LEFT:
            self.change_direction()
            self.rect.x -= 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.x += 1
                self.change_direction()
                self.move()
        elif self.direction == RIGHT:
            self.change_direction()
            self.rect.x += 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.x -= 1
                self.change_direction()
                self.move()