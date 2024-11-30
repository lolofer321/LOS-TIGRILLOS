import random
class Auto:
    def __init__(self, game):
        self.game = game

    def generate_action(self):
        return random.randint(0, 1000)
    
    def execute(self):
        if self.generate_action() > 5:
            for i in self.game.enemies:
                if i.type != "door":    
                    if self.generate_action() > 970:
                        for e in self.game.enemies:
                            e_center = e.get_center()
                            objetive_center = self.game.player[0].get_center()
                            e.direccion = [objetive_center[0] - e_center[0], objetive_center[1] - e_center[1]]
                            magnitude = (e.direccion[0] ** 2 + e.direccion[1] ** 2) ** 0.5
                            if magnitude != 0:
                                e.direccion = [e.direccion[0] / magnitude * e.move_speed, e.direccion[1] / magnitude * e.move_speed]
                            self.game.move(e)
                    if self.generate_action() % 100 == 0:
                        self.game.shoot(i, self.game.player[0])

        