"""
Variables: Un espacio en la memoria de lacomputadora donde guardamos un dato
Sintaxis:nombreVariable = datoQqueAlmacenaLaVariable

Tipos de datos:
    -Numeros:van sin comillas 1,2,3,4
    -Strings: Van entre comillas, ej:"Jose", "abc-050"
    -Booleano: true/false, verdadero/falso, 1/0
    "12" ::: 12
    asi sea numero si va entre comillas cambia y se vuelve string

Tipos de Datos:
    -numeros enteros: int
    -numeros decimales: float
    -strings: str

    
ej: nombre, cedula...
"""
nombreJugador = "Camila"
nombreJugador = "Rose"
print("Bienvenida(o))", nombreJugador)

nombreJugador = input("Ingrese su nombre (presione enterpara): ")
print("Bienvenida(o))", nombreJugador)

bombilloApagado = False
print("Bombillo apagado?", bombilloApagado)

bombilloApagado = True
print("Bombillo apagado?", bombilloApagado)

# Conversion de datos
puntaje = int(input("Ingrese su puntaje: "))
print("su puntaje mas 5 es: " , puntaje + 5)

tipoCambio = float(input("El tipo de cambio del euro: "))
print("El tipo de cambio del euro: " , tipoCambio + 5)