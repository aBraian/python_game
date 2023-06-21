import pygame
from audio import *
from background import *
from constants import *
from gui import *
from text import *

def screen_main_menu(screen, dict_audio, menu):
    
    #Audio
    audio_main_menu = dict_audio.get_audio("audio_main_menu") 
    audio_main_menu.play_audio(1.0, -1)
    audio_button = Audio(AUDIO_BUTTON)
    
    #Background
    background = Background(IMAGE_BACKGROUND_6, 0, 0)
    background_copy = background.copy()

    #Fps
    fps = pygame.time.Clock()

    #Gui
    image_audio_off = Gui(IMAGE_SOUND_OFF, WIDTH_SCREEN - 22, HEIGHT_SCREEN - 32)
    image_audio_on = Gui(IMAGE_SOUND_ON, WIDTH_SCREEN - 22, HEIGHT_SCREEN - 32) 
    logo = Gui(IMAGE_GAME_NAME, WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 - 150) 
    logo.scale(400, 50)
    list_gui_menu = GuiSprites()
    list_gui_menu.add(logo)  
    
    #Text
    text_how_play = Text(TWITCH, SILVER, 16, "Guia", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + 70)
    text_score = Text(TWITCH, SILVER, 16, "Marcadores", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + (70 * 2))
    text_start = Text(TWITCH, SILVER, 16, "Jugar", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2)
    text_quit = Text(TWITCH, SILVER, 16, "Salir", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + (70 * 3))
    text_how_play_reaction = Text(TWITCH, YELLOW, 16, "Guia", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + 70)
    text_score_reaction = Text(TWITCH, YELLOW, 16, "Marcadores", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + (70 * 2))
    text_start_reaction = Text(TWITCH, YELLOW, 16, "Jugar", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2)
    text_quit_reaction = Text(TWITCH, YELLOW, 16, "Salir", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 + (70 * 3))
    
    list_text = TextSprites()
    list_text.add(text_how_play, text_score, text_start, text_quit)
    collision_coordinates = None
    
    #Program Execution
    running = True

    while running:
        clic_event = False
        audio_main_menu.check_mute()
        
        #Events in execution
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                audio_main_menu.stop_audio()
                menu.option = "0"
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: 
                    dict_audio.mute()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    collision_coordinates = event.pos
                    clic_event = True        
            if event.type == pygame.MOUSEMOTION:
                collision_coordinates = event.pos
                    
        #Background Move 
        background.vertical_move(screen, True, background_copy, 1)
        background.draw(screen)

        #Gui in execution
        audio_main_menu.mute_icon(screen, image_audio_off, image_audio_on)
        list_gui_menu.draw(screen)
        
        #Menu Options in execution
        if text_quit.collision(collision_coordinates) and clic_event:
            audio_button.play_audio(1.0)
            audio_main_menu.stop_audio()
            menu.option = "0"
            running = False
        if text_start.collision(collision_coordinates) and clic_event:
            audio_button.play_audio(1.0)
            audio_main_menu.stop_audio()
            menu.option = "1"
            running = False
        if text_how_play.collision(collision_coordinates) and clic_event:
            audio_button.play_audio(1.0)
            audio_main_menu.stop_audio()
            menu.option = "2"
            running = False
        if text_score.collision(collision_coordinates) and clic_event:
            audio_button.play_audio(1.0)
            audio_main_menu.stop_audio()
            menu.option = "3"
            running = False
        
        #Text in execution    
        list_text.draw(screen)
        text_how_play.reaction(screen, text_how_play_reaction, collision_coordinates)
        text_score.reaction(screen, text_score_reaction, collision_coordinates)
        text_start.reaction(screen, text_start_reaction, collision_coordinates)
        text_quit.reaction(screen, text_quit_reaction, collision_coordinates)
        
        pygame.display.flip()

        fps.tick(FPS)