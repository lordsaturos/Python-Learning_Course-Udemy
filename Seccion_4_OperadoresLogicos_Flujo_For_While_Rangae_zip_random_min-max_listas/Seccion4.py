#Inicio Sección 4. Operadores lógicos, flujo de control, for, while, range, random, min-max, listas....

#Video 41 Operadores de comparación.

#== igual a
#!= distinto a
#> mayor que
#< menor que
#>= mayor o igual que
#<= menor o igual que
#Si es verdadera devuelve true, si es falsa devuelve false.

mi_variable = 'hola mundo' #asignación
#hago una comparación
mi_bool = 10 == 25 #esto es una comparación, devuelve un booleano. En este caso false.
print(mi_bool) #imprimo el booleano, en este caso false.

mi_bool2 = 30 < 25 #esto es una comparación, devuelve un booleano. En este caso false.
print(mi_bool2) #imprimo el booleano, en este caso false.
mi_bool3 = 'blanco' == 'rojo' #esto es una comparación, devuelve un booleano. En este caso false.
print(mi_bool3) #imprimo el booleano, en este caso false.
#La comparación de string es sensible a Mayus y Minúsculas.
mi_bool4 = 'Python' == 'python' #esto es una comparación, devuelve un booleano. En este caso false.
print(mi_bool4) #imprimo el booleano, en este caso false.

mi_bool4 = 'Python'.lower() == 'python' #esto es una comparación, devuelve un booleano. En este caso true.
print(mi_bool4) #imprimo el booleano, en este caso true.

mi_bool5 = '100'== 100 #esto es una comparación, devuelve un booleano. En este caso false.
print(mi_bool5) #imprimo el booleano, en este caso false.

mi_bool6 = 100.0 == 100 #esto es una comparación, devuelve un booleano. En este caso true.
print(mi_bool6) #imprimo el booleano, en este caso true.

#Ejercicio de codificación 55 Practca de operadores de comparación 1
#Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. 
# Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha 
# comparación en una variable llamada mi_bool
num1 = 36
num2 = 17
mi_bool = num1 >= num2

#Ejercicio de codificación 56 Practca de operadores de comparación 2
#Crea dos variables (num1 y  num2):
#Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
#Dentro de num2, almacena el número 5.
#Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 25**0.5
num2 = 5

mi_bool = num1 == num2

#Ejercicio de codificación 57 Practca de operadores de comparación 3
#Crea dos variables (num1 y  num2):

#Dentro de num1, almacena el resultado de la operación 64 x 3
#Dentro de num2, almacena el resultado de la operación 24 x 8
#Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 64*3
num2 = 24*8

mi_bool = num1 != num2

#Video 42 Operadores lógicos.
#and, or, not
#En python no se usa && ni || como operadores logicos
#Existe & y | pero son operadores bit a bit.
mi_bool = 4 < 5 < 6
print(mi_bool) #imprime true, porque 4 es menor que 5 y 5 es menor que 6.
mi_bool = 4 < 5 and 5 < 6
print(mi_bool) #imprime true, porque 4 es menor que 5 y 5 es menor que 6. 

mi_bool = 4 < 5 and 7 < 6
print(mi_bool) #imprime false, porque 4 es menor que 5 pero 7 no es menor que 6.

mi_bool = (4 < 5) and (-2 > 0)
print(mi_bool) #imprime false, porque 4 es menor que 5 pero -2 no es mayor que 0.   

#Operador or
mi_bool10= (10 == 10) or ( 3 == 3)
print(mi_bool10) #imprime true, porque 10 es igual a 10 o 3 es igual a 3.
mi_bool11= (10 == 10) or ( 3 == 4)
print(mi_bool11) #imprime true, porque 10 es igual a 10 o 3 no es igual a 4.

text = "Esta frase es breve"
mi_bool12 = ("breve" in text) and ("frase" in text)
print(mi_bool12) #imprime true, porque "breve" esta en el texto.

mi_bool12 = ("hola" in text) and ("frase" in text)
print(mi_bool12) #imprime false, porque "hola" no esta en el texto pero "frase" si.

mi_bool13 = 'a' == "a"
print(mi_bool13) #imprime true, porque 'a' es igual a "a".
mi_bool14 = 'a' == "A"  
print(mi_bool14) #imprime false, porque 'a' no es igual a "A" (diferencia de mayusculas y minusculas).

mi_bool15 = not 'b' == "b"
print(mi_bool15) #imprime false, porque 'b' es igual a "b".

