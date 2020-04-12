import pygame as pg
import random
from game_settings import *

class Ghost(pg.sprite.Sprite):
    def __init__(self, game, x = 275, y = 200, color = YELLOW):
        pg.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.game = game
        self.image = pg.Surface((30, 30))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.direction = UP
        self.directions = []

    def change_direction(self):
        # self.directions = [UP, DOWN, LEFT, RIGHT]
        if self.direction in self.directions:
           self.directions.remove(self.direction)
        self.direction = self.directions[random.randint(0, int(len(self.directions) - 1))]
        
    def is_sprite_collide(self):
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if hits:
            return True
        
        return False
        
    def possible_directions(self):
        self.directions.clear()
        
        # check direction up
        self.rect.y -= 40
        if not self.is_sprite_collide():
            self.directions.append(UP)
        self.rect.y += 40
        
        # check direction down
        self.rect.y += 40
        if not self.is_sprite_collide():
            self.directions.append(DOWN)
        self.rect.y -= 40
        
        # check direction left
        self.rect.x -= 40
        if not self.is_sprite_collide():
            self.directions.append(LEFT)
        self.rect.x += 40
        
        # check direction right
        self.rect.x += 40
        if not self.is_sprite_collide():
            self.directions.append(RIGHT)
        self.rect.x -= 40
        
        if self.direction in self.directions:
            self.directions.remove(self.direction)
        if len(self.directions) > 2:
            return True
        else:
            return False

    def move(self):
        # get possible directions and change direction if coin
        if self.possible_directions():
            coin = random.randint(0, 1)
            if coin:
                coin2 = random.randint(0, 1)
                if coin2:
                    self.change_direction()
        
        if self.direction == UP:
            self.rect.y -= 1
            if self.is_sprite_collide():
                self.rect.y += 1
                self.change_direction()

        elif self.direction == DOWN:
            self.rect.y += 1
            if self.is_sprite_collide():
                self.rect.y -= 1
                self.change_direction()
                
        elif self.direction == LEFT:
            self.rect.x -= 1
            if self.is_sprite_collide():
                self.rect.x += 1
                self.change_direction()
                
        elif self.direction == RIGHT:
            self.rect.x += 1
            if self.is_sprite_collide():
                self.rect.x -= 1
                self.change_direction()