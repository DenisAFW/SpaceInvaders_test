import sys
import pygame
from bullets import Bullets
from alien import Army


def update_screen(screen, settings, gun, bullets, army, play_button, stats, sb):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.blit_gun()
    army.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_events(gun, army, settings, screen, bullets, play_button, stats, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, gun, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, gun)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(gun, army, settings, screen, play_button, bullets, stats, sb, mouse_x, mouse_y)


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


def update_bullets(settings, screen, gun, army, bullets, stats, sb):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))

    check_bullet_alien_collision(settings, screen, gun, army, bullets, stats, sb)


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


def check_army_edges(settings, army):
    for alien in army.sprites():
        if alien.check_edges():
            change_army_direction(settings, army)
            break


def change_army_direction(settings, army):
    for alien in army.sprites():
        alien.rect.y += settings.y_drop_distance
    settings.army_direction *= -1


def check_bullet_alien_collision(settings, screen, gun, army, bullets, stats, sb):
    bullets.update()
    collisions = pygame.sprite.groupcollide(bullets, army, True, True)

    if collisions:
        for army in collisions.values():
            stats.score += settings.alien_points * len(army)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(army) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()

        create_fleet(settings, screen, gun, army)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_army_bottom(settings, screen, gun, army, bullets, stats, sb):
    screen_rect = screen.get_rect()
    for alien in army.sprites():
        if alien.rect.bottom >= (screen_rect.bottom - settings.gun_height):
            death_gun(settings, stats, screen, gun, army, bullets, sb)


def death_gun(settings, stats, screen, gun, army, bullets, sb):
    if stats.gun_lives > 0:
        stats.gun_lives -= 1

        army.empty()
        bullets.empty()
        create_fleet(settings, screen, gun, army)
        gun.center_ship()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_play_button(gun, army, settings, screen, play_button, bullets, stats, sb, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        army.empty()
        bullets.empty()

        create_fleet(settings, screen, gun, army)
        gun.center_ship()


def update_aliens(settings, screen, gun, army, bullets, stats, sb):
    check_army_edges(settings, army)
    army.update()
    check_army_bottom(settings, screen, gun, army, bullets, stats, sb)
    if pygame.sprite.spritecollide(gun, army, True):
        print("Gun dead")
