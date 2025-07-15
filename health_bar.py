import pygame

RED = (255, 0, 0)
class HealthBar(pygame.sprite.Sprite):

    def update(self):
        self.get_health()

    def get_health(self):
        return self.health
    
    def set_health(self, ammount):
        self.health += ammount
        self.image = pygame.Surface((self.health, 20))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)


    def __init__(self, health, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.health = health
        self.image = pygame.Surface((health, 20))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
