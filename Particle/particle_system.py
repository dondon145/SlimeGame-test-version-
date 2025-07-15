import pygame
from pygame.locals import *
import random

pygame.init()

class ParticleSystem(pygame.sprite.Sprite):

    def draw_particle(self):

        self.image = pygame.draw.circle(self.display, self.color, (self.pos_x, self.pos_y), self.radius, 0)

    def get_position(self):

        return self.pos_x, self.pos_y
    
    def set_position(self):

        self.pos_x += self.velocity_x
        self.pos_y -= self.velocity_y

    def get_velocity(self):
        return self.velocity_x, self.velocity_y
    
    def set_velocity(self):
        self.velocity_x = random.randrange(-5, 5)
        self.velocity_x *= 0.1
        self.velocity_y = 0.2

    def set_life(self):
        self.life -= 0.003
        self.life_int = int(self.life)

    def erase(self):
        if self.life_int < 0:
            self.kill()
            particle_list.remove(self)

    def update(self):
        self.draw_particle()
        self.set_position()
        self.set_life()
        self.erase()

    def __init__(self, x, y, color, surface):
        super().__init__()
        self.image = pygame.Surface((50,50))

        self.display = surface
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.radius = 25
        self.velocity_x = random.randrange(-2,2)
        self.velocity_x *= 0.05
        self.velocity_y = 0.15
        self.life = random.randrange(3, 6)

        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.w/2, self.rect.h/2)
        self.image = pygame.draw.circle(self.display, self.color, (self.pos_x, self.pos_y), self.radius, 0)


WIDTH = 800
HEIGHT = 800

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

RED = (255, 0, 0)
BLACK = (0, 0, 0)
particle_list = []

for i in range(5):
    particle_obj = ParticleSystem(400, 400, RED, DISPLAY)
    particle_list.append(particle_obj)

particle_group = pygame.sprite.Group()

for i in range(len(particle_list)):
    particle_group.add(particle_list[i])

while running:
    DISPLAY.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_list = pygame.mouse.get_pressed(num_buttons = 3)
        if event.type == pygame.MOUSEBUTTONDOWN :
            for i in range(5):
                particle_obj = ParticleSystem(400, 400, RED, DISPLAY)
                particle_list.append(particle_obj)
                particle_group.add(particle_list[i])

    particle_group.update()

    pygame.display.flip()