import pygame
class Utils:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.assets = {}

    #Cargar imagenes
    def load_assets(self):
        self.assets = {
            "background1":pygame.transform.scale(pygame.image.load("assets/background1.png"), (self.width, self.height)),
            "background2":pygame.transform.scale(pygame.image.load("assets/background2.png"), (self.width, self.height)),
            "background3":pygame.transform.scale(pygame.image.load("assets/background3.png"), (self.width, self.height)),
            "obstacle_type1":pygame.transform.scale(pygame.image.load("assets/tree1.png"), (88, 100)),
            "obstacle_type2":pygame.transform.scale(pygame.image.load("assets/fence1.png"), (68, 68)),
            "obstacle_type3":pygame.transform.scale(pygame.image.load("assets/stone1.png"), (80, 80)),
            "obstacle_type4":pygame.transform.scale(pygame.image.load("assets/skulls1.png"), (80, 80)),
            "obstacle_type5":pygame.transform.scale(pygame.image.load("assets/rock1.png"), (80, 80)),
            "obstacle_type6":pygame.transform.scale(pygame.image.load("assets/car1.png"), (80, 80)),
            "obstacle_type6":pygame.transform.scale(pygame.image.load("assets/car2.png"), (80, 80)),
            "door1":None,
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
            "enemy_type1MR":[pygame.transform.scale(pygame.image.load("assets/enemies/e1MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR4.png"), (88, 88))
                      ],
            "enemy_type1ML":[pygame.transform.scale(pygame.image.load("assets/enemies/e1ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML4.png"), (88, 88))
                      ],
            "enemy_type2":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type3":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type4":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type5":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type6":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type7":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type8":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "enemy_type9":pygame.transform.scale(pygame.image.load("assets/EnemySheetTest2.png"), (80, 80)),
            "bullet_type1":pygame.transform.scale(pygame.image.load("assets/bullet.png"), (16, 16)),
            "font":pygame.font.Font("assets/font.otf", 32),
            "cursor":pygame.transform.scale(pygame.image.load("assets/cursor.png"), (40, 40)),
            "life":pygame.transform.scale(pygame.image.load("assets/life.png"), (40, 40))}