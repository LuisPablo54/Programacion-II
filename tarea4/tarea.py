import random

def votar():
    votoRandom = random.randint(0, 100) # Se generan numeros entre 1 y 200 
    salida = 0
    if votoRandom < 10: 
        salida = 1
        return salida
    if votoRandom < 50:
        salida = 2
        return salida
    if votoRandom <=  100:
        salida = 3  
        return salida
   


#Simulacion de votos
def simunlacionVotos():
    contador1 = 0   
    contador2 = 0
    contador3 = 0
    
    for i in range(1, 2001):
        voto = votar()
        if voto == 1:
            contador1 += 1
        if voto == 2:
            contador2 += 1
        if voto == 3:
            contador3 += 1
      
    return contador1, contador2, contador3

#Primera simulacion
contador1, contador2, contador3 = simunlacionVotos()
print("Primera simulacion")

#Abstencion
contador1, contador2, contador3 = simunlacionVotos()
contador1 = (contador1 * 0.50) /10 # Tiene un 50% de abstinencia
contador2 = (contador2 * 0.53) /10 # Tiene un 47% de abstinencia
contador3 = (contador3 * 0.47) /10 # Tiene un 53% de abstinencia

print("Votos para el candidato A: ", contador1, "%")
print("Votos para el candidato B: ", contador2, "%")
print("Votos para el candidato C: ", contador3 , "%")


#Segunda simulacion
print("\nSegunda simulacion")
maximaDiferencia = 0
menorDiferencia = 100
caso1 = 0 # El candidato B gana
print("Simulacion de 2000 elecciones")

for i in range(1, 2001): #Ejercicio 8 serian 10,000 simulaciones
    contador1, contador2, contador3 = simunlacionVotos()
    contador1 = (contador1 * 0.50) # Tiene un 50% de abstinencia
    contador2 = (contador2 * 0.59) # Tiene un 45% de abstinencia
    contador3 = (contador3 * 0.47) # Tiene un 53% de abstinencia

    if contador2 > contador3:
        caso1 += 1
        #print("El candidato B gana", i, "simulado")
    
    if contador3 - contador2 > maximaDiferencia:
        maximaDiferencia = contador3 - contador2
    
    if contador3 - contador2 < menorDiferencia:
        menorDiferencia = contador3 - contador2


print("El candidato B gana: ", caso1, "veces")
porcentaje = (caso1 * 100) / 2000
print("El porcentaje de veces que gana el candidato B es: ", porcentaje , "%")
print("La maxima diferencia de votos es: ", maximaDiferencia / 10, "%")
print("La menor diferencia de votos es: ", menorDiferencia / 10, "%")