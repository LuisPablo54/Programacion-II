import random

class Circulo:
    def __init__(self, pr_xc, pr_yc, pr_radio):
        self.xc = pr_xc 
        self.yc = pr_yc
        self.radio = pr_radio
        return
    
    def Dentro(self, x, y):
        d = (x - self.xc)**2 + (y - self.yc)**2  # Corrige el cálculo de la distancia
        if d <= self.radio**2:  # Compara con el cuadrado del radio
            return True
        else:
            return False
    
  
class Cuadrado:
    def __init__(self, pr_xc, pr_yc, pr_lado):
            self.x1 = pr_xc - pr_lado/2
            self.x2 = pr_xc + pr_lado/2
            self.y1 = pr_yc - pr_lado/2
            self.y2 = pr_yc + pr_lado/2

    def Dentro(self, x, y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return True
        else:
            return False
        
# Programa principal
# Programa principal
EsteCirculo = Circulo(50, 50, 20)  # Cambia el centro del círculo a (50, 50)
EsteCuadrado = Cuadrado(50, 50, 20)  # Cambia el centro del cuadrado a (50, 50)

#Simula gotas de lluvia
cntCuadrado = 0 #Gotas dentro del cuadrado
cntCirculo = 0 #Gotas dentro del círculo

for i in range(1, 500000): #Simula 100 gotas de lluvia
    xGota = random.uniform(0, 100.0)
    yGota = random.uniform(0, 100.0)
    if EsteCuadrado.Dentro(xGota, yGota) == True: #Si la gota está dentro del cuadrado
        cntCuadrado += 1
    if EsteCirculo.Dentro(xGota, yGota)== True: #Si la gota está dentro del círculo
        cntCirculo += 1
print("Gotas dentro del cuadrado:", cntCuadrado)
print("Gotas dentro del círculo:", cntCirculo)

PI = cntCirculo / cntCuadrado

print("PI:", PI)

    