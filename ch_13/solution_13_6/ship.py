import os
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),"images", "rocket_small.png"))
        self.rect = self.image.get_rect()

        # Start each new ship at the center of the left side of the screen.
        self.center_ship()

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect.
        if self.moving_up and self.rect.top if self.rect is not None else 1 > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom if self.rect is not None else 0 < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y
        if self.rect is not None:
            self.rect.y = int(self.y)

    def center_ship(self):
        """Center the ship on the left side of the screen."""
        if self.rect is not None:
            self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y if self.rect is not None else 0)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
