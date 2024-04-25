#duplicando clases
#Mala idea
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def NombreCompleto(self):
        return self.apellido + ", " + self.nombres
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, num_cuenta):
        self.num_cuenta = num_cuenta
        #Invocamos el constructor de la clase base
        Persona.__init__(self, nombre, apellido)
        return

    def cuenta(self, cuenta):
        self.cuenta = cuenta
        return
#Programa principal

Juan = Persona("Juan", "Perez")
Arturo = Estudiante("Arturo", "Gomez")