import pygame
import random
from audio import *
from background import *
from character_enemy_1 import *
from character_enemy_2 import *
from character_enemy_3 import *
from character_player import *
from constants import *
from explosions import *
from gui import *
from power_up_ammo import *
from power_up_health import *
from screen_game_over import *
from shoots import *
from text import *

def screen_level_2(screen, dict_audio, menu, player):
    
    #Audio
    audio_level_2 = dict_audio.get_audio("audio_level_2")
    audio_level_2.play_audio(1.0, -1)
    
    #Background
    background = Background(IMAGE_BACKGROUND_5, 0, 0)
    background_copy = background.copy()
    
    #Character - Enemies
    enemy_1 = E1(IMAGE_ENEMY_1)
    enemy_2 = E2(IMAGE_ENEMY_2)
    enemy_3 = E3(IMAGE_ENEMY_3)
    enemy_1.speed_x = random.choice([-6, -7])
    enemy_1.speed_y = random.choice([-6, -7])
    enemy_1.rate_fire = random.randrange(2500, 3000)
    enemy_2.speed = 8
    list_e1 = E1Sprites()
    list_e1_2 = E1Sprites()
    list_e2 = E2Sprites()
    list_e3 = E3Sprites()
    list_e1.spawn(enemy_1, 11, 1, 0)
    list_e1_2.spawn(enemy_1, 9, 2, 4)
    
    #Character - Player
    player.fire_mode = 0
    player.hp = 100
    player.speed = 5
    
    #Explosions
    list_explosions = ExplosionSprites()
    
    #Fps
    fps = pygame.time.Clock()
    
    #Gui
    image_audio_off = Gui(IMAGE_SOUND_OFF, WIDTH_SCREEN - 22, HEIGHT_SCREEN - 32)
    image_audio_on = Gui(IMAGE_SOUND_ON, WIDTH_SCREEN - 22, HEIGHT_SCREEN - 32)   
    image_clock = Gui(IMAGE_CLOCK, WIDTH_SCREEN / 2 - 40, 25)
    image_lifes = Gui(IMAGE_LIFES, WIDTH_SCREEN - 160, 25)
    image_score = Gui(IMAGE_STAR, WIDTH_SCREEN / 2 - 232, 25)
    list_gui = GuiSprites()
    list_mute_icon = GuiSprites()
    list_gui.add(image_clock, image_lifes, image_score)
    list_mute_icon.add(image_audio_off, image_audio_on)
    
    #Power Up - Ammo
    list_ammo = AmmoSprites()

    #Power Up - Health
    list_health = HealthSprites()
    
    #Return
    return_level = False
    
    #Shoot
    list_shoots_enemies = ShootSprites()
    list_shoots_player = ShootSprites() 
    
    #Text
    list_text = TextSprites()
    time = 90
    
    #Timer
    timer_time = pygame.USEREVENT + 0
    timer_drop_ammo = pygame.USEREVENT + 1
    timer_drop_health = pygame.USEREVENT + 2
    timer_enemy_2 = pygame.USEREVENT + 3
    timer_enemy_3 = pygame.USEREVENT + 4
    pygame.time.set_timer(timer_time, 1 * 1000)
    pygame.time.set_timer(timer_drop_ammo, 20 * 1000)
    pygame.time.set_timer(timer_drop_health, 15 * 1000)
    pygame.time.set_timer(timer_enemy_2, 5 * 1000)
    pygame.time.set_timer(timer_enemy_3, 10 * 1000)
    
    #Program Execution
    running = True
    
    while running: 
        audio_level_2.check_mute()
        if player.no_lifes():
            
            #Screen Game Over
            audio_level_2.stop_audio()
            running = False
            screen_game_over(screen, menu, player)      
        elif not player.no_lifes() and time == 0:
            
            #Level Complete
            audio_level_2.stop_audio()
            running = False
            return_level = True
        else:
            
            #Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    audio_level_2.stop_audio()
                    menu.option = "0"
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m: 
                        dict_audio.mute() 
                if event.type == timer_time:
                    time -= 1
                if event.type == timer_enemy_2:
                    list_e2.spawn(enemy_2, 3)
                if event.type == timer_enemy_3:
                    list_e3.spawn(enemy_3, 3, 3)
                if event.type == timer_drop_ammo:
                    list_ammo.spawn_ammo(IMAGE_AMMO, player)
                if event.type == timer_drop_health:
                    list_health.spawn_health(IMAGE_HEALTH, player)
                        
            #Background Move
            background.vertical_move(screen, True, background_copy, 1)
            background.draw(screen)
            
            #Character - Enemies in execution
            list_e1.update(list_explosions, player, list_shoots_enemies, list_shoots_player)
            list_e1_2.update(list_explosions, player, list_shoots_enemies, list_shoots_player)    
            list_e2.update(list_explosions, player, list_shoots_player)
            list_e3.update(list_explosions, player, list_shoots_enemies, list_shoots_player)
            list_e1.draw(screen)
            list_e1_2.draw(screen)
            list_e2.draw(screen)
            list_e3.draw(screen)
            list_e1.respawn(enemy_1, 11, 1, 0)
            list_e1_2.respawn(enemy_1, 9, 2, 4)
            
            #Character - Player in execution
            player.update(list_explosions, list_shoots_enemies, list_shoots_player, WIDTH_SCREEN / 2, HEIGHT_SCREEN - 40)
            player.update(list_explosions, list_shoots_enemies, list_shoots_player, WIDTH_SCREEN / 2, HEIGHT_SCREEN - 40)
            player.draw(screen)    
            
            #Explosions
            list_explosions.update()
            list_explosions.draw(screen)
                
            #Shoots in execution
            list_shoots_enemies.update(5)
            list_shoots_player.update(-10)
            list_shoots_enemies.draw(screen)
            list_shoots_player.draw(screen) 
            
            #Power Up - Ammo in execution
            list_ammo.update(player)
            list_ammo.draw(screen)
            
            #Power Up - Health in execution
            list_health.update(player)
            list_health.draw(screen)
            
            #Gui in execution
            list_gui.draw(screen)
            audio_level_2.mute_icon(screen, image_audio_off, image_audio_on)
            player.hp_bar(screen, BLUE, SILVER, WIDTH_SCREEN - 130, 25, 100, 20)
            
            #Text in execution
            text_score = Text(TWITCH, SILVER, 18, f"{str(player.score).zfill(7)}", WIDTH_SCREEN / 2 - 150, 5)
            text_time = Text(TWITCH, SILVER, 18, f"{time}", WIDTH_SCREEN / 2, 5)
            list_text.add(text_score, text_time)
            list_text.draw(screen)
            list_text.clear()
            
            #Update Screen
            pygame.display.flip()
            fps.tick(60)
    
    return return_level