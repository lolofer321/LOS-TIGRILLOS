from ClassEntity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image, speed)
        self.health = 5
        self.shootInterval = 500
        self.lastShootTime = 0
    

    

    