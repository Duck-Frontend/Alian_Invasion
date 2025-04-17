import sys
import pygame
from setting import Settigns
from ship import Ship


class AlianInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.settings = Settigns()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            self.ship.update() # Обновление координат корабля на экране
            self._check_events() # Проверка нажатых клавишь
            self._update_screen() # Обновление отображения объектов на экране
            self.clock.tick(60)

    def _check_events(self):
        """Обрабатывает нажатие с клавиатуры и мыши"""
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
                
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль вправо
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlianInvasion()
    ai.run_game()
