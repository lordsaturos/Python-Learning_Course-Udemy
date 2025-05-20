# Seccion 3 String, SubStrings, Listas, Diccionarios, Tuplas, Sets, Booleanos

# Video 27 Metodo Index() de la clase String

# Se puede acceder a los string desde la posición 0 a la izquierda hasta la n en la derecha.
# Tambien existe la posición inversa, donde la posición más a la derecha del string es el -1, luego -2 etc. 
# Hasta que llega a la izquierda del todo que pasa a tener el valor de 0
mi_texto = "Hola Mundo"
print(mi_texto.index("l")) # Devuelve la posición de la primera l que encuentra, en este caso 2

resultado = mi_texto[0] 
print(resultado) # Devuelve la letra H, que es la posición 0 del string

print(mi_texto[-2]) # Devuelve la letra u, que es la posición -2 del string


# resultado = mi_texto.index("X")
print(resultado)

texto2 = "Lore ipusum dolor sit amet, consectetur adipiscing elit."
print(texto2.index("dolor"))

print(texto2.index("s", 15, 25))

print(texto2.rindex("s")) # Devuelve la posición de la última s que encuentra

# Ejercicio codificacion 28. Practica metodo Index()
# Práctica Método Index() 1 Encuentra y muestra en pantalla qué caracter ocupa la quinta posición 
# dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])

# Ejercicio codificacion 29. Practica metodo Index()
# Encuentra y muestra en pantalla el índice de la primera aparición 
# de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

# Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.rindex("práctica"))

# Video 28. Extraer Sub-Strings
mi_variable = "esta palabra será extraida"
variable2 = mi_variable[5:12]

texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[7:14] # extrae desde la posición 7 hasta la 14, sin incluir la 14
print(fragmento)

fragmento = texto[7:] # extrae desde la posición 7 hasta el final
print(fragmento)

fragmento = texto[:30] # extrae desde el principio hasta la posición 30, sin incluir la 30
print(fragmento)

fragmento = texto[0:30:3] # extrae desde el principio hasta la posición 30, sin incluir la 30
print(fragmento)

# Ejercicio codificación 31. Practica sub-Strings 1
#  Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# Pista: "Controlar" tiene un largo de 9 caracteres.
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])

# Ejercicio codificación 32. Practica sub-Strings 2
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])

# Video 29. Metodos de String
    # upper() convierte a mayúsculas
    # lower() convierte a minúsculas
    # split() divide el string en una lista de strings
    # join() une una lista de strings en un solo string usando separador
    # find() busca un string dentro de otro y devuelve la posición de la primera aparición
    # replace() reemplaza un string por otro dentro de un string
    
texto = "Este es el texto de saturnalia"
resultado = texto.upper() # Convierte a mayúsculas
resultado  = print(resultado)

resultado = texto.lower() # Convierte a mayúsculas
print(resultado)

resultado = texto.split() # Convierte a split
print(resultado) # Devuelve una lista de strings

texto2 = "Este es el texto de saturnalia altenativo"
resultado2 = texto2.split("t") # Convierte a split
print(resultado2) # Devuelve una lista de strings

a = "Aprender"
b = "Python"
c = "esta"
d = "bien"
e = " "
frase = " ".join([a, b, c, d])
print(frase) # Devuelve una lista de strings

resultado = texto.find("texto") # Busca el string "texto" dentro de texto y devuelve la posición
# de la primera aparición. A diferencia de index. si no existe no da errror.
print(resultado) # Devuelve la posición de la primera aparición del string "texto"

resultado_r = texto.replace("texto", "frase") # Reemplaza el string "texto" por "frase"
print(resultado_r) # Devuelve el string con el texto reemplazado

# Ejercicio de codificación 34. Metodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

# Ejercicio de codificación 35. Metodos de String 2
#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, 
# y muestra en pantalla el resultado."
lista_palabras = ["La","legibilidad","cuenta."]
lista_palabras = " ".join(lista_palabras)
print(lista_palabras)

# Ejercicio de codificación 36. Metodos de String 3
# Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")
print(frase)

# Video 30. Propiedades de los Strings.
# Los string son inmutables. (pero se pueden volver a modificar usando otras variables o cambiando el contendio de la variable)
# Los strings pueden cocnatenarse " + "
# Los srint pueden multiplicarse con " *"
# Los strings pùeden tener saltos de linea con \n o con """ texto
# multi linea""""

