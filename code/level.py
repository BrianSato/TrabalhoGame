import pygame
from code import entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self,window, name):
        self.window = window
        self.name = name
        self.entity_list : list[entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        pygame.mixer_music.stop()
        pygame.mixer_music.load('./assets/sounds/sound02.mp3')
        pygame.mixer_music.play()
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,dest=ent.rect)
                ent.move()
            pygame.display.flip()
