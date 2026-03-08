import pygame
from code.const import ENTITY_SPEED

class Projectile:
    def __init__(self,x,y,direction,image_path,owner):
        self.owner = owner
        self.direction = direction
        self.speed = ENTITY_SPEED['GENIUS_MAGIC']
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))

    def move(self):
        self.rect.centerx += self.speed * self.direction

    def draw(self,window):
        window.blit(self.image,self.rect)