# Te puede devolver true o false si hay un contenido dentro de otro string como por ejemplo
print("Hola" in "Hola Mundo") # Devuelve True
# calcular longitud de un string
hola_sistema = "Hola Sistemas"
print(len(hola_sistema)) # Devuelve la longitud del string

nombre = "Kaladin"
apellido = "Stormblessed"
print(nombre + " " + apellido) # Devuelve el string concatenado
# nombre[0] = "C" # Esto lanza error
print(nombre) # Devuelve el string original, ya que los strings son inmutables
nombre = "Caladin"
print(nombre) # Devuelve el string modificado, ya que se ha creado una nueva variable con el nuevo valor

# Sumar strings
n1 = "Kala"
n2 = "din"
n3 = n1 + n2 # Concatenar strings
print(n3) # Devuelve el string concatenado

# Multiplicar Strings
print(n3 * 10) # Devuelve el string multiplicado por 10

# Un string puede estar formado por varias lineas, seaprando con """
poema = """Mil pequeños peces blancos
en el agua de la luna bailan. Aromas
blancos dulces nieves"""
print(poema) # Devuelve el string con saltos de linea
print("agua" in poema) # Devuelve True, ya que el string "agua" está dentro del string poema
print("agua" not in poema) # Devuelve True, ya que el string "agua" está dentro del string poema

print(len(poema)) # Devuelve la longitud del string poeama

# Ejericio codificación 37. Propiedades de los Strings 1
# Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que 
# los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
texto = "Repetición"

print(texto * 15)

# Ejericio codificación 38. Propiedades de los Strings 2
# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias
verso = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in verso)

# Ejericio codificación 39. Propiedades de los Strings 2
# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
palabro = "electroencefalografista"
print(len(palabro))

# Video 31. Listas

mi_lista = [a, b, c, d, e] # Lista de strings
print(type(mi_lista))
print(mi_lista)

segunda_lista = [0, -5, 3.56, "hola"] # Lista de diferentes tipos de datos]
print("La longitud de la segunda_lista es: " + str(len(segunda_lista))) # Devuelve la longitud de la lista

lista_modificada= segunda_lista [0:2] # REcuerda que no incluye la posición 2.
print(lista_modificada)


mi_lista = ['a', 'b', 'c', 'd']
mi_lista2 = ['e', 'f', 'g', 'h']
resultado_listas = mi_lista[0:] # Devuelve la lista desde la posición 0 hasta el final
print(mi_lista + mi_lista2)   # Devuelve la lista concatenada
mi_lista3 = mi_lista + mi_lista2 # Devuelve la lista concatenada
mi_lista3[0] = "Tiranidos"
print(mi_lista3) # Devuelve la lista concatenada

mi_lista3.append("Tau")
print(mi_lista3)

elementos_eliminados = mi_lista3.pop() # Sin argumento elimina el último elemento de la lista
print(mi_lista3) # Devuelve la lista sin el último elemento

elementos_eliminados = mi_lista3.pop(2) # Con argumenta elimina el elemento de la posición 2
print(mi_lista3) # Devuelve la lista sin el último elemento

lista = ["Guardianes", "de", "la", "galaxia"]
nueva_lista = lista.sort() # Ordena la lista alfabéticamente
print(lista) # Devuelve la lista ordenada alfabéticamente
print(nueva_lista) # Devuelve None, ya que sort() no devuelve nada

lista.reverse() # Invierte el orden de la lista
print(lista) # Devuelve la lista invertida

# Ejercicio de codificación 40. Listas 1
# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = ["Tiranidos", "Tau", "Mech", "Devoradores de Mundos", "Aeldari", "Necrones"], # Lista de strings
print(mi_lista) # Devuelve la lista de strings

# Crea una lista con 5 elementos

# dentro de la variable mi_lista2. Puedes incluir strings, booleanos, números, etc.
mi_lista = [0, -5, 3.56, "hola", True] # Lista de diferentes tipos de datos

# Ejercicio de codificación 41. Listas 2
#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# No debes modificar la línea de código ya suministrada, sino que debes emplear el 
# método apropiado de listas para añadir un nuevo elemento.
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte2 = medios_transporte.append("motocicleta")

# Ejercicio de codificación 42. Listas 3
# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
# manzana
# banana
# mango
# cereza
# sandía
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

