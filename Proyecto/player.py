from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0
        self.health_recovery_delay = 800 # Es el tiempo que tarda en recuperar un punto de vida
        self.time_prev = pg.time.get_ticks() 
        # El tiempo en el que se recupero el ultimo punto de vida
        self.diag_move_corr = 1 / math.sqrt(2)

    def recover_health(self): #Recupera la vida del jugador
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self): #Comprueba el tiempo de recuperacion de la vida
        time_now = pg.time.get_ticks() #Obtenemos el tiempo actual
        if time_now - self.time_prev > self.health_recovery_delay: 
            self.time_prev = time_now #Actualizamos el tiempo de recuperacion
            return True

    def check_game_over(self): #Comprueba si el jugador ha perdido
        if self.health < 1:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def get_damage(self, damage): #Obtiene el daño
        self.health -= damage #Restamos la vida
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over() 

    def single_fire_event(self, event): #Evento de disparo
        if event.type == pg.MOUSEBUTTONDOWN: 
            if event.button == 1 and not self.shot and not self.game.weapon.reloading: #Si se presiona el boton izquierdo del raton
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True 
 
    def movement(self): #Movimiento del jugador
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
 
        keys = pg.key.get_pressed() #Obtenemos las teclas presionadas
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        #  Si se presionan dos teclas a la vez, se reduce la velocidad
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)

    
        self.angle %= math.tau #Actualizamos el angulo  

    def check_wall(self, x, y): #Comprueba si hay una pared
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy): #Comprueba la colision con la pared
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self): #Dibuja al jugador
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.x * 100 + WIDTH * math.cos(self.angle), 
                     self.y * 100 + WIDTH * math. sin(self.angle)), 2)  # Dibujamos la direccion del jugador
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15) 

    def mouse_control(self): #Control del raton
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self): #Actualiza al jugador
        self.movement()
        self.mouse_control()
        self.recover_health()

    @property 
    def pos(self): #Posicion del jugador
        return self.x, self.y

    @property
    def map_pos(self): #Posicion en el mapa
        return int(self.x), int(self.y)