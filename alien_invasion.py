import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize the game and build a screen class
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen.width, ai_settings.screen.length)
    )
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption('Alien Invasion')
    bullets = Group()

    # Start the circulation of the game
    while True:
        # Monitor the keyboard and mouse event
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
