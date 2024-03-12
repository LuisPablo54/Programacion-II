# Generador de números distribución normal
import random

# Genera una lista de 100 números distribuidos normalmente con media 100 y desviación estándar 15
resultado = []
for i in range(1, 100):
    valor = random.gauss(100, 15)
    resultado.append(valor)

# Calcula el promedio de los números generados
promedio = sum(resultado) / len(resultado)
print("Promedio: %3.3f" % (promedio))

# Define los límites de las clases y crea listas para almacenar las clases y las cuentas
LimiteInferior = 40
Ancho = 10
classses = []
cuenta = []

# Crea las clases y las inicializa con conteos de cero
while LimiteInferior <= 170:
    classses.append(LimiteInferior)
    cuenta.append(0)
    LimiteInferior += Ancho

# Muestra las clases y las cuentas iniciales
print("Clases:", classses)
print("Cuenta:", cuenta)

# Cuenta cuántos elementos caen en cada clase
for estaManzana in resultado:
    for i in range(0, len(classses) - 1):
        LimiteInferior = classses[i]
        LimiteSuperior = classses[i + 1]
        if LimiteInferior <= estaManzana < LimiteSuperior:
            cuenta[i] += 1

# Muestra los resultados
for i in range(0, len(classses) - 1):
    print("Clases", classses[i], "Piezas:", cuenta[i])

#Tarea
#Graficar con matplot