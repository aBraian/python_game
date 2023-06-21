import pygame
import random
from audio import *
from constants import *

class Health:

    class_type = "Health"

    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_health = image.get_rect()
        self.image = image 
        self.rect = rect_health   
        self.rect.bottom = 0
        self.rect.left = random.randrange(0, WIDTH_SCREEN - self.image.get_width())

class HealthSprites:
    
    class_type = "HealthSprites"
        
    def __init__(self):
        self.list = []
        
    def add(self, pu_health):
        self.list.append(pu_health)
    
    def spawn_health(self, image_path, player, quantity = 1):
        if player.hp < 100:
            for _ in range(quantity):
                self.add(Health(image_path))
    
    def move(self):
        for pu_health in self.list:
            pu_health.rect.y += 5
    
    def out_screen(self):
        list_aux = HealthSprites()
        for pu_health in self.list:
            if pu_health.rect.top > HEIGHT_SCREEN:
                list_aux.add(pu_health)
        return list_aux
            
    def collision(self, player):
        list_aux = HealthSprites()
        for pu_health in self.list:
            if pu_health.rect.colliderect(player.collision):
                Audio(AUDIO_POWER_UP).play_audio(1.0)
                list_aux.add(pu_health)
                player.hp += 25
                if player.hp > 100:
                    player.hp = 100
        return list_aux
        
    def remove(self, *args):
        for list_remove in args:
            if len(list_remove.list) > 0:
                for pu_health in list_remove.list:
                    if pu_health in self.list:
                        self.list.remove(pu_health)

    def update(self, player):
        self.move()
        collision = self.collision(player)
        out_screen = self.out_screen()
        self.remove(collision, out_screen)
        
    def draw(self, screen):
        for pu_healt in self.list:
            screen.blit(pu_healt.image, pu_healt.rect)