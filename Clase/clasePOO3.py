class Fracciones():
    def __init__(self, prNum, prDen): 
        self.num = int(prNum)
        self.den = int(prDen)
        #self.Simplifacion() #Al ingresar Simplifica, C/u de los valores ingresados se simplifican
        return

    def __str__(self):
        texto = str(self.num) + "/" + str(self.den)
        return texto

    def __add__(self, other):
        print("Type self", type(self))
        print("Type other", type(other))
        #rDen = self.den * other.den
        #rNum = other.den * self.num + self.den * other.num
        #resultado = Fracciones(rNum, rDen)
        #resultado.Simplifacion()
        #return resultado
        if (isinstance(other,Fracciones)):
            den = self.den * other.den
            num = self.num * other.num + self.num * other.den
            return Fracciones (num,den)

        if (isinstance(other,init)):
            den = self.den
            num = self.num + other*self.den
            return Fracciones (num,den)
            
        if (isinstance(other,float)):
            return self.num / self.den * other

            #Si llegue aqui esta mal
        raise NameErro("Esto no se puede resolver asi")
            
               



# Programa inicial
a = Fracciones(3, 9)
b = Fracciones(6, 9)
c = a + b

print(type(a))
print("b: ", b)
print("a: ", a)
print("c: ", c)


