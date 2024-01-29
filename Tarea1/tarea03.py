#Tarea 03: Crear lista 
#Luis Pablo López Iracheta 192301-9
def PreguntaLista(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    return lista


numeroEntero = int(input("Número entero: "))
resultado = PreguntaLista(numeroEntero)

print(resultado)