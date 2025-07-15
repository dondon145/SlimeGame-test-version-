import pygame
from pygame.locals import *
import slime
import grimoire_fire
import crosshair
import fire_element_magic
import training_dummy

pygame.init()
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 60

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BACKGROUND = (80, 80, 160)

player_x = 300
player_y = 300
player = slime.Slime(player_x, player_y)
casting_flame = grimoire_fire.Fire((player_x +50), (player_y -25))
crosshair_obj = crosshair.Crosshair()
Dummy = training_dummy.Training_Dummy(600, 400)

moving_objects = pygame.sprite.Group()

moving_objects.add(Dummy)
moving_objects.add(player)


pressed_mouse = { 0: False, 1: False, 2: False }
pressed_key = {"a": False, "w": False, "d": False, "s": False}
running = True


while running:
    for event in pygame.event.get():

        mouse_list = pygame.mouse.get_pressed(num_buttons = 3)
        key_list = pygame.key.get_pressed()

        if event.type == QUIT:
            running = False


        if event.type == MOUSEBUTTONDOWN:
            if mouse_list[2]== True:
                pressed_mouse[2]= True
                casting_flame.isStart = True
        elif event.type == MOUSEBUTTONUP:
            if mouse_list[2] == False:
                pressed_mouse[2] = False
                casting_flame.isEnd = True

        # slime movemnt turn on 
        if event.type == KEYDOWN:
            if key_list[K_a]== True:
                pressed_key["a"] = True
            if key_list[K_s] == True:
                pressed_key["s"] = True
            if key_list[K_w]== True:
                pressed_key["w"] = True
            if key_list[K_d] == True:
                pressed_key["d"] = True

        # slime movement turn off
        elif event.type == KEYUP:
            if key_list[K_a] == False:
                pressed_key["a"] = False
            if key_list[K_s] == False:
                pressed_key["s"] = False
            if key_list[K_w]== False:
                pressed_key["w"] = False
            if key_list[K_d] == False:
                pressed_key["d"] = False
    
    # changing slime position if moving 
    if pressed_key["a"]== True:
        player.pos_x -= 5
        casting_flame.pos_x -=5
    if pressed_key["d"]== True:
        player.pos_x += 5
        casting_flame.pos_x +=5
    if pressed_key["w"]== True:
        player.pos_y -= 5
        casting_flame.pos_y -=5
    if pressed_key["s"]== True:
        player.pos_y += 5
        casting_flame.pos_y +=5

    # using scope
    if pressed_mouse[2] == True:
        moving_objects.add(crosshair_obj)
        moving_objects.add(casting_flame)
        crosshair_obj.isShowing = True
        
    elif pressed_mouse[2] == False:
        crosshair_obj.isShowing = False
    

    DISPLAYSURF.fill(BACKGROUND)

    moving_objects.update()
    moving_objects.draw(DISPLAYSURF)
    pygame.display.flip()
    clock.tick(FPS)
