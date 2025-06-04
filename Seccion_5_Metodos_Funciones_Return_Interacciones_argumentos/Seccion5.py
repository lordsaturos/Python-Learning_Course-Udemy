#Video 59. Metodos, ayuda y documentación
dic = {'clave1': 'valor1',
       'clave2': 'valor2',
       'clave3': 'valor3'}

a = dic.popitem()

print(a)  # Imprime el último par clave-valor eliminado del diccionario

#Ejericio de codificación 88. Practica métodos y ayuda 1
#Remueve los caracteres a la izquierda de nuestro texto principal:
#,
#:
#%
#_
##

#Utiliza el método lstrip(). Imprime el resultado en pantalla:
#",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
#Busca en la documentación acerca del funcionamiento del método solicitado para saber
# cómo actúa. Puedes utilizar variables intermedias si las necesitas.

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

for posicion in texto:
    texto = texto.lstrip()
    texto = texto.lstrip(',')
    texto = texto.lstrip(':')
    texto = texto.lstrip('%')
    texto = texto.lstrip('_')
    texto = texto.lstrip('#')
print(texto)

#Ejercicio de codificación 89. Practica Métodos y ayuda 2
#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
#el método insert():
#frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
#Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,'naranja')
print(frutas)  # Imprime la lista de frutas con "naranja" insertado en la posición 2

#Ejercicio de codificación 90. Practica Métodos y ayuda 3
#Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:
#marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
#marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
#Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

#Video 60. Funciones
#En los siguientes videos vamso a aprender las funciones.

#Video 61. Crear Funciones
#Una función empieza con def.
def mi_funcion():
    '''
    Esta es una función de ejemplo que imprime un mensaje en pantalla.
    '''
    print("Hola, esta es mi función")

#Llamamos a la función
mi_funcion()

def saludar_persona():
    '''
    Esta funcion saluda a una persona.
    '''
    print("Hola, ¿cómo estás persona?")
    
#Llamamos a la función
saludar_persona()

def saludar_persona_custom(nombre):
    '''
    Esta funcion saluda a una persona.
    '''
    print(f"Hola, ¿cómo estás {nombre}?")
    
saludar_persona_custom("Juan")

#Ejericio de codificación 91. Crea una función
#Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla 
# "¡Hola mundo!"
#Solo debes definir la función, no debes invocarla luego.
def saludar():
    print("¡Hola mundo!")
    
#Ejericio de codificación 92. Crea una función
#Declara una función llamada bienvenida, que tome como argumento el nombre de una 
# persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

#Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

#Solo debes definir la función y crear la variable, no debes invocar la función luego.
nombre_persona = "Amaia"

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

#Ejercicio de codificación 93. Crea una función
#Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y 
# que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir,
# la potencia 2 del valor).

#El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable 
# y asígnale un número cualquiera.

#Solo debes definir la función y crear la variable, no debes invocar la función luego.
un_numero = 9
def cuadrado(un_numero):
    valor_cuadrado = un_numero**2
    print(f"{valor_cuadrado}")
    
#Video 62. Return
def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(5, 3)

#Ejercicio de codificación 94. Return 1
#Crea una función llamada potencia que tome dos valores numéricos como 
# argumentos. Deberá devolver el número que resulte de resolver una potencia,
# utilizando el primer número como base, y el segundo como exponente:

def potencia (base,exponente):
    return base ** exponente

#Ejercicio de codificacion 95. Return 2
#Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
#Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.
#Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.
dolares = 100

def usd_a_eur(dolares):
    return dolares * 0.9
    
print(usd_a_eur(dolares))

#Ejercicio de codificación 96. Return 3
#Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

#Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

#También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.
#Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

palabra = "Python"
def invertir_palabra(palabra):
    palabra = palabra.upper()
    return palabra[::-1]

print(invertir_palabra(palabra))

#Video Seccion 63. Funciones Dinamicas
#Vamos a juntar en las funciones los loops, condiciona,es for, while, etc..

