#primer programa en pygame
#principio de pong
import pygame
import sys
import settings as CP
import main as MJ


from map import *
from player import *

#creamos la ventana del juego
tamano= CP.RES
screen=pygame.display.set_mode(tamano)

deltaTiempo_s= 0.01 #el tiempo que pasa entre un cuadro y otro



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
    
    

    
pygame.display.quit()

print("fin del programa")

