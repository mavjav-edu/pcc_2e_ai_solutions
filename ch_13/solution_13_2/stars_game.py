import sys
from random import randint

import pygame
from settings import Settings
from star import Star


class StarsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """Create a sky full of stars."""
        # Create an star and find the number of stars in a row.
        # Spacing between each star is equal to two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size if star.rect is not None else (0,0)
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        #   We'll just fill most of the screen with stars.
        available_space_y = self.settings.screen_height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        # Fill the sky with stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size if star.rect is not None else (0,0)
        if star.rect is not None:
            star.rect.x = star_width + 2 * star_width * star_number
            star.rect.y = star.rect.height + 2 * star.rect.height * row_number

        # Randomize the positions of the stars.
        #  This effect looks much better with a tiny star. If you're curious,
        #  you might want to play around with the spacing a little.
        if star.rect is not None:
            star.rect.x += randint(-5, 5)
            star.rect.y += randint(-5, 5)

        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sg = StarsGame()
    sg.run_game()
