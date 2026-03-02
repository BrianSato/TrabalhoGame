import pygame.image
from pygame import Surface, Rect, K_KP1, K_KP2
from pygame.font import Font

from code.const import FRAME_DIABLO, FRAME_GENIUS, FRAME_DRAGON, FRAME_LITTLE_MONSTER, FRAME_MEDUSA, COLOR_ORANGE, \
    WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_BLACK, MENU_INSTRUCTION, COLOR_BLUE
from code.player import Player

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_principal.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.characters = [
            Player(50,260,FRAME_DIABLO),
            Player(100, 200, FRAME_GENIUS),
            Player(470, 200, FRAME_DRAGON),
            Player(470, 300, FRAME_LITTLE_MONSTER),
            Player(440, 280, FRAME_MEDUSA)
        ]

    def run(self, ):
        #play the background music
        pygame.mixer_music.load('./assets/sounds/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf,dest=self.rect)

            for character in self.characters:
                character.animate()
                character.draw(self.window)

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()# end game
                if event.type == pygame.KEYDOWN:
                    if event.unicode == '1':
                        return 'char_select'
                    if event.unicode == '2':
                        pygame.quit()
                        quit()
            pygame.display.flip()