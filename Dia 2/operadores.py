x=6
y=2
z=7

print(f"{x} + {y} es igual a {x+y}")
print(f"{x} - {y} es igual a {x-y}")
print(f"{x} X {y} es igual a {x*y}")
print(f"{x} / {y} es igual a {x/y}")

#division al paso, es decir quita decimales. por ejemplo en la division 7/2=3.5 pero solo mostraria el 3
print(f"{z} / al piso {y} es igual a {z//y}")#asi se copia una division al piso
#modulo
print(f"{z} modulo de {y} es igual a {z%y}")
#potencia
print(f"{x} elevado a la {y} es igual a {x**y}")
#Raiz cuadrada
print(f"La raiz cuadrada de {x} es {x**0.5}")

#Ejercicio 1: Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27
x=874
y=27
print(x//y)

#Ejercicio 2: Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.
x=456%33
print(x)

#Ejercicio 3: Calcula y muestra en pantalla la raíz cuadrada de 783
print(783**0.5)