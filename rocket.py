import pygame


class Rocket:
    def __init__(self, rg):
        self.screen = rg.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rg.settings


        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.speed
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitrocket(self):
        self.screen.blit(self.image, self.rect)
