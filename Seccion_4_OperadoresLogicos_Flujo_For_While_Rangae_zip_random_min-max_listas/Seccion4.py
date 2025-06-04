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
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in list(enumerate(lista_nombres)):
    print(f'{nombre} se encuentra en el índice {indice}')
    
#Ejercicio de codificación 74 Practica de enumerar 2
#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate()
# los índices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices .
palabra = "Python"
lista_indices = list(enumerate(palabra))

print(lista_indices)

#Ejercicio de codificación 75 Practica de enumerar 3
#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:
#Loops
#Condicionales if
#El método enumerate()
#Métodos de strings o indexado
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in list(enumerate(lista_nombres)):
    if nombre.startswith('M'):
        print(indice)
        
#Video 49. Zip. Junta 2 listas para hacer un par.
#zip une dos listas en una sola lista de tuplas.
lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']
lista_zip = list(zip(lista1, lista2))  # Une las dos listas en una lista de tuplas
print(lista_zip)  # Imprime la lista de tuplas

nombres = ['Juan', 'Ana', 'Pedro', 'Maria']
edades = [25, 30, 35, 40]
lista_zip1 = zip(nombres, edades)  # Une las dos listas en una lista de tuplas
print(lista_zip1)  # Imprime la lista de tuplas
print(list(lista_zip1))  # Convierte el zip a una lista y la imprime

for nombre,edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")  # Imprime el nombre y la edad de cada persona
    
#Si no tiene la misma longitud ambas listas, se acorta el sobrante a la más corta.
ciudades = ['Madrid', 'Berlin', 'Varsovia', 'Atenas']
nombres = ['Juan', 'Ana', 'Pedro']
edades= [25, 30, 35, 40]
lista_zip2 = zip(ciudades, nombres, edades)  # Une las tres listas en una lista de tuplas
print(list(lista_zip2))  # Convierte el zip a una lista y la imprime

for ciudad, nombre, edad in zip(ciudades, nombres, edades):
    print(f"En la ciudad {ciudad} vive {nombre} y tiene {edad} años")  # Imprime la ciudad, el nombre y la edad de cada persona")
    
#Ejercicio de codificación 76 Practica de zip 1
#Muestra en pantalla frases como la del siguiente ejemplo:
#La capital de Alemania es Berlín
#Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
#capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
#paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista_zip_A = zip(capitales,paises)

for ciudad, pais in lista_zip_A:
    print(f"La capital de {pais} es {ciudad}")
    
#Ejercicio de codificación 77 Practica de zip 2
#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú 
# prefieras, dentro de la variable mi_zip.
marcas = ["Nike","Adidas","Reebook","Jumanji"]
productos = ["Zapatillas","Chanclas", "Tacon", "Muerte"]

mi_zip = zip(marcas, productos)

#Ejercicio de codificación 78 Practica de zip 3
#Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
#uno / um / one
#dos / dois / two
#tres / três / three
#cuatro / quatro / four
#cinco / cinco / five
#El resultado deberá seguir la estructura:
#[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

#1: uno / um / one
#2: dos / dois / two
#3: tres / três / three
#4: cuatro / quatro / four
#5: cinco / cinco / five

num_spa = ["uno", "dos", "tres", "cuatro", "cinco"]
num_por = ["um", "dois", "três", "quatro", "cinco"]
num_ingl = ["one", "two", "three", "four", "five"]


numeros = list(zip(num_spa, num_por, num_ingl))


#Video 50 Min y Max.
#min y max. Sirve para detectar tanto minimos como en maximos en listas.
#Sirve tanto para numeros como para strings.
menor = min(58,96, 14, -5, 30, 0)
print(menor)  # Imprime el menor de los numeros
mayor = max(58,96, 14, -5, 30, 0)
print(mayor)  # Imprime el mayor de los numeros

#Otra forma es trabajar directamente con listas.
lista = [58,96, 14, -5, 30, 0]
menor = min(lista)  # Imprime el menor de los numeros
mayor = max(lista)  # Imprime el mayor de los numeros   
print(menor)  # Imprime el menor de los numeros
print(mayor)  # Imprime el mayor de los numeros

lista_string = ['hola', 'mundo', 'python', 'programacion']  
menor_string = min(lista_string)  # Imprime el menor de los strings
mayor_string = max(lista_string)  # Imprime el mayor de los strings 
print(menor_string)  # Imprime el menor de los strings  
print(mayor_string)  # Imprime el mayor de los strings  

string_unico = 'hola mundo'
menor_string_unico = min(string_unico)  # Imprime el menor de los caracteres del string
mayor_string_unico = max(string_unico)  # Imprime el mayor de los caracteres del string
print(menor_string_unico)  # Imprime el menor de los caracteres del string
print(mayor_string_unico)  # Imprime el mayor de los caracteres del string

dic = {'ZZ': '10', 'E': '14', 'a': '55'}
menor_dic = min(dic)  # Imprime la clave menor del diccionario  
mayor_dic = max(dic)  # Imprime la clave mayor del diccionario
print(menor_dic)  # Imprime la clave menor del diccionario  
print(mayor_dic)  # Imprime la clave mayor del diccionario  

#Ejercicio de codificación 79 Practica de min y max 1
#Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

#lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

#Ejercicio de codificación 80 Practica de min y max 2
#Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

#lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

#Ejercicio de codificación 81 Practica de min y max 3
#Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

#diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
#Almacena dicho valor en una variable llamada edad_minima.
#También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)