def check_tres_cifras(lista):
    '''
        Esta función verifica si un número está entre 100 y 1000.
    '''
    lista_resultados = []
    
    for n in lista:
        if n in range(100, 1001):
            lista_resultados.append(n)
            
        else:
            pass
    
    return lista_resultados
    
    
lista = [25, 589, 5567, -45, 10, 666, 349]
resultado = check_tres_cifras(lista)
print(resultado)  # Imprime True si el número está entre 100 y 1000, False en caso contrario

#Ejercicio de codificacion 97. Funciones dinámicas 1
#Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva 
# True si todos los valores de una lista son positivos, y False si al menos uno de los valores es 
# negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

#No invoques la función, solo es necesario definirla.

lista_numeros = [-20, 0, 14, -999, 457, 45, -1]

def todos_positivos(lista):
    valor = True
    for n in lista:
        if n > 0:
            valor = valor and True
        elif n <= 0:
            valor = valor and False
    
    return valor

#Ejercicio de codificacion 98. Funciones dinámicas 2
#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre 
# y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
lista_numeros = [-999, 14, 0, 458, 14, 1000, 1001, -5]

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if (n > 0) and (n < 1000):
            suma = suma + n
    return suma

#Ejercicio de codificación 99. Funciones dinámicas 3
#Crea una función (cantidad_pares) que cuente la cantidad 
# de números pares que existen en una lista (lista_numeros), 
# y devuelva el resultado de dicha cuenta.
lista_numeros = [14, 7, 12, 56, 11, 3, 9]

def cantidad_pares(lista):
    cantidad = 0
    for n in lista:
        if n % 2 == 0:
            cantidad +=1
    return cantidad

#Video 64. Ejemplo de función

precios_productos = [('capuchino', 2.5), ('latte', 3.0), ('espresso', 1.5), ('mocha', 3.5)]

def cafe_mas_caro(precios):
    '''
    Esta función recibe una lista de tuplas con el nombre del café y su precio, 
    y devuelve el nombre del café más caro.
    '''
    max_caro = precios[0][0]
    max_precio = precios[0][1]
    for cafe, precio in precios:
        if precio > max_precio:
            max_caro = cafe
            max_precio = precio
            

    return (max_caro,max_precio)

print(cafe_mas_caro(precios_productos))
cafe, precio = cafe_mas_caro(precios_productos)
print(f"El café más caro es {cafe} con un precio de {precio} euros.")

#Video 65. Interacción entre funciones
#importamos random para mezclar los palitos
from random import shuffle
#Lista inicial

palitos = ['-', '--', '---', '----']

# mezclar palitos
def mezclar_palitos(lista):
    '''
    Esta función recibe una lista de palitos y los mezcla aleatoriamente.
    '''
    shuffle(lista)
    return lista

mezclar_palitos(palitos)

# pedirle al usuario que elija un palito
def probar_suerte(lista):
    '''
    Esta función pide al usuario que elija un palito de la lista y devuelve el palito elegido.
    '''
    intento = ''
    print("Elige un palito de la siguiente lista:")
    while intento not in ['1', '2', '3', '4']:
        intento = input("Eligue un número del 1 al 4: ")

    return int(intento)

probar_suerte(palitos)

# funcion comprobar si el palito es correcto
def check_intento(lista, intento):
    '''
    Esta función comprueba si el palito elegido por el usuario es correcto.
    '''
    
    print(f"Has elegido el palito: {lista[intento -1]}")
    if lista[intento - 1] == '----':
        print("¡Felicidades! Has elegido el palito correcto.")
    else:
        print("Lo siento, has elegido un palito incorrecto. Inténtalo de nuevo.")
    return

check_intento(palitos, probar_suerte(palitos))

#Ejercicio de codificacion 100. Interaccion entre funciones 1
#Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
#La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
#Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
#Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
#Si la suma es menor o igual a 6:
#"La suma de tus dados es {suma_dados}. Lamentable"
#Si la suma es mayor a 6 y menor a 10:
#"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#Si la suma es mayor o igual a 10:
#"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
#Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

