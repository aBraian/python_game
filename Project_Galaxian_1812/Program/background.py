import pygame
from constants import *

class Background:

    class_type = "Background"

    def __init__(self, image_path, axis_x, axis_y):
        image = pygame.image.load(image_path).convert_alpha()
        rect_image = image.get_rect()
        rect_image.x = axis_x
        rect_image.y = axis_y
        self.image_path = image_path
        self.image = image
        self.rect = rect_image

    def copy(self):
        image_copy = Background(self.image_path, self.rect.x, self.rect.y)
        return image_copy

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def vertical_move(self, screen, direction, image_copy, speed):
        screen.blit(image_copy.image, (image_copy.rect.x, image_copy.rect.y))
        if direction:
            image_copy.rect.bottom = self.rect.top
            self.rect.bottom += speed
            if image_copy.rect.bottom == HEIGHT_SCREEN:
                self.rect.top = image_copy.rect.top
        else:
            image_copy.rect.top = self.rect.bottom
            self.rect.y -= speed
            if image_copy.rect.top == 0:
                self.rect.bottom = image_copy.rect.bottom