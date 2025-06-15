#Sección 6. Leer / escribir ficheros.
#path, directorios, archivos y funciones

#Video 77. Abrir y Manipular ficheros.
import os
print(os.getcwd())


mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')
#He tenido que poner en referencia de directorio porque daba fallo . Tal vez por ejecutar en servidor.
#Cuidado con las barras que se usa. Usar doble barra o barra /

print(mi_archivo.read()) #Leo el archivo e imprimo por pantalla
#recomendacion cerrar siempre el fichero tras leerlo.
mi_archivo.close()

mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')
linea = mi_archivo.readline()
print(linea) #imprimimos linea 1

linea = mi_archivo.readline()
print(linea) #imprimimos linea 2

linea = mi_archivo.readline()
print(linea) #imprimimos linea 3
#vemos que en esta forma cada linea tiene su propio salto de linea así como el de print.
#para evitar el salto de linea automatico
print(linea.rstrip())

print(linea.rstrip().upper()) #Y lo pasamos todo a mayus

mi_archivo.close()
mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')
for l in mi_archivo:
    print("aqui dice: " + l)
    
    
    
mi_archivo.close()
mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')
#Otra forma de sacar las lineas en una lista.
todas = mi_archivo.readlines() #carga todo el fichero. Ojo en ficheros muy grandes
print(todas)

#Ejercicio de codificacion 109. abrir y manipular ficheros 1
#Abre el archivo texto.txt e imprime su contenido.
#Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')

for l in mi_archivo:
    print(l.rstrip())

mi_archivo.close()

#Ejercicio de codificacion 109. abrir y manipular ficheros 2
#Imprime la primera línea del archivo texto.txt
#No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
#Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

mi_texto = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')

linea = mi_texto.readline()

print(linea)
mi_texto.close()


#Ejercicio de codificacion 109. abrir y manipular ficheros 3
#Abre el archivo texto.txt e imprime únicamente la segunda línea.
mi_texto = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt')

texto = mi_texto.readlines()
print(texto[1])

mi_texto.close()


#Viode 78. Crear y escribir ficheros.

mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba.txt','r') #Por defecto, solo lectura
mi_archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba2.txt','w') #Solo escritura al principio / crea fichero. Reemplaza todo
mi_archivo = open('archivo.txt','a') #Solo escritura al final del archivo

archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba2.txt','a')

archivo.write('soy el nuevo texto\n')
archivo.write('hola\n')
archivo.write('mundo')
archivo.write('''Hola mundo
              aqui estoy poniendo
              varias lineas
              seguidas.
              adios.     
                       
              ''')
archivo.writelines(['hola','mundo','y','adios','en','lista','\n'])
#Mejor un loop for poniendo salto de linea entre palabras.
listado = ['hola','mundo','y','adios','en','lista','bucleada']
for l in listado:
    archivo.write(l)
    archivo.write(' ')
archivo.close()

archivo = open('E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/Prueba2.txt','a')

#Ejercicio de codificacion 109. crear y escribir ficheros 1
#Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
fichero = open('mi_archivo.txt','w')
fichero.write('Nuevo texto')
fichero.close()

fichero = open('mi_archivo.txt','r')
linea = fichero.readline()
print(linea)
'''
#Ejercicio de codificacion 109. crear y escribir ficheros 2
#Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
nuevo_texto = "Nuevo inicio de sesión"

fichero = open('mi_archivo.txt','a')
fichero.write(nuevo_texto)
fichero.close()

fichero = open('mi_archivo.txt','r')
for l in fichero:
    print(l.rstrip())
'''


#Ejercicio de codificacion 109. crear y escribir ficheros 3
'''
Utiliza el método writelines para escribir los valores de la siguiente lista al final del 
archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás 
cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
'''
'''
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt','a')

for p in registro_ultima_sesion: 
    archivo.writelines(p + "\t")


archivo.close()
archivo = open('registro.txt','r')

for l in archivo:
    print(l.rstrip())
'''

#Video 79. Directorios
#En window tenemos que usar para las barras "//"
#En mac usamops "/"
#Pero he visto que en window tambien podemos  usar "/"

import os #importamos modulo del sistema

ruta = os.getcwd() #Coger directorio de trabajo actual
print(ruta)

ruta2 = os.chdir("E:\\1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio") #Efectivamente puedo usar ambos metodos
print(ruta2)
archivo_subdirectorio = open("otro_archivo.txt",'w')
print(archivo_subdirectorio)

archivo_subdirectorio.write('soy el nuevo texto en un fichero que esta en otro directorio\n')
archivo_subdirectorio.write('hola\n')
archivo_subdirectorio.write('mundo')
archivo_subdirectorio.write('''Hola mundo
              aqui estoy poniendo
              varias lineas
              seguidas.
              adios.     
                       
              ''')

archivo_subdirectorio.close()

