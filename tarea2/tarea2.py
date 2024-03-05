#Tarea 2
class Tiempos():
    def __init__(self, prDia, prHora, prMin, prSeg):
        self.dia = prDia
        self.hora = prHora
        self.min = prMin
        self.Seg = prSeg
    
    def normalizar(self):
        pass 

#Tiempo Uno
print("\nTiempo uno: ")
diaI = int(input("Dia: "))
horaI = int(input("Hora: "))
minutoI = int(input("Minuto: "))
segundoI = int(input("Segundos: "))
#Tiempo dos
print("\nTiempo dos: ")
diaII = int(input("Dia: "))
horaII = int(input("Hora: "))
minutoII = int(input("Minuto: "))
segundoII = int(input("Segundos: "))


fechaI = (diaI, horaI, minutoI, segundoI)
fechaII = (diaII, horaII, minutoII, segundoII)

print(fechaI)
print(fechaII)