import pygame
import random
from explosions import *
from audio import *
from constants import *
from shoots import *

class E1: 

    class_type = "E1"

    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_character = image.get_rect()
        self.enemy_input = True
        self.image = image
        self.image_path = image_path
        self.last_shoot = pygame.time.get_ticks()
        self.lifes = 2
        self.rate_fire = random.randrange(2000, 2500)
        self.rect = rect_character
        self.rect.left = 0
        self.rect.bottom = 0
        self.speed_x = random.choice([-7, -6, -5])
        self.speed_y = random.choice([-7, -6, -5])
        
    def shoot(self, shoots):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.rate_fire:
            self.last_shoot = now 
            self.spawn_shoots(shoots)
        
    def spawn_shoots(self, shoots):
        Audio(AUDIO_SHOOT).play_audio(0.5)
        shoot = Shoot(IMAGE_SHOOT_ENEMY, self.rect.centerx, self.rect.bottom)
        shoots.add(shoot)

class E1Sprites():

    class_type = "E1Sprites"

    def __init__(self):
        self.list = []

    def add(self, enemy):
        self.list.append(enemy)
        
    def collision_with_player(self, list_delete, explosion, index, player):
        if self.list[index].rect.colliderect(player.collision):
            Audio(AUDIO_EXPLOSION).play_audio(0.5)
            explosion.add(Explosion(self.list[index].rect.center, "Enemy"))
            list_delete.append(self.list[index])
            player.hp -= 25

    def collision_with_shoots(self, list_delete, explosion, index, player, shoots):
        shoots_delete = []    
        for shoot in shoots.list:
            if self.list[index].rect.colliderect(shoot.rect):
                shoots_delete.append(shoot)
                self.list[index].lifes -= 1
                if self.list[index].lifes > 0:
                    Audio(AUDIO_IMPACT).play_audio(0.5)
                else:
                    Audio(AUDIO_EXPLOSION).play_audio(0.5)
                    explosion.add(Explosion(self.list[index].rect.center, "Enemy"))
                    player.score += 500
                    list_delete.append(self.list[index])
        shoots.remove(shoots_delete)
        
    def draw(self, screen):
        for enemy in self.list:
            screen.blit(enemy.image, enemy.rect)
            
    def move(self, index):
        if self.list[index].enemy_input:
            self.list[index].rect.y += 5
            if self.list[index].rect.bottom > HEIGHT_SCREEN / 2:
                self.list[index].enemy_input = False
        elif self.list[index].enemy_input == False:
            self.list[index].rect.x += self.list[index].speed_x
            self.list[index].rect.y += self.list[index].speed_y
            if self.list[index].rect.left < 0:
                self.list[index].speed_x = self.list[index].speed_x * (-1)
            if self.list[index].rect.right > WIDTH_SCREEN:
                self.list[index].speed_x = self.list[index].speed_x * (-1)
            if self.list[index].rect.top < 0:
                self.list[index].speed_y = self.list[index].speed_y * (-1)
            if self.list[index].rect.bottom > HEIGHT_SCREEN / 2:
                self.list[index].speed_y = self.list[index].speed_y * (-1)
    
    def remove(self, *args):
        for list_delete in args:
            if list_delete != None and len(list_delete) > 0:
                for enemy_delete in list_delete:
                    if enemy_delete in self.list:
                        self.list.remove(enemy_delete)
    
    def respawn(self, enemy, quantity, reference_x, reference_y):
        if len(self.list) <= 0:
            self.spawn(enemy, quantity, reference_x, reference_y)
            
    def spawn(self, enemy, quantity, reference_x, reference_y):
        for i in range(quantity):
            enemy_copy = E1(enemy.image_path)
            enemy_copy.rect.x = (enemy_copy.rect.x + enemy_copy.rect.width) * reference_x + (i * enemy_copy.rect.width)  
            enemy_copy.rect.bottom = enemy_copy.rect.bottom - enemy_copy.rect.height * reference_y
            self.add(enemy_copy)
    
    def update(self, explosion, player, shoots_enemy, shoots_player):
        delete_items_1 = []
        delete_items_2 = []
        for index, _ in enumerate(self.list):
            self.move(index)
            self.collision_with_player(delete_items_1, explosion, index, player) 
            self.collision_with_shoots(delete_items_2, explosion, index, player, shoots_player)
            self.list[index].shoot(shoots_enemy)
        self.remove(delete_items_1, delete_items_2)