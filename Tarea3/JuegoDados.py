#Tarea 3: Juego de los dados
#Autor: Luis Pablo López Iracheta 192301-9
'''
░░▄███▄███▄
░░█████████
░░▒▀█████▀░
░░▒░░▀█▀
░░▒░░█░
░░▒░█
░░░█
░░█░░░░███████
░██░░░██▓▓███▓██▒
██░░░█▓▓▓▓▓▓▓█▓████
██░░██▓▓▓(◐)▓█▓█▓█
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█
░▒░░▒░░██▓██░░░██▓▓██
████████████████████████
█▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█
██─██▀█─██─██─█─███─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

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
total = 0

for j in range(11): #Imprime la frecuencia de cada combinación
    porcentaje = (frecuencias[j] / intentos) * 100
    print("Combinación %2.1f salió %2.2f porciento."%((j+2), porcentaje))
    total += porcentaje

ganancias = {
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