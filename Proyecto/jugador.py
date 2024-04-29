from configuracion import Confi
import pygame as pg
import math

class Jugador:
    def __init__(self, game): #constructor de la clase
        self.game = game
        self.x, self.y = Confi.jugadorPos
        self.angle = Confi.jugadorAngulo

    def movimiento(self): #movimiento del jugador
        sing_a = math.sin(self.angle) #seno del angulo
        cos_a = math.cos(self.angle)#coseno del angulo
        dx, dy = 0, 0 #desplazamiento en x y y
        speed = Confi.jugadorVelocidad * self.game.dalta_Tiempo_s #velocidad del jugador
        speed_cos_a = speed * cos_a #velocidad por coseno del angulo
        speed_sing_a = speed * sing_a #velocidad por seno del angulo

        keys = pg.key.get_pressed() #teclas presionadas por el jugador
        if keys[pg.K_w]:
            dx += speed_cos_a
            dy += speed_sing_a
        if keys[pg.K_s]:
            dx += -speed_cos_a
            dy += -speed_sing_a
        if keys[pg.K_a]:
            dx += speed_sing_a
            dy += -speed_cos_a
        if keys[pg.K_d]:
            dx += -speed_sing_a
            dy += speed_cos_a
        
        self.VerificarMuros(dx, dy) #verifica si hay muros

        if keys[pg.K_LEFT]: #si se presiona la tecla izquierda
            self.angle -= Confi.jugadorRotacion * self.game.dalta_Tiempo_s  #rota el jugador
        if keys[pg.K_RIGHT]:
            self.angle += Confi.jugadorRotacion * self.game.dalta_Tiempo_s
        self.angle %= math.tau #angulo en radianes
    
    def Muros(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def VerificarMuros(self, dx, dy):
        if self.Muros(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.Muros(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self): #dibuja el jugador
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 
                     (self.x * 100 + Confi.ancho * math.cos(self.angle),
                        self.y * 100 + Confi.ancho * math.sin(self.angle)), 2) 
        pg.draw.circle(self.game.screen, 'green', (int(self.x * 100), int(self.y * 100)), 15)

    def update(self): #actualiza el jugador
        self.movimiento()

    def pos(self): #posicion del jugador
        return self.x, self.y
    
    def map_pos(self): #posicion en el mapa
        return int(self.x), int(self.y)