import pygame
import constants
class Control:
    def __init__(self, game):
        self.game = game
        self.lastShootTime = 0
        self.shootInterval = 1000

    def detect_controls(self, key, value):
        if len(self.game.player) != 0:
            if key == pygame.K_LEFT or key == pygame.K_a:
                self.game.player[0].controls["left"] = value
            elif key == pygame.K_RIGHT or key == pygame.K_d:
                self.game.player[0].controls["right"] = value
            elif key == pygame.K_UP or key == pygame.K_w:
                self.game.player[0].controls["up"] = value
            elif key == pygame.K_DOWN or key == pygame.K_s:
                self.game.player[0].controls["down"] = value
            elif key == pygame.K_DOWN or key == pygame.K_1:
                self.game.player[0].attack_speed = 300
                self.game.player[0].damage = 1
                self.game.player[0].gun_type = "gun1"
            elif (key == pygame.K_DOWN or key == pygame.K_2) and self.game.player[0].coin >= 110:
                self.game.player[0].attack_speed = 200
                self.game.player[0].damage = 1
                self.game.player[0].gun_type = "gun2"
            elif (key == pygame.K_DOWN or key == pygame.K_3) and self.game.player[0].coin >= 260:
                self.game.player[0].attack_speed = 300
                self.game.player[0].damage = 2
                self.game.player[0].gun_type = "gun3"

            self.game.player[0].direccion[0] = self.game.player[0].controls["right"] - self.game.player[0].controls["left"]
            self.game.player[0].direccion[1] = self.game.player[0].controls["down"] - self.game.player[0].controls["up"]
            magnitude = ((self.game.player[0].direccion[0]) ** 2 + (self.game.player[0].direccion[1]) ** 2) ** 0.5
            if magnitude != 0:
                self.game.player[0].direccion[0] /= magnitude
                self.game.player[0].direccion[1] /= magnitude

    def check_buttons(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.run = False
            elif event.type == pygame.KEYDOWN:
                self.detect_controls(event.key, True)
            elif event.type == pygame.KEYUP:
                self.detect_controls(event.key, False)
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.time.get_ticks() - self.lastShootTime > self.game.player[0].attack_speed and len(self.game.player) != 0:
                self.game.shoot(self.game.player[0], self.game.cursor[0])
                self.lastShootTime = pygame.time.get_ticks()