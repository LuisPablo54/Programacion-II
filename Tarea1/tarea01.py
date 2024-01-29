#Tarea 01: Numero mayor 
#Luis Pablo López Iracheta 192301-9
def numeromayor(num1, num2, num3):#Funcion para encontrar al mayor de 3 numeros
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print("Calculadora de numero mayor")
#Ingresa los numero 
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

resultado = numeromayor(numero1, numero2, numero3) #Manda a llamar a la función

print(f"El numero mayor de los que se ingresaron, es: {resultado}")