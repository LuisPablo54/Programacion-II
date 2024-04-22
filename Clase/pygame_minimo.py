#primer programa en pygame
#principio de pong
import sys,pygame
pygame.init()
import juegodePOong as JP
import ConfiPOONG as CP

#creamos la ventana de jueto
tamano=(800,600)
screen=pygame.display.set_mode(tamano)

MiJuego = JP.Juego()
amarillo=(255,255,0,225)
rosa=(223,32,133)

cnt = 0
x = 0
y = 300
vx_px_s= 266 #pixeles por segundo 

salir=False
while salir==False:


    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True        
                
    #Entrada por teclado
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    #Aqui recalculamos todas las variables 
    MiJuego.Recalcular()
    MiJuego.Dibujar(screen)
    
    
    
    #flip para pantalla
    pygame.display.flip()
    pygame.time.wait(int(CP.Confi.deltaTiempo_s *1000))

    
pygame.display.quit()

print("fin del programa")

