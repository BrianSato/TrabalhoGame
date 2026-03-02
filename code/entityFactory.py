import pygame
from code.background import Background
from code.const import WIN_WIDTH, FRAME_DIABLO_WALK, FRAME_GENIUS, FRAME_GENIUS_WALK
from code.diablo_player import Diablo
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
                frame_path = FRAME_DIABLO_WALK
                player = Diablo(x,y,frame_path)
                return player
            case 'GENIUS':
                frame_path = FRAME_GENIUS_WALK
                player = Genius(x, y, frame_path)
                return player

        pass
