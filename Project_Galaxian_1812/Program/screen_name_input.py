import pygame
from audio import *
from background import *
from constants import *
from gui import *
from text import *

def screen_name_input(screen, menu, player):
    
    #Background
    background = Background(IMAGE_BACKGROUND_6, 0, 0)
    background_copy = background.copy()
    
    #Fps
    fps = pygame.time.Clock()
    
    #Text
    name_input = TextInput()
    text = Text(TWITCH, SILVER, 32, "Ingrese su nombre", WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2 - 100)
    list_text = TextSprites()
    list_text.add(text)
    
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
                    if not name_input.empty():
                        player.name = name_input.string
                        running = False   
                if event.key == pygame.K_BACKSPACE:
                    name_input.delete()
                if event.key == pygame.K_a:
                    name_input.input("a")
                if event.key == pygame.K_b:
                    name_input.input("b")
                if event.key == pygame.K_c:
                    name_input.input("c")
                if event.key == pygame.K_d:
                    name_input.input("d")
                if event.key == pygame.K_e:
                    name_input.input("e")
                if event.key == pygame.K_f:
                    name_input.input("f")
                if event.key == pygame.K_g:
                    name_input.input("g")
                if event.key == pygame.K_h:
                    name_input.input("h")
                if event.key == pygame.K_i:
                    name_input.input("i")
                if event.key == pygame.K_j:
                    name_input.input("j")
                if event.key == pygame.K_k:
                    name_input.input("k")
                if event.key == pygame.K_l:
                    name_input.input("l")
                if event.key == pygame.K_m:
                    name_input.input("m")
                if event.key == pygame.K_n:
                    name_input.input("n")
                if event.key == pygame.K_o:
                    name_input.input("o")
                if event.key == pygame.K_p:
                    name_input.input("p")
                if event.key == pygame.K_q:
                    name_input.input("q")
                if event.key == pygame.K_r:
                    name_input.input("r")
                if event.key == pygame.K_s:
                    name_input.input("s")
                if event.key == pygame.K_t:
                    name_input.input("t")
                if event.key == pygame.K_u:
                    name_input.input("u")
                if event.key == pygame.K_v:
                    name_input.input("v")
                if event.key == pygame.K_w:
                    name_input.input("w")
                if event.key == pygame.K_x:
                    name_input.input("x")
                if event.key == pygame.K_y:
                    name_input.input("y")
                if event.key == pygame.K_z:
                    name_input.input("z")
                if event.key == pygame.K_0:
                    name_input.input("0")
                if event.key == pygame.K_1:
                    name_input.input("1")
                if event.key == pygame.K_2:
                    name_input.input("2")
                if event.key == pygame.K_3:
                    name_input.input("3")
                if event.key == pygame.K_4:
                    name_input.input("4")
                if event.key == pygame.K_5:
                    name_input.input("5")
                if event.key == pygame.K_6:
                    name_input.input("6")
                if event.key == pygame.K_7:
                    name_input.input("7")
                if event.key == pygame.K_8:
                    name_input.input("8")
                if event.key == pygame.K_9:
                    name_input.input("9")
                
        #Background Move 
        background.vertical_move(screen, True, background_copy, 1)
        background.draw(screen)
        
        #Text in execution
        name_input.update(TWITCH, SILVER, 16, WIDTH_SCREEN / 2, HEIGHT_SCREEN / 2)
        name_input.draw(screen)
        list_text.draw(screen)
        
        #Update Screen
        pygame.display.flip()
        fps.tick(FPS)