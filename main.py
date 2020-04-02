import pygame as pg
from os import *
from game_settings import *
from player import *
from walls import *
from ghost import *

class Game:
    def __init__(self):
        pg.init()
        # define group for map sprites
        self.map_sprite = pg.sprite.Group()
        
        self.running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def new_game(self):
        self.player_sprite = pg.sprite.Group()
        self.player = Player(self)
        self.player_sprite.add(self.player)
        self.ghost_sprite = pg.sprite.Group()
        self.ghost = Ghost(self)
        self.ghost_sprite.add(self.ghost)
        self.run()

    def run(self):
        self.clock.tick(10)
        while self.running:
            # events check
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            keys = pg.key.get_pressed()

            if keys[pg.K_LEFT]:
                self.player.move_left()
            if keys[pg.K_RIGHT]:
                self.player.move_right()
            if keys[pg.K_UP]:
                self.player.move_up()
            if keys[pg.K_DOWN]:
                self.player.move_down()
            
            
            self.player_sprite.update()
            self.move_ghost()
            self.screen.fill(BLACK)
            self.draw()
            pg.display.flip()

    def draw(self):
        self.draw_map()
        self.map_sprite.draw(self.screen)
        self.player_sprite.draw(self.screen)
        self.ghost_sprite.draw(self.screen)

    def draw_map(self):
        #self.map_sprite = pg.sprite.Group()
        for i in MAP_LIST:
            #           x,    y,    width, height
            wall = Wall(i[0], i[1], i[2], i[3])
            self.map_sprite.add(wall)
            
    def move_ghost(self):
        if self.ghost.move_up():
            print ('move up')
            return
        elif self.ghost.move_down():
            print ('move down')
            return
        elif self.ghost.move_left():
            return
        elif self.ghost.move_right():
            return
            
game = Game()          
while game.running:
    game.new_game()

pg.quit()