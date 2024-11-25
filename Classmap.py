import pygame

class map:
    def __init__(self, window, width, height, level, elements, assets):
        self.window = window
        self.width = width
        self.height = height
        self.level = level
        self.elements = elements
        self.assets = assets

    def render(self):
        if self.level == "level1":
            self.window.blit(self.assets["background1"], (0, 0))
        else:
            self.window.blit(self.assets["background2"], (0, 0))
        for i in self.elements:
            if i.type == "type1":
                self.window.blit(self.assets["obstacle_type1"], (i.pos_x, i.pos_y))
            elif i.type == "type2":
                self.window.blit(self.assets["obstacle_type2"], (i.pos_x, i.pos_y))
            elif i.type == "door":
                self.window.blit(self.assets["door"], (i.pos_x, i.pos_y))