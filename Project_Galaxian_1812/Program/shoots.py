import pygame
from constants import *

class Shoot:

    class_type = "Shoot"

    def __init__(self, image_path, axis_x, axis_y):
        image = pygame.image.load(image_path).convert_alpha()
        rect_shoot = image.get_rect()
        rect_shoot.centerx = axis_x
        rect_shoot.bottom = axis_y  
        self.image = image
        self.rect = rect_shoot

class ShootSprites:
    
    class_type = "ShootSprites"

    def __init__(self):
        self.list = []

    def add(self, *args):
        for shoot in args:
            self.list.append(shoot)
    
    def draw(self, screen):
        for shoot in self.list:
            screen.blit(shoot.image, shoot.rect)

    def move(self, speed):
        for index, shoot in enumerate(self.list):
            shoot.rect.y += speed
            if shoot.rect.top == 0 or shoot.rect.bottom == HEIGHT_SCREEN:
                del self.list[index]
                break

    def remove(self, list_delete):
        if len(list_delete) > 0:
            for item_delete in list_delete:
                if item_delete in self.list:
                    self.list.remove(item_delete)

    def update(self, speed):
        self.move(speed)