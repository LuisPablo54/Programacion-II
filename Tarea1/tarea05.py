#Tarea 05: Encontrar el minimo de una lista 
#Luis Pablo López Iracheta 192301-9

def Minimo (lista):
    mi_lista = lista[0]
    for i in lista:
        if i < mi_lista:
            mi_lista = i
    return mi_lista

valores = [5, 3, 8, 9, 7]
resultado = Minimo(valores)
print(f"El valor minimo de la lista es: {resultado}")