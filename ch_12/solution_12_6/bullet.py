import pygame
from pygame.sprite import Sprite
from sideways_shooter import SidewaysShooter


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ss_game: SidewaysShooter):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midright = ss_game.ship.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        if self.rect is not None:
            self.rect.x = int(self.x)

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        if self.rect is not None:
            pygame.draw.rect(self.screen, self.color, self.rect)
