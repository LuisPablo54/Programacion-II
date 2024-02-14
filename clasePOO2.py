#Clase 5
#Primer ejemplo POO
#Clase vs objeto
#Contrucctor __init__
#Contrucctor del objeto
#Propiedades -> Variables
#Metodos -> Funciones (No contamos al __init__)

#____REGLAS___
#Asigna todas las propiedades en init
#No crear propiedades fuera del init
class Kardex:
    def __init__(self,prNombre,prApellido): #Metodo iniciador
        print("Esto es clase")
        self.nombre = prNombre
        self.apellido = prApellido
        self.parcial1 = 0
        self.parcial2 = 0
        self.parcial3 = 0
        return
    
    def __str__(self): 
        texto = "Kardex: "+ self.nombre + " " + self.apellido
        return texto #Obligatorio que sea texto

    def imprimir(self): #Funciona pero no es lo ideal para ver las propiedades
        texto = "Kardex: "+ self.nombre + " " + self.apellido
        print(texto)
        return 

    def NombreCompleto(self):
        return self.nombre + " " + self.apellido
    
    def Promedio(self):
        resultado = (self.parcial1 + self.parcial2 + self.parcial3)
        return resultado


#Programa principal
print("\nInicio de clase\n")

#Este es un objeto kardex
nombre = input("Ingresa nombre: ")
apellido = input("Ingresa apellido: ")
miKardex = Kardex(nombre, apellido) #Esto es para contruir el objeto, el objeto es "miKardex"

alias = miKardex #Crea un alias para evaluar

#print(miKardex) #Evaluo su dirección de momoria para ver si es un alias o clon
#print(alias) #Evaluo su dirección de momoria para ver si es un alias o clon


#print(miKardex.NombreCompleto()) #Ejecuto la función dentro de la clase
#print(alias.NombreCompleto()) #Ejecuto la función dentro de la clase

#Para mostrar los metodos de la clase
print(miKardex)

print("\nFin del programa")