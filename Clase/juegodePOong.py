#simulador del juego de pong
import  sys,pygame
import ConfiPOONG as CP
verde = (0,255,0)


class Cancha:
    def __init__(self, pr_x1, pr_y1, pr_x2, pr_y2):
        self.pr_x1 = pr_x1
        self.pr_y1 = pr_y1
        self.pr_x2 = pr_x2
        self.pr_y2 = pr_y2
        return
    
    def Dibujar(self, pr_screen):
        ancho = self.pr_x2 - self.pr_x1
        alto = self.pr_y2 - self.pr_y1
        rect = ((self.pr_x1, self.pr_y1), (ancho, alto))
        pygame.draw.rect(pr_screen, verde, rect)
        return  
    
class Juego():
    def __init__(self):
        print("Inicializando juego")
        x1 = 20
        y1 = 20
        x2 = CP.Confi.CanchaAncho - 20
        y2 = CP.Confi.CanchaAlto - 20
        self.EstaCancha = Cancha(x1, y1, x2, y2)
        self.EstaPelota = Pelota(CP.Confi.CanchaAncho / 2, CP.Confi.CanchaAlto // 2)
        self.Raqueta1 = Raqueta(50, CP.Confi.CanchaAlto // 2, 10, 60, (255, 255, 255))
        return
    
    def Dibujar(self, pr_screen):
        self.EstaCancha.Dibujar(pr_screen)
        self.EstaPelota.Dibujar(pr_screen)
        self.Raqueta1.Dibujar(pr_screen)
        return
    
    def Recalcular(self):
        self.EstaPelota.ActualizaPosiccion(CP.Confi.deltaTiempo_s)
        return
class Raqueta():
    def __init__(self, pr_x, pr_y, pr_ancho, pr_alto, pr_color):
        self.x = pr_x
        self.y = pr_y
        self.ancho = pr_ancho
        self.alto = pr_alto
        self.color = pr_color
        return
    
    def Dibujar(self, pr_screen):
        x1 = self.x - self.ancho // 2
        x2 = self.x + self.ancho // 2
        rect = ((x1, self.y), (self.ancho, self.alto))
        pygame.draw.rect(pr_screen, self.color, rect)
        return
    
    def Mover(self, pr_dy):
        if key[pygame.K_UP]:
            self.y += 20
        if key[pygame.K_DOWN]:
            self.y -= 20
    
  
    
class Pelota():
    def __init__(self, pr_x, pr_y):
        self.x = pr_x
        self.y = pr_y
        self.vx = CP.Confi.pelotaPXx_s
        self.vy = CP.Confi.PelotaPXy_s
        self.radio = CP.Confi.pelotaRadio
        self.color = CP.Confi.pelotaColor
        return
    
    def ActualizaPosiccion(self, pr_deltaTiempo_s):
        self.x = self.x + self.vx * pr_deltaTiempo_s
        self.y = self.y + self.vy * pr_deltaTiempo_s
        
        # Rebotar al tocar la pared
        if self.x - self.radio <= 23 or self.x + self.radio >= CP.Confi.CanchaAncho - 23:
            self.vx = -self.vx
        if self.y - self.radio <= 23 or self.y + self.radio >= CP.Confi.CanchaAlto - 23:
            self.vy = -self.vy
        
        return
    
    def Dibujar(self, pr_screen):
        pygame.draw.circle(pr_screen, self.color, (self.x, self.y), self.radio)
        return