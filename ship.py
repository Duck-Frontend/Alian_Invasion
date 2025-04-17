import pygame


class Ship:
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
       
       # Сохранение вещественной координаты центра корабля 
        self.x = float(self.rect.x)
        
        # Флаг перемещения: начинаем с неподвижного корабля
        self.moving_right = False
        self.moving_left = False 
    
    def update(self):
        if self.moving_right:
            self.x += self.setting.ship_speed
        if self.moving_left:
            self.x -= self.setting.ship_speed
        
        self.rect.x = self.x 

    def blitme(self):
        self.screen.blit(self.image, self.rect)
