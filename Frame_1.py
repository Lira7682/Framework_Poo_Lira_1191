print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio

class Persona:   #se crea clase
#utiliza la __init__()función para asignar valores para el nombre y la edad
    def __init__(self, nombre='', edad=0, dni=''): #contruye la clase
        self.nombre = nombre  
        self.edad = edad
        self.dni = dni

    def mostrar(self): #muestra los detalles de la persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):#muestra si es mayor de edad
        return self.edad >= 18  
#self instancia actual de la clase
persona = Persona("Devora", 30, "12345678A") #datos a agregar a los detalles
persona.mostrar() #muestra los datos anteriores
print("Es mayor de edad:", persona.esMayorDeEdad()) #imprime q es mayor de edad

print(" ")#espacio