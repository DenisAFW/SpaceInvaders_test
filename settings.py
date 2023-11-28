class Settings:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        """Настройки экрана"""
        self.screen_width = 700
        self.screen_height = 800
        self.bg_color = self.black

        """Настройки пушки"""
        self.gun_speed = 0.75
        self.gun_height, self.gun_width = 70, 44
        self.gun_limit = 3

        """Настройки пули"""
        self.bullet_speed = 3
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = self.red
        self.bullet_allowed = 30

        """Настройки флота"""
        self.army_direction = 1

        """Настройки ускорения игры"""
        self.speed_up = 1.2
        self.score_scale = 0.75
        self.dynamic_settings()

        self.alien_points = 50

    def dynamic_settings(self):
        self.alien_speed = 10
        self.y_drop_distance = 5

    def increase_speed(self):
        """Увеличение темпа игры"""
        self.alien_speed *= self.speed_up
        self.y_drop_distance *= self.speed_up

        self.alien_points = int(self.alien_points * self.score_scale)
