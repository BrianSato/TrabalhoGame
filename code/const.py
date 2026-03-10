#Background Configuration
import pygame

ENTITY_SPEED = {
    'bg_image01': 1,
    'bg_image02': 2,
    'bg_image03': 3,
    'bg_image04': 4,
    'bg_image05': 5,
    'DIABLO': 5,
    'GENIUS': 2,
    'GENIUS_MAGIC': 5,
    'DRAGON': 3
}

#Color Condiguration
COLOR_ORANGE = (255,165,0)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)


#Character Configuration
ENTITY_HEALTH = {
'DIABLO': 5,
'GENIUS': 5,
'LITTLE_MONSTER': 3,
'MEDUSA': 3,
'DRAGON' : 10
}
FRAME_DIABLO =  [
            './assets/characters/diablo/diablo_parado01.png',
            './assets/characters/diablo/diablo_parado02.png',
            './assets/characters/diablo/diablo_parado03.png'
        ]
FRAME_DIABLO_SELECT=[
            './assets/characters/diablo/diablo_select01.png',
            './assets/characters/diablo/diablo_select02.png',
            './assets/characters/diablo/diablo_select01.png'
]
FRAME_DIABLO_WALK=[
    './assets/characters/diablo/diablo_andando01.png',
    './assets/characters/diablo/diablo_andando02.png',
    './assets/characters/diablo/diablo_andando03.png',
    './assets/characters/diablo/diablo_andando04.png',
    './assets/characters/diablo/diablo_andando05.png'
]
FRAME_DIABLO_FIGHT=[
    './assets/characters/diablo/diablo_ataque01.png',
    './assets/characters/diablo/diablo_ataque02.png',
    './assets/characters/diablo/diablo_ataque03.png'
]
FRAME_DIABLO_HIT=[
    './assets/characters/diablo/diablo_ferido01.png',
    './assets/characters/diablo/diablo_ferido02.png',
    './assets/characters/diablo/diablo_morte06.png'
]
FRAME_DIABLO_DEATH=[
    './assets/characters/diablo/diablo_morte01.png',
    './assets/characters/diablo/diablo_morte02.png',
    './assets/characters/diablo/diablo_morte03.png',
    './assets/characters/diablo/diablo_morte04.png',
    './assets/characters/diablo/diablo_morte05.png',
    './assets/characters/diablo/diablo_morte06.png',
]
FRAME_DRAGON =  [
            './assets/characters/dragon/dragon_parado01.png',
            './assets/characters/dragon/dragon_parado02.png',
            './assets/characters/dragon/dragon_parado03.png'
        ]
FRAME_DRAGON_WALK =  [
            './assets/characters/dragon/dragon_morte01.png',
            './assets/characters/dragon/dragon_andando01.png',
            './assets/characters/dragon/dragon_andando03.png'
        ]
FRAME_DRAGON_FIGHT=[
            './assets/characters/dragon/dragon_ataque04.png',
            './assets/characters/dragon/dragon_ataque03.png',
            './assets/characters/dragon/dragon_ataque02.png',
            './assets/characters/dragon/dragon_ataque03.png',
            './assets/characters/dragon/dragon_ataque04.png'
]
FRAME_DRAGON_HIT=[
            './assets/characters/dragon/dragon_machucado01.png',
            './assets/characters/dragon/dragon_machucado02.png',
            './assets/characters/dragon/dragon_ataque01.png',
            './assets/characters/dragon/dragon_ataque02.png',
            ]
FRAME_DRAGON_DEATH=[
            './assets/characters/dragon/dragon_morte01.png',
            './assets/characters/dragon/dragon_morte02.png',
            './assets/characters/dragon/dragon_morte03.png',
            './assets/characters/dragon/dragon_morte04.png',
            './assets/characters/dragon/dragon_morte05.png',
            './assets/characters/dragon/dragon_morte05.png',
            './assets/characters/dragon/dragon_morte05.png',
]
DRAGON_FIRE= './assets/characters/dragon/fire/dragon_chama02.png'

FRAME_GENIUS =  [
            './assets/characters/genius/genio_voando01.png',
            './assets/characters/genius/genio_voando02.png',
            './assets/characters/genius/genio_voando03.png',
            './assets/characters/genius/genio_voando04.png'
        ]
FRAME_GENIUS_SELECT = [
            './assets/characters/genius/genio_select01.png',
            './assets/characters/genius/genio_select02.png',
            './assets/characters/genius/genio_select01.png',

        ]
