import pygame

pygame.init()

projectiles = []

#Constantes de color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)

#Fuente de texto
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)

#Imagenes
CURSOR = pygame.image.load("assets/cursor.png")

#Pantalla
WINDOW_SIZE = (1280, 720)
WINDOW_TITLE = "Tigres vs zombies"
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

background = pygame.transform.scale(pygame.image.load("assets/background.png"), WINDOW_SIZE)

#fps
FRAME_RATE = 120

#Puertas
DOOR_SIZE = (20, 100)
door_room1 = pygame.Rect(WINDOW_SIZE[0] - DOOR_SIZE[0], WINDOW_SIZE[1] // 2 - DOOR_SIZE[1] // 2, DOOR_SIZE[0], DOOR_SIZE[1])

#Habitacion
CURRENT_ROOM = 1

objects = []
bullets = []
enemies = []

#Reloj
CLOCK = pygame.time.Clock()

class Object:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.velocity = [0, 0]
        self.collider = [width, height]

        objects.append(self)

    def draw(self):
        WINDOW.blit(pygame.transform.scale(pygame.image.load(self.image), (self.width, self.height)), (self.x, self.y))

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.draw()

    def get_center(self):
        return self.x + self.width / 2, self.y + self.height / 2

class Entity(Object):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed
    def update(self):
        self.x += self.velocity[0] * self.speed
        self.y += self.velocity[1] * self.speed
        self.draw()
    def shoot(self):
        self_center = self.get_center()
        bullet = Object(self_center[0], self_center[1], 16, 16, "assets/bullet.png")

        target_center = target.get_center()
        bullet.velocity = [target_center[0]- self_center[0], target_center[1] - self_center[1]]

        magnitude = (bullet.velocity[0] ** 2 + bullet.velocity[1] ** 2) ** 0.5

        bullet.velocity = [bullet.velocity[0] / magnitude * 10, bullet.velocity[1] / magnitude * 10]

        bullets.append(bullet)    
    
class Player(Entity):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image, speed)
    
    def check_input(self, key, value):
        if key == pygame.K_LEFT or key == pygame.K_a:
            player_input["left"] = value
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            player_input["right"] = value
        elif key == pygame.K_UP or key == pygame.K_w:
            player_input["up"] = value
        elif key == pygame.K_DOWN or key == pygame.K_s:
            player_input["down"] = value

class Enemy(Entity):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image, speed)
        self.health = 5
        self.collider = [width / 2, height / 2]
        enemies.append(self)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        objects.remove(self)
        enemies.remove(self)

def check_collisions(obj1, obj2):
    x1, y1 = obj1.get_center()
    x2, y2 = obj2.get_center()
    w1, h1 = obj1.collider[0] / 2, obj1.collider[1] / 2
    w2, h2 = obj2.collider[0] / 2, obj2.collider[1] / 2
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2:
        return y1 + h2 > y2 - h2 and y1 - h2 < y2 + h2
    return False

player_input = {"left": False, "right": False, "up": False, "down": False}


player = Player(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, 75, 75, "assets/playerSheetTest.png", 5)
target = Object(0, 0, 50, 50, "assets/cursor.png")
enemy = Enemy(WINDOW_SIZE[0] / 2 + 300, WINDOW_SIZE[1] /2, 75, 75, "assets/EnemySheetTest.png", 5)

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            player.check_input(event.key, True)
        elif event.type == pygame.KEYUP:
            player.check_input(event.key, False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()
    
    mousePos = pygame.mouse.get_pos()
    target.x = mousePos[0] - target.width / 2
    target.y = mousePos[1] - target.height / 2

    player.velocity[0] = player_input["right"] - player_input["left"]
    player.velocity[1] = player_input["down"] - player_input["up"]

    WINDOW.blit(background, (0, 0))

    for obj in objects:
        obj.update()

    for e in enemies:
        for b in bullets:
            if check_collisions(b, e):
                e.take_damage(2)
                bullets.remove(b)
                objects.remove(b)


    CLOCK.tick(FRAME_RATE)
    pygame.display.update()
