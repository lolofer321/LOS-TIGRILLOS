import pygame
from ClassObject import Object
class Button(Object):
    def __init__(self, pos_x, pos_y, width, height, image):
        super().__init__(pos_x, pos_y, width, height)
        self.image = image

    def render(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def check_input(self, position):
        if position[0] in range(int((self.pos_x)//1),int((self.pos_x+self.width)//1)) and position[1] in range(int(self.pos_y//1), int((self.pos_y+self.height)//1)):
            return True
        return False