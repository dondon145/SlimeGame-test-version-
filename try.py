"""
The quality of the picture gets worse every time it is rotated, which is why it is better to create some other surface with this same picture but with other angle, 
This does not worsen the quality of the picture, since the picture itself is never rotated
"""
import pygame
import spritesheet
from pygame.locals import *
import math


pygame.init()

def rotate(surface, angle, scale ):
    rotated_surface = pygame.transform.rotozoom(surface, angle, scale)
    rotated_rect = rotated_surface.get_rect()
    return rotated_surface, rotated_rect

def get_angle(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    delta_x = mouse_x - x
    delta_y = mouse_y - y
    
    if delta_x == 0:
        return 0
    
    radians = math.atan2(delta_y, delta_x)
    angle = math.degrees(radians)*-1
    return angle

class Fire(pygame.sprite.Sprite) :

    def get_sprites(self, animation, frames, frame_width, frame_height, image):
        image = pygame.image.load(f"/home/big-orange/Desktop/TestGame/Magic animations/Fire Ball/{image}")
        image_spritesheet = spritesheet.SpriteSheet(image)

        for i in range(0, frames-1):
            animation.append(pygame.transform.scale(image_spritesheet.get_frames(i, frame_width, frame_height, BLACK, 0), (50,50)))

    def fire_ball_move(self):
        
        if self.isFireball_move == True:
            
            if self.current_animation != 0:
                self.current_animation = 0
                self.current_sprite = 0
            
            if self.isFireball_in_action == False:
                self.angle += get_angle(self.pos_x, self.pos_y)
                self.image, self.rect = rotate(self.all_animations[self.current_animation][int(self.current_sprite)], self.angle, 1)
                self.rect.center = (self.pos_x, self.pos_y)
                
                print(self.angle)
                self.angle = 0
            
            elif self.isFireball_in_action == True:
                    
                self.current_sprite += 0.1
                self.pos_x += 1.5

                if self.current_sprite > len(self.all_animations[self.current_animation]):
                    self.current_sprite = 0
                
                self.image = self.all_animations[self.current_animation][int(self.current_sprite)]
                self.rect.center = (self.pos_x, self.pos_y)
            


    def update(self):
        self.fire_ball_move()

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.fire_ball_move_animation = []

        self.get_sprites(self.fire_ball_move_animation, 6, 48, 28, "Move.png")

        self.isFireball_move = False
        self.isFireball_in_action = False
        self.isFireball_explosion = False

        self.all_animations = [self.fire_ball_move_animation, ]
        self.current_animation = 0
        self.current_sprite = 0

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = 0
        
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.image = self.all_animations[self.current_animation][self.current_sprite]


WIDTH = 800
HEIGHT = 800
BLACK = (0,0,0)

clock = pygame.time.Clock()
FPS = 60
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROTATING")

running = True

fire_obj  = Fire(400, 400)

moving_group = pygame.sprite.Group()
moving_group.add(fire_obj)

while running:
    
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        mouse_list = pygame.mouse.get_pressed(num_buttons = 3)

        if event.type == MOUSEBUTTONDOWN:
            if mouse_list[2]== True:
                fire_obj.isFireball_move = True
    
    moving_group.update()
    moving_group.draw(DISPLAYSURF)
    


    
    clock.tick(FPS)
    pygame.display.flip()
    