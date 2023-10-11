# La clase CuentaInversion tendra dos atributos propios: plazo e interes.
# Tendra una funcion para heredar datos de la clase CuentaBancaria(init).
# Una funcion para calcular el valor total del interes (monto * interes /100).
# Y otra funcion para mostrar la informacion, datos del titular, monto inicial, plazo, interes, 
# total de interes y monto final.

from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_Inversion(Cuenta_Bancaria):
    def __init__(self, titular: str, fecha: str, monto: float, plazo: int, interes: float):
        super().__init__(titular, fecha, monto)
        self.__plazo = plazo
        self.__interes = interes
        
    def get_plazo(self):
        return self.__plazo
    
    def get_interes(self):
        return self.__interes
    
    def calculo(self):
        c = self.get_monto * self.__interes / 100
        #c = self.get_monto * self.get_interes / 100
        #c = super().get_monto * self.__interes / 100
        return c
    
    def imprimir(self):
        print('Informacion de la Cuenta Interes: ')  
        super().imprimir()
        print(f'Plazo: {self.__plazo}')
        print(f'Interes: {self.__interes}')
        print(f'Total de Interes: {self.calculo()}')
        print(f'Monto Final: {self.__monto + self.calculo()}')
        
    def __str__(self):
        imp = super().__str__()
        imp += f'\nPlazo: {self.__plazo}'
        imp += f'\nInteres: {self.__interes}'
        imp += f'\nCalculo del Interes: {self.calculo()}'
        return imp