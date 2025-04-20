import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings

        # Загрузга изображенния пришельца
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизантальной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца вправо"""
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """Возвращает True если пришелец находиться у края экрана"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
