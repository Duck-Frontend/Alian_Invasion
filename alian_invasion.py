import sys
import pygame # type: ignore
from setting import Settign


class AlianInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.setting = Settign()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.setting.bg_color)
            # Отображение последнего прорисовоного экрана
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlianInvasion()
    ai.run_game()
