#encoding: UTF-8
#Luis Fernando Figueroa Rendon, A01746139
#Juego Snake, en el cual cada 5 objetos que comas aumenta la velocidad y ganas cuando llegas a 30.

import pygame, sys, time
from pygame.locals import *
from random import randint

ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO= (0,0,0)


def dibujarMenu(ventana, botonJugar, imagenFondo, x, imgSnake):
    ventana.blit(imagenFondo, (x,0))
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(imgSnake.image, imgSnake.rect)

def dibujarVibora(vibora, ventana,):
    for i in range(len(vibora)):
        pygame.draw.rect(ventana, (0, 0, 0, 0), (vibora[i][1] * 20, vibora[i][0] * 20, 20, 20), 5)


def actualizarVibora(vibora, nuevaPos):
    for i in reversed(range(1, len(vibora))):
        vibora[i] = vibora[i - 1]
    vibora[0] = nuevaPos
    return vibora


def dibujarReintentar(ventana, botonReintentar, imagenFondo, x):
    ventana.blit(imagenFondo, (x, 0))
    ventana.blit(botonReintentar.image, botonReintentar.rect)


def dibujarWin(ventana, botonReintentar, imagenFondo, x, imgWin):
    ventana.blit(imagenFondo, (x, 0))
    ventana.blit(imgWin.image, imgWin.rect)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado = "menu"              #jugando, fin...

    #cargar imagenes
    imgBtnJugar = pygame.image.load("button_Jugar.png")
    #Sprite
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO//2 - botonJugar.rect.width//2
    botonJugar.rect.top = ALTO//1.5 - botonJugar.rect.height//4

    imgBtnReintentar = pygame.image.load("button_reintentar.png")
    # Sprite
    botonReintentar = pygame.sprite.Sprite()
    botonReintentar.image = imgBtnReintentar
    botonReintentar.rect = imgBtnReintentar.get_rect()
    botonReintentar.rect.left = ANCHO // 2 - botonReintentar.rect.width // 2
    botonReintentar.rect.top = ALTO // 1.5 - botonReintentar.rect.height // 4


    #Serpiente
    snake= pygame.image.load("Snake.png")
    imgSnake = pygame.sprite.Sprite()
    imgSnake.image = snake
    imgSnake.rect = snake.get_rect()
    imgSnake.rect.left = ANCHO // 2 - imgSnake.rect.width // 2
    imgSnake.rect.top = ALTO // 3 - imgSnake.rect.height // 2

    #Ganaste
    win = pygame.image.load("win.png")
    imgWin = pygame.sprite.Sprite()
    imgWin.image = win
    imgWin.rect = win.get_rect()
    imgWin.rect.left = ANCHO // 2 - imgWin.rect.width // 2
    imgWin.rect.top = ALTO // 3 - imgWin.rect.height // 2

    #Fondo
    imagenFondo = pygame.image.load("FondoPasto1.jpg")
    x = -1

    vibora, limites = [[5, 7], [5, 6], [5, 5]], [5, 7, 5, 5]
    derecha, izquierda, arriba, abajo, rand1, rand2 = True, False, False, False, 10, 10
    R, G, B = 0, 0, 255

    #Tiempos, Contadores
    timerTiempo = 0

    recolectados= 0

    #Musica
    pygame.mixer.init()
    pygame.mixer.music.load("SevenNation.mp3")
    pygame.mixer.music.play(-1)


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:     #El usuario hizo click
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB= botonJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                        #cambiar de ventana
                            estado = "jugando"
                elif estado == "jugando":

                    while estado == "jugando":
                        ventana.fill(BLANCO)
                        ventana.blit(imagenFondo, (x, 0))
                        timerTiempo += 1 /7.5
                        fuente = pygame.font.SysFont("Arial black", 20)
                        tiempo = fuente.render("Tiempo: " + str(("%.2f") % timerTiempo), 1, NEGRO)
                        score = fuente.render("Score: " +  str(("%.2f") % recolectados), 1, NEGRO)
                        ventana.blit(tiempo, (ANCHO - 140, 0))
                        ventana.blit(score, (ANCHO - 800, 0))
                        dibujarVibora(vibora, ventana)
                        pygame.draw.rect(ventana, (R, G, B, 0), (rand1 * 20, rand2 * 20, 20, 20), 7)

                        for events in pygame.event.get():
                            if events.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif events.type == KEYDOWN:
                                if events.key == K_DOWN and arriba == False:
                                    abajo, arriba, derecha, izquierda = True, False, False, False
                                elif events.key == K_UP and abajo == False:
                                    arriba, abajo, derecha, izquierda = True, False, False, False
                                elif events.key == K_RIGHT and izquierda == False:
                                    derecha, arriba, abajo, izquierda = True, False, False, False
                                elif events.key == K_LEFT and derecha == False:
                                    izquierda, arriba, derecha, abajo = True, False, False, False

                        if len(vibora) >= ANCHO and len(vibora)<= 0:
                            estado = "Reintentar"
                        elif len(vibora) >= ALTO and len(vibora)<= 0:
                            estado = "Reintentar"

                        elif vibora[0][0] == rand2 and vibora[0][1] == rand1:
                            vibora.append([0, 0])
                            rand1, rand2, R, G, B = randint(1, 25), randint(1, 25), randint(10, 225), randint(10,225), randint(10, 225)
                            recolectados += 1

                        for i in range(1, len(vibora)):
                            if vibora[0][0] == vibora[i][0] and vibora[0][1] == vibora[i][1]:
                                estado = "Reintentar"


                        if derecha == True:
                            vibora = actualizarVibora(vibora, [vibora[0][0], vibora[0][1] + 1])
                        elif izquierda == True:
                            vibora = actualizarVibora(vibora, [vibora[0][0], vibora[0][1] - 1])
                        elif arriba == True:
                            vibora = actualizarVibora(vibora, [vibora[0][0] - 1, vibora[0][1]])
                        elif abajo == True:
                            vibora = actualizarVibora(vibora, [vibora[0][0] + 1, vibora[0][1]])
                        if recolectados < 5:
                            time.sleep(.1)
                        elif recolectados >= 5 and recolectados <10:
                            time.sleep(.08)
                        elif recolectados >=10 and recolectados <15:
                            time.sleep(.05)
                        elif recolectados >=15 and recolectados <20:
                            time.sleep(.03)
                        elif recolectados >=20 and recolectados <25:
                            time.sleep(.02)
                        elif recolectados >=25 and recolectados <30:
                            time.sleep(.01)
                        elif recolectados==30:
                            estado = "Ganaste"
                        pygame.display.update()

                elif estado == "Reintentar":
                    xb, yb, anchoB, altoB = botonReintentar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # cambiar de ventana
                            estado = "menu"


        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, botonJugar, imagenFondo, x, imgSnake)
        elif estado == "Reintentar":
            dibujarReintentar(ventana, botonReintentar, imagenFondo, x)
        elif estado == "Ganaste":
            dibujarWin(ventana, botonReintentar, imagenFondo, x, imgWin)
        pygame.display.flip()   # Actualiza trazos

        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame






def main():
    dibujar()


main()