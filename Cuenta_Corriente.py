# La clase CuentaCorriente tendra una funcion para heredar datos de la clase CuentaBancaria(init).
# Y tres funciones: Depositar en la cuenta, Girar un monto de dinero de la cuenta y Obtener el saldo de la cuenta.
# Al crear una cuenta debe tener saldo cero, y al girar se debe validar que tenga saldo.
# En caso contrario, le debe indicar que tiene saldo insuficiente para realizar la operacion.

from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_Corriente(Cuenta_Bancaria):
    def __init__(self, titular: str, fecha: str, monto: float):
        super().__init__(titular, fecha, monto)
    
    def deposito(self, saldo):
        d = self.get_monto + saldo
        return d
    
    def giro(self, saldo):
        if self.get_monto >= saldo:
            self.get_monto -= saldo
        else:
            print('El es insuficioente en este momento')
            
    def obtener_saldo(self):
        return self.get_monto
    
    def imprimir(self):
        return super().imprimir()
    
    def __str__(self):
        imp = super().__str__()
        imp += f'\nDeposito: {self.deposito()}'
        imp += f'\nGiro: {self.giro()}'
        imp += f'\nObtener Saldo: {self.obtener_saldo()}'
        return imp