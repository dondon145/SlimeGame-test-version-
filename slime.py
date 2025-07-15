import pygame

class Slime(pygame.sprite.Sprite):

    def get_idle_sprites(self, width, height, slime_type):
        frame_1 = pygame.image.load(f'/home/big-orange/Desktop/TestGame/Slime_animations/{slime_type}_slime_idle/frame_1.png')
        frame_2 = pygame.image.load(f'/home/big-orange/Desktop/TestGame/Slime_animations/{slime_type}_slime_idle/frame_2.png')
        frame_3 = pygame.image.load(f'/home/big-orange/Desktop/TestGame/Slime_animations/{slime_type}_slime_idle/frame_3.png')

        self.idle_sprites.append(pygame.transform.scale(frame_1, (width, height)))
        self.idle_sprites.append(pygame.transform.scale(frame_2, (width, height)))
        self.idle_sprites.append(pygame.transform.scale(frame_3, (width, height)))

    def animate_idle(self):

        if self.isIdle == True:

            self.current_animation = 0
            self.current_sprite += 0.1
            
            if self.current_sprite > len(self.idle_sprites):
                self.current_sprite = 0
            
            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]

    def get_pos(self):
        return self.pos_x, self.pos_y
    
    def set_rect_top_left(self):
        self.rect.topleft = (self.pos_x, self.pos_y)


    def update(self):
        self.animate_idle()
        self.get_pos()
        self.set_rect_top_left()

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.isIdle = True
        
        self.idle_sprites = []
        self.get_idle_sprites(50, 50, "fire")

        self.all_animations = [self.idle_sprites]
        self.current_animation = 0
        self.current_sprite = 0

        self.image = pygame.Surface((80, 80))
        self.image = self.all_animations[self.current_animation][self.current_sprite]

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)