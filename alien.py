import pygame
from pygame.sprite import Sprite


class Army(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.load_image = pygame.image.load('images/pixil-frame-1.png')
        self.image = pygame.transform.scale(self.load_image, (50, 40))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit_army(self):
        self.screen.blit(self.image, self.rect)
