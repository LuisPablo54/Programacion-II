#Tarea 2
class Tiempos():
    def __init__(self, prYear, prMes, prDia, prSeg):
        self.year = prYear
        self.Mes = prMes
        self.Dia = prDia
        self.Seg = prSeg


print("\nTiempo uno: ")
añoI = int(input("Año: "))
mesI = int(input("Mes: "))
diaI = int(input("Día: "))
segundoI = int(input("Segundos: "))

print("\nTiempo dos: ")
añoII = int(input("Año: "))
mesII = int(input("Mes: "))
diaII = int(input("Día: "))
segundoII = int(input("Segundos: "))

fechaI = (añoII, mesII, diaII, segundoII)
fechaII = (añoI, mesI, diaI, segundoI)

print(fechaI)
print(fechaII)