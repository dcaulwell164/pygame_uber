
import pygame
class Mixer:
    def __init__(self):
        pygame.mixer.init()
        self.channelsUsed = 0

    def play_sound(self, name, volume, repeat):
        path = f"assets/sounds/{name}.mp3"

        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        sound.play(repeat)

    # channel = self.channelsUsed

    # pygame.mixer.music.load(path)
    # pygame.mixer.Channel(channel).music.play(repeat)
    # 