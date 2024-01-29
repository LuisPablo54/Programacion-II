#Tarea 02: Pulgadas a centimetros 
#Luis Pablo López Iracheta 192301-9

def PulgadaCentimetros(pulgada_in):
    centimetro_cm = pulgada_in * 2.54 #Multiplicación para convertir a centimetros
    return centimetro_cm

medida_in = float(input("Ingrese la medida en pulgadas: ")) #Ingresar la medida a convertir
resultado_cm = PulgadaCentimetros(medida_in)
print(f"El resultado es: {resultado_cm} cm")

