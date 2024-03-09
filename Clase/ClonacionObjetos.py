class MiClase():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = [1, 2, 3, 4]
        return

    def imprime(self):
        print(self.a, ",", self.b)
        return

    def clon(self):
        nuevo = MiClase(0,0)
        nuevo.a = self.a
        nuevo.b = self.b
        nuevo.c = self.c[:]
        return nuevo

objetoA = MiClase(10, 20)
objetoA.imprime()
print(objetoA)
alias = objetoA
print("Alias: ", alias)
alias.a = 1000
objetoA.imprime()

#Clon
clon = objetoA.clon()
print("Clon: ", clon)
clon.imprime()

#instance(a,MiClase) Par ver si la variable es de esa clase