# Video 32. Diccionarios
# Un diccionario es una colección de pares clave-valor
# Se definen con {}
# Se accede a los valores mediante las claves
mi_diccionario = {
    "nombre": "Kaladin",
    "apellido": "Stormblessed",
    "edad": 25,
    "altura": 1.80,
    "peso": 75
}

print(mi_diccionario) # Devuelve el diccionario completo
print(mi_diccionario["nombre"]) # Devuelve el valor de la clave "nombre"

diccionario = {'c1': 'valor1', 'c2': 'valorB', 'c3': 'parametro3'}
print(type(diccionario)) # Devuelve el tipo de dato del diccionario
print(diccionario)
print(type(diccionario["c3"])) # Devuelve el tipo de dato del valor de la clave "c3"
print(diccionario["c3"]) # Devuelve el valor de la clave "c3"

cliente = {'nombre':'Pedro', 'apellido1':'Rodriguez', 'apellido2':'Lopez', 'edad': 34, 'telefono': 666445533}
consulta = print(cliente['apellido1'])
consulta2 = cliente['telefono']
print(consulta2) # Devuelve el valor de la clave "telefono"

dic = {'clave1':33, 'clave2':[6,12,18], 'clave3':{'superclave1':3.14, 'superclave2':"Hola"}}
print(type(dic))
print(type(dic['clave3']))
print(dic['clave3']['superclave2']) # Devuelve el valor de la clave "superclave2" dentro de la clave "clave3"

dicprueba  = {'cla1':['a', 'b', 'c'], 'cla2':['d', 'e', 'f'], 'cla3':['g', 'h', 'i']}
print(dicprueba['cla1'])
print(dicprueba['cla1'][1])
print(dicprueba['cla2'][1].upper()) # Devuelve el valor de la clave "cla2" en mayúsculas

dicprueba['cla1'][1]="X"
print(dicprueba) # Devuelve el diccionario completo
# Tambien puedo añadir nuevas claves y varlores al diccionario
dicprueba['cla4'] = "Hola"
print(dicprueba.keys())
print(dicprueba.values())
print(dicprueba.items()) # Devuelve una lista de tuplas con las claves y valores del diccionario

# Ejercicio de codificación 43. Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna.
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista

mi_dic = {'nombre':"Karen",'apellido':"Jurgens",'edad':35,'ocupacion':"Periodista"}


# Ejercicio de codificación 43. Diccionarios 2

#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en 
# esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

# Ejercicio de codificación 44. Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['pais']="Colombia"

mi_dic['ocupacion']="Editora"
mi_dic['edad']=36

#Video 33. Tuplas
# Una tupla es una colección de elementos inmutables
# Se definen con ()
# Se accede a los elementos mediante índices
mi_tupla = (1, 2, 3, 4, 5)
print(type(mi_tupla)) # Devuelve el tipo de dato de la tupla
print(mi_tupla) # Devuelve la tupla completa
print(mi_tupla[0]) # Devuelve el primer elemento de la tupla
print(mi_tupla[1:3]) # Devuelve los elementos de la posición 1 a la 3, sin incluir la 3
print(mi_tupla[1:]) # Devuelve los elementos de la posición 1 hasta el final
print(mi_tupla[:3]) # Devuelve los elementos desde el principio hasta la posición 3, sin incluir la 3
print(mi_tupla[::2]) # Devuelve los elementos de la tupla de 2 en 2
print(mi_tupla[::-1]) # Devuelve los elementos de la tupla en orden inverso
print(mi_tupla.count(1)) # Devuelve el número de veces que aparece el elemento 1 en la tupla
print(mi_tupla.index(3)) # Devuelve la posición del elemento 3 en la tupla
print(mi_tupla.index(1, 0, 2)) # Devuelve la posición del elemento 1 en la tupla, empezando a buscar desde la posición 0 hasta la 2

mi_tupla2 = (1,2,3,4)
print(type(mi_tupla2)) # Devuelve el tipo de dato de la tupla

tupla_rara = ("hola", 3.14, 5, -8, {"clave1": "valor1", "clave2": "valor2"})
print(type(tupla_rara)) # Devuelve el tipo de dato de la tupla

#Podemos anidar en una tupla
tupla3 = (1,2,(3,4,5),6)
print(tupla3)
print(tupla3[2]) # Devuelve la tupla (3,4,5)
print(tupla3[2][1]) # Devuelve el segundo elemento de la tupla (3,4,5)

