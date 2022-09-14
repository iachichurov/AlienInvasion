class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self) -> None:
        """Инициалирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_heigth = 800
        self.background_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        # Настройки пришельцев
        self.fleet_drop_speed = 8
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 3.6
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 0.6
        self.fleet_direction = 1  # 1 обозначает движение вправо, -1 движение влево
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)