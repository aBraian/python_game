import pygame
from audio import *
from constants import *
from explosions import *
from gui import *
from shoots import *

class Player:
    
    class_type = "Player"
    
    def __init__(self, image_path, speed, axis_x, axis_y):
        image = pygame.image.load(image_path).convert_alpha()
        rect_character = image.get_rect()
        rect_character.centerx = axis_x
        rect_character.bottom = axis_y
        self.collision = pygame.Rect(rect_character.left + 8 , rect_character.top, image.get_width() - 15, image.get_height())
        self.damage_point = 25
        self.fire_mode = 0
        self.hp = 100
        self.image = image    
        self.last_shoot = 0
        self.lifes = 1
        self.name = ""
        self.rate_fire = 250
        self.rect = rect_character
        self.score = 0
        self.speed = speed
    
    def hp_bar(self, screen, color_hp, color_border, axis_x, axis_y, width, height):
        calculate_hp = self.hp * width / 100
        hp = pygame.Rect(axis_x, axis_y, calculate_hp, height)
        border_1 = pygame.Rect(axis_x, axis_y,  width / 4, height)
        border_2 = pygame.Rect(border_1.right, axis_y,  width / 4, height)
        border_3 = pygame.Rect(border_2.right, axis_y,  width / 4, height)
        border_4 = pygame.Rect(border_3.right, axis_y,  width / 4, height)
        pygame.draw.rect(screen, color_hp, hp)
        pygame.draw.rect(screen, color_border, border_1, 2)
        pygame.draw.rect(screen, color_border, border_2, 2)
        pygame.draw.rect(screen, color_border, border_3, 2)
        pygame.draw.rect(screen, color_border, border_4, 2)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.speed
            self.collision.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right <= WIDTH_SCREEN:
            self.rect.x += self.speed
            self.collision.x += self.speed
        """
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
            self.collision.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT_SCREEN:
            self.rect.y += self.speed
            self.collision.y += self.speed
        """

    def spawn_shoots(self, shoots):
        Audio(AUDIO_SHOOT).play_audio(0.5)
        first_shoot = Shoot(IMAGE_SHOOT_PLAYER, self.rect.centerx, self.rect.top)
        second_shoot = Shoot(IMAGE_SHOOT_PLAYER, self.rect.left + 8, self.rect.top + 24)
        third_shoot = Shoot(IMAGE_SHOOT_PLAYER, self.rect.right - 8, self.rect.top + 24)
        if self.fire_mode == 0:
            shoots.add(first_shoot)
        elif self.fire_mode == 1:
            shoots.add(second_shoot, third_shoot)
        else:
            shoots.add(first_shoot, second_shoot, third_shoot)

    def shoot(self, shoots):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shoot > self.rate_fire:
                self.last_shoot = now 
                self.spawn_shoots(shoots)   
                
    def collision_with_shoots(self, shoots):
        shoots_delete = []
        for shoot in shoots.list:
            if self.collision.colliderect(shoot.rect):
                Audio(AUDIO_IMPACT).play_audio(0.5)
                shoots_delete.append(shoot)
                self.hp -= self.damage_point
        shoots.remove(shoots_delete)
                
    def no_lifes(self):
        return_value = False
        if self.lifes < 0:
            return_value = True
        return return_value
                
    def lose_life(self):
        if self.hp <= 0:
            self.lifes -= 1
            return True
    
    def kill(self, explosion, axis_x, axis_y):
        if self.lose_life():
            Audio(AUDIO_EXPLOSION).play_audio(0.5)
            explosion.add(Explosion(self.rect.center, "Player"))
            self.fire_mode = 0
            self.hp = 100
            self.rect.centerx = axis_x
            self.rect.bottom = axis_y
            self.collision.center = self.rect.center
                
    def update(self, explosion, shoots_enemy, shoots_player, axis_x, axis_y):
        self.collision_with_shoots(shoots_enemy)
        self.move()
        self.shoot(shoots_player)
        self.kill(explosion, axis_x, axis_y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)