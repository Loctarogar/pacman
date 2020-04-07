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
        # self.directions = [UP, DOWN, LEFT, RIGHT]
        #self.directions.remove(self.direction)
        self.direction = self.directions[random.randint(0, int(len(self.directions) - 1))]
        
    def check_change_direction(self):
        self.directions.clear()
        
        # check direction up
        self.rect.y -= 20
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if not hits:
            self.directions.append(UP)
        self.rect.y += 20
        
        # check direction down
        self.rect.y += 20
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if not hits:
            self.directions.append(DOWN)
        self.rect.y -= 20
        
        # check direction left
        self.rect.x -= 20
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if not hits:
            self.directions.append(LEFT)
        self.rect.x += 20
        
        # check direction right
        self.rect.x += 20
        hits = pg.sprite.spritecollide(self.game.ghost, self.game.map_sprite, False)
        if not hits:
            self.directions.append(RIGHT)
        self.rect.x -= 20
        print (self.directions)
        print (len(self.directions))
        if len(self.directions) > 2:
            return True
        else:
            return False

    def move(self):
        # get possible directions
        print (self.check_change_direction())
        if self.check_change_direction():
            # should change directions
            coin = random.randint(0, 1)
            if coin:
                self.change_direction()
        
        
        print (self.direction)
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