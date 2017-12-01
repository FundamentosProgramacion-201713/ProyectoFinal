# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Juego SpaceInvaders - ProyectoFinal Fundamentos de Programación

import pygame
# Movimiento del mouse
from pygame.locals import *

from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
NEGRO = (0, 0, 0)
VERDEINTENSO = (47, 255, 19)


def dibujarMenu(ventana, boton):
    ventana.blit(boton.image, boton.rect)


# DibujarFondo
def dibujarFondo(ventana, imagenFondoINICIO):
    ventana.blit(imagenFondoINICIO, (0, 0))


def dibujarJuego(ventana, listaEnemigos, listaBalas):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas, listaEnemigos):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue

        borrarBala = False

        for k in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[k]

            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala = True
                break

        if borrarBala:
            listaBalas.remove(bala)


def generarEnemigos(listaEnemigos, imgEnemigo):
    for x in range(8):
        for y in range(3):
            # Generar el enemigo en x, y
            cx = 50 + x * 100
            cy = 50 + y * 120
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = (cx - enemigo.rect.width // 2)
            # Enemigos aparecen arriba de la mitad de la pantalla
            enemigo.rect.top = (cy - enemigo.rect.height // 2) // 2
            listaEnemigos.append(enemigo)


def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    cx = randint(0, ANCHO)
    cy = randint(0, ALTO)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    enemigo.rect.left = cx - enemigo.rect.width // 2
    # Enemigos aparecen arriba de la mitad de la pantalla
    enemigo.rect.top = (cy - enemigo.rect.height // 2) // 2
    listaEnemigos.append(enemigo)
    return cx


def actualizarSCORE(listaBalas, listaEnemigos, SCORE):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            SCORE = SCORE - 5

        for k in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                SCORE = SCORE + 10

    return SCORE


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo

    # Nombre de la pantalla del Juego
    pygame.display.set_caption("SpaceInvaders.2017 - Por: Carlos Pano Hernández")

    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    estado = "menu"  # Agregar jugando, fin, etc.

    # Carga de Fondos
    imagenFondoINICIO = pygame.image.load("FondoJuego.png")
    fondoMovimiento = pygame.image.load("Fondo estrellas LARGO.png")
    y = 0
    imagenFondoFINPERDER = pygame.image.load("FondoJuegoFINPERDER.png")
    imagenFondoFINGANAR = pygame.image.load("FondoJuegoGANAR.png")
    imagenFondoFINInvasion = pygame.image.load("FondoJuegoFINInvasion.png")
    imagenFondoAcerca = pygame.image.load("FondoJuegoAcerca.png")
    imagenFondoPuntajes = pygame.image.load("FondoPuntajes.png")

    # Cargar imagen/Sprite = ButonJugar
    imgBtnJugar = pygame.image.load("button_Jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2 + 50

    # Cargar imagen/Sprite = ButonSALIR
    imgBtnSalir = pygame.image.load("Salir.png")
    botonSalir = pygame.sprite.Sprite()
    botonSalir.image = imgBtnSalir
    botonSalir.rect = imgBtnSalir.get_rect()
    botonSalir.rect.left = ANCHO // 2 - botonSalir.rect.width // 2 - 300
    botonSalir.rect.top = ALTO // 2 - botonSalir.rect.height // 2 + 287

    # Cargar imagen/Sprite = ButonPuntajes
    imgBtnPuntajes = pygame.image.load("button_mejores-puntajes.png")
    botonPuntajes = pygame.sprite.Sprite()
    botonPuntajes.image = imgBtnPuntajes
    botonPuntajes.rect = imgBtnPuntajes.get_rect()
    botonPuntajes.rect.left = ANCHO // 2 - botonPuntajes.rect.width // 2 - 250
    botonPuntajes.rect.top = ALTO // 2 - botonPuntajes.rect.height // 2 + 150

    # Cargar imagen/Sprite = Acerca de
    imgBtAcerca = pygame.image.load("button_acerca-de.png")
    botonAcerca = pygame.sprite.Sprite()
    botonAcerca.image = imgBtAcerca
    botonAcerca.rect = imgBtAcerca.get_rect()
    botonAcerca.rect.left = ANCHO // 2 - botonAcerca.rect.width // 2 + 250
    botonAcerca.rect.top = ALTO // 2 - botonAcerca.rect.height // 2 + 150

    # Cargar imagen/Sprite = Menú
    imgBtPrincipal = pygame.image.load("button_menu-principal.png")
    botonPrincipal = pygame.sprite.Sprite()
    botonPrincipal.image = imgBtPrincipal
    botonPrincipal.rect = imgBtPrincipal.get_rect()
    botonPrincipal.rect.left = ANCHO // 2 - botonPrincipal.rect.width // 2 - 300
    botonPrincipal.rect.top = ALTO // 2 - botonPrincipal.rect.height // 2 + 278

    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Invader 1.png")
    imgEnemigo2 = pygame.image.load("Invader 2.png")
    imgEnemigo3 = pygame.image.load("Invader 3.png")

    generarEnemigos(listaEnemigos, imgEnemigo)
    generarEnemigos(listaEnemigos, imgEnemigo2)
    generarEnemigos(listaEnemigos, imgEnemigo3, )

    # Nave
    imgNave = pygame.image.load("Nave.png")
    xNave = 0

    # Balas
    listaBalas = []
    imgBala = pygame.image.load("Bala.png")

    timerInvader2 = 0
    timerInvader3 = 0
    timerTIEMPO = 0

    # Puntos

    listaPuntajes = []
    puntajes = open("Puntajes.txt")
    puntajes2 = puntajes.readlines()

    for linea in puntajes2:
        listaPuntajes.append(linea)

    puntajeMax = max(listaPuntajes)

    SCORE = 0

    pygame.mixer.init()
    pygame.mixer.music.load("Space Invaders.mp3")
    pygame.mixer.music.play(-1)

    efecto = pygame.mixer.Sound("Shoot.wav")
    efecto2 = pygame.mixer.Sound("button.wav")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Mouse en los diferentes estados...
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click
                # Posición del mouse
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    # Posición del botón
                    xb, yb, anchoB, altoB = botonJugar.rect
                    xbA, ybA, anchoBA, altoBA = botonAcerca.rect
                    xbP, ybP, anchoBP, altoBP = botonPuntajes.rect
                    xbS, ybS, anchoBS, altoBS = botonPuntajes.rect

                    if xm > xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana/estado
                            timerTIEMPO = 0
                            efecto2.play()
                            estado = "jugando"

                    if xm > xbA and xm <= xbA + anchoBA:
                        if ym >= ybA and ym <= ybA + altoBA:
                            # Cambiar de ventana/estado
                            efecto2.play()
                            estado = "Acerca"

                    if xm > xbP and xm <= xbP + anchoBP:
                        if ym >= ybP and ym <= ybP + altoBP:
                            # Cambiar de ventana/estado
                            efecto2.play()
                            estado = "Puntajes"

                if estado == "Fin" or "Acerca":
                    xb, yb, anchoB, altoB = botonPrincipal.rect
                    if xm > xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana/estado
                            efecto2.play()
                            estado = "menu"

                # Ventana jugando, dibujar enemigos

                elif estado == "jugando":
                    enemigo = pygame.sprite.Sprite()
                    enemigo.image = imgEnemigo
                    enemigo.rect = imgEnemigo.get_rect()
                    enemigo.rect.left = xm - enemigo.rect.width // 2
                    enemigo.rect.top = ym - enemigo.rect.height // 2
                    listaEnemigos.append(enemigo)

                    if xm > xbS and xm <= xbS + anchoBS:
                        if ym >= ybS and ym <= ybS + altoBS:
                            # Cambiar de ventana/estado
                            estado = "menu"

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    efecto.play()
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = xNave + 18
                    bala.rect.top = ALTO - bala.rect.height - 50
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Generar enemigos cada 2 segundos
        timerInvader2 += 1 / 40
        timerInvader3 += 1 / 40
        timerTIEMPO += 1 / 40

        if timerInvader2 >= 2:
            generarEnemigoAzar(listaEnemigos, imgEnemigo)
            timerInvader2 = 0

        if timerInvader3 >= 5:
            generarEnemigoAzar(listaEnemigos, imgEnemigo2)
            timerInvader3 = 0

        if estado == "menu":
            dibujarFondo(ventana, imagenFondoINICIO)
            dibujarMenu(ventana, botonJugar)
            dibujarMenu(ventana, botonPuntajes)
            dibujarMenu(ventana, botonAcerca)

        elif estado == "jugando":

            # DibujarFondoConAnimacion
            ventana.blit(fondoMovimiento, (0, y))
            ventana.blit(fondoMovimiento, (0, ALTO + y))
            y -= 1

            if y <= -ALTO:
                y = 0

            # Continuar con Juego
            dibujarJuego(ventana, listaEnemigos, listaBalas)
            actualizarBalas(listaBalas, listaEnemigos)
            SCORE = actualizarSCORE(listaBalas, listaEnemigos, SCORE)

            xEnemigos = 0

            if timerInvader2 >= 1.5:
                for a in range(0, len(listaEnemigos), 1):
                    listaEnemigos[a].rect.top = listaEnemigos[a].rect.top + 3.5
                    coordenada = listaEnemigos[a].rect.top

                    if coordenada >= ALTO:
                        estado = "FinInvasion"

            if len(listaEnemigos) < 30 or timerTIEMPO >= 5:
                for a in range(0, len(listaEnemigos) - 1, 1):

                    if listaEnemigos[a].rect.left < ANCHO - listaEnemigos[a].rect.width:
                        listaEnemigos[a].rect.left = listaEnemigos[a].rect.left + xEnemigos
                        xEnemigos = xEnemigos + 1


                    elif listaEnemigos[a].rect.left >= ANCHO - listaEnemigos[a].rect.width:
                        listaEnemigos[a].rect.left = listaEnemigos[a].rect.left - ANCHO + listaEnemigos[a].rect.width
                        xEnemigos = xEnemigos + 1

            # Nave
            ventana.blit(imgNave, (xNave, ALTO - 75))
            xNave, yNave = pygame.mouse.get_pos()

            # Barra de datos
            pygame.draw.rect(ventana, NEGRO, (0, ALTO - 25, ANCHO, 200), 0)

            fuente = pygame.font.SysFont("American Typewriter", 20)

            tiempo = fuente.render("Tiempo: " + str(("%.2f") % timerTIEMPO), 1, VERDEINTENSO)
            ventana.blit(tiempo, (ANCHO - 140, ALTO - 25))

            TSCORE = fuente.render("SCORE: " + str(SCORE) + " |", 1, VERDEINTENSO)
            ventana.blit(TSCORE, (ANCHO - 275, ALTO - 25))

            Cenemigos = fuente.render("Cantidad de Enemigos: " + str(len(listaEnemigos)) + " |", 1,
                                      VERDEINTENSO)

            dibujarMenu(ventana, botonSalir)

            ventana.blit(Cenemigos, (ANCHO - 550, ALTO - 25))

            if (len(listaEnemigos) == 0):
                estado = "Ganar"
                # Saca archivo nuevo con puntaje nuevo
                salida = open("Puntajes.txt", "a+", encoding="UTF-8")
                salida.write(str(SCORE) + '\n')

            if timerTIEMPO >= 20:
                estado = "Fin"


        elif estado == "Fin":
            dibujarFondo(ventana, imagenFondoFINPERDER)
            dibujarMenu(ventana, botonPrincipal)

        elif estado == "FinInvasion":
            dibujarFondo(ventana, imagenFondoFINInvasion)
            dibujarMenu(ventana, botonPrincipal)

        elif estado == "Ganar":
            dibujarFondo(ventana, imagenFondoFINGANAR)
            dibujarMenu(ventana, botonPrincipal)

            fuente = pygame.font.SysFont("American Typewriter", 30)
            SCOREFINAL = fuente.render("Tu puntuación fue de: " + str(("%s") % SCORE), 1, BLANCO)
            ventana.blit(SCOREFINAL, (ANCHO - 425, ALTO - 200))

        elif estado == "Acerca":
            dibujarFondo(ventana, imagenFondoAcerca)
            dibujarMenu(ventana, botonPrincipal)

        elif estado == "Puntajes":
            dibujarFondo(ventana, imagenFondoPuntajes)

            fuente = pygame.font.SysFont("American Typewriter", 20)
            listaPuntajesFinal = fuente.render(puntajeMax, 1, BLANCO)
            ventana.blit(listaPuntajesFinal, (ANCHO // 2 - 30, ALTO // 2 + 10))

            dibujarMenu(ventana, botonPrincipal)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


# Función main
def main():
    dibujar()
main()