print(type(tupla3)) # Devuelve el tipo de dato de la tupla
#Lo convierto a una lista
tupla3 = list(tupla3)
print(tupla3) # Devuelve la lista
print(type(tupla3)) # Devuelve el tipo de dato de la lista

tupla3 = tuple(tupla3)

#Ejercicio de codificación 46. Tuplas 1
#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla,
# y muestra el resultado (integer) en pantalla:

#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))

#Ejercicio de codificación 47. Tuplas 2
#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

#Ejercicio de codificación 48. Tuplas 3.
#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
#mi_tupla = (1, 2, 3, 4)
mi_tupla = (1, 2, 3, 4)
a = mi_tupla[0]
b = mi_tupla[1]
c = mi_tupla[2]
d = mi_tupla[3]

#Video 34. Sets
# Un set es una colección de elementos únicos
# Se definen con {}
# Se accede a los elementos mediante índices
mi_set = {1, 2, 3, 4, 5} #Asi no tengo que decir que es un set
print(type(mi_set)) # Devuelve el tipo de dato del set
print(mi_set) # Devuelve el set completo
print(len(mi_set)) # Devuelve la longitud del set
mi_set2 = {1, 2, 3, 4, 5, 1, 2, 3}
print(mi_set2) # Devuelve el set completo, sin duplicados
set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']) # Devuelve el set completo. Lo defino de esta forma sin llaves curvas
#Se descartan los valores repetidos.
#Son inmutables. No estan ordenados por indices. No se pueden acceder a los elementos por indices. O rganziarlo
#No se les puede incluir listas o diccionarios.

nuevo_set = set([1,2,3,4,5])
print(nuevo_set) # Devuelve el set completo
print(type(nuevo_set)) # Devuelve el tipo de dato del set

otro_set={'z','z1','z2','z3','z4','z5','z6','z7','z8','z9','z10','z11','z12','z13','z14','z15','z16','z17','z18','z19','z20','z','z'}
print(otro_set) # Devuelve el set completo  
print(type(otro_set)) # Devuelve el tipo de dato del set
#sE permite un set con tuplas
mi_set = {('x1','x2','x3'),('y1','y2','y3'),('z1','z2','z3')}   
print(mi_set) # Devuelve el set completo
print(type(mi_set)) # Devuelve el tipo de dato del set

#Puedo pedirle consultas Comprobar si el 2 esta dentro del set
set2 = {1,2,3,4,5}
print(2 in set2) # Devuelve True
print(6 in set2) # Devuelve False

#Unión de sets
set1 = {1,2,3}  
set2 = {3,4,5}
s3 = set1.union(set2) # Devuelve la unión de los sets
print(s3) # Devuelve el set completo
s3.add(6) # Añade el elemento 6 al set
print(s3) # Devuelve el set completo
s3.remove(6) # Elimina el elemento 6 del set. Si no existiera da error
print(s3) # Devuelve el set completo
s3.discard(5) # Elimina el elemento 5 del set. Si no existiera no da error
print(s3) # Devuelve el set completo
s3.pop() # Elimina el primer elemento del set. Es aleatorio
print(s3) # Devuelve el set completo
s3.clear() # Elimina todos los elementos del set
print(s3) # Devuelve el set completo

# Ejercicio de codificación 49. Sets 1
#Une los siguientes sets en uno solo, llamado mi_set_3:
#{1, 2, "tres", "cuatro"}
#{"tres", 4, 5}
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)

# Ejercicio de codificación 50. Sets 2
#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
#sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo) # Devuelve el set completo

#Ejercicio de codificación 51. Sets 3
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

#Video 35. Booleanos
# Un booleano es un tipo de dato que puede ser True o False
# Se definen con True o False
mi_booleano = True
print(type(mi_booleano)) # Devuelve el tipo de dato del booleano
print(mi_booleano) # Devuelve el booleano completo
mi_booleano2 = False

var1 = True
var2 = False
print(var1 and var2) # Devuelve False
print(var1 or var2) # Devuelve True
print(not var1) # Devuelve False
print(not var2) # Devuelve True

numero = 5 >= 2+3
print(type(numero)) # Devuelve el tipo de dato del booleano
print(numero) # Devuelve el booleano completo

#Ejercicio de codificación 52. Prácticas Booleanos 1
#Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba
prueba = 7 < 10

#Ejercicio de codificación 53. Prácticas Booleanos 2
#Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
print(17834/34 > 87*56)

#Ejercicio de codificación 54. Prácticas Booleanas 3
#Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
print(25**0.5 == 5)
