from screen_congratulations import *
from screen_level_1 import *
from screen_level_2 import *
from screen_level_3 import *
from screen_name_input import *
from screen_next_level import *

def screen_menu_levels(screen, dict_audio, menu, player):
    running = True
    level = 1
    game_completed = False
    while running:
        screen_next_level(screen, level, menu)
        if menu.option != "0": 
            if level == 1:
                if screen_level_1(screen, dict_audio, menu, player):
                    level = 2
                else:
                    running = False
            elif level == 2: 
                if screen_level_2(screen, dict_audio, menu, player):
                    level = 3
                else:
                    running = False
            elif level == 3:
                if screen_level_3(screen, dict_audio, menu, player):
                    game_completed = True
                else:
                    screen_name_input(screen, menu, player)
                    running = False
            if not running and menu.option != "0":
                screen_name_input(screen, menu, player)
            if game_completed:
                screen_congratulations(screen, menu, player)
                screen_name_input(screen, menu, player)
                running = False
        else:
            running = False