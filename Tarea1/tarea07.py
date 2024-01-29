#Tarea 07: 
#Luis Pablo López Iracheta 192301-9

def Mediana(lista):
    n = len(lista)

    # Ciclo burbuja para ordenar 
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    if n % 2 == 1:
        # Si la lista tiene un número impar
        return lista[n // 2]
    else:
        # Si la lista tiene un número par 
        mitad_superior = n // 2
        mitad_inferior = mitad_superior - 1
        return (lista[mitad_inferior] + lista[mitad_superior]) / 2


valores = [5.5, 3.2, 8.7, 1.1, 7.3, 2.8, 7.4]
resultado = Mediana(valores)
print(resultado)
