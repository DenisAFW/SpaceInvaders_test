import pygame
from settings import Settings
import functional as fun
from gun import Gun
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
    sb = Scoreboard(settings, screen, stats)
    play_button = Button(settings, screen, "Play")


    while True:
        clock.tick(FPS)
        fun.check_events(gun, army, settings, screen, bullets, play_button, stats, sb)
        if stats.game_active:
            gun.update()
            fun.update_bullets(settings, screen, gun, army, bullets, stats, sb)
            fun.update_aliens(settings, screen, gun, army, bullets, stats, sb)
        fun.update_screen(screen, settings, gun, bullets, army, play_button, stats, sb)


run_game()
