import pygame as pg
from os import *
from game_settings import *

class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        
    def new_game(self):
        self.run()
                
    def run(self):
        # events check
        self.clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self.screen.fill(BLACK)
        self.draw_map()
        pg.display.flip()

    def draw_map(self):
        for i in MAP_LIST:
            pg.draw.rect(self.screen, WHITE, (i))
      
game = Game()          
while game.running:
    game.new_game()
        
pg.quit()