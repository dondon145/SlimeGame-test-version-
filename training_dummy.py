import pygame
import spritesheet

BLACK = (0,0,0)
class Training_Dummy(pygame.sprite.Sprite):

    def get_idle_frames(self, scale_size, width, height):
        global BLACK

        image = pygame.image.load("/home/big-orange/Desktop/SlimeGame/Training Dummy Sprite Sheet.png")
        idle_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = idle_spritesheet.get_frames(0, width, height, BLACK, 0)
        frame_1 = idle_spritesheet.get_frames(1, width, height, BLACK, 0)
        frame_2 = idle_spritesheet.get_frames(2, width, height, BLACK, 0)
        frame_3 = idle_spritesheet.get_frames(3, width, height, BLACK, 0)

        self.idle_animation.append(pygame.transform.scale(frame_0, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_1, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_2, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_3, (scale_size, scale_size)))

    def get_hit_frames(self, scale_size, width, height):
        global BLACK

        image = pygame.image.load("/home/big-orange/Desktop/SlimeGame/Training Dummy Sprite Sheet.png")
        hit_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = hit_spritesheet.get_frames(0, width, height, BLACK, 1)
        frame_1 = hit_spritesheet.get_frames(1, width, height, BLACK, 1)
        frame_2 = hit_spritesheet.get_frames(2, width, height, BLACK, 1)
        frame_3 = hit_spritesheet.get_frames(3, width, height, BLACK, 1)
        frame_4 = hit_spritesheet.get_frames(4, width, height, BLACK, 1)

        self.hit_animation.append(pygame.transform.scale(frame_0, (scale_size, scale_size)))
        self.hit_animation.append(pygame.transform.scale(frame_1, (scale_size, scale_size)))
        self.hit_animation.append(pygame.transform.scale(frame_2, (scale_size, scale_size)))
        self.hit_animation.append(pygame.transform.scale(frame_3, (scale_size, scale_size)))
        self.hit_animation.append(pygame.transform.scale(frame_4, (scale_size, scale_size)))
    
    def animate_idle(self):

        if self.isIdle == True:
            self.current_animation = 0
            self.current_sprite += 0.06
            
            if self.current_sprite > len(self.idle_animation):
                self.current_sprite = 0
                return
            
            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]
        
        else :
            return
    def animate_hit(self):

        if self.isHit == True:

            if self.current_animation != 1:
                self.current_sprite = 0
            
            self.isIdle = False
            self.current_animation = 1
            self.current_sprite += 0.06

            if self.current_sprite > len(self.hit_animation):
                self.current_sprite = 0
                self.isHit = False
                self.isIdle = True
                return
            
            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def update(self):
        self.animate_idle()
        self.animate_hit()



    def __init__(self, position_x, position_y):
        super().__init__()

        # Animations
        self.idle_animation = []
        self.hit_animation = []
        self.all_animations = [self.idle_animation, self.hit_animation]

        # Getting frames for animations
        self.get_idle_frames(100, 33, 34)
        self.get_hit_frames(100, 32, 34)

        # Booleans
        self.isHit = False
        self.isIdle = True

        # Image values
        self.pos_x = position_x
        self.pos_y = position_y
        self.image = pygame.Surface([100,100])
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

        # Setting initial frame values
        self.current_animation = 0
        self.current_sprite = 0
        self.image = self.all_animations[self.current_animation][self.current_sprite]