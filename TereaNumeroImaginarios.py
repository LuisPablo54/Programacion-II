#Tara 03 Numeros Imaginarios

class Complejos():
    def __init__(self, prReal, prImaginario):
        self.real = float(prReal)
        self.imaginario = float(prImaginario)

    def __str__(self):
        texto ="("+  str(int((self.real))) + ")+(" + str(int(self.imaginario))+"i)"
        return texto

    def __lt__(self, other):
        return self.magnitud() < other.magnitud()

    def __gt__(self, other):
        return self.magnitud() > other.magnitud()

    def __add__(self, other):
        numReales = self.real + other.real
        numImag = self.imaginario + other.imaginario
        return Complejos(numReales, numImag)

    def __sub__(self, other):
        numReales = self.real - other.real
        numImag = self.imaginario - other.imaginario
        return Complejos(numReales, numImag)
    
    def __mul__(self, other):
        numReales = self.real * other.real
        numImag = self.imaginario * other.imaginario
        return Complejos(numReales, numImag)

    def magnitud(self):
        magnitud = ((self.real ** 2)+(self.imaginario ** 2)) * 0.5
        return magnitud

a = Complejos(10,3)
b = Complejos(5,20)

#Alias
y = a





