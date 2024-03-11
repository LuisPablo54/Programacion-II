#Publico y privado
#Estado de cuenta
class EstadoCuenta:
    def __init__(self, nombre, saldo_inicial):
        self.__saldo = saldo_inicial
        self.__nombre = nombre
        self.__movimientos = []
        self.__cntGetSaldo = 0

    def Movimiento(self, descripcion, monto):
        if monto < 0 and self.__saldo < abs(monto):
            print("No se puede retirar más dinero del que se tiene en la cuenta")
        else:
            movimiento = (descripcion, monto)
            self.__movimientos.append(movimiento)
            self.__saldo += monto

    def imprime(self):
        print(self.__nombre, "Saldo: $", self.__saldo)
        for mov in self.__movimientos:
            print(mov)
        print("El saldo se ha consultado", self.__cntGetSaldo)

    def getSaldo(self):
        self.__cntGetSaldo += 1
        return self.__saldo

class Banco:
    __Cuentas = []

    def __init__(self, *cuentas):
        for cuenta in cuentas:
            self.AgregaCuenta(cuenta)

    def AgregaCuenta(self, objEstadoDeCuentas):
        if isinstance(objEstadoDeCuentas, EstadoCuenta):
            self.__Cuentas.append(objEstadoDeCuentas)
            NumCuenta = self.__Cuentas.index(objEstadoDeCuentas)
            return NumCuenta
        else:
            print("El argumento no es de tipo EstadoCuenta.")

    def imprimeCuenta(self, NumCuenta):
        if 0 <= NumCuenta < len(self.__Cuentas):
            self.__Cuentas[NumCuenta].imprime()
        else:
            print("Número de cuenta fuera de rango.")
    
    def bancoMovimiento(self, NumCuenta, Descripcion, monto):
        self.__Cuentas[NumCuenta].Movimiento(Descripcion, monto)

    def getSaldo(self, NumCuenta):
        if 0 <= NumCuenta < len(self.__Cuentas):
            return self.__Cuentas[NumCuenta].getSaldo()
        else:
            print("Número de cuenta fuera de rango.")
            return None

# Programa principal
CuentaJuan = EstadoCuenta("Juan", 1000)
CuentaJuan.Movimiento("Depósito", 500)
CuentaJuan.Movimiento("Retiro", -300)

CuentaLuis = EstadoCuenta("Luis", 3424)
CuentaAndre = EstadoCuenta("Andre", 2000)
MiBanco = Banco(CuentaJuan, CuentaAndre, CuentaLuis)

MiBanco.imprimeCuenta(0)  # Imprime la cuenta


#print(CuentaJuan.__saldo)  #no funciona
#print(CuentaJuan.__movimientos) #no funciona
#print(CuentaJuan.__nombre) #no funciona
