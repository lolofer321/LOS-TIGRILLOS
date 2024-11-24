import pygame

pygame.init()

#Constantes de color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)

#Fuente de texto
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)

#Pantalla
WINDOW_SIZE = (1280, 720)
WINDOW_TITLE = "Tigres vs zombies"
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

background = pygame.transform.scale(pygame.image.load("assets/background.png"), WINDOW_SIZE)

#fps
FRAME_RATE = 120

#Ballas
BULLET_SPEED = 4

GAME_PAUSE = False

objects = []
bulletsA = []
bulletsB = []
enemies = []
playerLS = []

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
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()    
    
class Player(Entity):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image, speed)
        self.health = 5
        self.shootInterval = 500
        self.lastShootTime = 0

        playerLS.append(self)

    def destroy(self):
        objects.remove(self)
        playerLS.remove(self)

    def shoot(self, objetive):
        self_center = self.get_center()
        bullet = Object(self_center[0], self_center[1], 16, 16, "assets/bullet.png")

        objetive_center = objetive.get_center()
        bullet.velocity = [objetive_center[0]- self_center[0], objetive_center[1] - self_center[1]]

        magnitude = (bullet.velocity[0] ** 2 + bullet.velocity[1] ** 2) ** 0.5

        bullet.velocity = [bullet.velocity[0] / magnitude * BULLET_SPEED, bullet.velocity[1] / magnitude * BULLET_SPEED]

        bulletsA.append(bullet)  

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
        self.shootInterval = 500
        self.lastShootTime = 0

        enemies.append(self)

    def destroy(self):
        objects.remove(self)
        enemies.remove(self)

    def shoot(self, objetive):
        self_center = self.get_center()
        bullet = Object(self_center[0], self_center[1], 16, 16, "assets/bullet.png")

        objetive_center = objetive.get_center()
        bullet.velocity = [objetive_center[0] - self_center[0], objetive_center[1] - self_center[1]]

        magnitude = (bullet.velocity[0] ** 2 + bullet.velocity[1] ** 2) ** 0.5
        if magnitude != 0:
            bullet.velocity = [bullet.velocity[0] / magnitude * BULLET_SPEED, bullet.velocity[1] / magnitude * BULLET_SPEED]

        bulletsB.append(bullet)

    def move(self, objetive):
        self_center = self.get_center()
        objetive_center = objetive.get_center()
        self.velocity = [objetive_center[0] - self_center[0], objetive_center[1] - self_center[1]]
        magnitude = (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5
        if magnitude != 0:
            self.velocity = [self.velocity[0] / magnitude * self.speed, self.velocity[1] / magnitude * self.speed]


def check_collisions(obj1, obj2):
    x1, y1 = obj1.get_center()
    x2, y2 = obj2.get_center()
    w1, h1 = obj1.collider[0] / 2, obj1.collider[1] / 2
    w2, h2 = obj2.collider[0] / 2, obj2.collider[1] / 2
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2:
        return y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2
    return False

player_input = {"left": False, "right": False, "up": False, "down": False}


player = Player(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, 75, 75, "assets/playerSheetTest.png", 5)
target = Object(0, 0, 50, 50, "assets/cursor.png")

# puertas 
DOOR_SIZE = (20, 100)
door_room1 = pygame.Rect(WINDOW_SIZE[0] - DOOR_SIZE[0] - 100, WINDOW_SIZE[1] // 2 - DOOR_SIZE[1] // 2, DOOR_SIZE[0], DOOR_SIZE[1])
CURRENT_ROOM = 0

def crear_enemigos(room):
    # Limpia los enemigos de la sala anterior
    global enemies, objects
    enemies = []
    

    # Define la cantidad, tipo y posición de los enemigos según la sala actual
    if room == 1:
        enemies.append(Enemy(300, 200, 75, 75, "assets/EnemySheetTest.png", 1))
        enemies.append(Enemy(400, 300, 75, 75, "assets/EnemySheetTest.png", 1))
        enemies.append(Enemy(600, 400, 75, 75, "assets/EnemySheetTest.png", 1))
    elif room == 2:
        enemies.append(Enemy(200, 200, 75, 75, "assets/EnemySheetTest.png", 1))
        
    elif room == 4:
        enemies.append(Enemy(350, 250, 75, 75 ,"assets/EnemySheetTest.png",1))  # Un nuevo tipo de enemigo
        enemies.append(Enemy(450, 350, 75, 75, "assets/EnemySheetTest.png",1))
    elif room == 5:
        enemies.append(Enemy(250, 150, 75, 75, "assets/EnemySheetTest.png", 1))
        enemies.append(Enemy(350, 250, 75, 75, "assets/EnemySheetTest.png", 1))
        enemies.append(Enemy(450, 350, 75, 75, "assets/EnemySheetTest.png", 1))
        enemies.append(Enemy(550, 450, 75, 75, "assets/EnemySheetTest.png", 1))
        
    # Añade más condiciones para más habitaciones y más tipos de enemigos si es necesario

    for enemy in enemies:
        objects.append(enemy)

pygame.mouse.set_visible(False)

def change_room():
    global CURRENT_ROOM, player, bulletsA, bulletsB, enemies, objects, playerLS
    CURRENT_ROOM += 1
    player.x = 100
    player.y = WINDOW_SIZE[1] // 2
    bulletsA = []
    bulletsB = []
    enemies = []
    objects = [player, target]
    playerLS = [player]
    crear_enemigos(CURRENT_ROOM)


while True:
    CURRENT_TIME = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_p:
                GAME_PAUSE = not GAME_PAUSE
            else:
                player.check_input(event.key, True)

        elif event.type == pygame.KEYUP:
            player.check_input(event.key, False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and CURRENT_TIME - player.lastShootTime > player.shootInterval and len(playerLS) != 0:
                player.shoot(target)
                player.lastShootTime = CURRENT_TIME

    if GAME_PAUSE:
        continue

    mousePos = pygame.mouse.get_pos()
    target.x = mousePos[0] - target.width / 2
    target.y = mousePos[1] - target.height / 2

    player.velocity[0] = player_input["right"] - player_input["left"]
    player.velocity[1] = player_input["down"] - player_input["up"]

    WINDOW.blit(background, (0, 0))

    # numero de cuarto
    room_text = TEXT_FONT.render(f'ROOM: {CURRENT_ROOM}', False, WHITE)
    WINDOW.blit(room_text, (50, 50))

    # colision de la puerta
    if CURRENT_ROOM < 12:
        pygame.draw.rect(WINDOW, RED, door_room1)
        if player.x + player.width > door_room1.x and player.x < door_room1.x + DOOR_SIZE[0] and player.y + player.height > door_room1.y and player.y < door_room1.y + DOOR_SIZE[1]:
            change_room()

    for e in enemies:
        for b in bulletsA:
            if check_collisions(b, e):
                e.take_damage(2)
                bulletsA.remove(b)
                objects.remove(b)

    for b in bulletsB:
        if check_collisions(player, b) and len(playerLS) != 0:
            player.take_damage(2)
            bulletsB.remove(b)
            objects.remove(b)
            if e.health <= 0:
                e.destroy()
            
    for b in bulletsB:
        if b.x > WINDOW_SIZE[0] - 100 or b.x < 100 or b.y > WINDOW_SIZE[1] - 100 or b.y < 100:
            bulletsB.remove(b)
            objects.remove(b)

    for e in enemies:
        e.move(player)
        if CURRENT_TIME - e.lastShootTime > e.shootInterval:
            e.shoot(player) 
            e.lastShootTime = CURRENT_TIME
        

    textPosicion = 10
    for obj in objects:
        txt2 = TEXT_FONT.render(f"{player.health}", 1, WHITE)
        WINDOW.blit(txt2, (10, WINDOW_SIZE[1] - 40))
        

        obj.update()
     #Establecer los límites de la pantalla
    if player_input["left"] == True and player.x - player.speed < player.width:
        player.x += player.speed
    if player_input["right"] == True and player.x + player.speed > WINDOW_SIZE[0] - player.width-80:
        player.x -= player.speed
    if player_input["up"] == True and player.y - player.speed < player.height:
        player.y += player.speed
    if player_input["down"] == True and player.y + player.speed > WINDOW_SIZE[1] - player.height-80:
        player.y -= player.speed

    
    CLOCK.tick(FRAME_RATE)
    pygame.display.update()
