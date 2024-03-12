#Metodo montecarlo: Generador de numeros aleatorios para resolver un problema
import random 

listaResutados = []

lista = []
for i in range(0,18):
    lista.append(0)

for i in range(1,1700):
    suerte = random.randint(1,17)
    listaResutados.append(suerte)
    lista[suerte] += 1

print("Resultados: ")
for i in range(1,18):
    print(i, ":", lista[i])
print("Lista: ", lista)
