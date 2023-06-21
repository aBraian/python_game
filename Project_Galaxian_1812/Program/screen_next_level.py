import pygame
from audio import *
from background import *
from constants import *
from gui import *
from text import *

def screen_next_level(screen, level, menu):
    
    #Background
    background = Background(IMAGE_BACKGROUND_6, 0, 0)
    background_copy = background.copy()
    
    #Fps
    fps = pygame.time.Clock()
    
    #Text
    text_level = Text(TWITCH, SILVER, 50, f"Nivel {level}", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 - 90)
    text_continue = Text(TWITCH, SILVER, 16, 'presione "Enter" para continuar', WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + 250)
    list_text = TextSprites()
    list_text.add(text_level, text_continue)
    
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
        list_text.draw(screen)
        
        pygame.display.flip()

        fps.tick(FPS)