mi_bool16 = not ('c' == "c")
print(mi_bool16) #imprime false, porque 'c' es igual a "c".

mi_bool17 = not ('c' == "d")
print(mi_bool17) #imprime true, porque 'c' no es igual a "d".

#Ejercicio de codificación 58 Practica de operadores lógicos 1
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 > num2) and (num1 < num3)
print(mi_bool)

#Ejercicio de codificación 59 Practica de operadores lógicos 2
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1 > num2) or (num1 < num3)
print(mi_bool)

#Ejercicio de codificación 60 Practica de operadores lógicos 3
#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = "éxito", y
#palabra2 = "tecnología"
#no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
#"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#Elon Musk
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = (palabra1 not in frase) and (palabra2 not in frase)

print(mi_bool)

#Video 43. Control de flujo.
#if, elif, else

if (10 > 9):
    print("10 es mayor que 9") #si la condicion se cumple, se ejecuta este bloque de codigo.
    
x = False
if (x == True):
    print("Entramso en bucle, por lo tanto x es true")
else:
    print("no entramos en blucle. por lo tanto x es false") #si la condicion no se cumple, se ejecuta este bloque de codigo.

mascota = "caballo"

if mascota == 'gato':
    print("tu mascota es un gato")
elif mascota == 'perro':
    print("tu mascota es un perro")
elif mascota == 'pez':
    print("tu mascota es un pez")
elif mascota =='caballo':
    print("tu mascota es un caballo")
    
edad = 15
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Edad no valida") 
    
nota = 4
if nota >= 9:
    print("Has sacado un sobresaliente")
elif nota >= 7:
    print("notable")
else: 
    print("Calificación no suficiente")
    
#ejercicio de codificación 61 Practica de control de flujo 1
#Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):
#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
#"num1 es mayor que num2"
#"num2 es mayor que num1"
#"num1 y num2 son iguales"
#Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
#Aclaración:
#1. No deben imprimirse strings adicionales a la respuesta del usuario.
#2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas".  Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if (num1 > num2):
    print(f"{num1} es mayor que {num2}")
elif (num2 > num1):
    print(f"{num2} es mayor que {num1}")
elif (num1 == num2):
    print(f"{num1} y {num2} son iguales")

#Ejercicio de codificación 62 Practica de control de flujo 2
#Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

#Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:
#"Puedes conducir"
#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
#"No puedes conducir. Necesitas contar con una licencia"

#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
edad = 16
tiene_licencia = False

if (edad >= 18):
    if (tiene_licencia == True):
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    
#Ejercicio de codificación 63 Practica de control de flujo 3
#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
#"Cumples con los requisitos para postularte"
#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
#"Para postularte, necesitas tener conocimientos de inglés"
#"Para postularte, necesitas saber programar en Python"
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

habla_ingles = True
sabe_python = False

