#encoding UTF-8
#Autor: Javier León Alcántara
#Proyecto final Videojuego

import pygame
import time
from random import randint
from pygame import mixer

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (23, 32, 255)
VERDE = (100, 255, 100)
ROJO = (230, 0, 38)


#Propiedades de la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flappy Batman Javier León")
reloj = pygame.time.Clock()


# Imagenes
murcielago = pygame.image.load("batman.png") #Carga la imagen
murcielago = pygame.transform.scale(murcielago,(100,79)) #Ajusta la imagen a los pixeles indicados

imgBotonJugar = pygame.image.load("button_jugar.png")
btnJugar = pygame.sprite.Sprite()     #SPRITE
btnJugar.image = imgBotonJugar
btnJugar.rect = imgBotonJugar.get_rect()
btnJugar.rect.left = ANCHO//2- btnJugar.rect.width//2
btnJugar.rect.top = ALTO//2- btnJugar.rect.height//2

#Musica de fondo
mixer.init()
mixer.music.load("Aliaksei_Yukhnevich_-_Epic_Action_Trailer.mp3")
mixer.music.play(-1)

#Efecto sonido
efecto = pygame.mixer.Sound("choque.wav")

#Medidas murcielago
anchoMurcielago = 100
altoMurcielago = 79


# Funcion para la barra de estado
def puntuacion(contador, level):
    textoPequeño = pygame.font.Font("freesansbold.ttf", 20)  #Parametros para el texto pequeño
    estado = "Puntos: " + str(contador) + "   Nivel:" + str(level)   #estado
    textoPeVentana, textoPePosicion = escribirTexto(estado, textoPequeño, BLANCO)  #Esta listo el texto
    textoPePosicion.center = ANCHO/7, ALTO-20  #Posicion en la pantalla

    ventana.blit(textoPeVentana, textoPePosicion) #Muestra en pantalla


# Funcion para dibujar los obstaculos
def obstaculos(x_torre, y_torre, anchoTorre, altoTorre, distanciaTorres, color):
    pygame.draw.rect(ventana, color, [x_torre, y_torre, anchoTorre, altoTorre])
    pygame.draw.rect(ventana, color, [x_torre, y_torre + altoTorre + distanciaTorres, anchoTorre, ALTO - distanciaTorres - altoTorre])

    # Dibuja las puntas de las torres
    pygame.draw.rect(ventana, AZUL, [x_torre - 5, altoTorre - 10, anchoTorre + 10, 30])
    pygame.draw.rect(ventana, AZUL, [x_torre - 5, y_torre + altoTorre + distanciaTorres, anchoTorre + 10, 30])


# Funcion para reiniciar
def reiniciar():
    for evento in pygame.event.get([pygame.KEYDOWN,pygame.K_SPACE,pygame.MOUSEBUTTONDOWN ,pygame.QUIT]):
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        else:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb,yb,anchoB,altoB = btnJugar.rect
                if xm>=xb and xm<=xb+anchoB:
                    if ym>=yb and ym<=yb+altoB:

                        return evento.type


    return None


# Funcion para el texto
def escribirTexto(texto, fuente, color):
    textoVentana = fuente.render(texto, True, color)
    return textoVentana, textoVentana.get_rect()


# Función para mostrar todos los mensajes
def mensaje(texto):

    textoPequeño = pygame.font.Font("freesansbold.ttf", 20)
    textoGrande = pygame.font.Font("freesansbold.ttf", 50)

    textoVentana, textoPosicion = escribirTexto(texto, textoGrande, ROJO)
    textoPosicion.center = ANCHO / 2, ALTO / 2   #Posicion del texto

    ventana.blit(textoVentana, textoPosicion)

    #textoPeVentana, textoPePosicion = escribirTexto("Presiona espacio para continuar", textoGrande, BLANCO)
    #textoPePosicion.center = ANCHO / 2, ((ALTO / 2) + 100)

    # Lee el mejor puntaje
    mejorPuntaje = open("score.txt", 'r')
    mejor_Puntaje = mejorPuntaje.readline()
    mejorPuntaje.close()
    lista = []
    for i in range(1):
        lista.append(mejor_Puntaje)

    mejorPunVentana, mejorPunPosicion = escribirTexto("Mejor Puntaje: " + mejor_Puntaje, textoPequeño, BLANCO)
    mejorPunPosicion.center = ANCHO / 2, 500

    #ventana.blit(textoPeVentana, textoPePosicion)
    ventana.blit(mejorPunVentana, mejorPunPosicion)
    btnJugar.rect.center = (ANCHO / 2, 400)
    ventana.blit(btnJugar.image, btnJugar.rect)


    # Actualiza la pantalla
    pygame.display.update()
    time.sleep(0.1)

    # Si el usuario presiona el boton reinicia
    while reiniciar() == None:
        reloj.tick(50)
    dibujar()


