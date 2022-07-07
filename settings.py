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