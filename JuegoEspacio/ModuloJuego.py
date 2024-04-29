import pygame
import configuracinJuego as CFG
import math as mt

class Juego():
    
    def __init__(self):
        self.EsteTablero = Tablero()
        self.Nave = Nave(50, 50, 10, 120, "C:\IBERO\Programacion-II\JuegoEspacio\Enterprise.png") #posicion x, posicion y, velocidad, angulo
        return
    
    def dibuja (self, screen):
        self.EsteTablero.dibuja(screen)
        self.Nave.dibuja(screen)  
        return
    
    def ActualizaVariables(self):
        self.Nave.avanza()
        return

class Tablero():
    def __init__(self):
        self.imgFondo = pygame.image.load("C:\IBERO\Programacion-II\JuegoEspacio\hubble2.bmp")
        return
    
    def dibuja(self, screen):
        rect = self.imgFondo.get_rect()
        screen.blit(self.imgFondo, rect)
        return

class Cuerpo():
    def __init__(self, pr_x, pr_y, pr_v, pr_alfa_deg):
        self.x = pr_x
        self.y = pr_y
        self.v = pr_v
        self.alfa_deg = pr_alfa_deg
        return

    def dibuja(self, screen):
        color = (255,0,0)
        pygame.draw.circle(screen, color, (self.x, self.y), 5)
        return
    
    def avanza(self):
        alfa_rad = mt.radians(self.alfa_deg)
        vx = self.v * mt.cos(alfa_rad)
        vy = self.v * mt.sin(alfa_rad)
        self.x = self.x + vx
        self.y = self.y + vy

        if self.x < 0:
            self.x = 800
        
        if self.x > 800:
            self.x = 0

        if self.y < 0:
            self.y = 600
        
        if self.y > 600:  
            self.y = 0



        return
    
class Nave(Cuerpo):
    def __init__(self, pr_x, pr_y, pr_v, pr_alfa_deg, pr_img):
        super().__init__(pr_x, pr_y, pr_v, pr_alfa_deg)
        self.imagen = pygame.image.load(pr_img)

    def dibuja(self, screen):
        rect = self.imagen.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        screen.blit(self.imagen, rect)
        super().dibuja(screen)