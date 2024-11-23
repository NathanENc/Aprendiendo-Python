# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
# hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así
# que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a
# demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el
# número de payasos y muñecas vendidos en el último pedido y calcule el peso total del
# paquete que será enviado.

# Peso de los jueguetes:
peso_payasos = 112
peso_muñecas = 75

# Pedir juguetes 
payasos = int(input("Escribe cuantos payasos quieres comprar: "))
muñecas = int(input("Escribe cuantas muñecas quieres comprar: "))

#Resultado de pesos
peso_total = ((payasos * peso_payasos ) + (muñecas * peso_muñecas)) 

# Calculo del peso de objetos
print(f"El peso total del paquete es de {peso_total} gramos")