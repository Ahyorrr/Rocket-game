import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, rg):
        """creating object for bullet"""
        super().__init__()
        self.screen = rg.screen
        self.settings = rg.settings
        self.color = rg.settings.bullet_colour

        # creating rect for bullet and positioning it
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_length)
        self.rect.midtop = rg.rocket.rect.midtop

        # storing bullet rect as float
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullets up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """drawing the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
