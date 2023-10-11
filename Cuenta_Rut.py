# La clase CuentaRut tendra una funcion para heredar los datos(init).
# Y uno para mostrar la informacion.

from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_Rut(Cuenta_Bancaria):
    def __init__(self, titular: str, fecha: str, monto: float):
        super().__init__(titular, fecha, monto)
        
    def imprimir(self):
        print('Informacion Cuenta Rut: ')
        return super().imprimir()
    
    def __str__(self):
        imp = super().__str__()
        return imp