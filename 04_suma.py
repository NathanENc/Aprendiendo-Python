# Escribir un programa que lea un entero positivo n,  introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.  La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = (n(n+1))/2

#Pedir numero principal
n = int(input("Escribe un número entero "))

# Calcular suma
suma = ((n * (n + 1)) / 2)

#Resultado Suma
print("El resultado de la suma desde 1 hasta",(n), "es", (suma))