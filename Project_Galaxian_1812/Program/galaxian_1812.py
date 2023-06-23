import pygame
from audio import * 
from constants import *
from character_player import *
from database import *
from screen_leaderboard import *
from screen_main_menu import *
from screen_menu_levels import *
from screen_menu import *
from screen_tutorial import *

pygame.init()

#Window
main_screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Galaxian 1812")
icon = pygame.image.load(IMAGE_ICON)
pygame.display.set_icon(icon)

#Audio
audio_level_1 = Audio(AUDIO_LEVEL_1, "audio_level_1") 
audio_level_2 = Audio(AUDIO_LEVEL_2, "audio_level_2")
audio_level_3 = Audio(AUDIO_LEVEL_3, "audio_level_3")
audio_main_menu = Audio(AUDIO_MAIN_MENU, "audio_main_menu")
dict_audio = AudioSprites()
dict_audio.add(audio_level_1, audio_level_2, audio_level_3, audio_main_menu)

#Character - Player
player = Player(IMAGE_PLAYER, 10 , WIDTH_SCREEN / 2, HEIGHT_SCREEN - 40)

#Fps
fps = pygame.time.Clock()

#Menu
menu = Menu()

#Program Execution
running = True

while running:
    
    #Character - Player in execution
    backup_name = player.name
    backup_score = player.score
    player = Player(IMAGE_PLAYER, 10 , WIDTH_SCREEN / 2, HEIGHT_SCREEN - 40)
    
    #Connection with Database
    list_scores = database_game(backup_name, backup_score)
    
    #Menu in execution
    screen_main_menu(main_screen, dict_audio, menu) 
    if menu.option == "1":
        screen_menu_levels(main_screen, dict_audio, menu, player)
    elif menu.option == "2":
        screen_tutorial(main_screen, menu)
    elif menu.option == "3":
        screen_leaderboard(main_screen, menu, list_scores)
    if menu.option == "0":
        running = False

pygame.quit()