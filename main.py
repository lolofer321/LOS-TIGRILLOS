import pygame
import random
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

pygame.init()

cursor = [Element(0, 0, 50, 50, "cursor")]
objects1 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type1"),
            Element(480, 560, 80, 80, "type1"),
            Element(480, 640, 80, 80, "type1"),
            Element(560, 640, 80, 80, "type1"),
            Element(640, 640, 80, 80, "type1"),
            Element(640, 160, 80, 80, "type1"),
            Element(560, 160, 80, 80, "type1"),
            Element(480, 160, 80, 80, "type1"),
            Element(720, 160, 80, 80, "type1"),
            Element(800, 160, 80, 80, "type1")
            ]
objects2 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects3 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects4 = []
objects5 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects6 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects7 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects8 = [
            ]
objects9 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects10 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects11 = [
            Element(160, 0, 80, 80, "type1"),
            Element(160, 80, 80, 80, "type1"),
            Element(160, 160, 80, 80, "type1"),
            Element(480, 480, 80, 80, "type2"),
            Element(480, 560, 80, 80, "type2"),
            Element(480, 640, 80, 80, "type2"),
            Element(560, 640, 80, 80, "type2"),
            Element(640, 640, 80, 80, "type2"),
            Element(640, 160, 80, 80, "type2"),
            Element(560, 160, 80, 80, "type2"),
            Element(480, 160, 80, 80, "type2"),
            Element(720, 160, 80, 80, "type2"),
            Element(800, 160, 80, 80, "type2")
            ]
objects12 = []
player = [
    Player(100, 100, 80, 80, 10, 8, 5, [0, 0],
           {"left": False, "right": False, "up": False, "down": False})]
enemies1 = [
            Enemy(720, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(560, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(600, 520, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(1180, 280, 100, 100, 10**10, 0, 0, [0, 0], 1,"door"),
            ]
enemies2 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies3 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies4 = [
            Enemy(720, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(560, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(600, 520, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], 1,"door"),
            ]
enemies5 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies6 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies7 = [
            Enemy(720, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(560, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(600, 520, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], 1,"door"),
            ]
enemies8 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies9 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type3"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies10 = [
            Enemy(720, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(560, 80, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(600, 520, 80, 80, 5, 5, 5, [0, 0], 1, "type1"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], 1,"door"),
            ]
enemies11 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
enemies12 = [
            Enemy(640, 80, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 240, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(640, 640, 80, 80, 5, 5, 5, [0, 0], "level12", "type2"),
            Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], "level12","door"),
            ]
bullets = []

CLOCK = pygame.time.Clock()

WINDOW_SIZE = (1280, 720)
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)
util = Utils(WINDOW_SIZE[0], WINDOW_SIZE[1])
util.load_assets()
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
level1 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level1", objects1, util.assets)
level2 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level2", objects2, util.assets)
level3 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level3", objects3, util.assets)
level4 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level4", objects4, util.assets)
level5 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level5", objects5, util.assets)
level6 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level6", objects6, util.assets)
level7 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level7", objects7, util.assets)
level8 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level8", objects8, util.assets)
level9 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level9", objects9, util.assets)
level10 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level10", objects10, util.assets)
level11 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level11", objects11, util.assets)
level12 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level12", objects12, util.assets)

game = Game(level1, player, enemies1, bullets, cursor, 1)
control= Control(game)  
auto = Auto(game)
pygame.mouse.set_visible(False)

while True:

    if len(player) == 0:
        exit()
    
    control.check_buttons()
    auto.execute()

    if game.current_level == 1:
        level1.render()
    elif game.current_level == 2:
        level2.render()
    elif game.current_level == 3:
        level3.render()
    if game.current_level == 4:
        level4.render()
    elif game.current_level == 5:
        level5.render()
    elif game.current_level == 6:
        level6.render()
    if game.current_level == 7:
        level7.render()
    elif game.current_level == 8:
        level8.render()
    elif game.current_level == 9:
        level9.render()
    if game.current_level == 10:
        level10.render()
    elif game.current_level == 11:
        level11.render()
    elif game.current_level == 12:
        level12.render()
    elif game.current_level == 13:
        exit()

    for i in bullets:
        game.move(i)
    if len(player) != 0:
        game.move(player[0])
    
    game.render(WINDOW)
    game.map_collisions()
    
    #Cambio de nivel
    if game.check_collisions(player[0], game.enemies[-1]) and len(game.enemies) == 1:
        game.current_level += 1
        if game.current_level == 2:
            game.map = level2
            game.enemies = enemies2
            map.elements = objects2
        if game.current_level == 3:
            game.map = level3
            game.enemies = enemies3
            map.elements = objects3
        if game.current_level == 4:
            game.map = level4
            game.enemies = enemies4
            map.elements = objects4
        if game.current_level == 5:
            game.map = level5
            game.enemies = enemies5
            map.elements = objects5
        if game.current_level == 6:
            game.map = level6
            game.enemies = enemies6
            map.elements = objects6
        if game.current_level == 7:
            game.map = level7
            game.enemies = enemies7
            map.elements = objects7
        if game.current_level == 8:
            game.map = level8
            game.enemies = enemies8
            map.elements = objects8
        if game.current_level == 9:
            game.map = level9
            game.enemies = enemies9
            map.elements = objects9
        if game.current_level == 10:
            game.map = level10
            game.enemies = enemies10
            map.elements = objects10
        if game.current_level == 11:
            game.map = level11
            game.enemies = enemies11
            map.elements = objects11
        if game.current_level == 12:
            game.map = level12
            game.enemies = enemies12
            map.elements = objects12
        player[0].pos_x = 50

    CLOCK.tick(120)
    pygame.display.update()