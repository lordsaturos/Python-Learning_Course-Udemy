# Fichero Python para la sección 2 del curso de Python
# Sección 2: Variables y Tipos de Datos

# Video 13 Tipos de datos
    # String(str) "hola","&%$",'1234', "1234.56"
    # Entero(int) 1, 2, 3, 4, 5, -1, -2, -3
    # Flotante(float) 1.0, 2.0, 3.0, 4.0, 5.0, -1.0, -2.0, -3.0
    # Booleano(bool) True, False
    # Listas(list) [1,2,3], ["hola", "adios"], [1.0, 2.0, 3.0], [True, False]
    # Tuplas(tuple) (1,2,3), ("hola", "adios"), (1.0, 2.0, 3.0), (True, False)
    # Conjuntos(set) {1,2,3}, {"hola", "adios"}, {1.0, 2.0, 3.0}, {True, False}
    # Diccionarios(dict) {"nombre": "Juan", "edad": 30}, {"nombre": "Maria", "edad": 25}    
    # NoneType(None) None
    # Complejos(complex) 1+2j, 3+4j, 5+6j, 7+8j, 9+10j, -1-2j, -3-4j, -5-6j, -7-8j, -9-10j
    # Bytes(bytes) b"hola", b"adios", b"1234", b"1234.56"
    # Bytearray(bytearray) bytearray(b"hola"), bytearray(b"adios"), bytearray(b"1234"), bytearray(b"1234.56")
    # Memoryview(memoryview) memoryview(b"hola"), memoryview(b"adios"), memoryview(b"1234"), memoryview(b"1234.56")
    
# Video 14 Variables
# Variable: Espacio en memoria donde se almacena un valor
    # Variable: Es una caja con un nombre donde se almacena un valor.
nombre = "Juan" # Variable de tipo string
print(nombre)
nombre = "Laura"
print(nombre)

edad = 30 # Variable de tipo entero
print(edad)
print(20 + edad) # Sumar 20 a la variable edad

nombre2 = input("Dime tu nombre: ")
print("Hola " + nombre2) # Concatenar cadenas de texto

frase = nombre2 + " Es su nombre y tiene " + str(edad) + " años."
print(frase) # Concatenar cadenas de texto y convertir la variable edad a string

# Ejercicio de codificación 10. Practica con variables 1.
nombre_ejercicio = "Tony Soprano"
edad_ejercicio = 51
print("Hola " + nombre_ejercicio + " tienes la friolera de " + str(edad_ejercicio) + " años.")

# Ejercicio de codificación 11. Practica con variables 2.
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print(nombrecompleto)

# Ejercicio de codificación 12. Practica con variables 3.
curso = "Python"
print("Estás tomando un curso de " + curso)

# Video 15 Los nombres de las variables

    # Regla1: Debe ser legible el nombre de la varaible
    # Regla2: No puede estar separado por espacios en blanco. Debe formar un unico nombre, se puede usar _ y minusculas.
        # No usar mayus, tildes, y la ñ convertir a anios.
    # Regla3: No puede empezar por un numero, ni contener caracteres especiales como @#$%&*(){}[];:,.<>?/\|`~^¨´
        # No puede empezar por un numero, ni contener caracteres especiales como @#$%&*(){}[];:,.<>?/\|`~^¨´
    # Regla4: No puede ser una palabra reservada de Python. Ejemplo: if, else, for, while, def, class, etc.
    # Regla5: No puede ser una variable ya definida. Ejemplo: nombre, edad, curso, etc.
    
# Video 16 Integers y Floats
    # Integers Enteros
    # Floats Flotantes. decimales
mi_numero = 1
print(mi_numero)
print(type(mi_numero))
    
mi_numero2 = 2.5
print(mi_numero2)
print(type(mi_numero2))
    
mi_numero2 = 5 + 2.5
print(mi_numero2)
print(type(mi_numero2))
    
