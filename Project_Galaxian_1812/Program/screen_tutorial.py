import pygame
from audio import *
from background import *
from constants import *
from gui import *
from text import *

def screen_tutorial(screen, menu):
    
    #Background
    background = Background(IMAGE_BACKGROUND_6, 0, 0)
    background_copy = background.copy()
    
    #Fps
    fps = pygame.time.Clock()
    
    #Gui
    image_arrow_up = Gui(IMAGE_ARROW_UP, WIDTH_SCREEN / 2, 110)
    image_arrow_down = Gui(IMAGE_ARROW_DOWN, WIDTH_SCREEN / 2, 150)
    image_arrow_left = Gui(IMAGE_ARROW_LEFT, WIDTH_SCREEN / 2 - 40, 150)
    image_arrow_right = Gui(IMAGE_ARROW_RIGHT, WIDTH_SCREEN / 2 + 40, 150)
    image_m = Gui(IMAGE_M, WIDTH_SCREEN / 2, 270)
    image_p = Gui(IMAGE_P, WIDTH_SCREEN / 2, 390)
    image_space = Gui(IMAGE_SPACE, WIDTH_SCREEN / 2, 510)
    image_arrow_up.scale(40, 44)
    image_arrow_down.scale(40, 44)
    image_arrow_left.scale(40, 44)
    image_arrow_right.scale(40, 44)
    image_m.scale(40, 44)
    image_p.scale(40, 44)
    image_space.scale(205, 44)
    list_images = GuiSprites()
    list_images.add(image_arrow_up, image_arrow_down, image_arrow_left, image_arrow_right, image_m, image_p, image_space) 
    
    #Text
    text_back = Text(TWITCH, SILVER, 16, 'presione "Enter" para regresar', WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + 250)
    text_menu = Text(TWITCH, SILVER, 16, 'Volver al menu', WIDTH_SCREEN / 2, 0)
    text_move = Text(TWITCH, SILVER, 16, 'Movimiento', WIDTH_SCREEN / 2, 0)
    text_mute = Text(TWITCH, SILVER, 16, 'Silenciar musica', WIDTH_SCREEN / 2, 0)
    text_shoot = Text(TWITCH, SILVER, 16, 'Disparar', WIDTH_SCREEN / 2,  0)
    text_menu.rect.bottom = image_p.rect.top - 15
    text_move.rect.bottom = image_arrow_up.rect.top - 15
    text_mute.rect.bottom = image_m.rect.top - 15
    text_shoot.rect.bottom = image_space.rect.top - 15
    list_text = TextSprites()
    list_text.add(text_back, text_menu, text_move, text_mute, text_shoot)
    
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
        
        #Gui in execution
        list_images.draw(screen)
        
        #Text in execution
        list_text.draw(screen)
        
        pygame.display.flip()

        fps.tick(FPS)