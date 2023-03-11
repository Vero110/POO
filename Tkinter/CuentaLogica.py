
class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= cantidad

    def depositar_otra_cuenta(self, cuenta_destino, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= cantidad
            cuenta_destino.ingresar_efectivo(cantidad)

