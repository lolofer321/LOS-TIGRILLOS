import pygame
import constants
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
            "obstacle_type1":pygame.transform.scale(pygame.image.load("assets/tree1.png"), (80, 100)),
            "obstacle_type2":pygame.transform.scale(pygame.image.load("assets/fence1.png"), (68, 68)),
            "obstacle_type3":pygame.transform.scale(pygame.image.load("assets/stone1.png"), (88, 76)),
            "obstacle_type4":pygame.transform.scale(pygame.image.load("assets/skulls1.png"), (88, 60)),
            "obstacle_type5":pygame.transform.scale(pygame.image.load("assets/rock1.png"), (88, 100)),
            "obstacle_type6":pygame.transform.scale(pygame.image.load("assets/car1.png"), (156, 72)),
            "obstacle_type6":pygame.transform.scale(pygame.image.load("assets/car2.png"), (152, 72)),
            "door1":None,
            "PLAYER":{
            "0":[pygame.transform.scale(pygame.image.load("assets/player/playerMR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerMR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/player/playerML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/player/playerML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE1:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e1MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e1ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e1ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE2:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e2MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e2ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e2ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE3:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e3MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e3ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e3ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE4:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e4MR1.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4MR2.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4MR3.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4MR4.png"), (128, 128))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e4ML1.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4ML2.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4ML3.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e4ML4.png"), (128, 128))
                      ]
            },constants.ENEMY_TYPE5:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e5MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e5ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e5ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE6:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e6MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e6ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e6ML4.png"), (88, 88))
                      ]
            },constants.ENEMY_TYPE7:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e7MR1.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7MR2.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7MR3.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7MR4.png"), (100, 100))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e7ML1.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7ML2.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7ML3.png"), (100, 100)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e7ML4.png"), (100, 100))
                      ]
            },
            constants.ENEMY_TYPE8:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e8MR1.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8MR2.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8MR3.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8MR4.png"), (128, 128))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e8ML1.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8ML2.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8ML3.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e8ML4.png"), (128, 128))
                      ]
            },constants.ENEMY_TYPE9:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e9MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e9ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e9ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE10:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e10MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e10ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e10ML4.png"), (88, 88))
                      ]
            },constants.ENEMY_TYPE11:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e11MR1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11MR2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11MR3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11MR4.png"), (88, 88))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e11ML1.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11ML2.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11ML3.png"), (88, 88)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e11ML4.png"), (88, 88))
                      ]
            },
            constants.ENEMY_TYPE12:{
            "0":[pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128))
                      ],
            "1":[pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128)),
                      pygame.transform.scale(pygame.image.load("assets/enemies/e121.png"), (128, 128))
                      ]
            },
            "bullet_type1":pygame.transform.scale(pygame.image.load("assets/bullet.png"), (16, 16)),
            "font":pygame.font.Font("assets/font.otf", 32),
            "cursor":pygame.transform.scale(pygame.image.load("assets/cursor.png"), (40, 40)),
            "life":pygame.transform.scale(pygame.image.load("assets/life.png"), (40, 40))}