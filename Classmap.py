import pygame

class map:
    def __init__(self, window, width, height, elements, assets):
        self.window = window
        self.width = width
        self.height = height
        self.elements = elements
        self.assets = assets

    def render(self):
        self.window.blit(self.assets["background"], (0, 0))
        for i in self.elements:
            if i.type == "type1":
                self.window.blit(self.assets["obstacle_type1"], (i.pos_x, i.pos_y))
            elif i.type == "type2":
                self.window.blit(self.assets["obstacle_type2"], (i.pos_x, i.pos_y))