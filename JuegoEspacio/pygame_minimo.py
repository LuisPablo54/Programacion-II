#primer programa en pygame
#principio de pong
import sys,pygame
import configuracinJuego as CFG
import ModuloJuego as MJ
pygame.init()

#creamos la ventana de jueto
tamano=(800,600)
screen=pygame.display.set_mode(tamano)

deltaTiempo_s=CFG.Confi.deltaTiempo_s #el tiempo que pasa entre un cuadro y otro

EsteJuego = MJ.Juego()

salir=False
while salir==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
            
                
    #Entrada por teclado
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    EsteJuego.ActualizaVariables()
    #Aqui recalculamos todas las variables 
    EsteJuego.dibuja(screen)

    #Aquí redibujamos todos los objetos.
     
    
  

    
    #flip para pantalla
    pygame.display.flip()

    pygame.time.wait(int(deltaTiempo_s*1000))

    
pygame.display.quit()

print("fin del programa")

