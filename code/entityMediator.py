from code.entity import Entity

class EntityMediator:

    @staticmethod
    def verify_collision(level):
        for players in level.entity_players_list:
            for enemy in level.entity_enemies_list:
                if players.rect.colliderect(enemy.rect):
                    #impede de atravessar
                    if players.rect.centerx < enemy.rect.centerx:
                        enemy.take_hit()
                        players.rect.right = enemy.rect.left
                    else:
                        players.rect.left = enemy.rect.right
                    if enemy.life <=0:
                        level.entity_enemies_list.remove(enemy)



            EntityMediator.__verify_collision_window(level)
        pass

    @staticmethod
    def __verify_collision_window(level):
        for enemy in level.entity_enemies_list[:]:
            # remove se sair da tela
            if enemy.x < -100:
                level.entity_enemies_list.remove(enemy)
        pass
