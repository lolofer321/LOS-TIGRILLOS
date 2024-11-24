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

objects = [
    Element(150, 250, 80, 80, "type1"),
    Element(450, 250, 80, 80, "type1"),
    Element(750, 250, 80, 80, "type1"),
    Element(1050, 250, 80, 80, "type1"),
    Element(150, 450, 80, 80, "type2"),
    Element(450, 450, 80, 80, "type2"),
    Element(750, 450, 80, 80, "type2"),
    Element(1050, 450, 80, 80, "type2")]
player = [
    Player(100, 100, 80, 80, 5, 5, 5, [0, 0],
           {"left": False, "right": False, "up": False, "down": False})]
enemies = [
    Enemy(200, 100, 80, 80, 5, 5, 5, [0, 0], None)]
bullets = []

CLOCK = pygame.time.Clock()

WINDOW_SIZE = (1280, 720)
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)
util = Utils(WINDOW_SIZE[0], WINDOW_SIZE[1])
util.load_assets()
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
level1 = map(WINDOW, WINDOW_SIZE[0], WINDOW_SIZE[1], objects, util.assets)

game = Game(level1, player, enemies, bullets)
control= Control(game)
auto = Auto(game)

while True:
    control.check_buttons()
    auto.execute()

    level1.render()
    for i in bullets:
        game.move(i)
    game.move(player[0])
    game.render(WINDOW)
    game.map_collisions()
    game.bullet_kill()

    CLOCK.tick(120)
    pygame.display.update()
