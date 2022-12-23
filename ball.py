import pygame
from random import randint


def new_speed():
    speed = randint(5, 7)
    speed = -speed if randint(0, 1) else speed
    return speed


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius):
        super().__init__()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image = self.image.convert_alpha()
        self.image.fill((255, 0, 0))
        self.image.set_colorkey((255, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect(center=self.area.center)

        self.x_speed = new_speed()
        self.y_speed = new_speed()

    def update(self):
        self.edges()
        self.rect = self.rect.move(self.x_speed, self.y_speed)

    def edges(self):
        top = self.rect.y - self.radius
        bottom = self.rect.y + self.radius
        if top < 0 or bottom > self.area.bottom:
            self.bounce_y()

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset(self):
        self.x_speed = new_speed()
        self.y_speed = new_speed()
        self.rect.center = self.area.center