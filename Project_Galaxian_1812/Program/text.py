import pygame
import re
from audio import *
from constants import *

class Text:
    
    class_type = "Text"

    def __init__(self, font_path, color, font_size, text, axis_x, axis_y):
        font = pygame.font.Font(font_path, font_size)
        text_to_show = font.render(text, True, color)
        rect_text = text_to_show.get_rect()
        rect_text.centerx = axis_x
        rect_text.top = axis_y
        self.button = pygame.Rect(rect_text.left, rect_text.top, rect_text.width, rect_text.height)  
        self.button.height = self.button.height / 2
        self.button.y = self.button.bottom
        self.rect = rect_text
        self.text = text_to_show
    
    def collision(self, collision_coordinates):
        if collision_coordinates != None and self.button.collidepoint(collision_coordinates):
            return True
        
    def reaction(self, screen, reaction, collision_coordinates):
        if self.collision(collision_coordinates):
            screen.blit(reaction.text, self.rect)
        
class TextSprites:

    class_type = "TextSprites"
    
    def __init__(self):
        self.list = []

    def add(self, *args):
        for text in args:
            self.list.append(text)

    def add_list(self, font_path, add_list, color, font_size, axis_x, axis_y):
        for i, player in enumerate(add_list):
            player_data = re.sub(r",", " ", str(player))
            player_data = re.sub(r"[^a-zA-Z0-9 ]", "", player_data)
            text_player = Text(font_path, color, font_size, player_data, axis_x, axis_y)
            text_player.rect.y = text_player.rect.y + text_player.rect.height * i
            self.add(text_player)

    def clear(self):
        self.list = []

    def draw(self, screen):
        for text in self.list:
            screen.blit(text.text, text.rect)
            
class TextInput:
    
    class_type = "TextInput"
    
    def __init__(self):
        self.list = []
        self.string = ""
        self.object_text = ""
        
    def input(self, char):
        self.list.append(char)
        
    def delete(self):   
        if self.list:
            self.list.pop(len(self.list) - 1)
            
    def empty(self):
        if len(self.list) == 0:
            return True
        
    def update(self, font_path, color, font_size, axis_x, axis_y):
        if len(self.list) > 10:
            self.delete()
        elif self.list:
            self.string = "".join(self.list)
            self.object_text = Text(font_path, color, font_size, self.string, axis_x, axis_y)
        
    def draw(self, screen):
        if self.list:
            screen.blit(self.object_text.text, self.object_text.rect)