import pygame

from code.entity import Entity


class Player:
    def __init__(self, x, y, frame_walk,frame_fight=None):
        #Walk
        self.frames_walk = [
            pygame.image.load(path).convert_alpha()
            for path in frame_walk
        ]
        #Fight(opcional)
        if frame_fight:
            self.frames_fight = [
                pygame.image.load(path).convert_alpha()
                for path in frame_fight
            ]
        else:
            self.frames_fight = None
        #Estado atual
        self.frames = self.frames_walk
        self.frame_atual = 0
        #Controle de Animação
        self.animation_speed = 100   # milissegundos
        self.last_update = pygame.time.get_ticks()
        #Movimento
        self.rect = self.frames[0].get_rect(topleft=(x,y))
        self.speed = 5
        #Estado de ataque
        self.fighting = False

    def animate(self):
        now = pygame.time.get_ticks()
        if not self.fighting and not getattr(self,'moving',False):
            self.frame_atual = 0
            self.image = self.frames[self.frame_atual]
            return
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_atual += 1
            if self.frame_atual >= len(self.frames):
                if self.fighting:
                    #terminou ataque -> volta walk
                    self.fighting = False
                    self.frames = self.frames_walk
                self.frame_atual = 0
        self.image = self.frames[self.frame_atual]

    def move(self,displacement_x):
        self.rect.x += displacement_x
        return displacement_x

    def fight(self):
        if self.frames_fight and not self.fighting:
            self.fighting = True
            self.frames = self.frames_fight
            self.frame_atual = 0

    def draw(self,window):
       window.blit(self.frames[self.frame_atual], self.rect)

