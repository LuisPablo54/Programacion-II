#Luis Pablo López Iracheta 192301-9
#Operaciones de fracciones
#Funciones para realizar operación
def SumaFracciones(a, b, c, d):
    numerador = (a * d) + (b * c)
    denominador = b * d
    return (numerador, denominador)

def Simplifacion(num1, num2): 
    if num2 == 0:
        return num1
    return Simplifacion(num2, num1 % num2)

def Producto(num1, den1, num2, den2):
    # Multiplica los numeradores y denominadores para obtener el producto de las fracciones
    nuevoNumerador = num1 * num2
    nuevoDenominador =  den1 * den2

    operacionSimplicado = Simplifacion(nuevoNumerador, nuevoDenominador)

    numeradorSimplificado = nuevoNumerador // operacionSimplicado
    denominadorSimplificado = nuevoDenominador // operacionSimplicado
    return numeradorSimplificado, denominadorSimplificado

def Divicion(num1, den1, num2, den2):
    # Multiplica los numeradores y denominadores para obtener el producto de las fracciones
    nuevoNumerador = num1 * den2
    nuevoDenominador =  den1 * num2

    operacionSimplicado = Simplifacion(nuevoNumerador, nuevoDenominador)

    numeradorSimplificado = nuevoNumerador // operacionSimplicado
    denominadorSimplificado = nuevoDenominador // operacionSimplicado
    return numeradorSimplificado, denominadorSimplificado

#Menu interactivo
print("""
_________Menú_________
1)Suma 2 Fraccionnes  | 
2)Suma 3 Fraccionnes  | 
3)Simplifica          | 
4)Producto            |
5)Divición            |
6)SALIR               |
______________________|
""")
#Menu de opciones a realizar: 
while True:
    usuario = int(input("Ingrese un valor: "))
    if usuario == 1: #Suma de dos fracciones
        a = 1
        b = 5
        c = 1
        d = 3
        numerador, denominador = SumaFracciones(a, b, c, d)
        print(f"\nLa suma de {a}/{b} + {c}/{d} es {numerador}/{denominador}\n")
    elif usuario == 2:#Suma de tres fracciones
        a = 1
        b = 2
        c = 1
        d = 2
        e = 6
        f = 3
        numerador, denominador = SumaFracciones(a, b, c, d) #Primera suma fracción
        numerador, denominador = SumaFracciones(numerador, denominador, e, f) #Segunda suma fracción
        print(f"\nLa suma de {a}/{b} + {c}/{d} + {e}/{f} es {numerador}/{denominador}\n")
    #TAREA
    elif usuario == 3: #Simplificar fracción
        num1 = 105
        num2 = 140
        operacion = Simplifacion(num1, num2)
        nuevoNumero1 = int(num1 / operacion)
        nuevoNumero2 = int(num2 / operacion)
        print(f"El valor de {num1} / {num2} simplificado = {nuevoNumero1} / {nuevoNumero2}\n")
    elif usuario == 4: #Produto de fracción
        num1 = 16
        num2 = 32
        num3 = 4
        num4 = 16
        numerador, denominador = Producto(num1, num2, num3, num4)
        print(f"El valor de {num1} / {num2}  * {num3} / {num4} simplificado = {numerador} / {denominador}\n")
    
    elif usuario == 5: #Divición de fracciones
        num1 = 16
        num2 = 32
        num3 = 4
        num4 = 16
        numerador, denominador = Divicion(num1, num2, num3, num4)
        print(f"El valor de {num1} / {num2}   entre  {num3} / {num4} simplificado = {numerador} / {denominador}\n")
    else:
        break
    pass

