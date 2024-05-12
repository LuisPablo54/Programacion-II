import math
import random


def PesoHuevos():
    cantidadHuevos = 0
    MenorPeso = 55
    MayorPeso = 65
    PesoTotal = 0

    for i in range(1, 36):
        peso = random.gauss(60, 4) #Promedio de 60 gramos y desviación estándar de 4 gramos
        if peso < MenorPeso:
            MenorPeso = peso
        if peso > MayorPeso:
            MayorPeso = peso
        PesoTotal += peso #Suma el peso del huevo
    
    return cantidadHuevos, MenorPeso, MayorPeso, PesoTotal
        



operacion, MinP, MaxP, Peso = PesoHuevos()    
print("Cantidad de huevos con peso entre 55 y 65 gramos:", operacion)
print("Peso del huevo más ligero:", MinP)
print("Peso del huevo más pesado:", MaxP)
print("Peso total de los huevos:", Peso)
if Peso < 2100:
    print("Faltan huevos")

        
