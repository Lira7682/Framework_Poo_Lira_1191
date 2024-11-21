print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
class Cuenta: #init para asignar valores a titular y a cantidad
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular   #valores 
        self.cantidad = cantidad #valores
#Self para ingresar a las variables
    def ingresar(self, cantidad):
        if cantidad > 0:  #si cantidad es mayor q 0
            self.cantidad += cantidad #mas o igual q 0
#Ingresa a variable de cantidad
    def retirar(self, cantidad):
        self.cantidad -= cantidad #cantidad menor o igual q cantidad

    def mostrar(self): #mostrar variable de self
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")#imprime detalles del titular

class CuentaJoven(Cuenta): #init asignar valores a titular, cantidad y bonificacion
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion #valores

    def esTitularValido(self): #verifica si el titular es valido
        return 18 <= self.cantidad < 25 #18 menor o igual q cantidad menor q 25

    def retirar(self, cantidad):#ingresa a variable de cantidad a retirar
        if self.esTitularValido():#si el titular es valido
            super().retirar(cantidad)
        else: #verifica si no es valido 
            print("No se puede retirar dinero: el titular no es válido.")#imprime mensaje

    def mostrar(self):#mostrar variable de self 
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")
#imprime detalles de la cuenta
cuenta_joven = CuentaJoven("Devora", cantidad=28, bonificacion=15)#detalles de cuenta_joven
cuenta_joven.mostrar()#mostrar detalles
cuenta_joven.ingresar(150)#ingresa 150
cuenta_joven.mostrar()#muestra cantidad
cuenta_joven.retirar(70)#retira 70
cuenta_joven.mostrar()#muestra cantidad
cuenta_joven.cantidad = 43  #cantidad de 43
cuenta_joven.retirar(50)#retira 50
print(" ")#espacio