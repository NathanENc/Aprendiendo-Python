# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión.

# Preguntar la cantidad a invertir
cantidad = float(input("Escribe la cantidad a invertir: "))
interes = float(input("Escribe la cantidad de interes: "))
año = float(input("Escribe el numero de años: "))

#Formula de interes compuesto
interes_comp = cantidad*((interes / 100) + 1)**año

# Resultado del interes
print(f"El capital de {cantidad} obtenido en el periodo de {año} año/s  con un interes de {interes} es igual a {round (interes_comp,2)} ")
