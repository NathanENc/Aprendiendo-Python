# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# Pedir dos números
n = int(input("Dame un valor entero: "))
m = int(input("Dame el segundo valor entero: "))

# Salida de pantalla
print(f"{n} entre {m} da un cociente {n // m} y un resto {n % m}")