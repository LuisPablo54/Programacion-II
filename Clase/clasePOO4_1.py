#Ejemplo de varibles estaticas 
#Como variables de configuración

class Camaras(): #Class for cameras
    def __init__(self, pr_ID):
        self.ID = pr_ID
        return
    
    def __str__(self):
        texto = "Camara ID: " + self.ID
        return texto

class Maquina(): #Class for machines to control the cameras
    def __init__(self):
        self.camaras = [] #List of cameras
        self.camaras.append( Camaras(Config.IDcam1))
        self.camaras.append( Camaras(Config.IDcam2))
        return

class Config(): #Class for configuration
    IDcam1 = "Faser2342" #ID of the first camera
    IDcam2 = "Faser2354"

#Programa principal:
EstaMaquina = Maquina()#Create a machine
print(EstaMaquina.camaras[0])#Print the first camera
print(EstaMaquina.camaras[1])#Print the second camera