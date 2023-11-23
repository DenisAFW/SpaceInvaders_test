import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen, settings):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.image2 = pygame.transform.scale(self.image, (70, 44))
        self.rect = self.image2.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.settings = settings

        self.movement = float(self.rect.centerx)

        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.movement += self.settings.gun_speed
        elif self.move_left and self.rect.left > 0:
            self.movement -= self.settings.gun_speed

        self.rect.centerx = self.movement

    def blit_gun(self):
        self.screen.blit(self.image2, self.rect)

    def center_ship(self):
        self.movement = self.screen_rect.centerx
