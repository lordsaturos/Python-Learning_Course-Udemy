#Este es el proyecto del dia 4

#SAbemos utilizar operadores de comparacion.
#Operadores logicos
#control de flujo
#loops
#declaraciones

#VAmos a hacer un juego

#El juego pregunta el nombre y luego tendra 8 intentos para adivinar un numero entre 1 y 100.
#Si el numero que dice el usuario es menor a uno o superior a 100, le dira que el numero no es correcto y tiene que volver a decirlo.
#Si el numero es inferior al numero secreto, le dira que es un numero inferior al numero secreto.
#Si el numero es superior al numero secreto, le dira que es un numero superior al numero secreto.
#Si el numero es correcto, le dira que ha ganado y le dira el numero de intentos que ha necesitado para adivinarlo.

from random import randint
secret_num = randint(1,100)
num_intentos = 0
juego_ganado = False
nombre = input("Hola, ¿cual es tu nombre? ")

print("Hola, " + nombre + ", vamos a jugar un  juego. Tienes 8 intentos para adivinar un numero entre 1 y 100.")
input("Presiona enter para continuar...")

while num_intentos < 8:
    input_num = int(input("Introduce un numero entre 1 y 100: "))
    if input_num < 1 or input_num > 100:
        print("El numero no es correcto, por favor introduce un numero entre 1 y 100.")
        continue
    
    if not input_num == secret_num:
        if input_num < secret_num:
            print("El numero es inferior al numero secreto.")
        else:
            print("El numero es superior al numero secreto.")
        num_intentos += 1
    elif input_num == secret_num:
        juego_ganado = True
        num_intentos += 1
        break



if juego_ganado == True:
    print("Felicidades, " + nombre + ", has ganado el juego en " + str(num_intentos) + " intentos.")

else:
    print("Lo siento, " + nombre + ", has perdido el juego. El numero secreto era " + str(secret_num) + ".")
