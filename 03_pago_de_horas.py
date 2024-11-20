#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

#Pedir horas trabajdas
horas_trabajadas = int(input("Cuantas horas trabajaste (solo valores numericos enteros) "))

#Pedir coste por hora (entero)
coste_horas =int(input("¿Cuantó vale cada hora? (solo valores numericos"))

# Calcular el pago (entero)
resultado = (horas_trabajadas * coste_horas)
#Mostrar el resultado
print("Lo que se te pagára es: ", resultado)