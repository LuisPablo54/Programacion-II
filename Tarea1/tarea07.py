#Tarea 07: 
#Luis Pablo López Iracheta 192301-9

def Mediana(lista):
    if not lista:
        return None  # Retorna None si la lista está vacía
    
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    if n % 2 == 1:
        # Si la lista tiene un número impar de elementos
        return lista_ordenada[n // 2]
    else:
        # Si la lista tiene un número par de elementos
        mitad_superior = n // 2
        mitad_inferior = mitad_superior - 1
        return (lista_ordenada[mitad_inferior] + lista_ordenada[mitad_superior]) / 2

# Ejemplo de uso:
valores = [5.5, 3.2, 8.7, 1.1, 7.3, 2.8]
resultado = Mediana(valores)
print(resultado)
