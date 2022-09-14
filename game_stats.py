class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game) -> None:
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        # Игра запускается в неактивном состоянии
        self.game_active = False
        # Рекорд не должен сбрасываться
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit