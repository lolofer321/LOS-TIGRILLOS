import pygame
class Utils:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.assets = {}

    def load_assets(self):
        self.assets = {
            "background":pygame.transform.scale(pygame.image.load("assets/0005.png"), (self.width, self.height)),
            "obstacle_type1":pygame.transform.scale(pygame.image.load("assets/0104.png"), (80, 80)),
            "obstacle_type2":pygame.transform.scale(pygame.image.load("assets/0105.png"), (80, 80)),
            "player":[pygame.transform.scale(pygame.image.load("assets/player/playerQR1.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerQR2.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerQR3.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerQR4.png"), (80, 80))],
            "enemy_type1":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest.png"), (80, 80)),
            "bullet_type1":pygame.transform.scale(pygame.image.load("assets/bullet.png"), (16, 16)),
            "font":pygame.font.Font("assets/font.otf", 32)}