archivo_subdirectorio = open("otro_archivo.txt",'r')
print(archivo_subdirectorio.read())

archivo_subdirectorio.close()

#makedirs para  crear directorios
ruta3 = os.makedirs("E:\\1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio/nuevo")
#Si lo lanzo más de una vez da error.

#Metodos basename y dirname para obtener los nombres por seaprado

ruta4 = "E:\\1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio/prueba.txt"

elemento = os.path.basename(ruta4) #damne el nombre de base de ruta4
print(elemento)
dirname = os.path.dirname(ruta4)
print(dirname)

elementos_split = os.path.split(ruta4)
print(elementos_split)

#Tambien puedo eliminar carpetas
#voy a borrar al carpeta "nuevo"
os.rmdir("E:\\1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio/nuevo")

otro_archivo = open("E:\\1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio/Otro_alternativo.txt")
print(otro_archivo.read())
#Fijate que no reconoce bien las tildes y simbolos extraños. ¿Como se abre con el formato correcto?


from pathlib import Path
#aqui vamos a importar objetos de gestión de path
carpeta = Path("E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio")
archivo_con_path = carpeta / "mi_archivo_con_path.txt"

mi_archivo_con_path = open(archivo_con_path)
print(mi_archivo_con_path.read())

#Video 80. Modulo Pathlib
from pathlib import Path

carpeta = Path("E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones/subdirectorio/mi_archivo_con_path.txt")
print(carpeta.read_text())

print(carpeta.name) #Devuelve el nombre del fichero

print(carpeta.suffix) #devuelve la terminación extensión de fichero

print(carpeta.stem) #Devuelve el nombre sin la terminación

if not (carpeta.exists()):
    print("El fichero no existe. ")
else:
    print("El fichero existe")
    
from pathlib import PureWindowsPath #Rutas puras de window

ruta_window_pura = PureWindowsPath(carpeta)

print(ruta_window_pura)


#Video 81. Path
#Util para crear o mover archivos
#enumerar archivos
#crear rutas basadas en strings

from pathlib import Path
mi_ruta = Path('Europa','España','Barcelona','Sagrada_Familia,.txt')
print(mi_ruta)

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)

print(guia.parent)
print(guia.parent.parent)

#Cambio la ruta a la de otra unidad
#Cambiar la ruta de home a otra unidad (por ejemplo, E:)
# Puedes crear un Path apuntando directamente a la ruta deseada
nueva_base = Path("E:/1_Estudio_Programacion/Udemy_Python_Total/Seccion_6_Abrir-ficheros_directorios_path_archivos_funciones")
print(nueva_base)

guia_secreta = Path(nueva_base, "Europa")
#Path es iterable

for txt in Path(guia_secreta).glob("*.txt"):
    print(txt)

for txt in Path(guia_secreta).glob("**/*.txt"):
    print(txt)
    
guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
    
#Ejercicio de codificación 115 Practica Path 1
'''
Práctica Path 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()
'''
from pathlib import Path
ruta_base = Path.home()

#Ejercicio de codificación 116 Practica Path 2
'''
 Práctica Path 2
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
'''
from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")


 #Ejercicio de codificación 117 Practica Path 3
'''
 Práctica Path 3
Implementa y crea una ruta absoluta que nos permita llegar al archivo
"practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar
Path, y de concatenar el objeto Path que refiere a la carpeta base del
usuario.
 '''
from pathlib import Path
ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py") 

#Video 82. Limpiar la Consola

#LImpiamos al consola. 
# Importamos funcion

from os import system
system('cls') #Este argumento depende del sistema operativo 
#cls para window y 
# clear para otro

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
system('cls')
print(f"Tu nombre es: {nombre}, y tu edad es: {edad} años")


#Video 83. Archivos y funciones 
# Podemos meter a una funcion ficheros y rutas

#Ejercicio de codificación 118 Practica Archivos y Funciones 1

'''
Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() 
que abra (open) un archivo indicado como
parámetro, y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    fichero = open(archivo)
    return fichero.readline()

#Ejercicio de codificación 118 Practica Archivos y Funciones 2
'''
Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo
indicado como parámetro, y sobrescriba cualquier contenido anterior 
por el texto "contenido eliminado"
'''

def sobrescribir(fichero):
    archivo = open(fichero,'w')
    return archivo.write('contenido eliminado')

#Ejercicio de codificación 118 Practica Archivos y Funciones 3
'''
Crea una función llamada registro_error() que abra (open) un archivo 
indicado como parámetro, y lo actualice añadiendo una línea al final 
que indique "se ha registrado un error de ejecución". Finalmente, debe 
cerrar el archivo abierto.
'''

def registro_error(fichero):
    archivo = open(fichero, 'a')
    archivo.writelines("se ha registrado un error de ejecución")
    return archivo.close()

#Aqui empieza el proyecto de la sección 6. Un directorio de recetas

