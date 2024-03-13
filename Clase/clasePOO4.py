#Variables estaticas: son de la Clase, no del objeto
#                     son compartidas por todos lo objetos
#Clase:
class Circulo(): #Class for circles

    variableEstatica = 20 #La variable estatica se queda dentro de la clase
    nuevaSerie = 0

    def __init__(self, prRadio): #Constructor
        self.radio = prRadio
        Circulo.nuevaSerie += 1
        self.numeroSerie = Circulo.nuevaSerie
        return
    def __str__(self):
        texto = "Circulo de readio: " + str(self.radio)
        return texto

#Inicio del programa principal
a = Circulo(5)
print(a)
print(Circulo.nuevaSerie) 
b = Circulo(3)
print(b)
print(Circulo.nuevaSerie) 


print(Circulo.variableEstatica) #Se muestra la varible estatica
#No usar el nombre objeto para llamar una varible estatica
