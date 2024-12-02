import random
import pygame
class Auto:
    def __init__(self, game):
        self.game = game

    def generate_action(self):
        return random.randint(0, 100)
    
    def execute(self):
        if self.generate_action() < 1:
            return
        for e in self.game.enemies:
            if e.type == "door" or self.generate_action() < 50:
                continue
            if self.generate_action() % 100 == 0:
                self.game.shoot(e, self.game.player[0])

            e_center = e.get_center()
            objetive_center = self.game.player[0].get_center()
            e.dir = pygame.Vector2(objetive_center[0] - e_center[0], objetive_center[1] - e_center[1])
            """e.dir = [objetive_center[0] - e_center[0], objetive_center[1] - e_center[1]]"""
            e.direccion = [e.dir.normalize()[0], e.dir.normalize()[1]]
            self.game.move(e)
            
        