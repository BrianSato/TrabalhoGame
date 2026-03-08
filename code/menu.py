import pygame.image
from code.const import FRAME_DIABLO, FRAME_GENIUS, FRAME_DRAGON, FRAME_LITTLE_MONSTER, FRAME_MEDUSA
from code.menu_character import MenuCharacter

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_principal.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.characters = [
            MenuCharacter('DIABLO',50,260,FRAME_DIABLO),
            MenuCharacter('GENIUS',100, 200, FRAME_GENIUS),
            MenuCharacter('DRAGON',470, 200, FRAME_DRAGON),
            MenuCharacter('LITTLE_MONSTER',470, 300, FRAME_LITTLE_MONSTER),
            MenuCharacter('MEDUSA',440, 280, FRAME_MEDUSA)
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