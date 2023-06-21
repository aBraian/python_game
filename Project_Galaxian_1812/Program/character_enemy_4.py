import pygame
from audio import *
from constants import *
from explosions import *
from gui import *
from shoots import *

class E4:
    
    class_type = "E4"
    
    def __init__(self, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        rect_character = image.get_rect()
        self.collision = pygame.Rect(rect_character.x , rect_character.y, image.get_width() - 40, image.get_height())
        self.input_enemy = True
        self.image = image
        self.last_shoot = pygame.time.get_ticks()
        self.lifes = 200
        self.rate_fire = 1500
        self.rect = rect_character
        self.rect.centerx = WIDTH_SCREEN / 2
        self.rect.bottom = 0
        self.speed_x = -6
        self.speed_y = -6
        self.speed_input = 5
        
    def check_lifes(self):
        if self.lifes < 0:
            return True
        
    def collision_with_player(self, player):
        if self.rect.colliderect(player.collision):
            player.hp -= 30

    def collision_with_shoots(self, explosion, player, shoots):
        shoots_delete = []    
        for shoot in shoots.list:
            if self.collision.colliderect(shoot.rect):
                shoots_delete.append(shoot)
                self.lifes -= 1
                if self.check_lifes():
                    Audio(AUDIO_EXPLOSION).play_audio(0.5)
                    explosion.add(Explosion(self.rect.center, "Enemy"))
                    player.score += 100000
                else:
                    Audio(AUDIO_IMPACT).play_audio(0.5)
        shoots.remove(shoots_delete)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self):
        if self.input_enemy:
            self.rect.y += self.speed_input
            self.collision.centerx = self.rect.centerx
            self.collision.centery = self.rect.centery
            if self.rect.bottom > HEIGHT_SCREEN * (3/4):
                self.input_enemy = False
        else:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collision.centerx = self.rect.centerx
            self.collision.centery = self.rect.centery
            if self.rect.left < 0:
                self.speed_x = self.speed_x * (-1)
            if self.rect.right > WIDTH_SCREEN:
                self.speed_x = self.speed_x * (-1)
            if self.rect.top < 0:
                self.speed_y = self.speed_y * (-1)
            if self.rect.bottom > HEIGHT_SCREEN * (3/4):
                self.speed_y = self.speed_y * (-1)

    def shoot(self, shoots):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.rate_fire:
            self.last_shoot = now 
            self.spawn_shoots(shoots)
        
    def spawn_shoots(self, shoots):
        Audio(AUDIO_SHOOT).play_audio(0.5)
        first_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.collision.right + 8, self.rect.bottom - self.collision.height / 2)
        second_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.collision.left - 8, self.rect.bottom - self.collision.height / 2)
        third_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.collision.right - 8, self.rect.bottom - self.collision.height / 2 + 16)
        fourth_shoot = Shoot(IMAGE_SHOOT_ENEMY, self.collision.left + 8, self.rect.bottom - self.collision.height / 2 + 16)
        shoots.add(first_shoot, second_shoot, third_shoot, fourth_shoot)

    def upgrade(self):
        if self.lifes == 100:
            self.rate_fire = 1000
        
class E4Sprites:
    
    class_type = "E4Sprites"
    
    def __init__(self):
        self.list = []    
    
    def add(self, enemy):
        self.list.append(enemy) 
        
    def copy(self):
        list_aux = []
        for enemy in self.list:
            list_aux.append(enemy)
        return list_aux
        
    def draw(self, screen):
        for enemy in self.list:
            screen.blit(enemy.image, enemy.rect)
        
    def remove(self):
        list_aux = self.copy()
        if len(self.list) > 0:
            for enemy in list_aux: 
                if enemy.check_lifes():
                    self.list.remove(enemy)
                    return True
                    
    def update(self, explosion, player, shoots_enemies, shoots_player):
        for enemy in self.list:
            enemy.move()
            enemy.collision_with_player(player)
            enemy.collision_with_shoots(explosion, player, shoots_player)
            enemy.shoot(shoots_enemies)
            enemy.upgrade()
        if self.remove():
            return True
        
    