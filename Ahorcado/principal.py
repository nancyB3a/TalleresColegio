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

#5 por cada letra de la palabra sorteada dibujo un guión '_' para desplegar
for _ in range(largo_palabra):
    para_mostrar += "_"

#6 hago un ciclo que se repetirá mientras no se acabe el juego
while not fin_del_juego:
    letra_elegida = input("Adivina la palabra. Dime una letra: ").lower()

    #7 la función clear sirve limpiar la pantalla en cada jugada
    os.system("cls")
    
    #8 verifico si se ingresa una letra repetida
    if letra_elegida in para_mostrar:
        print(f"{nombre}: Ya habías adivinado la letra {letra_elegida}")

    #9 verifico si la letra ingresada coincide con alguna de la palabra que debe adivinar
    for posicion in range(largo_palabra):
        letra = palabra_sorteada[posicion]
        if letra == letra_elegida:
            para_mostrar[posicion] = letra
            print("Bien, le achuntaste!")
    print(f"{' '.join(para_mostrar)}")

    #10 verifico si la letra ingresada NO coincide con alguna de la palabra que debe adivinar
    if letra_elegida not in palabra_sorteada:
        print(f"Elegiste {letra_elegida} y NO está en la palabra. Perdiste una vida!!!")
        vidas -= 1
        if vidas == 0:
            fin_del_juego = True
            print(f"{nombre}: La palabra que debías adivinar era {palabra_sorteada}. Perdiste el juego 😵 ")
    
    #11 verifico si ganó
    if not "_" in para_mostrar:
        fin_del_juego = True
        print(f" 😜 {nombre}: {ganador} 😜 ")

    #12 si no ha finalizado imprimo el ahorcado según se va quemando
    if not fin_del_juego:
        print(etapas[vidas])
