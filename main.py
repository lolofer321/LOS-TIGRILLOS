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

#fps
FRAME_RATE = 60

#Puertas
DOOR_SIZE = (20, 100)
door_room1 = pygame.Rect(WINDOW_SIZE[0] - DOOR_SIZE[0], WINDOW_SIZE[1] // 2 - DOOR_SIZE[1] // 2, DOOR_SIZE[0], DOOR_SIZE[1])

#Habitacion
CURRENT_ROOM = 1

#Reloj
CLOCK = pygame.time.Clock()

#Argumentos del jugador
player_x = WINDOW_SIZE[0] / 2
player_y = WINDOW_SIZE[1] / 2
player_size = 40
player_input = {"left": False, "right": False, "up": False, "down":False}
player_velocity = [0, 0]
player_speed = 10

def change_room():
    global CURRENT_ROOM, player_x, player_y
    CURRENT_ROOM += 1
    player_x = 100

def check_input(key, value):
    if key == pygame.K_LEFT or key == pygame.K_a:
        player_input["left"] = value
    elif key == pygame.K_RIGHT or key == pygame.K_d:
        player_input["right"] = value
    elif key == pygame.K_UP or key == pygame.K_w:
        player_input["up"] = value
    elif key == pygame.K_DOWN or key == pygame.K_s:
        player_input["down"] = value

while True:
    #Comprobar eventos del jugador
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_input(event.key, True)
        elif event.type == pygame.KEYUP:
            check_input(event.key, False)

    #Velocidad del jugador
    player_velocity[0] = player_input["right"] - player_input["left"]
    player_velocity[1] = player_input["down"] - player_input["up"]

    #Pintar la ventana
    WINDOW.fill(BLACK)

    #Texto con la habitacion actual
    room_text = TEXT_FONT.render(f'ROOM: {CURRENT_ROOM}', False, WHITE)
    WINDOW.blit(room_text, (50, 50))

    #Dibujar jugador
    PLAYER = pygame.draw.circle(WINDOW, PURPLE, (player_x, player_y), player_size)

    #Puertas
    if CURRENT_ROOM < 12:
        pygame.draw.rect(WINDOW, RED, door_room1)
        #Comprobar la colision puerta-jugador
        if CURRENT_ROOM and PLAYER.colliderect(door_room1):
            change_room()

    #Ajustar la posicion del jugagor
    player_x += player_velocity[0] * player_speed
    player_y += player_velocity[1] * player_speed

    #Establecer los límites de la pantalla
    if player_input["left"] == True and player_x - player_speed < player_size:
        player_x += player_speed
    if player_input["right"] == True and player_x + player_speed > WINDOW_SIZE[0] - player_size:
        player_x -= player_speed
    if player_input["up"] == True and player_y - player_speed < player_size:
        player_y += player_speed
    if player_input["down"] == True and player_y + player_speed > WINDOW_SIZE[1] - player_size:
        player_y -= player_speed

    #Reloj y actualizacion de pantalla
    CLOCK.tick(FRAME_RATE)
    pygame.display.update()
