import pygame
from pygame.locals import *
import spritesheet

"""
This doesn't seem to suit my game for now as a player.
Might need to change it a bit, or use it as an NPC instead.

"""

pygame.init()
BLACK = (0,0,0,0)
RED = (255,0,0)
BACKGROUND = (80,160,80)
count = 0

class GreenSlime(pygame.sprite.Sprite):
    
    
    def idle_get_frames(self, width, height):
        global BLACK


        # separating spritesheet into multiple frames
        # makes it possible to stich it all together later into an animation
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/IdleSpritesheet.png')
        idle_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 0)
        frame_1 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_2 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 1)
        frame_3 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 1)
        frame_4 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 2)
        frame_5 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 2)

        # the sprites are too small, so rescaling them is better for visual and comfort 
        self.idle_sprites.append(pygame.transform.scale(frame_0,(width,height)))
        self.idle_sprites.append(pygame.transform.scale(frame_1,(width,height)))
        self.idle_sprites.append(pygame.transform.scale(frame_2,(width,height)))
        self.idle_sprites.append(pygame.transform.scale(frame_3,(width,height)))
        self.idle_sprites.append(pygame.transform.scale(frame_4,(width,height)))
        self.idle_sprites.append(pygame.transform.scale(frame_5,(width,height)))

    def death_get_frames(self, width, height):
        global BLACK

        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/DeathSpritesheet.png')
        death_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = death_spritesheet.get_frames(0, 20, 20, BLACK, 0)
        frame_1 = death_spritesheet.get_frames(1, 20, 20, BLACK, 0)
        frame_2 = death_spritesheet.get_frames(2, 20, 20, BLACK, 0)
        frame_3 = death_spritesheet.get_frames(0, 20, 20, BLACK, 1)
        frame_4 = death_spritesheet.get_frames(1, 20, 20, BLACK, 1)
        frame_5 = death_spritesheet.get_frames(2, 20, 20, BLACK, 1)
        frame_6 = death_spritesheet.get_frames(0, 20, 20, BLACK, 2)
        frame_7 = death_spritesheet.get_frames(1, 20, 20, BLACK, 2)

        self.death_sprites.append(pygame.transform.scale(frame_0,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_1,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_2,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_3,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_4,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_5,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_6,(width,height)))
        self.death_sprites.append(pygame.transform.scale(frame_7,(width,height)))


    def hit_get_frames(self, width, height):
        global BLACK

        # separating spritesheet into multiple frames
        # makes it possible to stich it all together later into an animation
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/HitSpritesheet.png')
        hit_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = hit_spritesheet.get_frames(0, 16, 16, BLACK, 0)
        frame_1 = hit_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_2 = hit_spritesheet.get_frames(0, 16, 16, BLACK, 1)
        frame_3 = hit_spritesheet.get_frames(1, 16, 16, BLACK, 1)

        # the sprites are too small, so rescaling them is better for visual and comfort 
        self.hit_sprites.append(pygame.transform.scale(frame_0,(width,height)))
        self.hit_sprites.append(pygame.transform.scale(frame_1,(width,height)))
        self.hit_sprites.append(pygame.transform.scale(frame_2,(width,height)))
        self.hit_sprites.append(pygame.transform.scale(frame_3,(width,height)))
        


    def animate_idle(self):

        if self.isIdle == True:
            if self.current_animation != 0:
                self.current_animation = 0
                self.current_sprite = 0

            self.current_animation = 0
            self.current_sprite += 0.12

            if self.current_sprite > len(self.idle_sprites):
                self.current_sprite = 0
                return

            self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return


    def animate_death(self):

        if self.isDead == True:

            if self.current_animation != 3:
                self.current_sprite = 0
            if self.current_sprite > (len(self.death_sprites))-1:
                    
                self.isDead = False
                self.isBouncing = False
                self.isDashing = False
                self.isIdle = False
                self.current_sprite = -1
                self.image = self.animations[self.current_animation][int(self.current_sprite)]
                return
            elif self.current_sprite <=(len(self.death_sprites))-1:
                self.isIdle = False
                self.current_animation = 3
                self.current_sprite += 0.12

                self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def animate_hit(self):

        if self.isHit == True:
            if self.current_animation != 4:
                self.current_animation = 4
                self.current_sprite = 0
                self.health -= 10

            if self.health <= 0:
                self.isHit = False
                self.isIdle = False
                self.isBouncing = False
                self.isDashing = False
                self.isDead = True
                return
            if self.current_sprite >= len(self.hit_sprites)-1:
                self.current_sprite = 0
                self.isIdle = True
                self.isHit = False
                return
            
            else:
                self.current_sprite += 0.12
                self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else:
                return



    def get_pos(self):
        return self.pos_x, self.pos_y
    
    def set_rect_top_left(self):
        self.rect.topleft = (self.pos_x, self.pos_y)


    def update(self):
        self.animate_idle()
        self.animate_death()
        self.animate_hit()
        self.get_pos()
        self.set_rect_top_left()





    def __init__(self, position_x, position_y, width, height):
        
        # initialising the super class, (pygame.sprite.Sprite)
        super().__init__()

        # actions booleans
        self.isIdle = True
        self.isHit = False
        self.isDead = False

        # all sprites for each action
        self.idle_sprites = []
        self.hit_sprites = []
        self.death_sprites = []

        # getting all sprites for each action 
        self.idle_get_frames(width, height)
        self.death_get_frames(width, height)
        self.hit_get_frames(width, height)

        # making it easier to switch between actions during game 
        self.animations = [self.idle_sprites, self.death_sprites, self.hit_sprites,]
        self.current_animation = 0
        self.current_sprite = 0

        # position values
        self.pos_x = position_x
        self.pos_y = position_y

        # Characters Stats
        self.health = 100
        self.stamina = 100
        self.mana = 100

        # this stores all the visual that is being put on the display
        self.image = pygame.Surface((width,height))
        self.image = self.animations[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    
