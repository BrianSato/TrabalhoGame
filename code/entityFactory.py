from code.background import Background
from code.const import WIN_WIDTH, FRAME_DIABLO_WALK, FRAME_GENIUS_WALK, FRAME_LITTLE_MONSTER_WALK, \
    FRAME_MEDUSA_WALK, FRAME_DRAGON_WALK, WIN_HEIGHT, FRAME_DIABLO_FIGHT, FRAME_GENIUS_FIGHT, FRAME_LITTLE_MONSTER_HIT, \
    FRAME_MEDUSA_HIT, FRAME_DIABLO_HIT, FRAME_GENIUS_HIT, FRAME_DRAGON_HIT, FRAME_DIABLO_DEATH, FRAME_GENIUS_DEATH, \
    FRAME_MEDUSA_DEATH, FRAME_DRAGON_DEATH, FRAME_LITTLE_MONSTER_DEATH
from code.diablo_player import Diablo
from code.dragon import Dragon
from code.enemy import Enemy
from code.genius_player import Genius


class EntityFactory:

    @staticmethod
    def get_entity(entity_name, x=100, y=300):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'bg_image0{i + 1}', (0, 0)))
                    list_bg.append(Background(f'bg_image0{i + 1}', (WIN_WIDTH, 0)))
                return list_bg
            case 'DIABLO':
                player = Diablo(x, y, FRAME_DIABLO_WALK, FRAME_DIABLO_HIT, FRAME_DIABLO_FIGHT, FRAME_DIABLO_DEATH)
                return player
            case 'GENIUS':
                player = Genius(x, y, FRAME_GENIUS_WALK, FRAME_GENIUS_HIT, FRAME_GENIUS_FIGHT, FRAME_GENIUS_DEATH)
                return player
            case 'LITTLE_MONSTER':
                enemy = Enemy('LITTLE_MONSTER', (WIN_WIDTH + 10, (WIN_HEIGHT - 45)), FRAME_LITTLE_MONSTER_WALK,
                              FRAME_LITTLE_MONSTER_HIT, FRAME_LITTLE_MONSTER_DEATH)
                return enemy
            case 'MEDUSA':
                enemy = Enemy('MEDUSA', (WIN_WIDTH + 10, (WIN_HEIGHT - 150)), FRAME_MEDUSA_WALK, FRAME_MEDUSA_HIT,
                              FRAME_MEDUSA_DEATH)
                return enemy
            case 'DRAGON':
                enemy = Dragon('DRAGON', (WIN_WIDTH - 10, (WIN_HEIGHT - 150)), FRAME_DRAGON_WALK, FRAME_DRAGON_HIT,
                               FRAME_DRAGON_DEATH)
                return enemy
