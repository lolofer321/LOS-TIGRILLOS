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
objects = [
    Element(149, 250, 80, 80, "type1"),
    Element(450, 250, 80, 80, "type1"),
    Element(750, 250, 80, 80, "type1"),
    Element(1050, 250, 80, 80, "type1"),
    Element(150, 450, 80, 80, "type2"),
    Element(450, 450, 80, 80, "type2"),
    Element(750, 450, 80, 80, "type2"),
    Element(1050, 450, 80, 80, "type2"),
    ]
player = [
    Player(100, 100, 80, 80, 20, 5, 5, [0, 0],
           {"left": False, "right": False, "up": False, "down": False})]
enemies1 = [
    Enemy(900, 100, 80, 80, 5, 5, 5, [0, 0], None, "type1"),
    Enemy(900, 300, 80, 80, 5, 5, 5, [0, 0], None, "type1"),
    Enemy(900, 500, 80, 80, 5, 5, 5, [0, 0], None, "type1"),
    Enemy(1180, 360, 100, 100, 100000, 0, 0, [0, 0], None,"door")]
enemies2 = [
    Enemy(900, 100, 80, 80, 5, 5, 5, [0, 0], None, "type2"),
    Enemy(900, 300, 80, 80, 5, 5, 5, [0, 0], None, "type2"),
    Enemy(900, 500, 80, 80, 5, 5, 5, [0, 0], None, "type2")]

bullets = []

CLOCK = pygame.time.Clock()

WINDOW_SIZE = (1280, 720)
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)
util = Utils(WINDOW_SIZE[0], WINDOW_SIZE[1])
util.load_assets()
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
level1 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level1", objects, util.assets)
level2 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], "level2", objects, util.assets)

game = Game(level1, player, enemies1, bullets, cursor, 1)
control= Control(game)  
auto = Auto(game)
pygame.mouse.set_visible(False)

while True:

    if len(player) == 0:
        exit()

    """for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game.enemies = enemies1
                game.current_level = 2
                game.map = level2"""
    
    control.check_buttons()
    auto.execute()

    if game.current_level == 1:
        level1.render()
    else:
        level2.render()
    for i in bullets:
        game.move(i)
    if len(player) != 0:
        game.move(player[0])
    game.render(WINDOW)
    game.map_collisions()

    game.bullet_atack()
    game.bullet_kill()
    if len(player) != 0:
        textPosicion = 10
        for obj in objects:
            """txt = TEXT_FONT.render(f"{obj}", 1, WHITE)
            WINDOW.blit(txt, (10, textPosicion))
            textPosicion += 30"""

            txt2 = TEXT_FONT.render(f"{player[0].health}", 1, (0,0,0))
            WINDOW.blit(txt2, (10, WINDOW_SIZE[1] - 40))

    if len(enemies1) == 1 and game.check_collisions(player[0], enemies1[-1]):
        player[0].pos_x = 50
        game.enemies = enemies2
        game.current_level = 2
        game.map = level2

    CLOCK.tick(120)
    pygame.display.update()