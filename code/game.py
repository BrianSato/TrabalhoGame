import pygame
from code.character_select import CharacterSelect
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.game_over_screen import GameOverScreen
from code.level import Level
from code.menu import Menu
from code.victory_screen import VictoryScreen


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_state = 'menu'
        self.menu = Menu(self.window)
        self.char_select = CharacterSelect(self.window)
        self.game_start = None
        self.victory = VictoryScreen(self.window)
        self.game_over = GameOverScreen(self.window)

    def run(self):

        while True:

            if self.current_state == 'menu':
                self.current_state = self.menu.run()
            elif self.current_state == 'char_select':
                selected_index = self.char_select.run()
                player_instance = self.char_select.characters_names[selected_index]
                self.game_start = Level(self,self.window,'Level1',player_instance)
                self.current_state = 'game_start'
            elif self.current_state == 'game_start':
                self.game_start.run()
            elif self.current_state == 'victory':
                self.current_state = self.victory.screen(self.game_start.player.score,self.game_start.game_time)
                self.current_state = 'menu'
            elif self.current_state == 'game_over':
                self.current_state = self.game_over.screen(self.game_start.player.score,self.game_start.game_time)
                self.current_state = 'menu'



            self.clock.tick(60)