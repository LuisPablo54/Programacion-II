#primer programa en pygame
#principio de pong
import pygame
import sys
import configuracion as CP


from mapa import *
from jugador import *

#creamos la ventana del juego
tamano=(CP.Confi.ancho,CP.Confi.alto)
screen=pygame.display.set_mode(tamano)

class Game:
    def __init__(self): #constructor
        pygame.init()
        self.screen = pygame.display.set_mode(tamano)
        self.clock = pygame.time.Clock()
        self.dalta_Tiempo_s = 1
        self.new_game()
        return
    
    def new_game(self): #inicializa variables
        self.map = Map(self) #crea el mapa
        self.jugador = Jugador(self) #crea el jugador
        return  
    
    def update(self): #actualiza variables
        self.jugador.update() #actualiza el jugador
        pygame.display.flip()
        self.dalta_Tiempo_s = self.clock.tick(60)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self): #dibuja en pantalla
        self.screen.fill('black')
        self.map.draw()
        self.jugador.draw()
        return

    def run(self): #bucle principal
        while True:
            self.check_events() #comprueba eventos
            self.update() #actualiza variables
            self.draw() #dibuja en pantalla

    def check_events(self): #comprueba eventos
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit() #cierra la ventana
                sys.exit()

