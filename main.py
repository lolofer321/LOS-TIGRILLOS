import pygame
import json
import constants

from ClassObject import Object
from ClassEnemy import Enemy
from ClassPlayer import Player
from Classmap import map
from ClassUtils import Utils
from ClassElement import Element
from ClassGame import Game
from ClassBullet import Bullet
from ClassControl import Control
from ClassPseudoAuto import Auto
from ClassButton import Button

pygame.init()

CLOCK = pygame.time.Clock()

#Pantalla
WINDOW_SIZE = (1280, 720)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
MENU = pygame.display.set_mode((WINDOW_SIZE))
BACKGROUNDMENU = pygame.image.load("assets/backgroundmenu.png")

TEXT_FONT = pygame.font.Font("assets/font.otf", 32)

#Cargar assets
util = Utils(WINDOW_SIZE[0], WINDOW_SIZE[1])
util.load_assets()

#Cargar datos
with open('gameconfig.json', 'r') as f:
    DATA = json.load(f)

ENEMIES = {}
LEVELS = {}
for stage in DATA["stages"]:
    name = stage["name"]
    next_level = stage["next_level"]
    OBJECTS = []
    for obj in stage["objects"]:
        object = Element(obj["posX"], obj["posY"], obj["alto"], obj["ancho"], obj["type"])
        OBJECTS.append(object)    
    enemies = []
    for en in stage["enemies"]:
        enemy = Enemy(en["posX"], en["posY"], en["alto"], en["ancho"], en["vida"], en["movimiento"], en["attackSpeed"], en["direccion"], en["nivel"], en["type"])
        enemies.append(enemy)
    ENEMIES[name] = enemies
    level = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], name, OBJECTS, util.assets, next_level)
    LEVELS[name] = level

#Objetos
cursor = [Element(0, 0, 50, 50, "cursor")]
player = [
    Player(100, 100, 80, 80, 10, 8, 5, [0, 0],
           {"left": False, "right": False, "up": False, "down": False})]
bullets = []

#Crear objeto juego, control y auto
game = Game(LEVELS[constants.NIVEL_INICIAL], player, ENEMIES[constants.NIVEL_INICIAL], bullets, cursor, constants.NIVEL_INICIAL)
control= Control(game)  
auto = Auto(game)

#Funcion principal para jugar
def play():
    pygame.mouse.set_visible(False)
    #Bucle principal
    while True:
        #Jugador muere
        if len(player) == 0:
            exit()
        
        #Acciones del jugador y enemigos
        control.check_buttons()
        auto.execute()

        #Renderizado de niveles
        LEVELS[game.current_level].render()

        #MLlamar movimiento de balas y el jugador
        for i in bullets:
            game.move(i)
        if len(player) != 0:
            game.move(player[0])
        
        #Renderizado del juego
        game.render(WINDOW)
        game.map_collisions()
        
        #Cambio de nivel
        if game.check_collisions(player[0], game.enemies[-1]) and len(game.enemies) == 1:
            game.current_level = LEVELS[game.current_level].next_level
            game.map = LEVELS[game.current_level]
            game.enemies = ENEMIES[game.current_level]
            map.elements = game.map.elements
            player[0].pos_x = 50

        CLOCK.tick(120)
        pygame.display.update()
#Menu
def main_menu():
    #Bucle menu
    pygame.mouse.set_visible(True)
    while True:
        MENU.blit(BACKGROUNDMENU, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button(0, 0, 1280, 720,
                             pygame.transform.scale(pygame.image.load("assets/playbutton.png"), (1280, 720)))
        PLAY_BUTTON.render(MENU)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_input(MENU_MOUSE_POS):
                    game.current_level == constants.NIVEL_INICIAL
                    play()
    
        pygame.display.update()

main_menu()