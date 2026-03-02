import pygame

from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity

class Background(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

    def draw(self, window):
        window.blit(self.surf,self.rect)


