# #Propiedades Privadas
# #Metodos Privados vs Publicos
class EstadoCuenta():
    def __init__(self, prNombre, prSaldoInicial):
        self.__nombre = prNombre
        self.__saldo = 0
        self.__movimientos = []
        self.movimiento("Deposito inicial", prSaldoInicial)

    def movimiento(self, prDescripcion, prMonto):
        movimiento = (prDescripcion, prMonto)
        self.__movimientos.append(movimiento)
        self.__saldo += prMonto

    def imprime(self):
        print(self.__nombre, " Saldo: $", self.__saldo)
        for mov in self.__movimientos:
            print(mov)
        print()
        print("Fin de estado de cuenta")

    def getSaldo(self):
        return self.__saldo

# Programa inicial
CuentaLuis = EstadoCuenta("Luis", 1000)
CuentaLuis.movimiento("Deposito", 500)
CuentaLuis.movimiento("Retiro", -300)

print(CuentaLuis.getSaldo())
CuentaLuis.imprime()
