#Tarea 3: Juego de los dados Casino
#Autor: Luis Pablo López Iracheta 192301-9
'''
________00000000000___________000000000000_________
______00000000_____00000___000000_____0000000______
____0000000_____________000______________00000_____
___0000000_______________0_________________0000____
__000000____________________________________0000___
__00000_____________________________________ 0000__
_00000______________________________________00000__
_00000_____________________________________000000__
__000000_________________________________0000000___
___0000000______________________________0000000____
_____000000____________________________000000______
_______000000________________________000000________
__________00000_____________________0000___________
_____________0000_________________0000_____________
_______________0000_____________000________________
_________________000_________000___________________
_________________ __000_____00_____________________
______________________00__00_______________________
________________________00_________________________

'''

import random
intentos = 1000
def tirarDados(): #Función que simula el lanzamiento de dos dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def calcularFrecuencia(): #Calcula la frecuencia de cada combinación de los dados
    frecuencias = [0] * 11 
    
    for i in range(intentos): #Simula el lanzamiento de los dados
        suma = tirarDados()
        frecuencias[suma - 2] += 1  

    return frecuencias

frecuencias = calcularFrecuencia()


MontoIncial = float(input("\nIngrese el monto inicial: "))

while MontoIncial > 0:


    monto_apostar = float(input("Ingrese el monto a apostar: "))
    while monto_apostar > MontoIncial:
        print("No tienes suficiente dinero")
        monto_apostar = float(input("Ingrese el monto a apostar: "))

    sumaDados = int(input("Ingrese la suma de los dados a apostar: "))
    while sumaDados < 2 or sumaDados > 12:
        print("Número inválido")
        sumaDados = int(input("Ingrese la suma de los dados a apostar: "))

    ganancias = 0
    MontoAMultiplicar = {
        2: 10,
        3: 9,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 3,
        9: 4,
        10: 5,
        11: 9,
        12: 10
        }

    suma = tirarDados()
    if suma == sumaDados:
        ganancias += monto_apostar * MontoAMultiplicar[sumaDados]
        print("Ganaste")
    else:
        ganancias -= monto_apostar
        print("Perdiste")

    print("Ganancias totales:", ganancias)
    
    MontoIncial += ganancias 
    print(f"Monto actual: {MontoIncial} \n")

    if MontoIncial <= 0:
        print("Te quedaste sin dinero")
        break

    seguir = input("¿Desea seguir jugando? (s/n): ")
    if seguir == "n":
        print("\nGracias por jugar \n")
        break


    

