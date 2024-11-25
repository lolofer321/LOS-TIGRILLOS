import pygame
class Utils:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.assets = {}

    def load_assets(self):
        self.assets = {
            "background1":pygame.transform.scale(pygame.image.load("assets/background1Test.png"), (self.width, self.height)),
            "background2":pygame.transform.scale(pygame.image.load("assets/background2Test.png"), (self.width, self.height)),
            "obstacle_type1":pygame.transform.scale(pygame.image.load("assets/rocka.png"), (80, 80)),
            "door":pygame.transform.scale(pygame.image.load("assets/door.png"), (100, 100)),
            "obstacle_type2":pygame.transform.scale(pygame.image.load("assets/rock2a.png"), (80, 80)),
            "playerMR":[pygame.transform.scale(pygame.image.load("assets/player/playerMR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR4.png"), (88, 88))
                      ],
            "playerML":[pygame.transform.scale(pygame.image.load("assets/player/playerML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML4.png"), (88, 88))
                      ],
            "enemy_type1":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest.png"), (80, 80)),
            "enemy_type2":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "bullet_type1":pygame.transform.scale(pygame.image.load("assets/bullet.png"), (16, 16)),
            "font":pygame.font.Font("assets/font.otf", 32),
            "cursor":pygame.transform.scale(pygame.image.load("assets/cursor.png"), (50, 50))}