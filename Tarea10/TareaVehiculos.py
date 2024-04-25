#Tarea 10
# Autor: Luis Pablo López Iracheta

class Vehiculo:
    siguienteNumeroSerie = 20210000

    def __init__(self, prRueda, prPrecio, prModelo, prColor):
        self.__ruedas = prRueda
        self.__precio = prPrecio
        self.__modelo = prModelo
        self.__color = prColor
        self.__numeroSerie = Vehiculo.siguienteNumeroSerie 
        Vehiculo.siguienteNumeroSerie += 1

    def __str__(self):
        return f"Ruedas: {self.__ruedas}, Precio: {self.__precio}, Modelo: {self.__modelo}, Color: {self.__color}, Numero de Serie: {self.__numeroSerie}"
        

class Hibrido(Vehiculo):
    def __init__(self, prRueda, prPrecio, prModelo, prColor, prPotenciaMotorCombustion_hp, prPotenciaMotorElectrico_hp, prCapacidadBateria_AmpHr):
        Vehiculo.__init__(self, prRueda, prPrecio, prModelo, prColor)
        self.__potenciaMotorCombustion_hp = prPotenciaMotorCombustion_hp
        self.__potenciaMotorElectrico_hp = prPotenciaMotorElectrico_hp
        self.__capacidadBateria_AmpHr = prCapacidadBateria_AmpHr

    def __str__(self):
        return f"{Vehiculo.__str__(self)}, Potencia Motor Combustion: {self.__potenciaMotorCombustion_hp}, Potencia Motor Electrico: {self.__potenciaMotorElectrico_hp}, Capacidad Bateria: {self.__capacidadBateria_AmpHr}"

class Combustion(Vehiculo):
    def __init__(self, prRueda, prPrecio, prModelo, prColor, prPotenciaMotorCombustion_hp):
        Vehiculo.__init__(self, prRueda, prPrecio, prModelo, prColor)
        self.__potenciaMotorCombustion_hp = prPotenciaMotorCombustion_hp
    
    def __str__(self):
        return f"{Vehiculo.__str__(self)}, Potencia Motor Combustion: {self.__potenciaMotorCombustion_hp}"

class Electico(Vehiculo):
    def __init__(self, prRueda, prPrecio, prModelo, prColor, prPotenciaMotorElectrico_hp, prCapacidadBateria_AmpHr):
        Vehiculo.__init__(self, prRueda, prPrecio, prModelo, prColor)
        self.__potenciaMotorElectrico_hp = prPotenciaMotorElectrico_hp
        self.__capacidadBateria_AmpHr = prCapacidadBateria_AmpHr

    def __str__(self):
        return f"{Vehiculo.__str__(self)}, Potencia Motor Electrico: {self.__potenciaMotorElectrico_hp}, Capacidad Bateria: {self.__capacidadBateria_AmpHr}"


#Programa principal
auto = Vehiculo(4, 100000, "Chevy", "Rojo")
print(auto)

auto2 = Hibrido(4, 125000, "Versa", "Plata", 100, 50, 200)
print(auto2)

auto3 = Combustion(4, 300000, "Sentra", "Azul", 100)
print(auto3)

auto4 = Electico(4, 150000, "Civic", "Plata", 50, 200)
print(auto4)