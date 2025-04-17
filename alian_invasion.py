import sys
import pygame
from setting import Settign
from ship import Ship


class AlianInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.setting = Settign()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Обрабатывает нажатие с клавиатуры и мыши"""
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlianInvasion()
    ai.run_game()
