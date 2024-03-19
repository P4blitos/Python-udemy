num1=25
num2=1.9

num1=num1+num2

print(type(num1))
print(type(num2))

#-------------------------------------

num3= 3.5
print(num3)
print(type(num3))

num4= int(num3) #Lo convertimos en entero
print(num4)
print(type(num4))

#-------------------------------------------

edad=input("Dime tu edad \n")
edad=int(edad)
nueva_edad= edad+1
print("Tu nueva edad va a ser: ",nueva_edad)# para concatenar enteros y strings debe ser con ","

#-----------------------------------------------
#Ejercicio 1
#Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
num1=int(num1)
print(type(num1))

#Ejercicio 2
#Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10
num2=float(num2)
print(type(num2))

#Ejercicio 3
#Suma los valores de num1 y num2. No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))