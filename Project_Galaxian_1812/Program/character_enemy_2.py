import pygame
import random
from explosions import *
from audio import *
from constants import *
from shoots import *

class E2: 

    class_type = "E2"

    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_character = image.get_rect()
        self.image = image
        self.image_path = image_path
        self.rect = rect_character
        self.rect.left = 0
        self.rect.bottom = 0
        self.spawn = False
        self.speed = 7

class E2Sprites:

    class_type = "E2Sprites"

    def __init__(self):
        self.list = []
    
    def add(self, enemy):
        self.list.append(enemy)
        
    def collision_with_player(self, enemies_delete,  explosion, index, player):
        if self.list[index].rect.colliderect(player.collision):
            Audio(AUDIO_EXPLOSION).play_audio(0.5)
            explosion.add(Explosion(self.list[index].rect.center, "Enemy"))
            enemies_delete.append(self.list[index])
            player.hp -= 20
            player.score -= 750
            if player.score < 0:
                player.score = 0

    def collision_with_shoots(self, enemies_delete, explosion, index, player, shoots):
        shoots_delete = []    
        for shoot in shoots.list:
            if self.list[index].rect.colliderect(shoot.rect):
                Audio(AUDIO_EXPLOSION).play_audio(0.5)
                shoots_delete.append(shoot)
                explosion.add(Explosion(self.list[index].rect.center, "Enemy"))
                player.score += 250
                enemies_delete.append(self.list[index])
        shoots.remove(shoots_delete)
        
    def draw(self, screen):
        for enemy in self.list:
            screen.blit(enemy.image, enemy.rect)
            
    def move(self, index):
        self.list[index].rect.y += self.list[index].speed
        
    def out_screen(self, enemies_delete):
        if len(enemies_delete) > 0:
            for enemy in self.list:
                if enemy.rect.top > HEIGHT_SCREEN:
                    enemies_delete.add(enemy)
        
    def remove(self, *args):
        for list_delete in args:
            if list_delete != None and len(list_delete) > 0:
                for enemy_delete in list_delete:
                    if enemy_delete in self.list:
                        self.list.remove(enemy_delete)

    def spawn(self, enemy, quantity): 
        ref_position = random.randrange(0, WIDTH_SCREEN - enemy.rect.width * 3)
        for i in range(quantity):
            enemy_copy = E2(enemy.image_path)
            enemy_copy.rect.left = ref_position + (i * enemy_copy.rect.width)
            self.add(enemy_copy)
    
    def update(self, explosion, player, shoots_player):
        enemies_delete_1 = []
        enemies_delete_2 = []
        enemies_delete_3 = []
        for index, _ in enumerate(self.list):
            self.move(index)
            self.collision_with_player(enemies_delete_1, explosion, index, player) 
            self.collision_with_shoots(enemies_delete_2, explosion, index, player, shoots_player)
            self.out_screen(enemies_delete_3)
        self.remove(enemies_delete_1, enemies_delete_2, enemies_delete_3)