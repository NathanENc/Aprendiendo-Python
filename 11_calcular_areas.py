# Escribe un programa que: 
# Pregunte al usuario su nombre.
# Solicite al usuario el radio de un círculo.
# Calcule el área y el perímetro del círculo.
# Muestre un mensaje personalizado con el resultado usando el nombre del usuario.

# Constante para valor de π PI = 3.14159
PI = 3.14159

# Solicitar el nombre del usuario
nombre = input("Escribe tu nombre: ")

radio = float(input(f"Hola {nombre} escribe el radio de un circulo para calcularlo: "))


# Calcular area y perimetro del circulo
area = PI * radio ** 2
perimetro = 2 * PI * radio

# Mostrar mensaje personalizado
print(f"Hola {nombre}, el area del círculo es: {area:.2f} y el perimetro {perimetro:.2f}")