import pygame


class ScoreKeeper(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.score = 0

        self.font = pygame.font.SysFont('comicsans', 40)
        self.image = self.font.render(str(self.score), True, (255, 255, 255))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.image = self.font.render(str(self.score), True, (255, 255, 255))
