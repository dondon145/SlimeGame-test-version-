import pygame
import spritesheet

BLACK = (0,0,0)
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
        self.isFireball_explosion = False

        self.all_animations = [self.fire_ball_move_animation, ]
        self.current_animation = 0
        self.current_sprite = 0

        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.image = self.all_animations[self.current_animation][self.current_sprite]