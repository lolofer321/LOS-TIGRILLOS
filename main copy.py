import pygame
import random
from ClassObject import Object
from ClassEnemy import Enemy
from ClassPlayer import Player
from Classmap import map

pygame.init()

#Constantes de color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)

#Fuente de texto
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)

#Pantalla
level1 = map(1280, 720, [])
WINDOW_TITLE = "Tigres vs zombies"
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

BORDER = 100

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

enemy_spawn_interval = 2000
last_time_spawn = 0

def draw(self):
    WINDOW.blit(pygame.transform.scale(pygame.image.load(self.image), (self.width, self.height)), (self.x, self.y))

def update():
    for obj in objects[::-1]:    
        obj.x += obj.velocity[0] * obj.speed
        obj.y += obj.velocity[1] * obj.speed
        draw(obj)  

def check_collisions(obj1, obj2):
    x1, y1 = get_center(obj1)
    x2, y2 = get_center(obj2)
    w1, h1 = obj1.collider[0] / 2, obj1.collider[1] / 2
    w2, h2 = obj2.collider[0] / 2, obj2.collider[1] / 2
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2:
        return y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2
    return False

def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            destroy(self) 

def destroy(self):
        if self in playerLS:
           playerLS.remove(self)  
        else:
            enemies.remove(self)
        objects.remove(self)

def get_center(self):
        return self.x + self.width / 2, self.y + self.height / 2

def shoot(self, objetive):
        self_center = get_center(self)
        #Los objetos deben ser creados en el render
        bullet = Object(self_center[0], self_center[1], 16, 16, "assets/bullet.png")
        if self in playerLS:
           bulletsA.append(bullet)  
        else:
            bulletsB.append(bullet)
        objects.append(bullet)

        objetive_center = get_center(objetive)
        bullet.velocity = [objetive_center[0] - self_center[0], objetive_center[1] - self_center[1]]

        magnitude = (bullet.velocity[0] ** 2 + bullet.velocity[1] ** 2) ** 0.5
        if magnitude != 0:
            bullet.velocity = [bullet.velocity[0] / magnitude * BULLET_SPEED, bullet.velocity[1] / magnitude * BULLET_SPEED]

def enemies_move(objetive):
    for self in enemies:
        self_center = get_center(self)
        objetive_center = get_center(objetive)
        self.velocity = [objetive_center[0] - self_center[0], objetive_center[1] - self_center[1]]
        magnitude = (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5
        if magnitude != 0:
            self.velocity = [self.velocity[0] / magnitude * self.speed, self.velocity[1] / magnitude * self.speed]

def enemies_shoot():
    for e in enemies:
        if CURRENT_TIME - e.lastShootTime > e.shootInterval:
            shoot(e, player) 
            e.lastShootTime = CURRENT_TIME

def player_move():
    player.velocity[0] = player_input["right"] - player_input["left"]
    player.velocity[1] = player_input["down"] - player_input["up"]

def check_input(key, value):
        if key == pygame.K_LEFT or key == pygame.K_a:
            player_input["left"] = value
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            player_input["right"] = value
        elif key == pygame.K_UP or key == pygame.K_w:
            player_input["up"] = value
        elif key == pygame.K_DOWN or key == pygame.K_s:
            player_input["down"] = value

def bullet_collision():
    for e in enemies:
        for b in bulletsA:
            if check_collisions(b, e):
                take_damage(e, 2)
                bulletsA.remove(b)
                objects.remove(b)

    for b in bulletsB:
        if check_collisions(player, b) and len(playerLS) != 0:
            take_damage(player, 2)
            bulletsB.remove(b)
            objects.remove(b)

def bullet_kill():
    for b in bulletsA + bulletsB:
        if b.x > WINDOW_SIZE[0] - BORDER or b.x < BORDER or b.y > WINDOW_SIZE[1] - BORDER or b.y < BORDER:
            if b in bulletsA:
                bulletsA.remove(b)
            else:
                bulletsB.remove(b)
            objects.remove(b)

def target_posicion():
    mousePos = pygame.mouse.get_pos()
    target.x = mousePos[0] - target.width / 2
    target.y = mousePos[1] - target.height / 2

def spawn_enemy():
    x_random = random.randint(BORDER, WINDOW_SIZE[0] - BORDER)
    y_random = random.randint(BORDER, WINDOW_SIZE[1] - BORDER)
    new_enemy = Enemy(x_random, y_random, 75, 75, "assets/EnemySheetTest.png", 1)

    objects.append(new_enemy)
    enemies.append(new_enemy)

def enemy_action():
    t = random.randint(10)
    if t < 6:
        enemies_move()
    else:
        enemies_shoot() 

player_input = {"left": False, "right": False, "up": False, "down": False}

target = Object(0, 0, 50, 50, "assets/cursor.png")
objects.append(target)
player = Player(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, 75, 75, "assets/playerSheetTest.png", 5)
objects.append(player)
playerLS.append(player)

pygame.mouse.set_visible(False)

while True:
    CURRENT_TIME = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_p:
                GAME_PAUSE = not GAME_PAUSE
            else:
                check_input(event.key, True)

        elif event.type == pygame.KEYUP:
            check_input(event.key, False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and CURRENT_TIME - player.lastShootTime > player.shootInterval and len(playerLS) != 0:
                shoot(player, target)
                player.lastShootTime = CURRENT_TIME

    if GAME_PAUSE:
        continue

    WINDOW.blit(background, (0, 0))

    target_posicion()
    player_move()
    
    bullet_collision()
    bullet_kill()

    enemies_shoot()
    enemies_move(player)

    if CURRENT_TIME - last_time_spawn > enemy_spawn_interval and len(playerLS) != 0:
        spawn_enemy()
        last_time_spawn = CURRENT_TIME

    textPosicion = 10
    for obj in objects:
        """txt = TEXT_FONT.render(f"{obj}", 1, WHITE)
        WINDOW.blit(txt, (10, textPosicion))
        textPosicion += 30"""

        txt2 = TEXT_FONT.render(f"{player.health}", 1, WHITE)
        WINDOW.blit(txt2, (10, WINDOW_SIZE[1] - 40))
        

    update()

    #Establecer los límites de la pantalla
    if player_input["left"] == True and player.x - player.speed < player.width:
        player.x += player.speed
    if player_input["right"] == True and player.x + player.speed > WINDOW_SIZE[0] - player.width - BORDER:
        player.x -= player.speed
    if player_input["up"] == True and player.y - player.speed < player.height:
        player.y += player.speed
    if player_input["down"] == True and player.y + player.speed > WINDOW_SIZE[1] - player.height - BORDER:
        player.y -= player.speed
    
    CLOCK.tick(FRAME_RATE)
    pygame.display.update()
