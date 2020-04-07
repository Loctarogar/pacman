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
        self.directions = []
        
    def change_direction(self):
        self.directions.clear()
        self.directions = [UP, DOWN, LEFT, RIGHT]
        self.directions.remove(self.direction)
        self.direction = self.directions[random.randint(0, int(len(self.directions) - 1))]
        

    def check_change_direction(self):
        self.directions.clear()
        
        # check direction up
        self.rect.y -= 5
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.directions.append(UP)
        self.rect.y += 5
        
        # check direction down
        self.rect.y += 5
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.directions.append(DOWN)
        self.rect.y -= 5
        
        # check direction left
        self.rect.x -= 5
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.directions.append(LEFT)
        self.rect.y += 5
        
        # check direction right
        self.rect.x += 5
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            self.directions.append(DOWN)
        self.rect.x -= 5

    def move(self):
        #self.check_change_direction()
        if self.direction == UP:
            self.rect.y -= 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.y += 1
                self.change_direction()
                self.move()

        elif self.direction == DOWN:
            self.rect.y += 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.y -= 1
                self.change_direction()
                self.move()
                
        elif self.direction == LEFT:
            self.rect.x -= 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.x += 1
                self.change_direction()
                self.move()
                
        elif self.direction == RIGHT:
            self.rect.x += 1
            hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
            if hits:
                self.rect.x -= 1
                self.change_direction()
                self.move()