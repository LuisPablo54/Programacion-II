#Metodo montecarlo: Generador de numeros aleatorios para resolver un problema
import random 

listaResutados = [] #List of results

lista = [] #List of numbers
for i in range(0,18): #Fill the list with zeros
    lista.append(0)

for i in range(1,1700): #Generate 1700 random numbers
    suerte = random.randint(1,17) #Random number between 1 and 17
    listaResutados.append(suerte) #Add the number to the list of results
    lista[suerte] += 1

print("Resultados: ")
for i in range(1,18):
    print(i, ":", lista[i]) #Print the results
    
print("Lista: ", lista)
