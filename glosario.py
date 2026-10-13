'''
Término: Algoritmo

Definición técnica: Un algoritmo es un conjunto finito y ordenado de instrucciones o pasos que permite resolver un problema o realizar una tarea determinada.

Aporte original: Para mí, un algoritmo es una guía de pasos que me permite organizar lo que debo hacer para llegar a un resultado. Primero puedo pensar en los pasos y después convertirlos en un programa.
'''

# Se suman dos números siguiendo una secuencia de pasos

numero1 = 10
numero2 = 5
resultado = numero1 + numero2

print("El resultado es:", resultado)

'''
Salida esperada:
El resultado es: 15

Utilidad:
Sirve para organizar la solución de un problema antes de escribir el programa. Los algoritmos pueden utilizarse para realizar cálculos, procesar información y automatizar diferentes tareas.

Fuente:
Python Software Foundation. (2026). The Python tutorial. Python Documentation.
https://docs.python.org/3/tutorial/
'''

'''
Término: Constante

Definición técnica: Una constante es un valor que se establece para permanecer sin cambios durante la ejecución de un programa. En Python no existe una forma de impedir que una constante sea modificada, pero por convención se utilizan nombres escritos en mayúsculas para indicar que su valor no debería cambiar.

Aporte original: Para mí, una constante es un valor que establezco porque necesito utilizarlo varias veces sin modificarlo. En Python puedo escribir su nombre en mayúsculas para identificar que debe mantenerse igual.
'''

# Se utiliza una constante para calcular el área de un círculo

PI = 3.1416
radio = 5
area = PI * radio ** 2

print("El área del círculo es:", area)

'''
Salida esperada:
El área del círculo es: 78.54

Utilidad:
Sirve para almacenar valores que se utilizan repetidamente y que deben mantenerse iguales durante el desarrollo del programa. Por ejemplo, puede utilizarse para representar valores matemáticos, límites o configuraciones.

Fuente:
van Rossum, G., Warsaw, B., & Coghlan, A. (2001). PEP 8 – Style Guide for Python Code. Python Enhancement Proposals.
https://peps.python.org/pep-0008/
'''

'''
Término: Dato

Definición técnica: Un dato es una representación de información que puede ser almacenada, procesada o utilizada por un programa. En Python existen diferentes tipos de datos, como números, cadenas de texto y valores booleanos.

Aporte original: Para mí, un dato es la información que utiliza el programa para realizar una operación, mostrar un resultado o tomar una decisión. Puede ser un nombre, un número, una respuesta u otro tipo de información.
'''

# Se almacenan diferentes tipos de datos

nombre = "Ana"
edad = 20
esEstudiante = True

print(nombre)
print(edad)
print(esEstudiante)

'''
Salida esperada:
Ana
20
True

Utilidad:
Los datos son necesarios para que un programa pueda funcionar. Se utilizan para almacenar información, realizar cálculos, tomar decisiones y generar resultados.

Fuente:
Python Software Foundation. (2026). The Python tutorial. Python Documentation.
https://docs.python.org/3/tutorial/
'''

'''
Término: Entrada y salida

Definición técnica: La entrada corresponde a la información que recibe un programa, mientras que la salida corresponde a la información que el programa produce o muestra. En Python, la función input() permite recibir información y print() permite mostrarla.

Aporte original: Para mí, la entrada es la información que llega al programa y la salida es lo que el programa muestra después de procesar esa información. Esto permite que exista comunicación entre el usuario y el programa.
'''

# Se recibe información y se muestra un resultado

nombre = "Laura"
edad = 22

print("Nombre:", nombre)
print("Edad:", edad)

'''
Salida esperada:
Nombre: Laura
Edad: 22

Utilidad:
Permite que los programas reciban y presenten información. Es fundamental para crear programas interactivos y para trabajar con datos proporcionados por usuarios u otras fuentes.

Fuente:
Python Software Foundation. (2026). Input and output. Python Documentation.
https://docs.python.org/3/tutorial/inputoutput.html
'''

'''
Término: Flujo condicional

Definición técnica: El flujo condicional es una estructura de control que permite ejecutar determinadas instrucciones dependiendo de si una condición es verdadera o falsa. En Python se implementa principalmente mediante las estructuras if, elif y else.

Aporte original: Para mí, el flujo condicional permite que un programa tome decisiones. Dependiendo de una situación, el programa puede seguir un camino diferente y ejecutar las instrucciones correspondientes.
'''

# Se verifica si la persona es mayor de edad

edad = 20

if edad >= 18:
    print("Es mayor de edad")

