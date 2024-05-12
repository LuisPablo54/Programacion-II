#primer programa en pygame
#principio de pong
import pygame
import sys
import configuracion as CP
import main as MJ


from mapa import *
from jugador import *

#creamos la ventana del juego
tamano=(CP.Confi.ancho,CP.Confi.alto)
screen=pygame.display.set_mode(tamano)

deltaTiempo_s=CP.Confi.deltaTiempo_s #el tiempo que pasa entre un cuadro y otro



salir=False
while salir==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
            
                
    #Entrada por teclado
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    #programa principal 
    game = MJ.Game()
    game.run()
    
    #flip para pantalla
    pygame.display.flip()

    pygame.time.wait(int(deltaTiempo_s*1000))

    
pygame.display.quit()

print("fin del programa")