if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif (habla_ingles == False) and (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif (habla_ingles == False) and (sabe_python == True):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif (habla_ingles == True) and (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")
    
#Video 44. Introducción a loops.

#Video 45. Loop for.
nombres = ["Juan", "Ana", "Pedro", "Maria"]
for elemento in nombres:
    print(elemento) #imprime cada elemento de la lista nombres.

lista = ['a', 'b', 'c']

for letra in lista:
    print(letra)  #imprime cada letra de la lista1
    
letrado = ['a', 'b', 'c', 'd', 'e']
for letra in letrado:
    numero_letra = letrado.index(letra) + 1
    print ("Letra: " + letra)
    print (f"Letra: {numero_letra}: {letra}")
    
lista_nombres = ['Juan', 'Ana', 'Pedro', 'Julen', 'Maria', 'Javier', 'Jose', 'Jorge']

for nombre in lista_nombres:
    if (nombre.startswith('J')):
        print(f"Hola {nombre}, tu nombre empieza con J")
        

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero #suma todos los numeros de la lista numeros
    print(f"Suma interna: {mi_valor}") #imprime la suma de los numeros de la lista numeros
    
print(f"La suma de los numeros es: {mi_valor}") #imprime la suma de los numeros de la lista numeros

palabra = 'python'

for letra in palabra: #Los string son iterables, por lo que se pueden recorrer letra a letra.
    print(letra)  #imprime cada letra de la palabra python


for objeto in [[1,2],[3,4],[7,8]]:
    print(objeto)
    

for a,b in [[1,2],[3,4],[7,8]]:
    print(a) #imprime el primer elemento de cada lista
    print(b) #imprime el segundo elemento de cada lista
    
for a,b in [[1,2],[3,4],[7,8]]:
    print(a) #imprime el primer elemento de cada lista

#Iterar en un diccionario

dic = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}  
for item in dic:
    print(item)  #imprime cada clave del diccionario
    
for item in dic.items():
    print(item)  #imprime cada clave y valor del diccionario como tupla (clave, valor)

for item in dic.values():
    print(item)  #imprime cada clave y valor del diccionario como tupla (clave, valor)
    
for a,b in dic.items():
    print(a,b)  #imprime cada clave y valor del diccionario como tupla (clave, valor)
    
#Ejercicio de codificación 64 Practica de loop for 1
#Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
#Por ejemplo: "Hola María"
#alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print("Hola " + alumno)
    
#Ejercicio de codificación 65 Practica de loop for 2
#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero 

#Ejercicio de codificación 66 Practica loop for 3
#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar
#num % 2 == 0 (valores pares)
#num % 2 == 1 (valores impares)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0 

for numero in lista_numeros:
    if numero % 2 == 0:
        #El valor es par
        suma_pares = suma_pares + numero
    else:
        #El valor es suma_impar
        suma_impares = suma_impares + numero


#Video 46 loop While
#El bucle while se ejecuta mientras la condicion sea verdadera.
#break, continue y pass
coin = 5
while coin >0:
    print(f"Monedas restantes: {coin}")
    coin = coin - 1 #resta 1 a la variable coin
else:
    print("No hay monedas restantes")
    
respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir jugando? (s/n): ")
else:
    print("Gracias por jugar")
    
    
#Ejemplo de pass
respuesta = 's'
while respuesta == 's':
    respuesta = 'n'
    pass #Esto mete bucle infinito

print("hola")

nombre = input("Introduce tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break #Si la letra es 'r', sale del bucle
    print(letra)
    
nombre = input("Introduce tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue #Si la letra es 'r', sale del bucle
    print(letra)
    
#Ejercicio de codificación 67 Practica de loop while 1
#Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10

while numero >= 0:
     print(numero)
     numero = numero -1
     
#Ejercicio de codificación 68 Practica de loop while 2
#Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
#- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
#- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
numero = 50

while numero >= 0:
  
    numero = numero -1
    if ((numero+1) % 5 == 0):
        print(numero+1) 

#Ejercicio de codificación 69 Practica de loop while 3
#Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:
#lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
#No debes cambiar el orden de la lista.
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for num in lista_numeros:

    if (num < 0):
        break
    else:
        print(num)
        
#Video 47 Range, rango
#range
for num in range(10): #range(10) genera una secuencia de numeros del 0 al 9
    print(num) #imprime los numeros del 0 al 9  
    
for num in range(20,45): #range(10) genera una secuencia de numeros del 20 al 45
    print(num) #imprime los numeros del 0 al 9      
    
    
for num in range(20,45,2): #range(10) genera una secuencia de numeros del 20 al 45 de 2 en 2 
    print(num) #imprime los numeros del 0 al 9    
    
    
list2 = list(range(0,101,1))
print(list2) #imprime una lista de numeros del 0 al 100

#ejercicio de codificación 70 Practica de range 1
# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en 
# la variable mi_lista.
mi_lista = list(range(2500,2586,1))

#Ejercicio de codificación 71 Practica de range 2
#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números
# múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(3,303,3))

#ejercicio de codificación 72 Practica de range 3
#Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
#Para ello:
#Crea un rango de valores que puedas recorrer en un loop
#Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
#Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
suma_cuadrados = 0

for i in range(1,16):
    suma_cuadrados = suma_cuadrados + i**2
    
#Video 48. Enumerador
lista = ['a', 'b', 'c', 'd', 'e']

indice = 0
for item in lista:
    print(indice,item) #imprime el indice y el item de la lista
    indice += 1 #incrementa el indice en 1
    
lista = ['a', 'b', 'c', 'd', 'e']

for item in enumerate(lista):
    print(item)
    

for indice,item in enumerate(lista):
    print(indice,item)
    
lista = ['a', 'b', 'c', 'd', 'e']
mi_tupla = list(enumerate(lista))
print(mi_tupla[1][0])

#Ejercicio de codificación 73 Practica de enumerar 1
#Imprime en pantalla frases como la siguiente:
#'{nombre} se encuentra en el índice {indice}'
#Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.
#Tip: utiliza loops!

