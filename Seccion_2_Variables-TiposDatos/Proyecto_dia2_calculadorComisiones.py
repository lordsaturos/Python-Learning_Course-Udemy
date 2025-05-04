#Ejercicio calculadora de comisiones. Proyecto dia 2.

nombreVendedor = input("Dime tu nombre: ")
ventasTotales = float(input("Dime el total de tus ventas: "))
comision = 0.13

print(f"El vendedor {nombreVendedor} ha vendido un total de {ventasTotales} y por lo tanto se lleva una comision de {round(ventasTotales * comision,2)})")