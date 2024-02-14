class Fracciones():
    def __init__(self, prNum, prDen): 
        self.num = int(prNum)
        self.den = int(prDen)
        self.Simplifacion() #Al ingresar Simplifica, C/u de los valores ingresados se simplifican
        return

    def __str__(self):
        texto = str(self.num) + "/" + str(self.den)
        return texto

    def __add__(self, other):
        rDen = self.den * other.den
        rNum = other.den * self.num + self.den * other.num
        #resultado = Fracciones(rNum, rDen)
        #resultado.Simplifacion()
        #return resultado
        return Fracciones(rNum, rDen)

    def __sub__(self, other):
        rDen = self.den * other.den
        rNum = other.den * self.num - self.den * other.num
        return Fracciones(rNum, rDen)
    
    def Simplifacion(self):
        num1 = self.num
        num2 = self.den 
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        mcd = num1
        self.num = self.num / mcd
        self.den = self.den / mcd
        return
    
    def __mul__(self, other):
        num1 = self.num * other.num
        num2 = self.den * other.den
        return Fracciones(num1, num2)
    
    def __truediv__(self, other):
        num2 = self.num * other.den
        num1 = self.den * other.num
        return Fracciones(num1, num2)

    def Decimal(self):
        return self.num / self.den
    
    def __gt__(self, other):
        if (self.Decimal() > other.Decimal()):
            return True
        else:
            return False



# Programa inicial
a = Fracciones(3, 9)
b = Fracciones(6, 9)
c = a + b

print(type(a))
print("b: ", b)
print("a: ", a)
print("c: ", c)


