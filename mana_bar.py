import pygame

BLUE = (0, 0, 128)
class ManaBar(pygame.sprite.Sprite):

    def update(self):
        self.get_mana()

    def get_mana(self):
        return self.mana
    
    def set_mana(self, ammount):
        self.mana += ammount
        self.image = pygame.Surface((self.mana, 20))
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)


    def __init__(self, mana, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.mana = mana
        self.image = pygame.Surface((mana, 20))
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)