#importo librerías importantes
import random
from monos import ganador,perdedor,iguales
#asigno de forma aleatoria un N° entre 1 y 3. Lo ocuparé para la jugada del PC
aleatorio = random.randint(1,3)
turnoPc = ""
print("1).- Piedra")
print("2).- Papel")
print("3).- Tijera")
#guardo la opción ingresada por el usuario
opcion = int(input("Que eliges: "))
#aplico las condicionales para saber qué ingresó el usuario
if opcion == 1:
    turnoJugador = "piedra"
elif opcion == 2:
    turnoJugador = "papel"
elif opcion == 3:
    turnoJugador = "tijera"
print("Tu eliges: ", turnoJugador)
#aplico las condicionales para saber cual es la jugada del PC según lo que resultó en el aleatorio
if aleatorio == 1:
    turnoPc = "piedra"
elif aleatorio == 2:
    turnoPc = "papel"
elif aleatorio == 3:
    turnoPc = "tijera"
print("PC eligió: ", turnoPc)
print("...")
#Resuelvo el CACHIPÚN con las condiciones posibles
if turnoPc == "piedra" and turnoJugador == "papel":
    print(ganador)
    print("Papel envuelve piedra")
elif turnoPc == "papel" and turnoJugador == "tijera":
    print(ganador)
    print("Tijera corta papel")
elif turnoPc == "tijera" and turnoJugador == "piedra":
    print(ganador)
    print("Piedra pisa tijera")
if turnoPc == "papel" and turnoJugador == "piedra":
    print(perdedor)
    print("Papel envuelve piedra")
elif turnoPc == "tijera" and turnoJugador == "papel":
    print(perdedor)
    print("Tijera corta papel")
elif turnoPc == "piedra" and turnoJugador == "tijera":
    print(perdedor)
    print("Piedra pisa tijera")
elif turnoPc == turnoJugador:
    print(iguales)