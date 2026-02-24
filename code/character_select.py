import pygame
from pygame import Surface, Rect

from code.const import COLOR_BLACK, WIN_WIDTH, FRAME_DIABLO_SELECT, FRAME_GENIUS_SELECT
from code.player import Player


class CharacterSelect:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_escolher_jogador01.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.characters = [
            Player(50, 170, FRAME_DIABLO_SELECT),
            Player(260, 190, FRAME_GENIUS_SELECT),
        ]

    def run(self):
        # play the background music
        pygame.mixer_music.load('./assets/sounds/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            for character in self.characters:
                character.update()
                character.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()# end game

            pygame.display.flip()

