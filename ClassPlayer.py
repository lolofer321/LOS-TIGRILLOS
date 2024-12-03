from ClassCharacter import Character

class Player(Character):
    def __init__(self, pos_x, pos_y, width, height, health, move_speed, attack_speed, direccion, damage, gun_type, controls):
        super().__init__(pos_x, pos_y, width, height, health, move_speed, attack_speed, direccion, damage, gun_type)
        self.controls = controls
        self.type = "PLAYER"
        self.coin = 0