import math
#Configuracion de la aplicacion

class Confi():
    #Configuracion de la ventana
    ancho = 1600
    alto = 900
    
    #Configuracion de la pantalla
    ress= ancho,alto
    deltaTiempo_s=0.01
    
    #Configuracion de la camara del jugador
    jugadorPos = 1.5, 1.5
    jugadorAngulo = 0
    jugadorVelocidad = 0.004
    jugadorRotacion = 0.005

    #Configuracion del RayCasting
    FOV = math.pi / 3
    HALF_FOV = FOV / 2
    NUM_RAYS = ancho // 2
    HALF_NUM_RAYS = NUM_RAYS // 2
    DELTA_ANGLE = FOV / NUM_RAYS
    MAX_DEPTH = 20

