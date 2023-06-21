import pygame
import random
from audio import *
from constants import *

class Ammo:

    class_type = "Ammo"

    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_ammo = image.get_rect()
        self.image = image 
        self.image_path = image_path
        self.rect = rect_ammo   
        self.rect.left = random.randrange(0, WIDTH_SCREEN - self.image.get_width())
        self.rect.bottom = random.randrange(0 - HEIGHT_SCREEN, 0)

class AmmoSprites:
    
    class_type = "AmmoSprites"
        
    def __init__(self):
        self.list = []
        
    def add(self, pu_ammo):
        self.list.append(pu_ammo)
    
    def collision(self, player):
        list_aux = AmmoSprites()
        for pu_ammo in self.list:
            if pu_ammo.rect.colliderect(player.collision):
                Audio(AUDIO_POWER_UP).play_audio(1.0)
                list_aux.add(pu_ammo)
                if player.fire_mode < 2:
                    player.fire_mode += 1
        return list_aux
    
    def draw(self, screen):
        for pu_healt in self.list:
            screen.blit(pu_healt.image, pu_healt.rect)
    
    def move(self):
        for pu_ammo in self.list:
            pu_ammo.rect.y += 5
    
    def out_screen(self):
        list_aux = AmmoSprites()
        for pu_ammo in self.list:
            if pu_ammo.rect.top > HEIGHT_SCREEN:
                list_aux.add(pu_ammo)
        return list_aux
        
    def remove(self, *args):
        for list_remove in args:
            if len(list_remove.list) > 0:
                for pu_ammo in list_remove.list:
                    if pu_ammo in self.list:
                        self.list.remove(pu_ammo)
                        
    def spawn_ammo(self, image_path, player, quantity = 1):
        if player.fire_mode < 2:
            for _ in range(quantity):
                self.add(Ammo(image_path))

    def update(self, player):
        self.move()
        collision = self.collision(player)
        out_screen = self.out_screen()
        self.remove(collision, out_screen)

"""        
class AmmoContainer:

    class_type = "AmmoContainer"

    def __init__(self):
        self.list = []

    def __delitem__(self, index):
        return self.list.pop(index)

    def add(self, ammo):
        self.list.append(ammo)
        
    def draw(self, screen):
        for ammo in self.list:
            screen.blit(ammo.image, ammo.rect)

    def move(self):
        for index, _ in enumerate(self.list):
            self.list[index].rect.y += 5
            if self.list[index].rect.top > HEIGHT_SCREEN:
                del self.list[index]
                break

    def pick_up_ammo(self, player):
        for index, ammo in enumerate(self.list):
            if player.rect.colliderect(ammo.rect):
                Audio(AUDIO_POWER_UP).play_audio(1.0)
                del self.list[index]
                if player.fire_mode < 2:
                    player.fire_mode += 1
                break
    
    def spawn_ammo(self, ammo, player, quantity):
        if ammo.limit(player):
            for _ in range(quantity):
                ammo_copy = Ammo(ammo.image_path)
                self.add(ammo_copy)

    def update(self, player):        
        self.move()
        self.pick_up_ammo(player)
"""