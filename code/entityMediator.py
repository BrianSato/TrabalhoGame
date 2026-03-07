from code import player, projectile
from code.const import WIN_WIDTH, SCORE_HIT_ENEMY
from code.entity import Entity
from code.player import Player
from code.projectile import Projectile


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
                    if enemy.life <=0:
                        if enemy in level.entity_enemies_list:
                            #passar chamada de morte do inimigo
                            level.entity_enemies_list.remove(enemy)
                        elif enemy in level.boss_list:
                            #passar chamada de morte do Boss
                            level.boss_list.remove(enemy)
                        players.add_score(SCORE_HIT_ENEMY)
                    if players.life <= 0 and players in level.entity_players_list:
                        # adicionar chamada de frames da morte do player
                        # passar chamada da tela de game over com score e tempo de jogo.
                        level.entity_players_list.remove(players)
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
                        print("Boss list:", level.boss_list)
                        if projectiles.rect.colliderect(enemy.rect):
                            enemy.take_hit_enemy()
                            print('COLISAO DETECTADA', type(enemy))

                            print(f'{projectiles.owner.name} {enemy.life} acertou!Score agora:{projectiles.owner.score}')
                            level.projectiles_list.remove(projectiles)
                        if enemy.life <=0:
                            if enemy in level.entity_enemies_list:
                                level.entity_enemies_list.remove(enemy)
                            elif enemy in level.boss_list:
                                level.boss_list.remove(enemy)
                            projectiles.owner.add_score(SCORE_HIT_ENEMY)

                elif projectiles.owner == 'DRAGON':
                    if projectiles.rect.colliderect(level.player.rect):
                        level.player.take_hit()
                        print('Player atingido pelo Dragon!')
                        if projectiles in level.projectiles_list[:]:
                            print("Projectile owner:", projectiles.owner)
                            level.projectiles_list.remove(projectiles)


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
