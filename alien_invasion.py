import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien 👽 Invasion 🛸")

        self.ship = Ship(self)

        # set the background color
        self.bg_color = (77, 0, 153)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """ respond to keypresses and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ respond to keypresses """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_F1:
            self._fullscreen()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """ update images on the screen and flip to the new screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _fullscreen(self):
        """ instead of automaticallly setting to fullscreen like the book,
        gives the option to change to fullscreen by pressing F1 """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # ship is not centered properly need to figure out how to redraw
        self.ship.blitme()


if __name__ == '__main__':
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
