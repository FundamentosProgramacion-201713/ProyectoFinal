# encoding: UTF-8
# Autor: Luis Enrique Neri Pérez
# Una carrera de tortugas, ¡prohibido apostar dentro del campus! :)

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarPista(ventana):
    '''
    Dibuja la línea de arranque y la meta
    '''
    pygame.draw.line(ventana, BLANCO, (64, ALTO), (64, 220), 10)
    pygame.draw.line(ventana, BLANCO, (ANCHO-5, ALTO), (ANCHO-5, 220), 10)


def dibujarCorredores(ventana,imagenTortuga, listaX, listaY):
    for indice in range(len(listaX)):
        x = listaX[indice]
        y = listaY[indice]
        ventana.blit(imagenTortuga, (x,y))


def moverCorredor(x):
    '''
    Actualiza la posición del corredor
    '''
    x += randint(0,3)
    return x


def dibujarGana(ventana,titulo):
    '''
    Muestra en la pantalla un mensaje de texto
    '''
    fuente = pygame.font.SysFont("monospace", 48)

    texto = fuente.render("¡Gana la "+titulo+"!", 1, BLANCO)
    ventana.blit(texto, (ANCHO//2-100, ALTO//2))


def dibujar():
    '''
    Simulación de una carrera de tortugas (¡20 tortugas!)
    '''
    # Imagen de fondo
    imagenFondo = pygame.image.load("Laberinto.jpg")
    # Imagen de tortugas
    listaImagenes = ["tortuga2.png","tortuga0.png","tortuga3.png","tortuga1.png","tortuga4.png","tortuga5.png"]

    # Ubica a los competidores
    NUM_TORTUGAS = 5
    listaX = [0,0,0,0,0]
    listaY = []
    delta = (ALTO)//(NUM_TORTUGAS+3)
    for indice in range(NUM_TORTUGAS):
        listaY.append(delta*(indice + 1)+140)

    print(listaY)

    hayGanador = False

    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    contador = 0
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        imagenTortuga = pygame.image.load("Rick2.png")

        contador = contador + 1
        if contador==4:
            contador=contador-4

        # Borrar pantalla
        ventana.blit(imagenFondo,(0,0))

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarPista(ventana)
        dibujarCorredores(ventana,imagenTortuga, listaX, listaY)

        for indice in range(NUM_TORTUGAS):
            if listaX[indice]>=ANCHO-74:
                hayGanador = True
            if not hayGanador:
                listaX[indice] = moverCorredor(listaX[indice])
        '''
        if xLiebre>=ANCHO-74:
            # Gana liebre
            dibujarGana(ventana,"Liebre")
        elif xTortuga>=ANCHO-74:
            dibujarGana(ventana, "Tortuga")
        else:
            xLiebre = moverCorredor(xLiebre)
            xTortuga = moverCorredor(xTortuga)
        '''
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(20)          # 45 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
