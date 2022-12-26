import pygame


class AudioPlayer():

    def __init__(self) -> None:
        pass

    def play_sound(self, sound_file):
        sound = pygame.mixer.Sound(sound_file)
        return sound