else:
    print("Es menor de edad")

'''
Salida esperada:
Es mayor de edad

Utilidad:
Sirve para que un programa pueda tomar decisiones según determinadas condiciones. Puede utilizarse para verificar edades, validar información, comparar resultados o determinar si una acción puede realizarse.

Fuente:
Python Software Foundation. (2026). More control flow tools. Python Documentation.
https://docs.python.org/3/tutorial/controlflow.html
'''

'''
Término: Flujo secuencial

Definición técnica: El flujo secuencial es la ejecución de las instrucciones de un programa en el mismo orden en que fueron escritas, de principio a fin.

Aporte original: Para mí, el flujo secuencial es como seguir una lista de pasos en orden. El programa comienza con la primera instrucción y continúa con las siguientes hasta completar el proceso.
'''

# Las instrucciones se ejecutan de manera secuencial

nombre = "Carlos"
edad = 25
mensaje = "Hola " + nombre

print(mensaje)
print("Tienes", edad, "años")

'''
Salida esperada:
Hola Carlos
Tienes 25 años

Utilidad:
Sirve para realizar procesos que deben ejecutarse siguiendo un orden determinado. Es común en cálculos y procedimientos donde cada paso depende del anterior.

Fuente:
Python Software Foundation. (2026). The Python tutorial. Python Documentation.
https://docs.python.org/3/tutorial/
'''

'''
Término: IDE

Definición técnica: IDE significa Integrated Development Environment o Entorno de Desarrollo Integrado. Es un programa que reúne herramientas para desarrollar software, como un editor de código, herramientas para ejecutar programas y herramientas para depuración.

Aporte original: Para mí, un IDE es un espacio de trabajo que reúne las herramientas necesarias para programar en un mismo lugar. Esto facilita escribir, ejecutar y revisar el código.
'''

# Programa sencillo que puede escribirse y ejecutarse en un IDE

nombre = "María"
saludo = "Hola " + nombre

print(saludo)

'''
Salida esperada:
Hola María

Utilidad:
Facilita el desarrollo de programas porque permite escribir y ejecutar código desde un mismo entorno. Muchos IDE también incluyen herramientas para detectar errores y depurar programas.

Fuente:
Red Hat. (2026). What is an IDE? Red Hat.
https://www.redhat.com/en/topics/middleware/what-is-ide
'''

'''
Término: Operadores aritméticos

Definición técnica: Los operadores aritméticos son símbolos que permiten realizar operaciones matemáticas sobre valores. En Python se utilizan operadores como + para sumar, - para restar, * para multiplicar, / para dividir, // para división entera, % para obtener el residuo y ** para elevar a una potencia.

Aporte original: Para mí, los operadores aritméticos son las herramientas que permiten realizar cálculos matemáticos dentro de un programa. Con ellos puedo transformar valores y obtener nuevos resultados.
'''

# Se realizan diferentes operaciones aritméticas

numero1 = 10
numero2 = 3

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

'''
Salida esperada:
Suma: 13
Resta: 7
Multiplicación: 30
División: 3.3333333333333335

Utilidad:
Sirven para realizar cálculos dentro de un programa. Se pueden utilizar para operaciones financieras, científicas, estadísticas, educativas y muchas otras aplicaciones.

Fuente:
Python Software Foundation. (2026). Expressions. Python Documentation.
https://docs.python.org/3/reference/expressions.html
'''

'''
Término: Operadores de comparación

Definición técnica: Los operadores de comparación permiten comparar dos valores y determinar la relación que existe entre ellos. En Python se utilizan ==, !=, <, >, <= y >=. El resultado de una comparación es un valor booleano: True o False.

Aporte original: Para mí, los operadores de comparación permiten hacer preguntas al programa sobre dos valores. El programa responde si la comparación es verdadera o falsa.
'''

# Se comparan diferentes valores

edad = 20

print(edad == 20)
print(edad > 18)
print(edad < 18)

'''
Salida esperada:
True
True
False

Utilidad:
Sirven para comparar valores y obtener resultados que pueden utilizarse posteriormente en decisiones. Por ejemplo, permiten comparar edades, precios, cantidades o resultados.

Fuente:
Python Software Foundation. (2026). Comparisons. Python Documentation.
https://docs.python.org/3/reference/expressions.html#comparisons
'''

'''
Término: Operadores lógicos

Definición técnica: Los operadores lógicos permiten combinar o negar expresiones booleanas. En Python los principales operadores lógicos son and, or y not.

Aporte original: Para mí, los operadores lógicos permiten combinar varias condiciones para que el programa pueda tomar decisiones más específicas.
'''

