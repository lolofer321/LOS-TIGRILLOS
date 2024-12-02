import pygame
import constants

class map:
    def __init__(self, window, width, height, level, elements, assets, next_level):
        self.window = window
        self.width = width
        self.height = height
        self.level = level
        self.elements = elements
        self.assets = assets
        self.next_level = next_level

    def render(self):
        if self.level in ["level1","level2","level3","level4"]:
            self.window.blit(self.assets["background1"], (0, 0))
        if self.level in ["level5","level6","level7","level8"]:
            self.window.blit(self.assets["background2"], (0, 0))
        if self.level in ["level9","level10","level11","level12"]:
            self.window.blit(self.assets["background3"], (0, 0))
        for i in self.elements:
                if i.type == constants.OBJECT_TYPE1:
                    self.window.blit(self.assets["obstacle_type1"], (i.pos_x, i.pos_y))
                elif i.type == constants.OBJECT_TYPE2:
                    self.window.blit(self.assets["obstacle_type2"], (i.pos_x, i.pos_y))
                elif i.type == constants.OBJECT_TYPE3:
                    self.window.blit(self.assets["obstacle_type3"], (i.pos_x, i.pos_y))
                elif i.type == constants.OBJECT_TYPE4:
                    self.window.blit(self.assets["obstacle_type4"], (i.pos_x, i.pos_y))
                elif i.type == constants.OBJECT_TYPE5:
                    self.window.blit(self.assets["obstacle_type5"], (i.pos_x, i.pos_y))
                elif i.type == constants.OBJECT_TYPE6:
                    self.window.blit(self.assets["obstacle_type6"], (i.pos_x, i.pos_y))
        