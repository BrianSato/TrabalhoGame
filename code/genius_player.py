import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player

class Genius(Player):
    def __init__(self, x, y, frame_walk,frame_hit,frame_fight):
        super().__init__('GENIUS',x, y, frame_walk,frame_hit,frame_fight)
        self.pressed_key = pygame.key.get_pressed()

    def move(self,pressed_key,level):
        displacement_x = 0
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.speed
            displacement_x = - self.speed
            self.animate()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            displacement_x =  self.speed
            self.animate()
        if pressed_key[pygame.K_UP]:
            self.rect.y -= self.speed
            self.animate()
        if pressed_key[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.animate()
        if pressed_key[pygame.K_SPACE] and not self.fighting:
            self.fight()
            self.magic(level)
        #impede sair pela esquerda
        if self.rect.left < 0:
            self.rect.left = 0
        #impede sair pela direita
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        # impede sair por cima
        if self.rect.top < 0:
            self.rect.top = 0
        # impede sair por baixo
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

        return displacement_x