import pygame
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name,position = (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'bg_image0{i+1}',(0,0)))
                    list_bg.append(Background(f'bg_image0{i+1}', (WIN_WIDTH, 0)))
                return list_bg
        pass
