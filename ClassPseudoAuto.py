import random
class Auto:
    def __init__(self, game):
        self.game = game

    def generate_action(self):
        return random.randint(0, 7)
    
    def execute(self):
        if self.generate_action() == 0:
            for i in self.game.enemies:
                if self.generate_action() == 0:
                    self.game.move(i)
                elif self.generate_action() == 1:
                    self.game.shoot(i, self.game.player[0])