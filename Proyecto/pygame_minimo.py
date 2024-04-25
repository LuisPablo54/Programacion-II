#primer programa en pygame
#principio de pong
import pygame
import sys
import configuracion as CP
pygame.init()


#creamos la ventana del juego
tamano=(CP.Confi.ancho,CP.Confi.alto)
screen=pygame.display.set_mode(tamano)

#bucle principal

salir=False
while salir==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True        
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    #Aqui recalculamos todas las variables 
  
    



    
    
    #flip para pantalla
    pygame.display.flip()
    pygame.time.wait(int(CP.Confi.deltaTiempo_s *1000))

    
pygame.display.quit()

print("fin del programa")

