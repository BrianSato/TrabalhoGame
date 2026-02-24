import pygame

class Player:
    def __init__(self,x,y,frame_paths):
        self.x = x
        self.y = y
        self.frames = [
            pygame.image.load(path).convert_alpha()
            for path in frame_paths
        ]
        self.frame_atual = 0
        self.animation_speed = 1000  # milissegundos
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)
            self.last_update = now

    def draw(self,window):
       window.blit(self.frames[self.frame_atual], (self.x,self.y))

