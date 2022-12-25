import pygame
from pygame.gfxdraw import aacircle, filled_circle
from random import randint
import math


def new_speed():
    speed = randint(5, 7)
    speed = -speed if randint(0, 1) else speed
    return speed


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius):
        super().__init__()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill((255, 0, 0))
        self.image.set_colorkey((255, 0, 0))
        aacircle(self.image, self.radius, self.radius, self.radius, (255, 255, 255))
        filled_circle(self.image, self.radius, self.radius, self.radius, (255, 255, 255))
        
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center=self.area.center)

        self.x_speed = new_speed()
        self.y_speed = new_speed()
        self.speed = 10

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

    def bounce_x(self, paddle):
        top = paddle.rect.top
        bottom = paddle.rect.bottom

        if paddle.side == 'right':
            angle = translate(self.rect.y, top, bottom, 225, 135)
        elif paddle.side == 'left':
            angle = translate(self.rect.y, top, bottom, -45, 45)

        self.x_speed = self.speed * math.cos(math.radians(angle))
        self.y_speed = self.speed * math.sin(math.radians(angle))

    def reset(self):
        self.x_speed = new_speed()
        self.y_speed = new_speed()
        self.rect.center = self.area.center
