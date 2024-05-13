import math
#Configuracion de la aplicacion

class Confi():
    #Configuracion de la ventana
    ancho = 800
    alto = 600
    HALF_WIDTH = ancho // 2
    HALF_HEIGHT = alto // 2    
    #Configuracion de la pantalla
    ress= ancho,alto
    deltaTiempo_s=0.01
    
    #Configuracion de la camara del jugador
    jugadorPos = 1.5, 1.5
    jugadorAngulo = 0
    jugadorVelocidad = 0.004
    jugadorRotacion = 0.002

    #Configuracion del RayCasting
    FOV = math.pi / 3
    HALF_FOV = FOV / 2
    NUM_RAYS = ancho // 2
    HALF_NUM_RAYS = NUM_RAYS // 2
    DELTA_ANGLE = FOV / NUM_RAYS
    MAX_DEPTH = 20

    #Configuracion de la distancia de la pantalla
    SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
    Escala = ancho // NUM_RAYS

    #Configuracion de texturas
    texturaEspacio = 256
    hal_texture = texturaEspacio // 2

