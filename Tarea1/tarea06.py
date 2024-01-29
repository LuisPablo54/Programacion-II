#Tarea 06: Definir si el valor esta en orden decendente
#Luis Pablo López Iracheta 192301-9

def Decendente (lista):
    mi_lista = lista[0]
    for i in lista:
        if i > mi_lista:
            return False
    return True

valores = [10, 8, 5, 3, 2]
resultado = Decendente(valores)

if resultado == True:
    print("Los valores de la lista son en orden descendente")
else:
    print("Los valores de la lista NO estan en orden descendente")