print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
class Cuenta:
#utiliza la __init__()función para asignar valores para el titular y la cantidad
    def __init__(self, titular, cantidad=0.0):
        if not titular:  #muestra si no es titular
            raise ValueError("El titular es obligatorio.")#imprime mensaje
        self.titular = titular
        self.cantidad = cantidad
#Muestra lo detalles del titular
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")#imprime los detalles
#self se utiliza para acceder a las variables
    def ingresar(self, cantidad):
        if cantidad > 0: #verifica si la cantidad es mayor q cero
            self.cantidad += cantidad #mayor o igual a la cantidad

    def retirar(self, cantidad): #accede a variable cantidad
        self.cantidad -= cantidad

cuenta = Cuenta("Devora")#cuenta del titular 
cuenta.mostrar()#mostrar titular
cuenta.ingresar(300)#cantidad a ingresar a la cuenta
cuenta.mostrar()#mostrar cantidad
cuenta.retirar(100)#cantidad a retirar de la cuenta
cuenta.mostrar()#mostrar cantidad a retirar
cuenta.retirar(500)#cantidad a retirar
cuenta.mostrar()#muestra cantidad
print(" ")#espacio