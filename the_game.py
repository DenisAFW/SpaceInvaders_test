import pygame
from settings import Settings
import functional as fun
from gun import Gun
from pygame.sprite import Group


def run_game():
    FPS = 200
    clock = pygame.time.Clock()
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Звездный позор")
    gun = Gun(screen, settings)
    bullets = Group()
    army = Group()
    fun.create_fleet(settings, screen, gun, army)

    while True:
        clock.tick(FPS)
        fun.events(gun, settings, screen, bullets)
        gun.update()
        fun.update_bullets(bullets)

        fun.update_screen(screen, settings, gun, bullets, army)


run_game()
