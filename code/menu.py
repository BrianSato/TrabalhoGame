#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/background_menu.png')
        self.rect = self.surf.get_rect(left=0,top=0)

    def run(self, ):
        #play the background music
        pygame.mixer_music.load('./assets/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf,dest=self.rect)
            pygame.display.flip()
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end game


