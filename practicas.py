colorFavorito = input("Color Favorito: ")
articuloElegido = input ("En que articulo prefiere verlo?")
frecuenciaUso = input ("Cada cuanto usa el articulo?")

print (" Gracias por compartir que su color favorito es", colorFavorito,"ahora podre comparte el", articuloElegido, "en ese color para que puedas usarlo", frecuenciaUso)





"""
Tipos de Datos:
    -numeros enteros: int
    -numeros decimales: float
    -strings: str

"""
nombreProducto = input(" Nombre de producto: ")

codigoProucto = print("Codigo de producto :1 ")

cantidad = int(input("Cantidad:"))

precioProducto = float(input("Precio de producto: "))
print("Precio de producto: ", precioProducto)

descuento = 15
print("Descuento %", descuento)

subtotal = cantidad * precioProducto
print(precioProducto, "*", cantidad, "=", subtotal)

montoDescuento = (subtotal * descuento)/100
print(montoDescuento - subtotal)


total = subtotal - montoDescuento
print(subtotal, "-", montoDescuento, "=", total)

#----------------------

nombre_trabajador = input("Ingresar nombre del trabajador:")
horas_semanales = int(input("Cuantas horas laboradas semanalmente:"))
pago_hora = float(input("Ingresar salario por hora:"))

salario_debengado = horas_semanales * pago_hora

print("Total de ingreso semanal:",salario_debengado)

#----------------------
"""
Nombres de las variables:

nombre
horas_trabajadas
pago_por_hora
salario_total
"""
nombre = input("Ingrese su nombre: ")
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

salario_total = horas_trabajadas * pago_por_hora

print("\n RESUMEN DE SALARIO ")
print(f"Nombre: {nombre}")
print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Pago por hora: {pago_por_hora:.3f}")
print(f"Salario total: {salario_total:.3f}")

#---------------------------
p = float(input("Precio: "))
d = 10
pf = p - d
print("Precio final:", pf)	 	 	 