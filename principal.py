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
