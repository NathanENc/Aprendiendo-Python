# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un
# descuento del 60%. Escribir un programa que comience leyendo el número de barras
# vendidas que no son del día. Después el programa debe mostrar el precio habitual de
# una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

# Pedir número de barras no frescas vendidas
pan = int(input("Cuantas panes quieres comprar que no son del día: "))

# Datos
precio_del_dia = 3.49
descuento = 0.6

# Cálculos
coste = pan * precio_del_dia * (1 - descuento)

print(f"El precio normal del pan es de {precio_del_dia} €")
print(f"El descuento que se le hace por no ser fresco es del {descuento * 100}")
print(f"El precio final es de {coste:.2f} €")