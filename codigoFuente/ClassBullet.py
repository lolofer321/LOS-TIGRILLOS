from ClassObject import Object
class Bullet(Object):
    def __init__(self, pos_x, pos_y, width, height, move_speed, direccion, damage, create_time):
        super().__init__(pos_x, pos_y, width, height)
        self.move_speed = move_speed
        self.direccion = direccion
        self.damage = damage
        self.create_time = create_time