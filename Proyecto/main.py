#Importamos la librerias necesarias
import pygame as pg
import sys

#Importamos los modulos necesarios
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import * #Modelo de busqueda de caminos


class Game:
    def __init__(self):
        pg.init() # Inicializamos pygame
        pg.mouse.set_visible(False) # Ocultamos el cursor del raton
        self.screen = pg.display.set_mode(RES) # Creamos la ventana del juego
        pg.event.set_grab(True) # Capturamos el raton
        self.clock = pg.time.Clock() # Creamos un reloj para controlar el tiempo
        self.delta_time = 1 # Variable para controlar el tiempo
        self.global_trigger = False # Variable para controlar los eventos globales
        self.global_event = pg.USEREVENT + 0 # Creamos un evento global
        pg.time.set_timer(self.global_event, 40) # Establecemos un temporizador para el evento global
        self.new_game() 

    def new_game(self): # Creamos una nueva partida
        self.map = Map(self) 
        self.player = Player(self) 
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self) 
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self) 
        pg.mixer.music.play(-1)
 
    def update(self): # Actualizamos el juego
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip() # Actualizamos la pantalla
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self): # Dibujamos el juego
        self.object_renderer.draw()
        self.weapon.draw()
        

    def check_events(self): # Comprobamos los eventos
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()



