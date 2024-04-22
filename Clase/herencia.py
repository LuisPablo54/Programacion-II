#duplicando clases
#Mala idea
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def NombreCompleto(self):
        return self.apellido + ", " + self.nombres
    
class Estudiante():
    def __init__(self, nombre, apellido, matricula):
        print("Creando un estudiante")
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula

    def NombreCompleto(self):
        return self.apellido + ", " + self.nombre
    
#Programa principal

Juan = Persona("Juan", "Perez")
Arturo = Estudiante("Arturo", "Gomez", 12345)