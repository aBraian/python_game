import pygame
from gui import *

class Audio:

    class_type = "Audio"

    def __init__(self, audio_path, name = ""):
        audio = pygame.mixer.Sound(audio_path)
        self.audio = audio
        self.muted = False
        self.name = name

    def mute_icon(self, screen, audio_off, audio_on):
        if self.muted:
            audio_off.draw(screen)
        else:
            audio_on.draw(screen)
            
    def check_mute(self):
        if self.muted:
            self.audio.set_volume(0.0)
        else:
            self.audio.set_volume(1.0)

    def play_audio(self, volume_level, playback_time = 0):
        self.audio.set_volume(volume_level)
        self.audio.play(playback_time)
        
    def stop_audio(self):
        self.audio.stop()
        
class AudioSprites:
    
    class_type = "AudioSprites"
    
    def __init__(self):
        self.dict = {}
        
    def add(self, *args):
        for audio in args:
            self.dict.update({audio.name : audio})
        
    def get_audio(self, name):
        for key, value in self.dict.items():
            if key == name:
                return value
                break 
        
    def mute(self):
        for audio in self.dict.values():
            audio.muted = not audio.muted