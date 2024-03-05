#Ejemplo de varibles estaticas 
#Como variables de configuración

class Camaras():
    def __init__(self, pr_ID):
        self.ID = pr_ID
        return
    
    def __str__(self):
        texto = "Camara ID: " + self.ID
        return texto

class Maquina():
    def __init__(self):
        self.camaras = []
        self.camaras.append( Camaras(Config.IDcam1))
        self.camaras.append( Camaras(Config.IDcam2))
        return

class Config():
    IDcam1 = "Faser2342"
    IDcam2 = "Faser2354"

#Programa principal:
EstaMaquina = Maquina()
print(EstaMaquina.camaras[0])
print(EstaMaquina.camaras[1])