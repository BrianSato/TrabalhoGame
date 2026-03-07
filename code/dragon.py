import random

import pygame

from code import level
from code.const import ENTITY_HEALTH, ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, FRAME_DRAGON_FIGHT, DRAGON_FIRE
from code.enemy import Enemy
from code.projectile import Projectile


class Dragon(Enemy):
    def __init__(self, name, position, frame_walk,frame_hit,projectile=None):
        super().__init__(name, position, frame_walk,frame_hit)
        #Atributos extras do Dragon
        self.name = name
        self.projectile = projectile #utilizado pro tiro
        self.life = ENTITY_HEALTH['DRAGON']
        #direções e velocidade do movimentos do Dragon
        self.speed_x = ENTITY_SPEED[self.name]
        self.speed_y = ENTITY_SPEED[self.name]
        self.direction_x = random.choice([-1,0,1])
        self.direction_y = random.choice([-1,0,1])
        self.change_dir_timer = pygame.time.get_ticks()
        self.change_dir_interval = 1000
        #efeitos de movimento
        self.taking_hit = False
        self.last_frame_update = pygame.time.get_ticks()
        self.frame_interval = 100
        self.frame_atual = 0
        #tiros
        self.min_shoot_cooldown = 1000
        self.max_shoot_cooldown = 3000
        self.last_shoot = 0
        self.next_shoot_time = random.randint(self.min_shoot_cooldown,self.max_shoot_cooldown)
        self.last_shoot = pygame.time.get_ticks()


    def move(self):
        now = pygame.time.get_ticks()
        frames = self.frame_hit if self.taking_hit else self.frame_walk
        # animação dos frames
        if now - self.last_frame_update > self.frame_interval:
            self.frame_atual = (self.frame_atual + 1) % len(frames)
            self.image = frames[self.frame_atual]
            self.last_frame_update = now

        if self.taking_hit and self.frame_atual == len(frames) - 1:
            self.taking_hit = False
            self.frame_atual = 0

        estado = 'HIT' if self.taking_hit else 'WALK'
        print(f'[DEBUG] {self.name} está animado: {estado} - Frame atual: {self.frame_atual}')

        # movimento aleatório:
        if now - self.change_dir_timer > self.change_dir_interval:
            self.direction_x = random.choice([-1, 0, 1])
            self.direction_y = random.choice([-1, 0, 1])
            self.change_dir_timer = now

        self.x += self.speed_x * self.direction_x
        self.y += self.speed_y * self.direction_y

        # Mantém dentro da tela
        self.x = max(WIN_WIDTH // 2, min(self.x, WIN_WIDTH - self.rect.width))
        self.y = max(0, min(self.y, WIN_HEIGHT - self.rect.height))
        self.rect.topleft = self.x, self.y

        self.fire(self.level)

    def fire(self,level):
        now = pygame.time.get_ticks()

        if now - self.last_shoot > self.next_shoot_time:
            projectile = Projectile(self.rect.left - 30, self.rect.centery,-1, DRAGON_FIRE, 'DRAGON')
            level.projectiles_list.append(projectile)
            self.last_shoot = now
            self.next_shoot_time = random.randint(self.min_shoot_cooldown, self.max_shoot_cooldown)



