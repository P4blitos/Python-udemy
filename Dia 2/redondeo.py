#Round(numero_a_redondear, Can_decimales)
#Redondea hacia arriba o abajo, cuando es 10.5 redondea hacia arriba
print(90/7)
print(round(90/7))

resultado= round(90/7)
print(resultado)
print("---------------")
valor= round(95.66666666666666, 2)
print(valor)
print(type(valor))
valor=round(95.66666666)
print(valor)
print(type(valor))
print("---------------")
#Ejercicio1: Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
print(round(10/3,2))

#Ejercicio2: Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
valor = 10.676767
valor= round(valor)
print(valor)

#Ejercicio3: Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
valor=round((5**0.5),4)
print(valor)