# Se combinan dos condiciones

edad = 20
tieneEntrada = True

puedeEntrar = edad >= 18 and tieneEntrada

print("¿Puede entrar?", puedeEntrar)

'''
Salida esperada:
¿Puede entrar? True

Utilidad:
Sirven para combinar condiciones dentro de un programa. Son útiles para crear validaciones y establecer reglas que dependen de más de una condición.

Fuente:
Python Software Foundation. (2026). Boolean operations. Python Documentation.
https://docs.python.org/3/reference/expressions.html#boolean-operations
'''

'''
Término: PEP 8

Definición técnica: PEP 8 es la guía de estilo para el código Python. Establece convenciones para mejorar la legibilidad y consistencia del código, incluyendo recomendaciones sobre nombres, indentación, espacios y organización.

Aporte original: Para mí, PEP 8 es una guía que ayuda a escribir código de una manera ordenada y fácil de entender. No solamente importa que el programa funcione, sino también que otras personas puedan leerlo.
'''

# Se utilizan nombres de variables claros

nombre_usuario = "Ana"
edad_usuario = 20

print(nombre_usuario)
print(edad_usuario)

'''
Salida esperada:
Ana
20

Utilidad:
Ayuda a mantener un estilo uniforme y facilita la lectura y comprensión del código. Es especialmente importante cuando varias personas trabajan en un mismo proyecto.

Fuente:
van Rossum, G., Warsaw, B., & Coghlan, A. (2001). PEP 8 – Style Guide for Python Code. Python Enhancement Proposals.
https://peps.python.org/pep-0008/
'''

'''
Término: Programa

Definición técnica: Un programa es un conjunto de instrucciones escritas en un lenguaje de programación que pueden ser ejecutadas por una computadora para realizar una tarea o resolver un problema.

Aporte original: Para mí, un programa es un conjunto organizado de instrucciones que le indica a la computadora qué debe hacer para obtener un resultado determinado.
'''

# Programa que calcula el total de dos productos

precio1 = 1500
precio2 = 2500

total = precio1 + precio2

print("Total a pagar:", total)

'''
Salida esperada:
Total a pagar: 4000

Utilidad:
Los programas permiten automatizar tareas y resolver problemas mediante instrucciones que una computadora puede ejecutar. Pueden utilizarse para crear aplicaciones, sistemas, herramientas y diferentes soluciones tecnológicas.

Fuente:
Python Software Foundation. (2026). The Python tutorial. Python Documentation.
https://docs.python.org/3/tutorial/
'''

'''
Término: Prueba unitaria

Definición técnica: Una prueba unitaria es una prueba que permite comprobar de forma aislada el funcionamiento esperado de una unidad de código, como una función. Python proporciona el módulo unittest para crear y ejecutar pruebas unitarias.

Aporte original: Para mí, una prueba unitaria sirve para comprobar que una parte específica del programa funciona correctamente antes de utilizarla dentro de un sistema más grande.
'''
# Se define un valor esperado
resultado_esperado = 10

# Se realiza una operación
resultado = 5 + 5

# Se comprueba si el resultado es correcto
if resultado == resultado_esperado:
    print("La prueba fue exitosa")
else:
    print("La prueba falló")
 
'''
Salida esperada:
- La prueba fue exitosa

Utilidad:
Sirve para detectar errores en funciones o partes específicas de un programa. También permite comprobar que los cambios realizados en el código no afecten funciones que anteriormente funcionaban correctamente.

Fuente:
Python Software Foundation. (2026). unittest — Unit testing framework. Python Documentation.
https://docs.python.org/3/library/unittest.html

'''

'''
Término: Variable

Definición técnica: Una variable es un nombre que permite hacer referencia a un valor u objeto dentro de un programa. En Python, mediante una asignación se puede asociar un nombre con un objeto y utilizarlo posteriormente.

Aporte original: Para mí, una variable es como una caja identificada con un nombre donde puedo guardar información para utilizarla dentro del programa. El valor asociado puede cambiar mediante una nueva asignación.
'''

# Se asignan valores a las variables

edad = 18
nombre = "Ana"

print(nombre, "tiene", edad, "años")

'''
Salida esperada:
Ana tiene 18 años

Utilidad:
Sirve para almacenar datos que se reutilizan durante el programa. Por ejemplo, puede utilizarse para guardar el nombre de un usuario, una edad, un precio o el resultado de una operación.

Fuente:
Python Software Foundation. (2026). The Python tutorial. Python Documentation.
https://docs.python.org/3/tutorial/
'''