# Funcion para GameOver
def gameOver(puntajeFinal):
    # Lee el mejor puntaje
    mejorPuntaje = open("score.txt", 'r')
    high_score = mejorPuntaje.read()
    mejorPuntaje.close()
    # Si no tiene ningun puntaje escribe el ultimo
    if high_score == "" or (int(high_score) < int(puntajeFinal)):
        escribirPuntaje = open("score.txt", "w")
        escribirPuntaje.write(str(puntajeFinal))
        escribirPuntaje.close()


    efecto.play()
    mensaje("Game Over")


# Función para comenzar el juego
def gameStart():
    # Lee el archivo
    try:
        mejorPuntaje = open("score.txt", 'r')
        mejor_Puntaje = mejorPuntaje.read()
        mejorPuntaje.close()
    except:
        escribirPuntaje = open("score.txt", "w")
        escribirPuntaje.write(str(0))
        escribirPuntaje.close()

    # Muestra el mensaje para comenzar
    mensaje("Flecha arriba para volar")


# funcion para mostrar al murcielago
def imagen(x, y, murcielago):
    ventana.blit(murcielago, (x, y))


def dibujar():

    # posiciones del murcielago
    x = 200
    y = 150
    # velocidad de movimiento del murcielago
    y_move = 4

    # Posiciones de las torres
    x_torre = ANCHO
    y_torre = 0
    anchoTorre = 80
    # Determina el alto de la torre
    altoTorre1 = randint(100, int(ALTO / 1.5) - 100)

    # parametros iniciales
    puntaje = 0
    i = 1
    nivel = 1

    # distancia entre las torres
    distanciaTorres = int(altoMurcielago * 4)
    # movimiento de las torres
    movimientoTorre = 4

    termina = False #Bandera para saber si termina la ejecución

    #Fondo
    fondo = pygame.image.load("Fondo.jpg")  # Carga el fondo
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  # Ajusta la imagen del fondo a la pantalla
    x_fondo = 0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                reiniciar()

            # Controles
            if evento.type == pygame.KEYDOWN:  #si la flecha arriba es presionada mueve al murcielago hacia arriba
                if evento.key == pygame.K_UP:
                    y_move = -4

            if evento.type == pygame.KEYUP:  #si la flecha abajo es presionada mueve al murcielago hacia abajo
                if evento.key == pygame.K_UP:
                    y_move = 4

        # actualiza la y del murcielago
        y += y_move

        # fondo
        ventana.fill(BLANCO)
        ventana.blit(fondo, (x_fondo, 0))
        ventana.blit(fondo, (ANCHO + x_fondo, 0))
        x_fondo -= 1
        if x_fondo <= -ANCHO:
            x_fondo = 0

        # murcielago
        imagen(x, y, murcielago)

        # dibuja las torres
        obstaculos(x_torre, y_torre, anchoTorre, altoTorre1, distanciaTorres, VERDE)
        # actualiza la x de las torres
        x_torre -= movimientoTorre

        # carga el puntaje en la ventana
        puntuacion(puntaje, nivel)

        # Si el murcielago toca arriba o abajo pierde
        if y > ALTO - altoMurcielago or y < 0:

            gameOver(puntaje)

        # Hace nuevas torres
        if x_torre < (-1 * anchoTorre):
            x_torre = ANCHO
            altoTorre1 = randint(0, int(ALTO / 1.5))

        # Colisiones

        # Si el murcielago esta debajo de la region de la torre superior
        if x + anchoMurcielago > x_torre:
            if x < x_torre + anchoTorre: #Esta dentro de la region

                if y < altoTorre1 + 15:  # Si cruza el limite superior
                    if x - anchoMurcielago < anchoTorre + x_torre: # Si choca

                        gameOver(puntaje) #Termina

        # Si el murcielago esta encima de la region de la torre inferior
        if x + anchoMurcielago > x_torre:
            if y + altoMurcielago -5 > altoTorre1 + distanciaTorres:
                if x < x_torre + anchoTorre:


                    gameOver(puntaje)  #Termina

        # Puntaje
        if x < x_torre + 40 and x > x_torre - movimientoTorre + i * 20:
            puntaje += 1

        # Dificultad
        # Incrementa la velocidad y la distancia entre las torres
        if 20 <= puntaje < 40:
            movimientoTorre = 8
            if x_torre < (-.99 * anchoTorre):
                distanciaTorres = int(altoMurcielago * 3)
                nivel = "2"

        if 40 <= puntaje < 60:
            movimientoTorre = 10
            if x_torre < (-.99 * anchoTorre):
                distanciaTorres = int(altoMurcielago * 2.5)
                nivel = "3"

        if 60 <= puntaje < 100:
            movimientoTorre = 11
            if x_torre < (-.99 * anchoTorre):
                distanciaTorres = int(altoMurcielago * 2)
                nivel = "4"

        if puntaje > 100:
            movimientoTorre = 12
            nivel = "5"

        pygame.display.update()  #Actualiza la pantalla
        reloj.tick(100)  #Con menos de 60 fps va muy lento


def main():  #Funcion main
    pygame.init() #Inicializa pygame
    gameStart() #Primera pantalla
    dibujar() # Logica
    pygame.quit()
    quit()


main()  #Llama funcion main