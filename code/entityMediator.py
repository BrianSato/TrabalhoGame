import pygame

from code.const import WIN_WIDTH, SCORE_HIT_ENEMY
from code.player import Player

class EntityMediator:

    @staticmethod
    def verify_collision(level):
        #colisão player com inimigos
        all_collision = level.entity_enemies_list + level.boss_list
        for players in level.entity_players_list[:]:
            for enemy in all_collision[:]:
                if players.rect.colliderect(enemy.rect):
                    #impede de atravessar
                    if players.rect.centerx < enemy.rect.centerx:
                        players.rect.right = enemy.rect.left
                    else:
                        players.rect.left = enemy.rect.right
                    if players.fighting:
                        enemy.take_hit_enemy()
                    else:
                        players.take_hit()
                    if enemy.life <=0 and not enemy.enemy_is_death:
                        enemy.enemy_death()
                        players.add_score(SCORE_HIT_ENEMY)
                    for enemy in level.entity_enemies_list[:]:
                        if enemy.enemy_is_death and enemy.frame_atual >= len(enemy.frames) - 1:
                            level.entity_enemies_list.remove(enemy)
                    for enemy in level.boss_list:
                        if enemy.enemy_is_death and enemy.frame_atual >= len(enemy.frames) - 1:
                            if level.victory_time is None:
                                level.victory_time = pygame.time.get_ticks()

                    if players.life <= 0 and players in level.entity_players_list:
                        players.player_death()
                        for players in level.entity_players_list[:]:
                            if players.is_death and players.frame_atual >= len(players.frames) - 1:
                                level.entity_players_list.remove(players)
                        if level.game_over_timer is None:
                            level.game_over_timer = pygame.time.get_ticks()
                    break
        #Colisão inimigo com BOSS
        for boss in level.boss_list[:]:
            for enemy in level.entity_enemies_list[:]:
                if boss.rect.colliderect(enemy.rect):
                    #impede de atravessar
                    if boss.rect.centerx < enemy.rect.centerx:
                        boss.rect.right = enemy.rect.left
                    else:
                        boss.rect.left = enemy.rect.right
        #Colisão de tiros com inimigos(MEDUSA,LITTLE_MONSTER e BOSS)
        all_enemies = level.entity_enemies_list + level.boss_list
        for projectiles in level.projectiles_list[:]:
                #Se o dono for Player,adiciona SCORE
                if isinstance(projectiles.owner,Player):
                    for enemy in all_enemies[:]:
                        if projectiles.rect.colliderect(enemy.rect):
                            enemy.take_hit_enemy()
                            if projectiles in level.projectiles_list:
                                level.projectiles_list.remove(projectiles)
                                break
                elif projectiles.owner == 'DRAGON':
                    if projectiles.rect.colliderect(level.player.rect):
                        level.player.take_hit()
                        if projectiles in level.projectiles_list[:]:
                            level.projectiles_list.remove(projectiles)
                        if level.player.life <= 0 and level.player in level.entity_players_list:
                            level.player.player_death()
                            for level.player in level.entity_players_list[:]:
                                if level.player.is_death and level.player.frame_atual >= len(level.player.frames) - 1:
                                    level.entity_players_list.remove(level.player)
                            if level.game_over_timer is None:
                                level.game_over_timer = pygame.time.get_ticks()
        for enemy in all_enemies[:]:
            if enemy.life <=0 and not enemy.enemy_is_death:
                enemy.enemy_death()
                level.player.add_score(SCORE_HIT_ENEMY)
            for enemy in level.entity_enemies_list[:]:
                if enemy.enemy_is_death and enemy.frame_atual >= len(enemy.frames) - 1:
                    level.entity_enemies_list.remove(enemy)
            for enemy in level.boss_list:
                if enemy.life <=0 and enemy.frame_atual >= len(enemy.frames) - 1:
                    enemy.enemy_death()
                    if level.victory_timer is None:
                        level.victory_timer = pygame.time.get_ticks()

        EntityMediator.__verify_collision_window(level)

    @staticmethod
    def __verify_collision_window(level):
        for enemy in level.entity_enemies_list[:]:
            # remove se sair da tela
            if enemy.x < -100:
                level.entity_enemies_list.remove(enemy)
        for projectile in level.projectiles_list[:]:
            if projectile.rect.x > WIN_WIDTH or projectile.rect.x < -50:
                level.projectiles_list.remove(projectile)
        pass
