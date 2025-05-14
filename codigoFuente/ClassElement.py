from ClassObject import Object
class Element(Object):
    def __init__(self, pos_x, pos_y, width, height, type):
        super().__init__(pos_x, pos_y, width, height)
        self.type = type