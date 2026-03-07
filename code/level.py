import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code import entity
from code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, SCORE_THRESHOLD
from code.dragon import Dragon
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.projectile import Projectile


class Level:
    def __init__(self,window, name,player):
        self.timeout = 20000  # 20segundos
        self.window = window
        self.name = name
        self.score = 0
        self.dragons_spawned = False
        self.dragons_spawn_event = pygame.USEREVENT + 1
        self.projectiles_list = []
        self.entity_bg_list : list[entity] = []
        self.entity_bg_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity(player,x=20,y=265)
        self.entity_players_list = [self.player]
        self.entity_enemies_list = []
        self.boss_list = []
        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)


    def run(self):
        pygame.mixer_music.stop()
        pygame.mixer_music.load('./assets/sounds/sound02.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            pressed_key = pygame.key.get_pressed()
            displacement_x = 0

            #calcula deslocamento baseado no player
            for player in self.entity_players_list:
                displacement_x += player.move(pressed_key,self)
                player.animate()
            #move background
            for bg in self.entity_bg_list:
                bg.move(displacement_x)
                bg.draw(self.window)
            #desenha player depois (fica na frente)
            for player in self.entity_players_list:
                player.draw(self.window)
            #desenha inimigos
            for enemy in self.entity_enemies_list:
                enemy.draw(self.window)
                enemy.move()
            #desenha Boss
            for boss in self.boss_list:
                boss.draw(self.window)
                boss.move()

            #desenha tiro
            for projectile in self.projectiles_list:
                projectile.draw(self.window)
                projectile.move()

            EntityMediator.verify_collision(self)
            print(f'Score: {self.score},dragon_spawened:{self.dragons_spawned} ')
            if self.player.score >= SCORE_THRESHOLD and not self.dragons_spawned:
                dragon = EntityFactory.get_entity('DRAGON')
                dragon.level = self
                self.boss_list.append(dragon)
                self.dragons_spawned = True
                print(f'DRAGON entrou no jogo Vida : {dragon.life}')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('LITTLE_MONSTER','MEDUSA'))
                    self.entity_enemies_list.append(EntityFactory.get_entity(choice))


            pygame.display.flip()

            # printed text
            total_entities = (len(self.entity_players_list) + len(self.entity_enemies_list)+len(self.entity_bg_list))
            self.level_text(14, f'{self.name} - Timeout:{self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'{clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades:{total_entities}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            self.level_text(14, f'Score:{self.score}', COLOR_WHITE, (100, WIN_HEIGHT - 20))
            pygame.display.flip()
            pass

    def level_text(self, text_size, text, text_color, text_pos):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
