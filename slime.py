import pygame

class Slime(pygame.sprite.Sprite):

    def get_idle_sprites(self, width, height):
        frame_1 = pygame.image.load('/home/big-orange/Desktop/TestGame/slime_idle/frame_1.png')
        frame_2 = pygame.image.load('/home/big-orange/Desktop/TestGame/slime_idle/frame_2.png')
        frame_3 = pygame.image.load('/home/big-orange/Desktop/TestGame/slime_idle/frame_3.png')

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


    def update(self):
        self.animate_idle()

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.isIdle = True
        
        self.idle_sprites = []
        self.get_idle_sprites(50, 50)

        self.all_animations = [self.idle_sprites]
        self.current_animation = 0
        self.current_sprite = 0

        self.image = pygame.Surface((80, 80))
        self.image = self.all_animations[self.current_animation][self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)