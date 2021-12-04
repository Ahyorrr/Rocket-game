import sys
import pygame
from rg_settings import Settings
from rocket import Rocket
from bullet import Bullet


class RocketGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.length))
        pygame.display.set_caption('ROCKET GAME')
        self.rocket = Rocket(self)
        self.bullet = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self.bullet.update()
            # removing bullets that have disappeared
            for bullet in self.bullet.copy():
                if bullet.rect.bottom <= 0:
                    self.bullet.remove(bullet)

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        if event.key == pygame.K_UP:
            self.rocket.move_up = True
        if event.key == pygame.K_DOWN:
            self.rocket.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self):
        self.rocket.move_left = False
        self.rocket.move_right = False
        self.rocket.move_up = False
        self.rocket.move_down = False

    def _fire_bullet(self):
        """firing new bullets"""
        new_bullets = Bullet(self)
        self.bullet.add(new_bullets)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitrocket()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()
