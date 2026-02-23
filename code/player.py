import pygame

from code.const import FRAME_DRAGON, FRAME_DIABLO, FRAME_GENIUS, FRAME_LITTLE_MONSTER, FRAME_MEDUSA

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame_diablo = [
            pygame.image.load(path).convert_alpha()
            for path in FRAME_DIABLO
        ]
        self.frame_dragon = [
            pygame.image.load(path).convert_alpha()
            for path in FRAME_DRAGON
        ]
        self.frame_genius = [
            pygame.image.load(path).convert_alpha()
            for path in FRAME_GENIUS
        ]
        self.frame_little_monster = [
            pygame.image.load(path).convert_alpha()
            for path in FRAME_LITTLE_MONSTER
        ]
        self.frame_medusa = [
            pygame.image.load(path).convert_alpha()
            for path in FRAME_MEDUSA
        ]
        self.frame_atual = 0
        self.animation_speed = 1000  # milissegundos
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.frame_atual = (self.frame_atual + 1) % len(self.frame_diablo)
            self.last_update = now

    def draw(self,window):
       window.blit(self.frame_diablo[self.frame_atual], (50, 260))
       window.blit(self.frame_genius[self.frame_atual], (100, 200))
       window.blit(self.frame_dragon[self.frame_atual], (430, 200))
       window.blit(self.frame_little_monster[self.frame_atual], (400, 300))
       window.blit(self.frame_medusa[self.frame_atual], (350, 280))
