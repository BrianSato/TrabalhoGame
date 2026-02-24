import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import FRAME_DIABLO, FRAME_GENIUS, FRAME_DRAGON, FRAME_LITTLE_MONSTER, FRAME_MEDUSA, COLOR_ORANGE, \
    WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_BLACK, MENU_INSTRUCTION, COLOR_BLUE
from code.player import Player

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_menu.png')
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
            self.draw_text(50, "Space", (COLOR_BLACK), ((WIN_WIDTH / 2), 100))
            self.draw_text(50, "Heroes", (COLOR_BLACK), ((WIN_WIDTH / 2), 150))

            for i in range(len(MENU_OPTION)):
                self.draw_text(20, MENU_OPTION[i], COLOR_BLUE, ((WIN_WIDTH / 2), 220 + 30 * i))

            for i in range(len(MENU_INSTRUCTION)):
                self.draw_text(10, MENU_INSTRUCTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 280 + 15 * i))

            for character in self.characters:
                character.update()
                character.draw(self.window)

            pygame.display.flip()
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end game

    def draw_text(self, text_size,text, text_color, text_center_pos):
        text_font = pygame.font.Font("./assets/fonts/BrunoAceSC-Regular.ttf",int(text_size))
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)