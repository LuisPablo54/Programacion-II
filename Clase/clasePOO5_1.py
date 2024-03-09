#Publico y privado

class MiClase():
    def __init__(self):
        self.__propiedadPrivda = 50 #Dos __ al inicio significa privada
        self.propiedadPublica = 30
        return
    def imprime(self):
        print("publica: ", self.propiedadPublica)
        print("publica: ", self.__propiedadPrivda)
    
    def __privado(self):
        print("Este es un metodo privado: ", self.__propiedadPrivda)
        return
    
    def publico(self):
        print("Este es un metodo publico: ", self.propiedadPublica)
        self.__privado()
        return
    
#Incio del programa:

A = MiClase()

print(A.propiedadPublica)
#print(A.__propiedadPrivda) Marca error al ser privado la variable 

A.imprime()
A.publico()