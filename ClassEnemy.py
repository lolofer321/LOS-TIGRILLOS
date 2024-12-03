from ClassCharacter import Character

class Enemy(Character):
    def __init__(self, pos_x, pos_y, width, height, health, move_speed, attack_speed, direccion, damage, gun_type, level, type):
        super().__init__(pos_x, pos_y, width, height, health, move_speed, attack_speed, direccion, damage, gun_type)
        self.level = level
        self.type = type
    

    