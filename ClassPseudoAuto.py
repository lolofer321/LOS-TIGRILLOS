import random
import pygame
class Auto:
    def __init__(self, game):
        self.game = game
        self.lastShootTime = 0

    def generate_action(self):
        return random.randint(0, 100)
    
    def execute(self):
        #Calcular lo que hacer el enemigo de manera aleatoria
        if self.generate_action() < 10:
            return
        for e in self.game.enemies:
            if e.type == "door":
                continue
            if self.generate_action() % 100 == 0 and pygame.time.get_ticks() - self.lastShootTime > e.attack_speed:
                self.game.shoot(e, self.game.player[0])
                self.lastShootTime = pygame.time.get_ticks()
            if self.generate_action() < 70:
                continue
            e_center = e.get_center()
            objetive_center = self.game.player[0].get_center()
            e.dir = pygame.Vector2(objetive_center[0] - e_center[0], objetive_center[1] - e_center[1])
            if e.dir.normalize()[0] == 0 or e.dir.normalize()[1] == 0:
                continue
            e.direccion = [e.dir.normalize()[0], e.dir.normalize()[1]]
            self.game.move(e)
            
        