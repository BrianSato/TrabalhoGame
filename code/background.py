from code.const import ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, displacement_x=0):
        self.rect.x -= displacement_x * ENTITY_SPEED[self.name]
        # impede sair pela esquerda
        if self.rect.left > 0:
            self.rect.left = 0
        # se a imagem sair totalmente da tela, reinicia
        if self.rect.right <= 0:
            self.rect.left = 0
        return displacement_x

    def draw(self, window):
        window.blit(self.surf, self.rect)
        # desenha segunda cópia ao lado
        window.blit(self.surf, (self.rect.x + self.surf.get_width(), self.rect.y))
