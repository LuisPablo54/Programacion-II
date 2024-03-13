#Publico y privado
#Estado de cuenta
class EstadoCuenta: #Class for bank account
    def __init__(self, nombre, saldo_inicial):
        self.__saldo = saldo_inicial
        self.__nombre = nombre
        self.__movimientos = []
        self.__cntGetSaldo = 0

    def Movimiento(self, descripcion, monto): #Function for the movements of the account
        if monto < 0 and self.__saldo < abs(monto): 
            print("No se puede retirar más dinero del que se tiene en la cuenta")
        else:
            movimiento = (descripcion, monto)
            self.__movimientos.append(movimiento)
            self.__saldo += monto

    def imprime(self): #Print the account
        print(self.__nombre, "Saldo: $", self.__saldo)
        for mov in self.__movimientos:
            print(mov) #Print the movements
        print("El saldo se ha consultado", self.__cntGetSaldo)

    def getSaldo(self): #Get the account
        self.__cntGetSaldo += 1
        return self.__saldo

class Banco: #Class for the bank
    __Cuentas = [] #List of accounts

    def __init__(self, *cuentas): 
        for cuenta in cuentas:
            self.AgregaCuenta(cuenta)

    def AgregaCuenta(self, objEstadoDeCuentas): #Add account
        if isinstance(objEstadoDeCuentas, EstadoCuenta):
            self.__Cuentas.append(objEstadoDeCuentas) #Add account to the list
            NumCuenta = self.__Cuentas.index(objEstadoDeCuentas) #Get the account number
            return NumCuenta
        else:
            print("El argumento no es de tipo EstadoCuenta.")

    def imprimeCuenta(self, NumCuenta): #Print the account
        if 0 <= NumCuenta < len(self.__Cuentas):
            self.__Cuentas[NumCuenta].imprime() #Print the account for the class EstadoCuenta
        else:
            print("Número de cuenta fuera de rango.")
    
    def bancoMovimiento(self, NumCuenta, Descripcion, monto): #Function for the movements of the bank
        self.__Cuentas[NumCuenta].Movimiento(Descripcion, monto)

    def getSaldo(self, NumCuenta): #Get the account
        if 0 <= NumCuenta < len(self.__Cuentas):
            return self.__Cuentas[NumCuenta].getSaldo()
        else:
            print("Número de cuenta fuera de rango.")
            return None

# Programa principal
CuentaJuan = EstadoCuenta("Juan", 1000) #first account
CuentaJuan.Movimiento("Depósito", 500)
CuentaJuan.Movimiento("Retiro", -300)

CuentaLuis = EstadoCuenta("Luis", 3424) #Second account
CuentaAndre = EstadoCuenta("Andre", 2000) #third account
MiBanco = Banco(CuentaJuan, CuentaAndre, CuentaLuis) #Create a bank

MiBanco.imprimeCuenta(0)  # Imprime la cuenta


#print(CuentaJuan.__saldo)  #no funciona
#print(CuentaJuan.__movimientos) #no funciona
#print(CuentaJuan.__nombre) #no funciona
