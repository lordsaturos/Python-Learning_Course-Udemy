#Proyecto del día 5
#Juego del ahorcado

#Proyecto del Día 5
#Y así hemos terminado la parte preparatoria de este 5º día de entrenamiento y ahora vamos
#a poner toda la carne en la parrilla porque se viene un desafío más que especial. Hoy vas a
#programar El Ahorcado. El juego es muy sencillo y popular, pero por si acaso te lo explico
#rápidamente.
#El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
#de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
#deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
#mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
#la palabra oculta, pierde una vida.
#En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo
#del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos
#gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una
#en una, cada vez que el jugador elija una letra incorrecta.
#Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
#completa antes de perder todas las vidas, el jugador gana.
#Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas:
# Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
#para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
#también vas a crear al comienzo.
# Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
#haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
#ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
#palabra o no, para verificar si ha ganado o no, etc.
# Recuerda escribir primero las funciones y luego el código que las implementa
#ordenadamente.
#Creo que este es un proyecto especial y de verdad quiero que sepas que no espero que lo puedas
#resolver sin ayuda. Las funciones parecen simples, pero cuando empezamos a poner funciones
#todas juntas en un código real, es difícil seguir mentalmente la sucesión del código porque se
#vuelve mucho menos lineal que antes. Lo importante es que lo intentes, que tu cabeza se
#zambulla en el problema y luego veremos cómo llegamos a la solución. 
from random import choice

def generar_cadena_oculta(palabra):
    cadena = []
    for letra in palabra:
        cadena.append("_")
    return cadena

def seleccionar_letra():
    letra_seleccionada = input(f"Nuevo turno. Te quedan {vidas} vidas restantes. Seleccione nueva letra: ")
    return letra_seleccionada

def comprobar_letra(letra_seleccionada, palabra_seleccionada, cadena_mostrada, vidas):
    una_letra_acertada = False
    for idx, letter in enumerate(palabra_seleccionada):
        if (letter == letra_seleccionada):
            print("Has acertado una letra.")
            una_letra_acertada = True
            cadena_mostrada[idx] = letter
    if una_letra_acertada == False:
        vidas -= 1    
        print(F"Lo siento, no has acertado ninguna letra. Te quedan ahora {vidas} vidas.")    
    return cadena_mostrada, vidas

def mostrar_cadena_conocida(cadena_conocida):
    print("La información que tenemos actualmente de la palabra es: ")
    print(cadena_conocida)
    
def comprobar_condiciones_victoria(cadena):
    palabra_terminada = 0 #La palabra esta terminada si despues de analizar con un for no detectamos ningun "_"
    for letter in cadena:
        if (letter == "_"):
            palabra_terminada += 1
        
    if (palabra_terminada == 0):
        return False #El juego termina porque ha sido resuelto
    elif (palabra_terminada != 0):
        return True #El juego tiene que continuar
        

vidas = 6
turno = 0
juego_en_proceso = True
palabras = ["cielo", "montaña", "rio", "arbol", "luz", "noche", "fuego", "tierra", "viento", "mar"]
print(palabras)

palabra_seleccionada = choice(palabras)
cadena_mostrada = list(generar_cadena_oculta(palabra_seleccionada))
mostrar_cadena_conocida(cadena_mostrada)

while (juego_en_proceso == True) and (vidas > 0):
    letra = seleccionar_letra()
    cadena_mostrada, vidas = comprobar_letra(letra, palabra_seleccionada, cadena_mostrada, vidas)
    mostrar_cadena_conocida(cadena_mostrada)
    juego_en_proceso = comprobar_condiciones_victoria(cadena_mostrada)
    turno += 1
    
if vidas <= 0:
    print("Lo siento, has fracasado.")
    print(f"La palabra correcta era: {palabra_seleccionada}")
    
if (juego_en_proceso == False) and (vidas > 0):
    print("Felicidades, te has pasado el juego.")
    print(f"Te quedaban vidas {vidas} restantes.")
    print(f"Te ha costado {turno} turnos en total")
    print(f"La palabra correcta era: {palabra_seleccionada}")

