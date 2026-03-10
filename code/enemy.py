import pygame

from code.const import ENTITY_HEALTH


class Enemy:
    def __init__(self, name, position, frame_walk, frame_hit=None, frame_death=None):
        self.name = name
        self.x, self.y = position
        self.frame_walk = self.load_frames(frame_walk)
        self.frame_hit = self.load_frames(frame_hit) if frame_hit else None
        self.frame_death = self.load_frames(frame_death) if frame_death else None
        self.frames = self.frame_walk
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 2
        self.life = ENTITY_HEALTH[self.name]
        self.taking_hit = False
        self.enemy_is_death = False
        self.knockback = 0

    def take_hit_enemy(self):
        if not self.taking_hit:
            self.life -= 1
            self.taking_hit = True
            self.frames = self.frame_hit
            self.frame_atual = 0
            # empurrão
            self.knockback = 20

    def enemy_death(self):
        if not self.enemy_is_death:
            self.enemy_is_death = True
            self.frames = self.frame_death
            self.frame_atual = 0

    def load_frames(self, frame_path):
        frames = []
        for frame in frame_path:
            frames.append(pygame.image.load(frame).convert_alpha())
        return frames

    def move(self):
        # se estiver na animação de morte, não se move
        if self.enemy_is_death:
            self.frame_atual += 0.2
            if self.frame_atual >= len(self.frames):
                self.frame_atual = len(self.frames) - 1
            self.image = self.frames[int(self.frame_atual)]
            return
        # movimento horizontal simples
        self.x -= self.speed
        self.rect.topleft = (self.x, self.y)
        # animação simples
        self.frame_atual += 0.2
        if self.frame_atual >= len(self.frames):
            if self.taking_hit:
                self.taking_hit = False
                self.frames = self.frame_walk
            self.frame_atual = 0
        self.image = self.frames[int(self.frame_atual)]
        # empurrão
        if self.knockback > 0:
            self.x += 4
            self.knockback -= 1
        self.rect.topleft = (self.x, self.y)

    def draw(self, window):
        window.blit(self.image, self.rect)
        pass
