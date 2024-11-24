from ClassObject import Object

class Character(Object):
    def __init__(self, pos_x, pos_y, width, height, health, move_speed, attack_speed, direccion):
        super().__init__(pos_x, pos_y, width, height)
        self.health = health
        self.move_speed = move_speed
        self.attack_speed = attack_speed
        self.direccion = direccion
    