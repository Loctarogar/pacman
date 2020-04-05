# screen settings
WIDTH = 800
HEIGHT = 600

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#directions for ghost
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

MAP_LIST = [
            # (x, y, width, height)
            # sides
            (1, 1, WIDTH, 5),
            (1, 1, 5, HEIGHT),
            (WIDTH - 5, 1, 5, HEIGHT),
            (1, HEIGHT - 5, WIDTH, 5),
            
            # horizontal walls
            (55, 40, 20, 200),
            (115, 40, 20, 200),
            (175, 40, 20, 200),
            (235, 40, 20, 200),
            (295, 40, 20, 200),
            (355, 40, 20, 200),
            (415, 40, 20, 200),
            (475, 40, 20, 200),
            (535, 40, 20, 200),
            (595, 40, 20, 200),
            (655, 40, 20, 200),
            (715, 40, 20, 200),
            
            # vertical walls
            (40, 280, 200, 20),
            (300, 280, 200, 20),
            (550, 280, 200, 20),
            
            # horizontal walls
            (55, 350, 20, 200),
            (115, 350, 20, 200),
            (175, 350, 20, 200),
            (235, 350, 20, 200),
            (295, 350, 20, 200),
            (355, 350, 20, 200),
            (415, 350, 20, 200),
            (475, 350, 20, 200),
            (535, 350, 20, 200),
            (595, 350, 20, 200),
            (655, 350, 20, 200),
            (715, 350, 20, 200),
            ]