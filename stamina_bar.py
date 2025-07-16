import pygame

GREEN = (0, 128, 0)
class StaminaBar(pygame.sprite.Sprite):

    def update(self):
        self.get_stamina()

    def get_stamina(self):
        return self.stamina
    
    def set_stamina(self, ammount):
        self.stamina += ammount
        self.image = pygame.Surface((self.stamina, 20))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)


    def __init__(self, stamina, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.stamina = stamina
        self.image = pygame.Surface((stamina, 20))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)