import pygame
from code.player import Player


class Diablo(Player):
    def __init__(self, x, y, frame_paths):
        super().__init__(x, y, frame_paths)
        self.pressed_key = pygame.key.get_pressed()
        # fisica do pulo
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_force = -15
        self.is_jumping = False
        self.moving = False
        self.ground_level = y  # posição inicial do chão

    def move(self,pressed_key):
        self.moving = False
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.moving = True
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.moving = True
        # Pulo(apenas se não estiver pulando)
        if pressed_key[pygame.K_UP] and not self.is_jumping:
            self.vel_y = self.jump_force
            self.is_jumping = True
        # Aplicar gravidade
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        # Checar se voltou ao chão
        if self.rect.y >= self.ground_level:
            self.rect.y = self.ground_level
            self.vel_y = 0
            self.is_jumping = False
        if self.moving:
            self.animate()
        else:
            self.frame_atual = 0