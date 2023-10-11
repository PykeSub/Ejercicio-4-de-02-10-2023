from Cuenta_Bancaria import Cuenta_Bancaria
from Cuenta_Rut import Cuenta_Rut
from Cuenta_Inversion import Cuenta_Inversion
from Cuenta_Corriente import Cuenta_Corriente

cb = Cuenta_Bancaria('Juanito', '07-10-2019', 50000)
print(cb)
cr = Cuenta_Rut('Pablo', '25-05-2021', 179000)
print(cr)
ci = Cuenta_Inversion('Ignacio', '31-11-2020', 20000, 3, 10.5)
print(ci)
cc = Cuenta_Corriente('Marco', '19-01-2023', 200000)
print(cc)