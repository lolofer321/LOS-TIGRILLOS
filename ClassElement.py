from ClassObject import Object
class Element(Object):
    def __init__(self, pos_x, pos_y, width, height, type):
        super().__init__(pos_x, pos_y, width, height)
        self.type = type
        """elif key == pygame.K_DOWN or key == pygame.K_1:
                self.game.player[0].attack_speed = 300
                self.game.player[0].damage = 1
                self.game.player[0].gun_type = "gun1"
            elif key == pygame.K_DOWN or key == pygame.K_2:
                self.game.player[0].attack_speed = 100
                self.game.player[0].damage = 1
                self.game.player[0].gun_type = "gun2"
            elif key == pygame.K_DOWN or key == pygame.K_3:
                self.game.player[0].attack_speed = 100
                self.game.player[0].damage = 2
                self.game.player[0].gun_type = "gun3"""