import pygame
from settings import Settings
import functional as fun
from gun import Gun
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    FPS = 150
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
    stats = GameStats(settings)
    play_button = Button(settings, screen, "Play")

    while True:
        clock.tick(FPS)
        fun.check_events(gun, army, settings, screen, bullets, play_button, stats)
        if stats.game_active:
            gun.update()
            fun.update_bullets(settings, screen, gun, army, bullets, stats)
            fun.update_aliens(settings, screen, gun, army, bullets)
        fun.update_screen(screen, settings, gun, bullets, army, play_button, stats)


run_game()
