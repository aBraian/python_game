import pygame
from audio import *
from background import *
from constants import *
from gui import *
from text import *

def screen_leaderboard(screen, menu, player_scores):
    
    #Background
    background = Background(IMAGE_BACKGROUND_6, 0, 0)
    background_copy = background.copy()
    
    #Fps
    fps = pygame.time.Clock()
    
    #Text
    text_back = Text(TWITCH, SILVER, 16, 'presione "Enter" para regresar', WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + 250)
    list_scores = TextSprites()
    list_scores.add_list(TWITCH, player_scores, SILVER, 16, WIDTH_SCREEN / 2, 100)
    list_scores.add(text_back)
    
    #Program Execution
    running = True

    while running:

        #Events in execution
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.option = "0"
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    running = False   
                
        #Background Move 
        background.vertical_move(screen, True, background_copy, 1)
        background.draw(screen)
        
        #Text in execution
        list_scores.draw(screen)
        
        pygame.display.flip()

        fps.tick(FPS)