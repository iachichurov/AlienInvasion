class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self) -> None:
        """Инициалирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_heigth = 800
        self.background_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 обозначает движение вправо, -1 движение влево