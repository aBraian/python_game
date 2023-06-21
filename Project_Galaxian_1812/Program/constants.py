import os

archive_folder = os.path.dirname(__file__)
game_folder = os.path.dirname(archive_folder)

#Audio
audio_folder = os.path.join(game_folder, "Audios")
audio_effects = os.path.join(audio_folder, "Effects")
audio_music = os.path.join(audio_folder, "Music")

#Audio - Effect
AUDIO_BUTTON = os.path.join(audio_effects, "Button.mp3")
AUDIO_BUTTON_SELECT = os.path.join(audio_effects, "Button_Select.mp3")
AUDIO_EXPLOSION = os.path.join(audio_effects, "Explosion.mp3")
AUDIO_IMPACT = os.path.join(audio_effects, "Hit.mp3")
AUDIO_POWER_UP = os.path.join(audio_effects, "Pick_Power_Up.mp3")
AUDIO_SHOOT = os.path.join(audio_effects, "Laser_Bullet.mp3")

#Audio - Music
AUDIO_LEVEL_1 = os.path.join(audio_music, "Cyber_Attack.mp3")
AUDIO_LEVEL_2 = os.path.join(audio_music, "Pepper_Steak.mp3")
AUDIO_LEVEL_3 = os.path.join(audio_music, "Bloodbath.mp3")
AUDIO_MAIN_MENU = os.path.join(audio_music, "Geometry_Dash_Menu.mp3")

#Colors RGB
BLACK = (0, 0, 0)
BLUE = (0, 108, 255)
GOLDEN = (217, 191, 75)
GREEN = (0, 193, 93)
RED = (255, 0, 58)
SILVER = (192, 192, 192)
VIOLET = (112, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 232, 17)

#Database
DATABASE = os.path.join(game_folder, "Galaxian_DB.db")

#Fonts
font_folder = os.path.join(game_folder, "Font")
ETNOCENTRIC = os.path.join(font_folder, "ethnocentric rg.otf")       
VICTORY_COMICS = os.path.join(font_folder, "victorycomicsexpand.ttf")
TWITCH = os.path.join(font_folder, "Twitchy.TV.ttf")

#Fps
FPS = 60

#Image
image_folder = os.path.join(game_folder, "Images")
image_background = os.path.join(image_folder, "Background") 
image_gui = os.path.join(image_folder, "Gui")
image_icon = os.path.join(image_folder, "Icon") 
image_power_ups = os.path.join(image_folder, "Power_Up")
image_shoots = os.path.join(image_folder, "Shoots")
image_spaceships = os.path.join(image_folder, "Spaceships")

#Image - Background
IMAGE_BACKGROUND_1 = os.path.join(image_background, "Background_1.png")
IMAGE_BACKGROUND_2 = os.path.join(image_background, "Background_2.png")
IMAGE_BACKGROUND_3 = os.path.join(image_background, "Background_3.jpg")
IMAGE_BACKGROUND_4 = os.path.join(image_background, "Background_4.png")
IMAGE_BACKGROUND_5 = os.path.join(image_background, "Background_5.png")
IMAGE_BACKGROUND_6 = os.path.join(image_background, "Background_6.png")

#Image - Enemies
IMAGE_ENEMY_1 = os.path.join(image_spaceships, "Enemy_1.png")
IMAGE_ENEMY_2 = os.path.join(image_spaceships, "Enemy_2.png")
IMAGE_ENEMY_3 = os.path.join(image_spaceships, "Enemy_3.png")
IMAGE_ENEMY_4 = os.path.join(image_spaceships, "Enemy_4.png") 

#Image - Gui
IMAGE_CLOCK = os.path.join(image_gui, "Clock_Icon_Gui.png")
IMAGE_GAME_NAME = os.path.join(image_gui, "Game_Name.png")
IMAGE_LIFES = os.path.join(image_gui, "Player_Gui.png")
IMAGE_SOUND_OFF = os.path.join(image_gui, "Sound_Off_Gui.png")
IMAGE_SOUND_ON = os.path.join(image_gui, "Sound_On_Gui.png")
IMAGE_STAR = os.path.join(image_gui, "Star_Gui.png")
IMAGE_WINDOW = os.path.join(image_gui,"Window_Gui.png")

#Image - Icon
IMAGE_ICON = os.path.join(image_icon, "Hangar_BTN.png")

#Image - Player
IMAGE_PLAYER = os.path.join(image_spaceships, "Player_1.png")

#Image - Power Ups
IMAGE_AMMO = os.path.join(image_power_ups, "Damage_Icon.png")
IMAGE_HEALTH = os.path.join(image_power_ups, "HP_Icon.png")

#Image - Shoots
IMAGE_SHOOT_ENEMY = os.path.join(image_shoots, "Laser_Bullet_2.png")
IMAGE_SHOOT_PLAYER = os.path.join(image_shoots, "Laser_Bullet_1.png")

#Screen
HEIGHT_SCREEN = 700
WIDTH_SCREEN = 525