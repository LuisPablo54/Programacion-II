#primer programa en pygame
#principio de pong
import sys,pygame
pygame.init()

#creamos la ventana de jueto
tamano=(800,600)
screen=pygame.display.set_mode(tamano)

deltaTiempo_s=1/20 #el tiempo que pasa entre un cuadro y otro


salir=False
while salir==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
            
                
    #Entrada por teclado
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    #Aqui recalculamos todas las variables 
    

    #Aquí redibujamos todos los objetos.
     
    
  

    
    #flip para pantalla
    pygame.display.flip()

    pygame.time.wait(int(deltaTiempo_s*1000))

    
pygame.display.quit()

print("fin del programa")

