class Settigns:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Настроики корабля
        self.ship_speed = 3.5
        
        # Параметры снаряда
        self.bullet_speed = 5.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        # Параметри пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1