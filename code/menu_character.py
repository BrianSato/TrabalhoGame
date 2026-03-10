import pygame

from code.const import ENTITY_SPEED

class MenuCharacter:
    def __init__(self, name, x, y, frame_path):
        self.name = name
        self.frames = []

        for frame in frame_path:
            self.frames.append(pygame.image.load(frame).convert_alpha())

        self.frame_atual = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        # Controla a animação
        self.animation_speed = ENTITY_SPEED[self.name]
        self.last_update = pygame.time.get_ticks()

    def animate(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_atual += 1
            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0
        self.image = self.frames[self.frame_atual]

    def draw(self, window):
        window.blit(self.frames[self.frame_atual], self.rect)
