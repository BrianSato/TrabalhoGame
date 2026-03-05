import random

import pygame
from code.background import Background
from code.const import WIN_WIDTH, FRAME_DIABLO_WALK, FRAME_GENIUS, FRAME_GENIUS_WALK, FRAME_LITTLE_MONSTER_WALK, \
    FRAME_MEDUSA_WALK, FRAME_DRAGON_WALK, WIN_HEIGHT, FRAME_DIABLO_FIGHT, FRAME_GENIUS_FIGHT
from code.diablo_player import Diablo
from code.enemy import Enemy
from code.genius_player import Genius
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name,x=100,y=300):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'bg_image0{i+1}',(0,0)))
                    list_bg.append(Background(f'bg_image0{i+1}', (WIN_WIDTH, 0)))
                return list_bg
            case 'DIABLO':
                player = Diablo(x,y,FRAME_DIABLO_WALK,FRAME_DIABLO_FIGHT)
                return player
            case 'GENIUS':
                player = Genius(x, y, FRAME_GENIUS_WALK,FRAME_GENIUS_FIGHT)
                return player
            case 'LITTLE_MONSTER':
                frame_path = FRAME_LITTLE_MONSTER_WALK
                enemy = Enemy('LITTLE_MONSTER',(WIN_WIDTH +10, (WIN_HEIGHT -45)),frame_path)
                return enemy
            case 'MEDUSA':
                frame_path = FRAME_MEDUSA_WALK
                enemy = Enemy('MEDUSA', (WIN_WIDTH + 10, (WIN_HEIGHT - 150)), frame_path)
                return enemy
            #case 'DRAGON':
            #    frame_path = FRAME_DRAGON_WALK
            #    player = Dragon(x, y, frame_path)
            #    return player
        pass
