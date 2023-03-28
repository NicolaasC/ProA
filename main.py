import paquete1
from paquete1 import resta

x=float(input ('Ingrese numero x:'))
y=float(input ('Ingrese numero y:'))

print(paquete1.suma(x,y),'Esta es la suma')
print(paquete1.resta(x,y), 'Esta es la resta')
print(paquete1.mul(x,y),'Esta es la multiplicacion')
print(paquete1.div(x,y),'Esta es la division')
print(paquete1.raiz2(x),'Esta es la raiz cuadrada')