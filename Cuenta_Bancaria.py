# Definir los atributos titular, fecha y monto.
# Y una funcion para imprimir los datos en la clase CuentaBancaria.

class Cuenta_Bancaria:
    def __init__(self, titular: str, fecha: str, monto: float):
        self.__titular = titular
        self.__fecha = fecha
        self.__monto = monto
        
    def get_titular(self):
        return self.__titular
    
    def get_fecha(self):
        return self.__fecha
    
    def get_monto(self):
        return self.__monto
    
    def imprimir(self):
        print(f'Titular: {self.__titular}')
        print(f'\nFecha: {self.__fecha}')
        print(f'\nMonto: {self.__monto}')
        
    def __str__(self):
        imp = f'Titular:{self.__titular}'
        imp += f'\nFecha: {self.__fecha}'
        imp += f'\nMonto: {self.__monto}'
        imp += f'\nTitular: {self.get_titular()}'
        imp += f'\nFecha: {self.get_fecha()}'
        imp += f'\nMonto: {self.get_monto()}'
        return imp