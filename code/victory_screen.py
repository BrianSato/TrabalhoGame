import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_WHITE, WIN_WIDTH

class VictoryScreen:

    def __init__(self,window):
        self.window = window
        pass
    def screen(self,score,game_time):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'menu'

            self.window.fill((0,0,0))

            self.level_text(80, 'YOU WIN', COLOR_WHITE, 50)
            self.level_text(50, f'SCORE:{score}', COLOR_WHITE, 150)
            self.level_text(20, f'TIME:{game_time}', COLOR_WHITE, 200)
            self.level_text(20, 'PRESS ENTER TO RETURN TO MENU', COLOR_WHITE, 320)
            pygame.display.flip()


    def level_text(self, text_size, text, text_color,y):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=(WIN_WIDTH//2,y))
            self.window.blit(source=text_surf, dest=text_rect)


