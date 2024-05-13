from sprite_object import * #Importamos la clase AnimatedSprite
from random import randint, random


class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        # Cargamos las imagenes de las animaciones
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')
        
        # Variables de movimiento
        self.attack_dist = randint(3, 6)
        self.speed = 0.01
        self.size = 20
        self.health = 100 # Salud del NPC predeterminada
        self.attack_damage = 10 # Daño del NPC predeterminado
        self.accuracy = 0.15 # Precisión del NPC predeterminada
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False  

    def update(self): # Actualizamos el NPC
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        # self.draw_ray_cast()

    def check_wall(self, x, y): # Comprobamos si hay una pared 
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy): # Comprobamos si hay colision con una pared
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def movement(self): # Movimiento del NPC para seguir al jugador
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos

        
        if next_pos not in self.game.object_handler.npc_positions: # Comprobamos si hay un NPC en la siguiente posicion
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x) # Calculamos el angulo
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collision(dx, dy) 

    def attack(self): # Ataque del NPC
        if self.animation_trigger:
            self.game.sound.npc_shot.play() # Reproducimos el sonido del disparo
            if random() < self.accuracy: # Comprobamos si el disparo acierta
                self.game.player.get_damage(self.attack_damage) # El jugador recibe daño

    def animate_death(self): # Animacion de muerte del NPC
        if not self.alive:
            if self.game.global_trigger and self.frame_counter < len(self.death_images) - 1: # Comprobamos si se ha terminado la animacion
                self.death_images.rotate(-1) # Rotamos la animacion
                self.image = self.death_images[0]
                self.frame_counter += 1 # Aumentamos el contador de frames

    def animate_pain(self): # Animacion de dolor del NPC
        self.animate(self.pain_images) # Animamos el NPC
        if self.animation_trigger:
            self.pain = False 

    def check_hit_in_npc(self): # Comprobamos si el jugador ha disparado al NPC
        if self.ray_cast_value and self.game.player.shot: 
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width: # Comprobamos si el disparo ha acertado
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage # El NPC recibe daño
                self.check_health()

    def check_health(self): # Comprobamos la salud del NPC
        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play() # Reproducimos el sonido de la muerte del NPC

    def run_logic(self): # Logica del NPC
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc() # Comprobamos si el jugador esta en la linea de vision del NPC
            self.check_hit_in_npc() # Comprobamos si el jugador ha disparado al NPC

            if self.pain:
                self.animate_pain()

            elif self.ray_cast_value:
                self.player_search_trigger = True # Activamos la busqueda del jugador

                if self.dist < self.attack_dist:
                    self.animate(self.attack_images) # Animamos el NPC para atacar
                    self.attack()
                else:
                    self.animate(self.walk_images) # Animamos el NPC para caminar
                    self.movement()

            elif self.player_search_trigger:
                self.animate(self.walk_images) # Animamos el NPC para caminar
                self.movement()

            else:
                self.animate(self.idle_images) # Animamos el NPC para estar en reposo
        else:
            self.animate_death() # Animamos el NPC para morir

    @property
    def map_pos(self): 
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self): # Raycast para comprobar si el jugador esta en la linea de vision del NPC
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontal
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH): 
            tile_hor = int(x_hor), int(y_hor) # Comprobamos si hay una pared en la horizontal
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor # Calculamos la distancia del jugador
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth # Calculamos la profundidad

        # vertical
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def draw_ray_cast(self): # Dibujamos el raycast
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15) # Dibujamos un circulo en la posicion del NPC
        if self.ray_cast_player_npc(): # Comprobamos si el jugador esta en la linea de vision del NPC
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                         (100 * self.x, 100 * self.y), 2) 


class SoldierNPC(NPC): # Clase del NPC Soldier
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.health = 50
        

class CacoDemonNPC(NPC):  # Clase del NPC CacoDemon
    def __init__(self, game, path='resources/sprites/npc/caco_demon/0.png', pos=(10.5, 6.5),
                 scale=0.7, shift=0.27, animation_time=250):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 50
        self.attack_damage = 10
        self.speed = 0.04
        self.accuracy = 0.35

class CyberDemonNPC(NPC): # Clase del NPC CyberDemon
    def __init__(self, game, path='resources/sprites/npc/cyber_demon/0.png', pos=(11.5, 6.0),
                 scale=1.0, shift=0.04, animation_time=210):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 4
        self.health = 150
        self.attack_damage = 20
        self.speed = 0.01
        self.accuracy = 0.25





















