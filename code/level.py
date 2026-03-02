import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code import entity
from code.const import COLOR_WHITE, WIN_HEIGHT
from code.entityFactory import EntityFactory

class Level:
    def __init__(self,window, name,selected_character):
        self.selected_character = selected_character
        self.window = window
        self.name = name
        self.entity_bg_list : list[entity] = []
        self.entity_bg_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_players_list =[]
        entity_name = 'DIABLO' if self.selected_character == 0 else 'GENIUS'
        self.entity_players_list.append(EntityFactory.get_entity(entity_name,x=20,y=270))
        self.timeout = 20000 #20segundos

    def run(self):
        pygame.mixer_music.stop()
        pygame.mixer_music.load('./assets/sounds/sound02.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            pressed_key = pygame.key.get_pressed()
            clock.tick(60)
            for bg in self.entity_bg_list:
                bg.move()
                bg.draw(self.window)
            for player in self.entity_players_list:
                player.move(pressed_key)
                player.draw(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

            # printed text
            self.level_text(14, f'{self.name} - Timeout:{self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'{clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades:{len(self.entity_bg_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            pass

    def level_text(self, text_size, text, text_color, text_pos):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
