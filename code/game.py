import pygame

from code.character_select import CharacterSelect
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_state = 'menu'
        self.menu = Menu(self.window)
        self.char_select = CharacterSelect(self.window)
        self.game_start = None


    def run(self):

        while True:

            if self.current_state == 'menu':
                self.current_state = self.menu.run()
            elif self.current_state == 'char_select':
                selected_index = self.char_select.run()
                player_instance = self.char_select.characters_names[selected_index]
                self.game_start = Level(self.window,'Level1',player_instance)
                self.current_state = 'game_start'

            elif self.current_state == 'game_start':
                self.game_start.run()
                self.current_state = 'menu'


            self.clock.tick(60)