import pygame
from constants import *

class Gui:

    class_type = "Gui"

    def __init__(self, image_path, axis_x, axis_y):
        image = pygame.image.load(image_path).convert_alpha()
        rect_gui = image.get_rect()
        rect_gui.centerx = axis_x
        rect_gui.y = axis_y
        self.image = image
        self.rect = rect_gui
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def scale(self, width, height):
        backup_axis_x = self.rect.centerx
        backup_axis_y = self.rect.y 
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.centerx = backup_axis_x
        self.rect.y = backup_axis_y

class GuiSprites:

    class_type = "GuiSprites"

    def __init__(self):
        self.list = []

    def add(self, *args):
        for gui in args:
            self.list.append(gui)

    def draw(self, screen):
        for gui in self.list:
            screen.blit(gui.image, gui.rect)     