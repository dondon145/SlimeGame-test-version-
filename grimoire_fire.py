import pygame
import spritesheet

BLACK = (0,0,0)
class Fire(pygame.sprite.Sprite):

    def get_start_sprites(self, width, height, color):
        image = pygame.image.load(f"/home/big-orange/Desktop/TestGame/Magic animations/IdleFire/png/{color}/start/burning_start_1.png")
        start_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = start_spritesheet.get_frames(0, 24, 32, BLACK, 0)
        frame_1 = start_spritesheet.get_frames(1, 24, 32, BLACK, 0)
        frame_2 = start_spritesheet.get_frames(2, 24, 32, BLACK, 0)
        frame_3 = start_spritesheet.get_frames(3, 24, 32, BLACK, 0)

        self.start_sprites.append(pygame.transform.scale(frame_0, (width, height)))
        self.start_sprites.append(pygame.transform.scale(frame_1, (width, height)))
        self.start_sprites.append(pygame.transform.scale(frame_2, (width, height)))
        self.start_sprites.append(pygame.transform.scale(frame_3, (width, height)))
    
    def animate_start(self):

        if self.isStart == True:
            if self.current_animation != 0:
                self.current_sprite = 0
            self.current_animation = 0
            self.current_sprite += 0.1
            
            if self.current_sprite > len(self.start_sprites):
                self.current_sprite = 0
                self.isStart = False
                self.isLoop = True

            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]

    def get_loop_sprites(self, width, height, color):
        image = pygame.image.load(f"/home/big-orange/Desktop/TestGame/Magic animations/IdleFire/png/{color}/loops/burning_loop_1.png")
        loop_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = loop_spritesheet.get_frames(0, 24, 32, BLACK, 0)
        frame_1 = loop_spritesheet.get_frames(1, 24, 32, BLACK, 0)
        frame_2 = loop_spritesheet.get_frames(2, 24, 32, BLACK, 0)
        frame_3 = loop_spritesheet.get_frames(3, 24, 32, BLACK, 0)

        self.loop_sprites.append(pygame.transform.scale(frame_0, (width, height)))
        self.loop_sprites.append(pygame.transform.scale(frame_1, (width, height)))
        self.loop_sprites.append(pygame.transform.scale(frame_2, (width, height)))
        self.loop_sprites.append(pygame.transform.scale(frame_3, (width, height)))
    
    def animate_loop(self):
        if self.isLoop == True:
            self.current_animation = 1
            self.current_sprite += 0.1

            if self.current_sprite > len(self.loop_sprites):
                self.current_sprite = 0

            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]
        

    def get_end_sprites(self, width, height, color):

        image = pygame.image.load(f"/home/big-orange/Desktop/TestGame/Magic animations/IdleFire/png/{color}/end/burning_end_1.png")
        end_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = end_spritesheet.get_frames(0, 24, 32, BLACK, 0)
        frame_1 = end_spritesheet.get_frames(1, 24, 32, BLACK, 0)
        frame_2 = end_spritesheet.get_frames(2, 24, 32, BLACK, 0)
        frame_3 = end_spritesheet.get_frames(3, 24, 32, BLACK, 0)

        self.end_sprites.append(pygame.transform.scale(frame_0, (width, height)))
        self.end_sprites.append(pygame.transform.scale(frame_1, (width, height)))
        self.end_sprites.append(pygame.transform.scale(frame_2, (width, height)))
        self.end_sprites.append(pygame.transform.scale(frame_3, (width, height)))

    def animate_end(self):
        if self.isEnd == True:

            self.isStart = False
            self.isLoop = False

            if self.current_animation != 2:
                self.current_sprite = 0

            self.current_animation = 2
            self.current_sprite += 0.1

            if self.current_sprite > len(self.end_sprites):
                self.current_sprite = 0
                self.isEnd = False
                self.kill()

            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]

    def update(self):
        self.animate_start()
        self.animate_loop()
        self.animate_end()


    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.start_sprites = []
        self.loop_sprites = []
        self.end_sprites = []

        self.get_start_sprites(50,50, "blue")
        self.get_loop_sprites(50,50, "blue")
        self.get_end_sprites(50,50, "blue")

        self.isShowing = False
        self.isStart = False
        self.isLoop = False
        self.isEnd = False

        self.all_animations = [self.start_sprites, self.loop_sprites, self.end_sprites]
        self.current_animation = 0
        self.current_sprite = 0

        self.image = pygame.Surface((50, 50))
        #self.image = self.all_animations[self.current_animation][self.current_sprite]

        self.pos_y = pos_y
        self.pos_x = pos_x
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)