#Archivo dónde escribiremos el programa principal
#1 Declarar librerias
import random,os
from monos import etapas, logo, ganador
from palabras import lista_palabras

#2 Imprimo el Logo del Ahorcado
print(logo)

#3 inicializo mis variables
fin_del_juego = False
vidas = len(etapas) - 1
para_mostrar = []

#3.1 saco una palabra al azar desde la lista
palabra_sorteada = random.choice(lista_palabras)
largo_palabra = len(palabra_sorteada)

#4 solicito el nombre del jugador y le doy la bienvenida
nombre=input("Ingresa tu nombre: ")
print()
print("*"*80)
print(f"*                    Hola {nombre.upper()}")
print(f"*       La PALABRA que debes adivinar tiene {largo_palabra} letras...")
print("*                   !!!MUCHA SUERTE!!!!!")
print("*"*80)
print()
