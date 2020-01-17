import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r'images\ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def moving(self):
        if self.moving_right:
            if self.rect.centerx < self.screen_rect.right:
                self.x += self.ai_settings.ship_speed

        elif self.moving_left:
            if self.rect.centerx > 0:
                self.x -= self.ai_settings.ship_speed

        elif self.moving_up:
            if self.rect.bottom > self.screen_rect.bottom/10:
                self.y -= self.ai_settings.ship_speed

        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.y += self.ai_settings.ship_speed

    def update(self):
        self.moving()
        self.rect.centerx = self.x
        self.rect.bottom = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


   def center_ship(self):
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.bottom
