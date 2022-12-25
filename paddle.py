import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, side):
        super().__init__()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.side = side

        self.x = 20 if self.side == 'left' else self.area.right - 20
        self.y = self.area.height / 2

        self.steps = 0

        self.image = pygame.Surface((20, 100))
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.move(self.steps)

    def move(self, steps):
        self.rect = self.rect.move(0, steps)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.area.bottom:
            self.rect.bottom = self.area.bottom
