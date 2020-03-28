import pygame as pg
from os import *
from game_settings import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # events check
        self.clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.player.move_left()
        if keys[pg.K_RIGHT]:
            self.player.move_right()
        if keys[pg.K_UP]:
            self.player.move_up
        if keys[pg.K_DOWN]:
            self.player.move_down

        self.all_sprites.update()
        self.screen.fill(BLACK)
        self.draw()
        pg.display.flip()
        
    def draw(self):
        self.draw_map()
        self.all_sprites.draw(self.screen)

    def draw_map(self):
        for i in MAP_LIST:
            pg.draw.rect(self.screen, WHITE, (i))

game = Game()          
while game.running:
    game.new_game()

pg.quit()