import pygame
import random
from audio import *
from constants import *
from explosions import *
from shoots import *

class E3: 

    class_type = "E3"

    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_character = image.get_rect()
        self.enemy_input_1 = True
        self.enemy_input_2 = True
        self.image = image
        self.image_path = image_path
        self.last_shoot = pygame.time.get_ticks()
        self.lifes = 5
        self.rate_fire = random.randrange(1500, 2000)
        self.rect = rect_character
        self.rect.left = 0
        self.rect.bottom = 0
        self.speed = 5
        self.speed_input = 5
        
    def shoot(self, shoots):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.rate_fire:
            self.last_shoot = now 
            self.spawn_shoots(shoots)
        
    def spawn_shoots(self, shoots):
        Audio(AUDIO_SHOOT).play_audio(0.5)
        first_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.rect.centerx, self.rect.bottom)
        second_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.rect.left + 10, self.rect.bottom - 20)
        third_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.rect.right - 10, self.rect.bottom - 20)
        shoots.add(first_shoot, second_shoot, third_shoot)

class E3Sprites():

    class_type = "E3Sprites"

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
                    player.score += 1500
                    list_delete.append(self.list[index])
        shoots.remove(shoots_delete)
        
    def draw(self, screen):
        for enemy in self.list:
            screen.blit(enemy.image, enemy.rect)
            
    def move(self, index):
        if self.list[index].enemy_input_1 or self.list[index].enemy_input_2:
            self.list[index].rect.y += self.list[index].speed_input
            if self.list[index].rect.bottom > HEIGHT_SCREEN * (3/4):
                self.list[index].enemy_input_1 = False
                self.list[index].speed_input *= (-1)
            elif self.list[index].enemy_input_1 == False and self.list[index].rect.bottom < HEIGHT_SCREEN * (1/4):
                self.list[index].enemy_input_2 = False
        else:
            self.list[index].rect.x += self.list[index].speed
            if self.list[index].rect.left < 0:
                self.list[index].speed = self.list[index].speed * (-1)
            if self.list[index].rect.right > WIDTH_SCREEN:
                self.list[index].speed = self.list[index].speed * (-1)
    
    def remove(self, *args):
        for list_delete in args:
            if list_delete != None and len(list_delete) > 0:
                for enemy_delete in list_delete:
                    if enemy_delete in self.list:
                        self.list.remove(enemy_delete)
            
    def spawn(self, enemy, quantity, reference_x):
        if len(self.list) <= 0:
            flag = True
            for i in range(quantity):
                enemy_copy = E3(enemy.image_path)
                if flag:
                    enemy_copy.rect.x = enemy_copy.rect.width 
                    previous_enemy = enemy_copy.rect.x
                    flag = False
                else:
                    enemy_copy.rect.x = previous_enemy + (enemy_copy.rect.width * reference_x * i) 
                self.add(enemy_copy)
    
    def update(self, explosion, player, shoots_enemy, shoots_player):
        delete_enemies_1 = []
        delete_enemies_2 = []
        for index, _ in enumerate(self.list):
            self.move(index)
            self.collision_with_player(delete_enemies_1, explosion, index, player) 
            self.collision_with_shoots(delete_enemies_2, explosion, index, player, shoots_player)
            self.list[index].shoot(shoots_enemy)
        self.remove(delete_enemies_1, delete_enemies_2)