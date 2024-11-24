import pygame
from ClassBullet import Bullet
class Game:
    def __init__(self, map, player, enemies, bullets):
        self.map = map
        self.player = player
        self.enemies = enemies
        self.bullets = bullets
        self.current_frame = 0
        self.frame_rate = 200
        self.last_frame = pygame.time.get_ticks()

    def move(self, entity):

        entity.pos_x += entity.direccion[0] * entity.move_speed
        entity.pos_y += entity.direccion[1] * entity.move_speed

        if entity.direccion[0] < 0 and entity.pos_x - entity.move_speed < 0:
            entity.pos_x += entity.move_speed
        if entity.direccion[0] > 0 and entity.pos_x + entity.move_speed > self.map.width - entity.width:
            entity.pos_x -= entity.move_speed
        if entity.direccion[1] < 0 and entity.pos_y - entity.move_speed < 0:
            entity.pos_y += entity.move_speed
        if entity.direccion[1] > 0 and entity.pos_y + entity.move_speed > self.map.height - entity.height:
            entity.pos_y -= entity.move_speed

    def shoot(self, source, target):
        source_center = source.get_center()
        #Los objetos deben ser creados en el render
        bullet = Bullet(source_center[0], source_center[1], 16, 16, 10, [0, 0], 2)
        self.bullets.append(bullet)

        objetive_center = target.get_center()
        bullet_velocity = [objetive_center[0] - source_center[0], objetive_center[1] - source_center[1]]

        magnitude = (bullet_velocity[0] ** 2 + bullet_velocity[1] ** 2) ** 0.5
        
        bullet.direccion[0] = bullet_velocity[0] / magnitude
        bullet.direccion[1] = bullet_velocity[1] / magnitude

    def check_collisions(self, obj1, obj2):
        x1, y1 = obj1.get_center()
        x2, y2 = obj2.get_center()
        w1, h1 = obj1.width / 2, obj1.height / 2
        w2, h2 = obj2.width / 2, obj2.height / 2
        if x1 + w1 >= x2 - w2 and x1 - w1 <= x2 + w2:
            return y1 + h1 >= y2 - h2 and y1 - h1 <= y2 + h2
        return False
    
    def map_collisions(self):
        for j in self.player + self.enemies:
            for i in self.map.elements:
                if self.check_collisions(i, j):
                    if j.direccion[0] < 0 and j.pos_x + j.direccion[0] * j.move_speed > i.pos_x + i.width / 2:
                        j.pos_x -= j.direccion[0] * j.move_speed
                    elif j.direccion[0] > 0 and j.pos_x + j.direccion[0] * j.move_speed < i.pos_x - i.width / 2:
                        j.pos_x -= j.direccion[0] * j.move_speed
                    if j.direccion[1] < 0 and j.pos_y + j.direccion[1] * j.move_speed > i.pos_y + i.height / 2:
                        j.pos_y -= j.direccion[1] * j.move_speed
                    elif j.direccion[1] > 0 and j.pos_y + j.direccion[1] * j.move_speed < i.pos_y - i.height / 2:
                        j.pos_y -= j.direccion[1] * j.move_speed

    def bullet_kill(self):
        for b in self.bullets:
            if b.pos_x > self.map.width - 40 or b.pos_x < 40 or b.pos_y > self.map.height - 40 or b.pos_y < 40:
                self.destroy(b)
            for i in self.map.elements:
                print(self.check_collisions(b, i))
                if self.check_collisions(b, i):
                    self.destroy(b)
    
    def destroy(self, target):
        if target in self.player:
            self.player.remove(target)
        elif target in self.enemies:
            self.enemies.remove(target)
        else:
            self.bullets.remove(target)
        
    def take_damage(self, target, bullet):
        target.health -= bullet.damage
        if target.health <= 0:
            self.destroy() 

    def render(self, window):
        for i in self.player:
            window.blit(self.map.assets["player"][self.current_frame], (i.pos_x, i.pos_y))
            if pygame.time.get_ticks() - self.last_frame >= self.frame_rate:
                self.current_frame += 1
                self.last_frame = pygame.time.get_ticks()
            if self.current_frame >= len(self.map.assets["player"]):
                self.current_frame = 0
        for i in self.enemies:
            window.blit(self.map.assets["enemy_type1"], (i.pos_x, i.pos_y))
        for i in self.bullets:
            window.blit(self.map.assets["bullet_type1"], (i.pos_x, i.pos_y))