from random import randint

def lanzar_dados():
    resultado =  randint(1,6)
    return resultado
    
    
def evaluar_jugada(valor1 = lanzar_dados(), valor2 = lanzar_dados()):
    string = ""
    suma_dados = valor1 + valor2
    if suma_dados <= 6:
        string = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif ((suma_dados) > 6) and ((suma_dados) < 10):
        string = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif ((suma_dados)) >= 10:
        string = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

    return string

dado1 = lanzar_dados()
dado2 = lanzar_dados()

print(f"{evaluar_jugada(dado1, dado2)}")

#Ejercicio de codificacion 101. Interacción entre funciones 2
#Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable 
# lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números
# si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.
#Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
#Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior 
# función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista_numeros_reducir):
    #eliminar duplicados dejando solo 1 si hay duplicados
    lista_numeros_reducir= list(set(lista_numeros_reducir))  # convierte la lista en un set para eliminar duplicados y luego vuelve a convertirla en lista
    lista_numeros_reducir.sort()  # ordena la lista de menor a mayor
    lista_numeros_reducir.pop() # elimina el último elemento de la lista, que es el más alto
    #eliminar el valor más alto
    return lista_numeros_reducir
    
def promedio(lista):
    #calcular promedio de los valores de la lista
    promedio = 0
    promedio = sum(lista)/len(lista) #suma de los valores de la lista y divide por el numero de elementos
    return promedio

print(lista_numeros)
lista_numeros = reducir_lista(lista_numeros)
promedio_lista = promedio(lista_numeros)
print(f"Lista reducida: {lista_numeros}")
print(f"Promedio de la lista reducida: {promedio_lista}")

#Ejercicio de codificación 102. Interacción entre funciones 3
#Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
# Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para 
# funcionar.
#Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el 
# resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera 
# (debes crear una lista con valores y llamarla lista_numeros).
#Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y 
# eliminarla (devolverla como lista vacía []).
#Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista 
# intacta.
#Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

from random import choice

lista_numeros = [4, 6, 14, 101, -14, 0]

def lanzar_moneda():
    resultados_posibles = ['Cara', 'Cruz']
    resultado = choice(resultados_posibles)
    return resultado
    
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruira")
        lista = []
        return lista
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
    
#Video 66. Argumentos indefinidos *args
# *args son argumentos indefinidos que se pueden pasar a una función.
def suma_numero(*num):
    suma = 0
    for n in num:
        suma += n
    return suma

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(3,4,7,11))

#Ejercicio de codificación 103. *args 1
#Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos,
# y que retorne la suma de sus valores al cuadrado.
#Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg**2
    return suma

suma_cuadrados(1,2,3)

#Ejercicio de codificación 104. *args 2
#Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión,
# y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, 
# o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    suma = 0
    for arg in args:
        if arg >= 0:
            suma += arg
        elif arg < 0:
            suma -= arg
    return suma

#Ejercicio de codificación 105. *args 3
#Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a 
# continuación, una cantidad indefinida de números.

#La función debe devolver el siguiente mensaje:

#"{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    
    texto = f"{nombre}, la suma de tus números es {suma_numeros}"
    return texto


#Video 67 Argumentos indefinidos **kwargs
# **kwargs son argumentos indefinidos que se pueden pasar a una función como diccionario.
#Esta muy relacionado con los diccionarios. 'key word args' kwargs

def suma(**kwargs):
    #código para sumar los valores de kwargs
    print(type(kwargs))
    
suma(a=1, b=2, c=3)
#Devuelve un diccionario con las claves y valores que se le pasen como argumentos.

def suma2(**kwargs):
    total = 0
    
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        total += valor
    return total


print(suma2(a=1, b=2, c=3))

def ejemplo(num1, num2, *args, **kwargs):
    print(f'El primer número es: {num1}')
    print(f'El segundo número es: {num2}')
    for arg in args:
        print(f'El argumento adicional es: {arg}')
    print(f'Los argumentos adicionales son: {args}')
    for kwarg in kwargs:
        print(f'El argumento de palabra clave es: {kwarg} con valor {kwargs[kwarg]}')
    print(f'Los argumentos de palabra clave son: {kwargs}')

