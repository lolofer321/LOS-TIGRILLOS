import pygame
import math
import constants
from ClassBullet import Bullet
pygame.init()
TEXT_FONT = pygame.font.Font("assets/font.otf", 32)
class Game:
    def __init__(self, map, player, enemies, bullets, cursor, current_level):
        self.map = map
        self.player = player
        self.enemies = enemies
        self.bullets = bullets
        self.cursor = cursor
        self.current_level = current_level
        self.current_frame = 0
        self.frame_rate = 200
        self.last_frame = pygame.time.get_ticks()

    #Movimiento de personajes
    def move(self, entity):

        if entity.direccion[0] < 0 and entity.pos_x - entity.move_speed < 0:
            entity.pos_x += entity.move_speed
        if entity.direccion[0] > 0 and entity.pos_x + entity.move_speed > self.map.width - entity.width:
            entity.pos_x -= entity.move_speed
        if entity.direccion[1] < 0 and entity.pos_y - entity.move_speed < 0:
            entity.pos_y += entity.move_speed
        if entity.direccion[1] > 0 and entity.pos_y + entity.move_speed > self.map.height - entity.height:
            entity.pos_y -= entity.move_speed

        entity.pos_x += entity.direccion[0] * entity.move_speed
        entity.pos_y += entity.direccion[1] * entity.move_speed

    #Disparos de personajes
    def shoot(self, source, target):
        source_center = source.get_center()
        objetive_center = target.get_center()

        bullet_velocity = [objetive_center[0] - source_center[0], objetive_center[1] - source_center[1]]

        magnitude = (bullet_velocity[0] ** 2 + bullet_velocity[1] ** 2) ** 0.5
        
        bullet = Bullet(source_center[0], source_center[1], 16, 16, 15, [0, 0], source.damage, pygame.time.get_ticks())
        self.bullets.append(bullet)

        bullet.direccion[0] = bullet_velocity[0] / magnitude
        bullet.direccion[1] = bullet_velocity[1] / magnitude

    def check_collisions(self, obj1, obj2):
        return pygame.Rect.colliderect(pygame.Rect(obj1.pos_x, obj1.pos_y, obj1.width, obj1.height), pygame.Rect(obj2.pos_x, obj2.pos_y, obj2.width, obj2.height))
    
    def map_collisions(self):
        for j in self.player + self.enemies:
            for i in self.map.elements:
                if self.check_collisions(i, j):               
                    if j.direccion[0] < 0 and j.pos_x + j.direccion[0] * j.move_speed > i.pos_x + i.width / 2:
                        j.pos_x = i.pos_x + j.width
                    elif j.direccion[0] > 0 and j.pos_x + j.direccion[0] * j.move_speed < i.pos_x - i.width / 2:
                        j.pos_x = i.pos_x - j.width
                    elif j.direccion[1] < 0 and j.pos_y + j.direccion[1] * j.move_speed > i.pos_y + i.height / 2:
                        j.pos_y = i.pos_y + j.height
                    elif j.direccion[1] > 0 and j.pos_y + j.direccion[1] * j.move_speed < i.pos_y - i.height / 2:
                        j.pos_y = i.pos_y - j.height

    def entitys_collisions(self):
        for j in self.player + self.enemies:
            for i in self.player + self.enemies:
                if i == j or i.type == "door" or j.type == "door":
                    continue
                if self.check_collisions(i, j):
                    if j.direccion[0] <= 0 and j.pos_x + j.direccion[0] * j.move_speed >= i.pos_x + i.width / 2 and i.direccion[0] >= 0 and i.pos_x + i.direccion[0] * i.move_speed <= j.pos_x - j.width / 2:
                        j.pos_x, i.pos_x = j.pos_x + 5, i.pos_x - 5
                    elif j.direccion[0] >= 0 and j.pos_x + j.direccion[0] * j.move_speed <= i.pos_x - i.width / 2 and i.direccion[0] <= 0 and i.pos_x + i.direccion[0] * i.move_speed >= j.pos_x + j.width / 2:
                        j.pos_x, i.pos_x = j.pos_x - 5, i.pos_x + 5
                    elif j.direccion[1] <= 0 and j.pos_y + j.direccion[1] * j.move_speed >= i.pos_y + i.height / 2 and i.direccion[1] >= 0 and i.pos_y + i.direccion[1] * i.move_speed <= j.pos_y - j.height / 2:
                        j.pos_y, i.pos_y = j.pos_y + 5, i.pos_y - 5
                    elif j.direccion[1] >= 0 and j.pos_y + j.direccion[1] * j.move_speed <= i.pos_y - i.height / 2 and i.direccion[1] <= 0 and i.pos_y + i.direccion[1] * i.move_speed >= j.pos_y + j.height / 2:
                        j.pos_y, i.pos_y = j.pos_y - 5, i.pos_y + 5

    #Bala hace daño
    def bullet_attack(self):
        for b in self.bullets:
            for e in self.enemies + self.player:
                if self.check_collisions(b, e) and pygame.time.get_ticks() - b.create_time > 200:
                    self.take_damage(e, b)
                    self.destroy(b)

    #Bala es destruida
    def bullet_kill(self):
        for b in self.bullets:
            if b.pos_x > self.map.width - 40 or b.pos_x < 40 or b.pos_y > self.map.height - 40 or b.pos_y < 40:
                self.destroy(b)   
            for i in self.map.elements:
                if self.check_collisions(b, i):
                    self.destroy(b)
    
    #Funcion para destruir
    def destroy(self, target):
        if target in self.player:
            self.player.remove(target)
        elif target in self.enemies:
            self.enemies.remove(target)
            self.player[0].coin += 10
        elif target in self.bullets:
            self.bullets.remove(target)
        
    #Personajes reciben daño y pupeden morir
    def take_damage(self, target, bullet):
        target.health -= bullet.damage
        if target.health <= 0:
            self.destroy(target)

    #Dibujar arma de cada personaje
    def draw_gun(self, entity, target, window):
        rel_x, rel_y = target.get_center()[0] - entity.get_center()[0], target.get_center()[1] - entity.get_center()[1]
        angle = math.degrees(math.atan2(-rel_y, rel_x))
        gunpos_x = entity.get_center()[0] - 64
        gunpos_y = entity.get_center()[1] - 20
        if target.pos_x < entity.pos_x:
            angle = math.degrees(math.atan2(-rel_y, rel_x))
            
            window.blit(pygame.transform.rotate((self.map.assets[entity.gun_type][1]), 180 + angle), (gunpos_x, entity.get_center()[1]))
        else:
            angle = math.degrees(math.atan2(-rel_y, rel_x))
            window.blit(pygame.transform.rotate((self.map.assets[entity.gun_type][0]), angle), (entity.get_center()[0], entity.get_center()[1]))

    #Dibujar personajes, balas, armas y vida
    def render(self, window):
        
        for i in self.enemies:
            if i.type == "door":
                continue
            #Dibujar movmientos de enemigo
            if i.direccion[0] > 0:
                window.blit(self.map.assets[i.type]["0"][self.current_frame], (i.pos_x, i.pos_y))
                if pygame.time.get_ticks() - self.last_frame >= self.frame_rate:
                    self.current_frame += 1
                    self.last_frame = pygame.time.get_ticks()
                if self.current_frame >= len(self.map.assets[i.type]["0"]):
                    self.current_frame = 0
            elif i.direccion[0] < 0:
                window.blit(self.map.assets[i.type]["1"][self.current_frame], (i.pos_x, i.pos_y))
                if pygame.time.get_ticks() - self.last_frame >= self.frame_rate:
                    self.current_frame += 1
                    self.last_frame = pygame.time.get_ticks()
                if self.current_frame >= len(self.map.assets[i.type]["1"]):
                    self.current_frame = 0
            else: window.blit(self.map.assets[i.type]["0"][self.current_frame], (i.pos_x, i.pos_y))
            #Dibujar vida de enemigos y llamar drawgun
            for j in range(i.health):
                pygame.draw.rect(window, (255,0,0), ((i.pos_x+i.width/2)-i.health/2*10+10*j,i.pos_y-10,10,10))
            self.draw_gun(i, self.player[0], window)
        
        for i in self.player:
            #Dibujar sprites de movimiento
            if i.direccion[0] > 0:
                window.blit(self.map.assets[i.type]["0"][self.current_frame], (i.pos_x, i.pos_y))
                if pygame.time.get_ticks() - self.last_frame >= self.frame_rate:
                    self.current_frame += 1
                    self.last_frame = pygame.time.get_ticks()
                if self.current_frame >= len(self.map.assets[i.type]["0"]):
                    self.current_frame = 0
            elif i.direccion[0] < 0:
                window.blit(self.map.assets[i.type]["1"][self.current_frame], (i.pos_x, i.pos_y))
                if pygame.time.get_ticks() - self.last_frame >= self.frame_rate:
                    self.current_frame += 1
                    self.last_frame = pygame.time.get_ticks()
                if self.current_frame >= len(self.map.assets[i.type]["1"]):
                    self.current_frame = 0
            else: window.blit(self.map.assets[i.type]["0"][self.current_frame], (i.pos_x, i.pos_y))

            #Llamar funcion drawgun
            self.draw_gun(i, self.cursor[0], window)
            #Dibujar vida y monedas
            if self.current_level == "level13":
                continue
            for j in range(i.health):
                window.blit(self.map.assets["life"], (40 + j*45, 40))
            window.blit(self.map.assets["coin"], (40, 640))
            txt3 = TEXT_FONT.render(f"{self.player[0].coin}", 1, (255, 255, 255))
            self.map.window.blit(txt3, (90, 642))
            txta = TEXT_FONT.render(f"[1] Arma 1", 1, (255, 255, 255))
            txtb = TEXT_FONT.render(f"[2] Arma 2", 1, (255, 255, 255))
            txtc = TEXT_FONT.render(f"[3] Arma 3", 1, (255, 255, 255))
            self.map.window.blit(txta, (250, 650))
            if self.player[0].coin >= 110:
                self.map.window.blit(txtb, (550, 650))
            if self.player[0].coin >= 260:
                self.map.window.blit(txtc, (850, 650))

        #Dibujar aviso para pasar a la siguiente habitacion
        if len(self.enemies) == 1 and self.current_level != 13:
            txt = TEXT_FONT.render(f"PASE AL SIGUIENTE NIVEL", 1, (255, 255, 255))
            self.map.window.blit(txt, (720, 80))
            window.blit(pygame.transform.rotate((self.map.assets["arrow"]), 90), (1200, 320))
        
        #Llamar funciones de la bala y dibujarlas
        self.bullet_kill()
        self.bullet_attack()
        for i in self.bullets:
            window.blit(self.map.assets["bullet_type1"], (i.pos_x, i.pos_y))
        
        #Dibujar cursor
        for i in self.cursor:
            if i.type == "cursor":
                mousePos = pygame.mouse.get_pos()
                i.pos_x = mousePos[0] - i.width / 2
                i.pos_y = mousePos[1] - i.height / 2
                window.blit(self.map.assets["cursor"], (i.pos_x, i.pos_y))