#Calificaciones
def Promedio(parcial1, parcial2, parcial3):
    suma = parcial1 + parcial2 + parcial3
    return suma/3
#Progrma Principal
Nombre = ["Juan", "pedro", "Luis", "Paco", "Eduardo"]

Parcial1 = [7, 6, 8, 0, 9]
Parcial2 = [8, 7, 7, 8, 9]
Parcial3 = [3, 8, 8, 7, 9]
print("  Nombre  | Parcial 1  |  Parcial 2 |  Parcial 1 |  Promedio  |")
print("__________|____________|____________|____________|____________|")
for index in range(0, len(Nombre)):
   promedio = Promedio(Parcial1[index], Parcial2[index], Parcial3[index])
   print(f"{Nombre[index]:^9} |  {Parcial1[index]:^9.2f} |  {Parcial2[index]:^9.2f} |  {Parcial3[index]:^9.2f} |  {promedio:^9.2f} |")
print("Fin del programa")