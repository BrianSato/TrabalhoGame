import pygame.image
from code.player import Player

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/background_menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.player = Player(70,250)

    def run(self, ):
        #play the background music
        pygame.mixer_music.load('./assets/sounds/sound_menu.mp3')
        pygame.mixer_music.play(-1)
        self.player.update()

        while True:
            self.window.blit(source=self.surf,dest=self.rect)
            self.player.update()
            self.player.draw(self.window)
            pygame.display.flip()
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end game


