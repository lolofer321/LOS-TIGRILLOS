class Object:
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def get_center(self):
        return self.pos_x + self.width / 2, self.pos_y + self.height / 2