ejemplo(1, 2, 3, 4, 5, a=6, b=7, c=8)

args =  [100, 250, 450, 750]
kwargs = {'a': 1, 'b': 2, 'c': 3}   

ejemplo(1, 14, *args, **kwargs)

#Ejercicio de codificación 106. **kwargs 1
#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se 
# entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    total = 0
    
    for kwarg in kwargs:
        total += 1
            
    return total

#Ejercicio de codificación 107. **kwargs 2
#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos 
# entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier 
# cantidad de argumentos de este tipo.
def lista_atributos(**kwargs):
    lista = []
    for kwarg in kwargs:
        lista.append(kwargs[kwarg])
    return lista

#Ejercicio de codificación 108. **kwargs 3
#Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

#Características de {nombre}:
#{nombre_argumento}: {valor_argumento}
#{nombre_argumento}: {valor_argumento}
#etc...
#Por ejemplo:

#describir_persona("María", color_ojos="azules", color_pelo="rubio")

#Mostrará en pantalla:

#Características de María:
#color_ojos: azules
#color_pelo: rubio

#Video 68 Problemas prácticos
#Ejercicio 1

#Ahora entramos en el proyecto de la semana 4.
#Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.

#Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
#Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
#Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de 
# valor intermedio

def devolver_distintos(a, b, c):
    sum = 0
    sum = a + b + c
    
    if sum > 15:
        return max(a, b, c)
    elif sum < 10:
        return min(a, b, c)
    else:
        return sorted([a, b, c])[1]  # Devuelve el valor intermedio
    
#Ejercicio 2
#Escribe una función (puedes ponerle cualquier nombre que
#quieras) que reciba cualquier palabra como parámetro, y que
#devuelva todas sus letras únicas (sin repetir) pero en orden
#alfabético.
#Por ejemplo si al invocar esta función pasamos la palabra
#"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
palabra = "entretenido"
def letras_unicas(palabra):
    set_string = set(palabra)
    set_string = sorted(set_string)  # Ordena las letras únicas alfabéticamente
    lista = list(set_string)  # Convierte el set a una lista
    return lista

print(letras_unicas(palabra))

#Ejercicio 3
#Escribe una función que requiera una cantidad indefinida de
#argumentos. Lo que hará esta función es devolver True si en
#algún momento se ha ingresado al numero cero repetido dos
#veces consecutivas.
#Por ejemplo:
#(5,6,1,0,0,9,3,5) >>> True
#(6,0,5,1,0,3,0,1) >>> False

def check_cero_consecutivo(*args):
    flag_cero = False
    for arg in args:
        if arg == 0:
            if flag_cero == True:
                return True
            else:
                flag_cero = True
        else:
            flag_cero  = False
    # Si no se encontró el cero consecutivo, devuelve False        
    
    return False

print(check_cero_consecutivo(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(check_cero_consecutivo(6, 0, 5, 1, 0, 3, 0, 1))  # False

#Ejercicio 4
#Escribe una función llamada contar_primos() que requiera un
#solo argumento numérico.
#Esta función va a mostrar en pantalla
#todos los números
#primos existentes en el rango que va desde cero hasta ese
#número incluido, y va a devolver la cantidad de números
#primos que encontró.
#Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(valor):
    numero_primos = []
    for n in range(2, valor + 1):
        for a in range(2, int(n**0.5) + 1):
            if n % a == 0:
                break
        else:
            #Es primo
            numero_primos.append(n)
    set(numero_primos)  # Elimina duplicados si los hubiera
    numero_primos = list(set(numero_primos))  # Convierte el set a una lista    
    
    print(f"Números primos encontrados: {numero_primos}")
    return len(numero_primos)
    
contar_primos(20)  # Debería imprimir los números primos hasta 20 y devolver su cantidad