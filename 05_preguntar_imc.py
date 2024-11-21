#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#Pedir peso
peso = float(input("Introduce tu peso en kilogramos: "))
#Pedir masa corporal
altura = float(input("Introduce tu altura en metros: "))

#Calcular imc
imc = round((peso/ (altura) ** 2 ), 2)

#Imprimir imc
print("Tu índice de masa corporal es:",(imc))