import pygame
from pygame import K_RETURN

from code.const import COLOR_BLACK, WIN_WIDTH, FRAME_DIABLO_SELECT, FRAME_GENIUS_SELECT, COLOR_WHITE, COLOR_ORANGE, \
    COLOR_BLUE
from code.level import Level
from code.player import Player


class CharacterSelect:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_escolher_jogador.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.selected_character = 0
        self.state = 'select'
        self.characters = [
            Player(40, 180, FRAME_DIABLO_SELECT),
            Player(220, 180, FRAME_GENIUS_SELECT),
        ]
        self.characters_names = ['DIABLO','GENIUS']

    def run(self):
        # play the background music
        pygame.mixer_music.load('./assets/sounds/sound_menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            for index,character in enumerate(self.characters):
                character.update()
                character.draw(self.window)

                if self.selected_character == index:
                    if self.state == 'select':
                        color = (COLOR_ORANGE)
                    elif self.state == 'confirm':
                        color = (COLOR_BLUE)
                else:
                    color = (COLOR_BLACK)

                self.menu_characters(
                    text_size = 30,
                    text = self.characters_names[index],
                    color = color,
                    character_rect = character.rect
                )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()# end game
                if event.type == pygame.KEYDOWN:
                    if self.state == 'select':
                        if event.key == pygame.K_RIGHT :
                            self.selected_character += 1
                            if self.selected_character >= len(self.characters):
                                self.selected_character = 0 #volta pro início
                        if event.key == pygame.K_LEFT:
                            self.selected_character -= 1
                            if self.selected_character < 0 :
                                self.selected_character = len(self.characters) -1
                        if event.key in (pygame.K_RETURN,pygame.K_KP_ENTER):
                            self.state = 'confirm'

                    elif self.state == 'confirm':
                        if event.key in (pygame.K_RETURN,pygame.K_KP_ENTER):
                            level = Level(self.window,'Level1')
                            level_start = level.run()
                            return self.selected_character
                if self.state == 'confirm':
                    self.menu_start(
                        text_size=30,
                        text='ENTER PARA JOGAR!',
                        color=(COLOR_BLUE),
                        x=520,
                        y=320
                    )

                pygame.display.flip()

    def menu_characters(self, text_size, text, color,character_rect):
        text_font = pygame.font.Font("./assets/fonts/Bangers-Regular.ttf", size=text_size)
        text_surf = text_font.render(text,True,color)
        text_rect = text_surf.get_rect(center=(character_rect.centerx,character_rect.bottom - 180))
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_start(self, text_size, text, color,x,y):
        text_font = pygame.font.Font("./assets/fonts/Bangers-Regular.ttf", size=text_size)
        text_surf = text_font.render(text,True,color)
        text_rect = text_surf.get_rect(center=(x,y))
        self.window.blit(source=text_surf, dest=text_rect)

