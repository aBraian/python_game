import os
import pygame

archive_folder = os.path.dirname(__file__)
game_folder = os.path.dirname(archive_folder)
image_folder = os.path.join(game_folder, "Images")
explosion_folder = os.path.join(image_folder, "Explosions")

def get_explosions(character_name):
    list_images = []
    character_path = os.path.join(explosion_folder, character_name)
    for explosion in os.listdir(character_path):
        image_path = os.path.join(character_path, explosion)
        image = pygame.image.load(image_path)
        list_images.append(image)
    return list_images
        
class Explosion:
    
    class_type = "Explosion"
    
    def __init__(self, center, character_name = ""):
        list_explosions = get_explosions(character_name)
        self.list_image = list_explosions
        self.next_image = 0
        self.image = self.list_image[self.next_image]
        self.delay_frame = 60
        self.last_frame = 0
        self.length = len(list_explosions)
        self.rect = self.image.get_rect()
        self.rect.center = center
    
class ExplosionSprites:
    
    class_type = "ExplosionSprites"
    
    def __init__(self):
        self.list = []
        
    def add(self, explosion):
        self.list.append(explosion)
        
    def __delitem__(self, index):
        return self.list.pop(index)
    
    def remove(self, *args):
        for list_delete in args:
            if list_delete != None and len(list_delete) > 0:
                for item_delete in list_delete:
                    if item_delete in self.list:
                        self.list.remove(item_delete)
    
    def update(self):
        list_explosions = []
        for explosion in self.list: 
            list_explosions.append(explosion)
            now = pygame.time.get_ticks()
            if now - explosion.last_frame > explosion.delay_frame:
                explosion.last_frame = now
                explosion.image = explosion.list_image[explosion.next_image] 
                explosion.next_image += 1
                if explosion.next_image == explosion.length:
                    self.remove(list_explosions)
        
    def draw(self, screen):
        for explosion in self.list:
            screen.blit(explosion.image, explosion.rect)
    