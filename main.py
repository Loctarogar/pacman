import pygame as pg
from os import *
from game_settings import *
from player import *
from walls import *
from ghost import *

class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # TODO: Clock doesn't work
        self.clock = pg.time.Clock()
        self.clock.tick(20)
        self.create_map()

    def new_game(self):
        self.player_sprite = pg.sprite.Group()
        self.player = Player(self)
        self.player_sprite.add(self.player)
        self.ghost_sprite = pg.sprite.Group()
        self.ghost = Ghost(self)
        self.ghost_sprite.add(self.ghost)
        self.ghost_sprite2 = pg.sprite.Group()
        self.ghost2 = Ghost(self, 395, 200, GREEN)
        self.ghost_sprite2.add(self.ghost2)
        self.run()

    def run(self):
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

            self.move_ghost()
            self.player_sprite.update()
            self.ghost_sprite.update()
            self.ghost_sprite2.update()
            self.screen.fill(BLACK)
            self.draw()
            pg.display.flip()

    def draw(self):
        self.map_sprite.draw(self.screen)
        self.player_sprite.draw(self.screen)
        self.ghost_sprite.draw(self.screen)
        self.ghost_sprite2.draw(self.screen)

    def create_map(self):
        self.map_sprite = pg.sprite.Group()
        for i in MAP_LIST:
            #           x,    y,    width, height
            wall = Wall(i[0], i[1], i[2], i[3])
            self.map_sprite.add(wall)

    def move_ghost(self):
        self.ghost.move()
        self.ghost2.move()

game = Game()          
while game.running:
    game.new_game()

pg.quit()