#Bueno, el tercer día no ha dejado nada.
#Hemos visto muchas cosas y de las buenas.
#Y ha llegado la hora de juntar todo lo aprendido y ponerlo en práctica, creando un programa perfectamente
#funcional desde cero.

#Ahora que ya sabes usar los métodos y las propiedades de los strings, que sabes indexar conjuntos de
#datos como los strings, las listas y los tapes.

#Y sobre todo, ahora que conoces todos los tipos de datos que necesitas para poder almacenar lo que
#sea, vas a poder encontrar una forma de programar un analizador de texto.
#
#La consigna es la siguiente Vas a crear un programa que primero le pida al usuario que ingrese un texto?
#Puede ser un texto cualquiera o un artículo entero, un párrafo, una frase, un poema, lo que quiera.
#Luego el programa le va a pedir al usuario que también ingrese tres letras a su elección y a partir
#de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y lo
#que va a hacer es devolverle al usuario la siguiente información Primero, cuantas veces aparece cada
#una de las letras que eligió?
#
#Para lograr esto te recomiendo almacenar esas letras en una lista y luego usar algún método propio de
#string que nos permita contar cuantas veces aparece un sub string dentro del string.
#Algo que debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas y esto
#va a afectar el resultado.
#
#Pero lo que deberías hacer para asegurarte de que se encuentren absolutamente todas las letras es pasar
#tanto el texto original como las letras a buscar en minúsculas.
#Segundo, le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
#Y para lograr esta parte, recuerda que hay un método de string que permite transformarlo en una lista
#y que luego hay una función que permite averiguar el largo de una lista.

#Tercero, nos va a informar cuál es la primera letra del texto y cuál es la última.
#Aquí claramente echaremos mano de la indexación cuando el sistema nos va a mostrar cómo quedaría el
#texto si invirtiéramos el orden de las palabras.
#Acaso hay algún método que permita invertir el orden de una lista y otro que permita unir esos elementos
#con espacios intermedios?
#Piénsalo.
#
#Y por último, el sistema nos va a decir si la palabra python se encuentra dentro del texto.
#Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista.
#Puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la manera de expresarle
#al usuario tu respuesta.
#Como siempre te digo, no espero que lo sepas hacer al primer intento y es probable, de hecho, que
#a pesar de que ya tienes todas las herramientas que necesitas, aún no puedas figurarte como combinarlas
#para lograr nuestro objetivo de hoy.

#Bueno, no te preocupes, lo único que si te pido, si o si como profesor es que lo intentes, que pongas
#tu cabeza a procesar el problema.
#Luego, si lo logras o no, eso es menos importante de lo que parece.
#
#Porque aunque no lo consigas resolver, si te pasas un buen tiempo pensándolo, cuando veas la forma
#en que lo solucionamos, vas a tener igualmente esa sensación de Eureka y el aprendizaje se va a producir
#igual, te lo prometo.
#
#Pero si pasas a la solución directamente, sin ponerte un buen tiempo a darle las vueltas necesarias,
#el aprendizaje va a ser de mucha menor calidad.
#Entonces vamos, pon buena música y a programar.

#Resumen
#El usuario pide que ingrese un texto, parrafo, string, poema, etc.
#El usuario pide 3 letras a su elección.

#El prorama hace 5 analisis
#1. Cuantas veces aparece cada una de las letras que eligió? Recomendación guarlar las letras en una lista y usar algun metodo de string. para contar substring en un string.
#Tener en cuenta las mayos y minus. Pasar todo el texto a minusculas.

#2Cuantas palabras hay a lo largo del texto. Transformar el string en una lista y usar la funcion len() para averiguar el largo de la lista.

#3Informar cual es la primera y ultima letra del texto. Indexar el string.

#4. Generar el texto al reves. Convertir el string en una lista. Invertir el orden de la lista y volver a generar el string.

#5. Comprobar si la palabra python aparece en el texto. Usar booleanos y un diccionario para expresar la respuesta al usuario.

#Pedimos al usuario que ingrese un texto.
texto = input("Ingrese un texto: ")
print("Texto ingresado: ", texto)

#Ahora pedimos al usuario que ingrese 3 letras. Separadas espacios.
letras = input("Ingrese 3 letras separadas por espacios: ")
print("Letras ingresadas: ", letras)
#Convierto las letras en una lista.
letras_lista = letras.split()
#Convierto las letras a minusculas.
letras_lista = letras_lista[0].lower(), letras_lista[1].lower(), letras_lista[2].lower()
print("Letras en lista: ", letras_lista)

#Converto el texto a minusculas
texto = texto.lower()
#Convierto el texto en una lista.
texto_lista = texto.split()
print("Texto en lista: ", texto_lista)

#Procedemos a hacer el analisis 1.
print("Analisis 1")
print("Letra 1: "+ letras_lista[0] + " aparece: " + str(texto.count(letras_lista[0])) + " veces.")
print("Letra 2: "+ letras_lista[1] + " aparece: " + str(texto.count(letras_lista[1])) + " veces.")
print("Letra 3: "+ letras_lista[2] + " aparece: " + str(texto.count(letras_lista[2])) + " veces.")

#Procedemos a hacer el analisis 2.
print("Analisis 2")
print("El texto tiene: " + str(len(texto_lista)) + " palabras.")    

#Procedemos a hacer el analisis 3
print("Analisis 3")
print("La primera letra del texto es " + texto[0] + " y la última letra es " + texto[-1] + ".")

#Procedemos a hacer el analisis 4
print("Analisis 4")
nuevo_texto = texto_lista[::-1]
print("Texto al reves: " + " ".join(nuevo_texto))

#Procedemos a hacer el analisis 5
print("Analisis 5")
#Creamos un diccionario para guardar el resultado.
resultado = {}
#Buscamos la palabra python en el texto.
if "python" in texto:
    resultado["python"] = True
    print("La palabra python se encuentra en el texto.")
    
else:
    resultado["python"] = False
    print("La palabra python no se encuentra en el texto.")
#Mostramos el resultado.
print("La palabra python se encuentra en el texto: " + str(resultado["python"]))
#Fin del programa.