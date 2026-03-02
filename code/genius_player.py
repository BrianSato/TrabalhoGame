import pygame
from code.player import Player


class Genius(Player):
    def __init__(self, x, y, frame_paths):
        super().__init__(x, y, frame_paths)

    def move(self,pressed_key):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.animate()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.animate()
        if pressed_key[pygame.K_UP]:
            self.rect.y -= self.speed
            self.animate()
        if pressed_key[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.animate()