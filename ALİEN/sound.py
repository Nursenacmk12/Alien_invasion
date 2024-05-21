import pygame

class Sound():
    def __init__(self, sounds_file):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sounds_file)

    def play(self, loops=0):
        self.sound.play(loops=loops)

    def stop(self):
        self.sound.stop()
    
    def set_volume(self, volume):
        self.sound.set_volume(volume)

lazer_sound = Sound("lazer_sound.wav")
lazer_sound.play()
lazer_sound.set_volume(0.5)
lazer_sound.stop()