# Todo lo que introduce el usuario por teclado es un string.
print(type(input("Escribe algo: "))) # Esto e4s un string str

# Ejercicio de codificación 13. Practica con integers
num_entero = 14
print(type(num_entero))

# Ejercicio de codificación 13. Practica con floats
num_decimal = 14.1259
print(type(num_decimal))

# Ejercicio de codificación 13. Practica con tipos de datos numericos
num1 = 7.5
num2 = 2.5

print(type(num1 + num2))

# Video 17 Conversiones entre tipos de datos
# En python pueden almacener string, int, float, etc etc. No hay que asignar tipos de datos. Entonces coo sabe que tipo de dato es?
# Y más importante, como se puede cambiar de un tipo de dato a otro? y cuando?

# Casting implicita y explicita
#Casting implicita se encarga python.

# Casting Explicito le pedidmos a python que convierta un tipo a otro diferente.
mi_valor = 1
otro_valor = str(mi_valor)
print(otro_valor) # Como esto ya es un string, puedo concatener string.

# Ejermplos  de conversión implicita por Python
num1 = 20
num2 = 30.5

num1 = num1 + num2 # Num1 automaticamente lo convierte en float

print(type(num1)) # 
print(type(num2))

#Ejemplo explicito por el usuario
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1) # Conversion forzaada de float a int y se pierde decimal. Redondeo hacia abajo.

print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = edad + 14
print(nueva_edad)
print(type(nueva_edad))


# Ejercicio de codificación 16. Practica con conversiones 1
num1 = 7.5
num1 = int(num1)
print(type(num1))
# Ejercicio de codificación 16. Practica con conversiones 2
num2 = 10
num2 = float(num2)
print(type(num2))
# Ejercicio de codificación 16. Practica con conversiones 3
num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))

# Video 18 Formatear Cadenas.
color_auto = 'rojo' #Diferencia entre comillas simples y dobles. Se puede usar cualquiera de las dos.
matricula = 266254
matricula = str(matricula)
print("Mi coche es de color " + color_auto + " y su matricula es " + matricula)

# Funcion Format
print("Mi coche es {} y su matricula es {}".format(color_auto, matricula)) # Conversion automatica. Problema de legibilidad.
# Cadenas literales
print(f"Mi coche es {color_auto} y su matricula es {matricula}")

# Ejercicio de codificación 19. Practica Formatear cadenas 1
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print("Estimado/a " + nombre_asociado + ", su número de asociado es: " + str(numero_asociado))
# Ejercicio de codificación 19. Practica Formatear cadenas 2
puntos_nuevos = 350
puntos_totales = 1225

print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_totales))
# Ejercicio de codificación 19. Practica Formatear cadenas 3
puntos_anteriores = 875
puntos_nuevos = 350

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")


# Video 19 Operadores Matématicos.
x = 5
y = 3
print(f"x + y = {x + y}")

# + Suma, - Resta, * Multiplicacion, / Division, // Division entera, % Modulo, ** Potencia

# Ejercicio de codificación 22. Practica operadores matematicos 1
print(f"{874 // 27}") #Muestra cociente entero
# Ejercicio de codificación 22. Practica operadores matematicos 2
print(f"{456 % 33}")
# Ejercicio de codificación 22. Practica operadores matematicos 3
print(f"{783 ** 0.5}")

# Video 20 Redondeos
#round(redondeo)
round(154.5454,parametro2) # Redondea x decimales. Si no pones el parametro te reondea ahcia arriba o abajo segun el valor.
print(90/7)
print(round(90/7))
print(round(90/7, 2))

# Ejercicio de codificación 23. Practica Redondeo 1
print(round(10/3,2))
# Ejercicio de codificación 23. Practica Redondeo 2
valor = 10.676767
print(round(valor))
# Ejercicio de codificación 23. Practica Redondeo 3
print(round(5**0.5,4))