#Video 51. Random
#importamos metodo randint() de la libreria random
#desde esta libreria importa este metodo
from random import randint
#O importamos toda la libreria random
#import random
aleatorio = randint(1, 50)
print(aleatorio)  # Imprime un numero aleatorio entre 1 y 50
from random import *

aleatorio2 = uniform(1, 5)
print(aleatorio2)

aleatorio3 = round(uniform(1, 5), 3)  # Genera un numero aleatorio entre 1 y 5 con 3 decimales  
print(aleatorio3)

#metodo random
aleatorio4 = random()
print(aleatorio4)  # Imprime un numero aleatorio entre 0 y 1

colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja']
aleatorio5 = choice(colores)  # Elige un color aleatorio de la lista
print(aleatorio5)  # Imprime un color aleatorio de la lista

shuffle(colores)  # Mezcla los colores de la lista
print(colores)  # Imprime la lista de colores mezclada

#Shuffle no se puede usar con strings, ya que no es un iterable.

#Ejercio de codificación 82 Practica de random 1
#Implementa la función randint() de la librería random que te permita obtener un número 
# entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
from random import randint
aleatorio = randint(1,10)

#Ejercicio de codificación 83 Practica de random 2
#Implementa la función random() de la librería random que te permita obtener un número decimal 
# entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
from random import random
aleatorio = random()

#Ejercicio de codificación 84 Practica de random 3
#Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de 
# nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
#nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)

#Video 52. Comprension de listas
#Vemos lo mismo haciendolo de forma más eficiente.
palabra = 'Python'

lista = []

for letra in palabra:
    lista.append(letra)  # Añade cada letra de la palabra a la lista
    
print(lista)

# Lo mismo pero más eficiente
palabra2 = 'Paises Bajos'
lista2 = [letra for letra in palabra2]
print(lista2)

lista2 = [letra for letra in "Santiago de Chile"]
print(lista2)

lista_num = [num for num in range(1, 100,2)]

print(lista_num)

lista_num3 = [n for n in range(1, 100, 3) if n % 3 == 0]  # Filtra los números que son múltiplos de 3
print(lista_num3)

lista_num4 = [n if n * 2 > 10 else 'no' for n in range(1, 21, 2)]  # Filtra los números que son múltiplos de 3
print(lista_num4)

pies = [10, 15, 20, 35, 40]

metros = [pie * 3.281 for pie in pies]  # Convierte los pies a metros
print(metros)

#Ejercicio de codificación 85 Practica de comprensión de listas 1
#Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
#Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
#valores = [1, 2, 3, 4, 5, 6, 9.5]

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]
print(valores_cuadrado)

#Ejercicio de codificación 86 Practica de comprensión de listas 2
#Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino 
# correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de 
# listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

#Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

#valores = [1, 2, 3, 4, 5, 6, 9.5]
valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [elemento for elemento in valores if (elemento % 2 == 0)]

print(valores_pares)

#Ejercicio de codificación 87 Practica de comprensión de listas 3
#Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino 
# correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de 
# listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

#Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:

#°C = (°F - 32) * (5/9)

#o expresado de otro modo:
#(grados_fahrenheit-32)*(5/9)
#La lista de temperaturas es la siguiente:
#temperatura_fahrenheit = [32, 212, 275] 
#Almacena esta nueva lista en una variable llamada grados_celsius

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [((tempF-32)*(5/9)) for tempF in temperatura_fahrenheit]

print(grados_celsius)


#Cuestionario 4.

#53 Soluciones a las practicas día 4.


#Video 54. Match actualización python
#Se ha añadido una variedad de if el Match. En otros lenguajes es switch case.

#Ejemplo de Match

Serie = "Breaking Bad"

#Ejemplo usando switch.
if Serie == "Breaking Bad":
    print("La mejor serie de la historia")
elif Serie == "Game of Thrones":
    print("La mejor serie de fantasía")
elif Serie == "The Wire":
    print("La mejor serie de crimen")
elif Serie == "The Sopranos":
    print("La mejor serie de mafia")

#Ahora hacemos lo mismo con match
match Serie:
    case "Breaking Bad":
        print("La mejor serie de la historia")
    case "Game of Thrones":
        print("La mejor serie de fantasía")
    case "The Wire":
        print("La mejor serie de crimen")
    case "The Sopranos":
        print("La mejor serie de mafia")
    case _:
        print("No es una serie que conozca")  # El guion bajo es el caso por defecto.
    
    
    #Creamos un diccionario
cliente = {'nombre': 'Paco',
          'edad': 30,
          'pais': 'España',
          'telefono': '123456789',
          'trabajo': 'Programador'}

pelicula = {'titulo': 'El Padrino',
           'ficha_tecnica': {'director': 'Francis Ford Coppola',
           'año': 1972,
           'genero': 'Crimen',
           'protagonistas': ['Marlon Brando', 'Al Pacino', 'James Caan']}}
    #Ejemplo de match con diccionario
    
elementos = [cliente, pelicula, 'libro']
for e in elementos:
    match e:
        case {'nombre': nombre, #Aqui esta estamos haciendo un match con el diccionario cliente
              'edad': edad,
              'trabajo': ocupacion}:
            print("Se trata de un cliente")
            print(f"Cliente: {nombre}, Edad: {edad}, Ocupación: {ocupacion}")
        case {'titulo': titulo, #Aqui estamos haciendo un match con el diccionario pelicula
              'ficha_tecnica': {'director': director,
                                'año': año,
                                'genero': genero,
                                'protagonistas': protagonistas}}:
            print(f"Pelicula: {titulo}, Director: {director}, Año: {año}, Género: {genero}, Protagonistas: {', '.join(protagonistas)}")
        case 'libro':
            print("Elemento es un libro")