FRAME_GENIUS_WALK=[
    './assets/characters/genius/genio_voando01.png',
    './assets/characters/genius/genio_voando02.png',
    './assets/characters/genius/genio_voando03.png',
    './assets/characters/genius/genio_voando04.png'
]
FRAME_GENIUS_FIGHT=[
    './assets/characters/genius/genio_luta01.png',
    './assets/characters/genius/genio_luta02.png',
    './assets/characters/genius/genio_luta03.png',
    './assets/characters/genius/genio_luta04.png'
]

FRAME_GENIUS_HIT=[
    './assets/characters/genius/genio_machucado01.png',
    './assets/characters/genius/genio_machucado02.png',
    './assets/characters/genius/genio_machucado01.png',
    './assets/characters/genius/genio_machucado02.png',
]
FRAME_GENIUS_DEATH=[
    './assets/characters/genius/genio_morte01.png',
    './assets/characters/genius/genio_morte02.png',
    './assets/characters/genius/genio_morte03.png',
    './assets/characters/genius/genio_morte04.png',
    './assets/characters/genius/genio_morte05.png',
    './assets/characters/genius/genio_morte06.png',
]

GENIUS_MAGIC = './assets/characters/genius/magic/genio_tiro01.png'

FRAME_LITTLE_MONSTER =  [
            './assets/characters/little_monster/monstrinho_parado01.png',
            './assets/characters/little_monster/monstrinho_parado02.png',
            './assets/characters/little_monster/monstrinho_parado03.png',

        ]
FRAME_LITTLE_MONSTER_WALK =  [
            './assets/characters/little_monster/monstrinho_andando01.png',
            './assets/characters/little_monster/monstrinho_andando02.png',
            './assets/characters/little_monster/monstrinho_andando03.png',
            './assets/characters/little_monster/monstrinho_andando04.png',
            './assets/characters/little_monster/monstrinho_andando05.png',
            './assets/characters/little_monster/monstrinho_ataque01.png',
            './assets/characters/little_monster/monstrinho_ataque02.png',
            './assets/characters/little_monster/monstrinho_ataque03.png',
            './assets/characters/little_monster/monstrinho_ataque05.png'
        ]
FRAME_LITTLE_MONSTER_HIT = [
            './assets/characters/little_monster/monstrinho_machucado01.png',
            './assets/characters/little_monster/monstrinho_machucado02.png',
            './assets/characters/little_monster/monstrinho_morte03.png',
            './assets/characters/little_monster/monstrinho_morte05.png'
]
FRAME_LITTLE_MONSTER_DEATH = [
        './assets/characters/little_monster/monstrinho_morte01.png',
        './assets/characters/little_monster/monstrinho_morte02.png',
        './assets/characters/little_monster/monstrinho_morte03.png',
        './assets/characters/little_monster/monstrinho_morte04.png',
        './assets/characters/little_monster/monstrinho_morte05.png',
        './assets/characters/little_monster/monstrinho_morte06.png',
        './assets/characters/little_monster/monstrinho_morte06.png',
        './assets/characters/little_monster/monstrinho_morte06.png'
]
FRAME_MEDUSA =  [
            './assets/characters/medusa/medusa_parada01.png',
            './assets/characters/medusa/medusa_parada02.png',
            './assets/characters/medusa/medusa_parada03.png'
        ]
FRAME_MEDUSA_WALK =  [
            './assets/characters/medusa/medusa_ataque04.png',
            './assets/characters/medusa/medusa_ataque07.png'
        ]
FRAME_MEDUSA_HIT =  [
            './assets/characters/medusa/medusa_machucada01.png',
            './assets/characters/medusa/medusa_machucada02.png'
        ]
FRAME_MEDUSA_DEATH = [
        './assets/characters/medusa/medusa_morte01.png',
        './assets/characters/medusa/medusa_morte02.png',
        './assets/characters/medusa/medusa_morte03.png',
        './assets/characters/medusa/medusa_morte04.png',
        './assets/characters/medusa/medusa_morte05.png',
        './assets/characters/medusa/medusa_morte06.png',
        './assets/characters/medusa/medusa_morte06.png',
        './assets/characters/medusa/medusa_morte06.png',
]
#Events Configurations
EVENT_ENEMY = pygame.USEREVENT +1


#Menu
MENU_OPTION = (
    ' 1 - JOGAR',
    ' 2 - SAIR'
)
MENU_INSTRUCTION =(
    'Comandos do Jogo:',
    'SETAS => MOVIMENTA O JOGADOR.',
    'ESPAÇO => ATACA'
)
#Score
SCORE_HIT_ENEMY = 20
SCORE_HIT_BOSS = 50
SCORE_THRESHOLD = 100
#Spawn Configuration
SPAWN_TIME = 4000

#Window Configuration
WIN_WIDTH = 640
WIN_HEIGHT = 360