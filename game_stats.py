class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False

        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.gun_lives = self.settings.gun_limit
        self.score = 0
