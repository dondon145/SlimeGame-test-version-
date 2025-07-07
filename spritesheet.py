# This class takes in a spritesheet and separates it into standalone sprites that could be used for animations

import pygame

pygame.init()

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    
    def get_frames(self, frame, width, height, color, row):
        
        image = pygame.Surface((width, height))


        # if the image has an alpha value it makes it impossible to set a colorkey for it 
        if image.get_alpha != None :
            #print(image.get_alpha())
            image.convert()
        elif image.get_alpha == None:
            #print(image.get_alpha())
            image.convert_alpha()

        rect_value = ((frame*width), (row*height), width, height)
        image.blit(self.sheet, (0,0), rect_value)
        image.set_colorkey(color)
        return image