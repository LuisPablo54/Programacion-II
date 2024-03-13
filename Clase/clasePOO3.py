class Fracciones(): #Class Fraction
    def __init__(self, prNum, prDen): 
        self.num = int(prNum)
        self.den = int(prDen)
        #self.Simplifacion() #Al ingresar Simplifica, C/u de los valores ingresados se simplifican
        return

    def __str__(self):#Return the fraction
        texto = str(self.num) + "/" + str(self.den)
        return texto

    def __add__(self, other): #Sum of the fractions
        print("Type self", type(self))
        print("Type other", type(other))
        #rDen = self.den * other.den
        #rNum = other.den * self.num + self.den * other.num
        #resultado = Fracciones(rNum, rDen)
        #resultado.Simplifacion()
        #return resultado
        if (isinstance(other,Fracciones)): #If the other is a fraction
            den = self.den * other.den
            num = self.num * other.num + self.num * other.den
            return Fracciones (num,den)

        if (isinstance(other,other)):#If the other is a integer
            den = self.den
            num = self.num + other*self.den
            return Fracciones (num,den)
            
        if (isinstance(other,float)): #If the other is a float
            return self.num / self.den * other

            #Si llegue aqui esta mal
        raise NameError("Esto no se puede resolver así")
            
               



# Programa inicial
a = Fracciones(3, 9)
b = Fracciones(6, 9)
c = a + b

print(type(a))
print("b: ", b)
print("a: ", a)
print("c: ", c)


