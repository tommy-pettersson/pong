from pygame.sprite import Sprite
from pygame.display import get_surface
from pygame.font import SysFont


class ScoreKeeper(Sprite):

    def __init__(self, x, y):
        super().__init__()
        screen = get_surface()
        self.area = screen.get_rect()

        self.score = 0

        self.font = SysFont('comicsans', 40)
        self.image = self.font.render(str(self.score), True, (255, 255, 255))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.image = self.font.render(str(self.score), True, (255, 255, 255))
