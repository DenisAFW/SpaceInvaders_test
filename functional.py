import sys

import pygame
from bullets import Bullets
from alien import Army


def update_screen(screen, settings, gun, bullets, army):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.blit_gun()
    army.draw(screen)

    pygame.display.flip()


def events(gun, settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, gun, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, gun)


def check_keydown_events(event, gun, settings, screen, bullets):
    if event.key == pygame.K_a:
        gun.move_left = True
    elif event.key == pygame.K_d:
        gun.move_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, gun, bullets)


def check_keyup_events(event, gun):
    if event.key == pygame.K_a:
        gun.move_left = False
    elif event.key == pygame.K_d:
        gun.move_right = False


def fire_bullet(settings, screen, gun, bullets):
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullets(settings, screen, gun)
        bullets.add(new_bullet)


def update_bullets(bullets):
    for bullet in bullets.copy():
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_alien(settings, screen, army, army_number, row_number):
    alien = Army(settings, screen)
    alien_width = alien.rect.width - 25
    alien.x = alien_width + 2 * alien_width * army_number
    alien.rect.x = alien.x
    alien_height = alien.rect.height - 10
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y
    army.add(alien)


def create_fleet(settings, screen, gun, army):
    alien = Army(settings, screen)
    number_columns = get_number_column(settings, alien.rect.width)
    number_rows = get_number_rows(settings, gun.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_columns):
            create_alien(settings, screen, army, alien_number, row_number)


# Рассчет кол-ва строк и столбцов для создания флота
def get_number_column(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_columns = int(available_space_x / (alien_width))
    return number_columns


def get_number_rows(settings, gun_height, alien_height):
    avilable_space_y = settings.screen_height - (3 * alien_height) - gun_height
    number_rows = int(avilable_space_y / (3 * alien_height))
    return number_rows


def update_aliens(settings, screen, gun, army, bullets):
    army.update()
