import pygame
import os
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, stars_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = stars_game.screen

        # Load the star image and set its rect attribute.
        #   Star image from: https://opengameart.org/content/star
        #   License: public domain
        
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),"images", "star.png"))
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact vertical position.
        self.x = 0
        self.y = float(self.rect.y)