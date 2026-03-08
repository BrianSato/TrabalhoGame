import pygame
from code.const import ENTITY_HEALTH, ENTITY_SPEED, GENIUS_MAGIC
from code.projectile import Projectile


class Player:
    def __init__(self, name,x, y, frame_walk,frame_hit=None,frame_fight=None,frame_death=None):
        self.name = name
        self.score = 0
        #carregar frames
        self.frames_walk = self.load_frames(frame_walk)
        self.frames_hit = self.load_frames(frame_hit) if frame_hit else None
        self.frames_fight = self.load_frames(frame_fight) if frame_fight else None
        self.frames_death = self.load_frames(frame_death) if frame_death else None

        #Estado inicial
        self.frames = self.frames_walk
        self.frame_atual = 0
        if not self.frames:
            raise ValueError(f'{self.name} não recebeu frames de animação')

        #Controle de Animação
        self.animation_speed = 100   # milissegundos
        self.last_update = pygame.time.get_ticks()
        #Posição
        self.rect = self.frames[0].get_rect(topleft=(x,y))
        self.speed = ENTITY_SPEED[self.name]
        #Estados
        self.fighting = False
        self.taking_hit = False
        #Vida
        self.life = ENTITY_HEALTH[self.name]
        #knockback
        self.knockback = 0

    def load_frames(self,frame_path):
        frames = []
        for frame in frame_path:
            frames.append(pygame.image.load(frame).convert_alpha())
        return frames

    def animate(self):
        now = pygame.time.get_ticks()
        if not self.fighting and not self.taking_hit and not getattr(self,'moving',False):
            self.frame_atual = 0
            self.image = self.frames[self.frame_atual]
            return
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_atual += 1
            if self.frame_atual >= len(self.frames):
                if self.taking_hit:
                    self.taking_hit = False
                    self.frames = self.frames_walk
                elif self.fighting:
                    self.fighting = False
                    self.frames = self.frames_walk
                self.frame_atual = 0
        self.image = self.frames[self.frame_atual]

    def move(self,displacement_x,level):
        self.rect.x += displacement_x
        return displacement_x

    def fight(self):
        if self.frames_fight and not self.fighting and not self.taking_hit:
            self.fighting = True
            self.frames = self.frames_fight
            self.frame_atual = 0
            self.image = self.frames[0]

    def magic(self,level):
        projectile = Projectile(self.rect.centerx+50, self.rect.centery, 1, GENIUS_MAGIC, self)
        level.projectiles_list.append(projectile)

    def take_hit(self):
        if not self.taking_hit and self.frames_hit:
            self.life -= 1
            self.taking_hit = True
            self.frames = self.frames_hit
            self.frame_atual = 0
            #empurrão
            self.knockback = 50

    def player_death(self):
        self.frames = self.frames_death
        self.frame_atual = 0

    def add_score(self, points):
        self.score += points

    def draw(self,window):
       window.blit(self.image, self.rect)
