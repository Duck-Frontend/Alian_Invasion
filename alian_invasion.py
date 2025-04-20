import sys
import pygame
from setting import Settigns
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlianInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.settings = Settigns()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            self._check_events()  # Проверка нажатых клавишь
            self.ship.update()  # Обновление координат корабля на экране
            self._update_bullets()
            self._update_alian()
            self._update_screen()  # Обновление отображения объектов на экране
            self.clock.tick(60)

    def _check_events(self):
        """Обрабатывает нажатие с клавиатуры и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:  # Переместить корабль вправо
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Переместить корабль влево
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:  # Переместить корабль вверх
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:  # Переместить корабль вниз
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_alian(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_keyup_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

    def _create_fleet(self):
        """Создаёт флот пришельцев"""
        # Создание пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._creat_alian(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _creat_alian(self, x_possition, y_possition):
        new_alian = Alien(self)
        new_alian.x = x_possition
        new_alian.rect.x = x_possition
        new_alian.rect.y = y_possition
        self.aliens.add(new_alian)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Отпускает весь флои и меняет направление"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == "__main__":
    ai = AlianInvasion()
    ai.run_game()
