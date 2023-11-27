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

        """Настройки пули"""
        self.bullet_speed = 3
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = self.red
        self.bullet_allowed = 30

        """Настройки флота"""

        self.y_drop_distance = 5
        self.alien_speed = 0.1
        self.army_direction = 1

        """Настройки ускорения игры"""
        self.speed_up = 1.1

    def increase_speed(self):
        """Увеличение темпа игры"""
        self.alien_speed *= self.speed_up
