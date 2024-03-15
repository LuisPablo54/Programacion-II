# Generador de números distribución normal
import random
import matplotlib.pyplot as plt


# Genera una lista de 100 números distribuidos normalmente con media 100 y desviación estándar 15
resultado = []
for i in range(1, 100):
    valor = random.gauss(100, 15)  # Cambia la desviación estándar a 15
    resultado.append(valor)
    

# Calcula el promedio de los números generados
promedio = sum(resultado) / len(resultado)
print("Promedio: %3.3f" % (promedio))


#Graficar en un solo paso
cuenta, clases,_ = plt.hist(resultado, 20, density=False, color='blue')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores')
plt.show()


# Muestra los resultados
for i in range(0, len(clases) - 1):
    print("Clases", round(clases[i]), "Piezas:", cuenta[i])

#Tarea
