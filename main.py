import pygame
from pygame.locals import *
import slime
import fire
import crosshair

pygame.init()
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 60

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BACKGROUND = (0, 0, 0)

player_x = 300
player_y = 300
player = slime.Slime(player_x, player_y)
fire_obj = fire.Fire((player_x +50), (player_y -25))
crosshair_obj = crosshair.Crosshair()

moving_objects = pygame.sprite.Group()
moving_objects.add(player)
moving_objects.add(fire_obj)

running = True
while running:
    for event in pygame.event.get():

        mouse_list = pygame.mouse.get_pressed(num_buttons = 3)

        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if mouse_list[2]== True:
                moving_objects.add(fire_obj)
                moving_objects.add(crosshair_obj)
                fire_obj.isStart = True
            
        if event.type == MOUSEBUTTONUP:
            crosshair_obj.kill()
            fire_obj.isEnd = True


    DISPLAYSURF.fill(BACKGROUND)

    moving_objects.update()
    moving_objects.draw(DISPLAYSURF)
    pygame.display.flip()
    clock.tick(FPS)
