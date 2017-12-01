# encoding: UTF-8
# Autor: Daniel Sahuer
# Proyecto Final

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)
GRIS = (160,160,160)
NEGRO = (0,0,0)
ROJO = (204,6,5)

def dibujarMenu(ventana,botonJugar,boton2):
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(boton2.image, boton2.rect)

def dibujarJuego(ventana, listaRojo, listaAmarillo, listaVerde, listaAzul, listaAzulFuerte,listaVidas):
    for enemigo in listaRojo:
        ventana.blit(enemigo.image, enemigo.rect)

    for enemigo in listaAmarillo:
        ventana.blit(enemigo.image, enemigo.rect)

    for enemigo in listaVerde:
        ventana.blit(enemigo.image, enemigo.rect)

    for enemigo in listaAzul:
        ventana.blit(enemigo.image, enemigo.rect)

    for enemigo in listaAzulFuerte:
        ventana.blit(enemigo.image, enemigo.rect)

    for vidas in listaVidas:
        ventana.blit(vidas.image, vidas.rect)


def generarEnemigosRojo(listaEnemigos, imgEnemigo):
    for x in range(7):
        for y in range(1):
            # Generar enemigo x,y
            cx = 12 + x*111
            cy = 80
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)


def generarEnemigosAmarillo(listaEnemigos, imgEnemigo):
    for x in range(7):
        for y in range(1):
            # Generar enemigo x,y
            cx = 12 + x*111
            cy = 80 + 33
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)


def generarEnemigosVerde(listaEnemigos, imgEnemigo):
    for x in range(7):
        for y in range(1):
            # Generar enemigo x,y
            cx = 12 + x*111
            cy = 80 + 66
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)


def generarEnemigosAzul(listaEnemigos, imgEnemigo):
    for x in range(7):
        for y in range(1):
            # Generar enemigo x,y
            cx = 12 + x*111
            cy = 80 + 99
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)


def generarEnemigosAzulFuerte(listaEnemigos, imgEnemigo):
    for x in range(7):
        for y in range(1):
            # Generar enemigo x,y
            cx = 12 + x*111
            cy = 80 + 132
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)


def generarVidas(listaVidas, corazon):
    for x in range(3):
        for y in range(1):
            cx = 20 + x*26
            cy = 15
            vida = pygame.sprite.Sprite()
            vida.image = corazon
            vida.rect = corazon.get_rect()
            vida.rect.left = cx
            vida.rect.top = cy
            listaVidas.append(vida)


def eliminarEnemigosAzulFuerte(pelota, listaEnemigos):
    for k in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[k]
        if pelota.colliderect(enemigo):
            listaEnemigos.remove(enemigo)
            return True


def eliminarEnemigosAzul(pelota, listaEnemigos):
    for k in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[k]
        if pelota.colliderect(enemigo):
            listaEnemigos.remove(enemigo)
            return True


def eliminarEnemigosVerde(pelota, listaEnemigos):
    for k in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[k]
        if pelota.colliderect(enemigo):
            listaEnemigos.remove(enemigo)
            return True


def eliminarEnemigosAmarillo(pelota, listaEnemigos):
    for k in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[k]
        if pelota.colliderect(enemigo):
            listaEnemigos.remove(enemigo)
            return True


def eliminarEnemigosRojo(pelota, listaEnemigos):
    for k in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[k]
        if pelota.colliderect(enemigo):
            listaEnemigos.remove(enemigo)
            return True


def eliminarVidas(y, listaVidas):
    for i in range(len(listaVidas) - 1, -1, -1):
        vidas = listaVidas[i]
        if y >= ALTO:
            listaVidas.remove(vidas)
            return True


def dibujar():

    # archivo puntuaciones
    entrada = open("puntAnterior.txt", 'r', encoding='UTF-8')
    contenido = entrada.read()
    salida = open("puntAnterior.txt", "w", encoding='UTF-8')
    entrada.close()

    # pelota
    x = ANCHO//2
    y = ALTO//2
    radio = 10

    # raqueta
    ALTO_RAQUETA = 20
    ANCHO_RAQUETA = 130
    xRAQUETA = ANCHO//2
    yRAQUETA = ALTO - 20
    moverRaqueta = False
    DX_RAQUETA = 10


    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado = "menu"  # jugando, fin

    # cargar imágenes
    imgBtnJugar = pygame.image.load("botonJugar.png")
    imgBtnV = pygame.image.load("botonPuntuaciones.png")
    imgBtnR = pygame.image.load("botonRegresar.png")
    imgBtnI = pygame.image.load("botonInicio.png")
    imgBtnC = pygame.image.load("botonContinuar.png")

    # Sprite botones
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO//2 - botonJugar.rect.width//2
    botonJugar.rect.top = ALTO//2 - botonJugar.rect.height//2+100

    botonPuntuaciones = pygame.sprite.Sprite()
    botonPuntuaciones.image = imgBtnV
    botonPuntuaciones.rect = imgBtnV.get_rect()
    botonPuntuaciones.rect.left = ANCHO//2 - botonPuntuaciones.rect.width//2
    botonPuntuaciones.rect.top = ALTO//2 - botonPuntuaciones.rect.height//2-50

    botonInicio = pygame.sprite.Sprite()
    botonInicio.image = imgBtnI
    botonInicio.rect = imgBtnI.get_rect()
    botonInicio.rect.left = ANCHO // 2 - botonInicio.rect.width // 2
    botonInicio.rect.top = ALTO // 2 - botonInicio.rect.height // 2 + 200

    botonContinuar = pygame.sprite.Sprite()
    botonContinuar.image = imgBtnC
    botonContinuar.rect = imgBtnC.get_rect()
    botonContinuar.rect.left = ANCHO // 2 - botonContinuar.rect.width // 2
    botonContinuar.rect.top = ALTO // 2 - botonContinuar.rect.height // 2 + 200

    # Enemigos
    listaEnemigosRojo = []
    listaEnemigosAmarillo = []
    listaEnemigosVerde = []
    listaEnemigosAzul = []
    listaEnemigosAzulFuerte = []
    imgEnemigo1 = pygame.image.load("rojo.png")
    imgEnemigo2 = pygame.image.load("amarillo.png")
    imgEnemigo3 = pygame.image.load("verde.png")
    imgEnemigo4 = pygame.image.load("azul.png")
    imgEnemigo5 = pygame.image.load("azulFuerte.png")

    # Generar enemigos
    generarEnemigosRojo(listaEnemigosRojo, imgEnemigo1)
    generarEnemigosAmarillo(listaEnemigosAmarillo, imgEnemigo2)
    generarEnemigosVerde(listaEnemigosVerde, imgEnemigo3)
    generarEnemigosAzul(listaEnemigosAzul, imgEnemigo4)
    generarEnemigosAzulFuerte(listaEnemigosAzulFuerte, imgEnemigo5)

    # Vidas
    listaVidas = []
    corazon = pygame.image.load("corazon.png")
    generarVidas(listaVidas,corazon)

    # Sonido
    pong = pygame.mixer.Sound('sonido.wav')

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True


            elif evento.type == pygame.MOUSEBUTTONDOWN: #El usuario hizo click con el mouse
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    xb, yb, anchoB, altoB = botonJugar.rect
                    xp, yp, anchoP, altoP = botonPuntuaciones.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            score = 0
                            dx = randint(3,5)
                            dy = randint(5,7)
                            #Cambiar de ventana
                            estado = "jugando"

                    if xm >= xp and xm <= xp + anchoP:
                        if ym >= yp and ym <= yp + altoP:
                            estado = "puntuaciones"


                if estado == "puntuaciones":
                    botonRegresar = pygame.sprite.Sprite()
                    botonRegresar.image = imgBtnR
                    botonRegresar.rect = imgBtnR.get_rect()
                    botonRegresar.rect.left = ANCHO // 2 - botonRegresar.rect.width // 2
                    botonRegresar.rect.top = ALTO // 2 - botonRegresar.rect.height // 2 + 200
                    xr, yr, anchoR, altoR = botonRegresar.rect
                    if xm >= xr and xm <= xr + anchoR:
                        if ym >= yr and ym <= yr + altoR:
                            #Cambiar de ventana
                            estado = "menu"


                if estado == "fin":
                    xr2, yr2, anchoR2, altoR2 = botonInicio.rect
                    if xm >= xr2 and xm <= xr2 + anchoR2:
                        if ym >= yr2 and ym <= yr2 + altoR2:
                            listaVidas = []
                            listaEnemigosRojo = []
                            listaEnemigosAmarillo = []
                            listaEnemigosVerde = []
                            listaEnemigosAzul = []
                            listaEnemigosAzulFuerte = []
                            generarVidas(listaVidas,corazon)
                            generarEnemigosRojo(listaEnemigosRojo, imgEnemigo1)
                            generarEnemigosAmarillo(listaEnemigosAmarillo, imgEnemigo2)
                            generarEnemigosVerde(listaEnemigosVerde, imgEnemigo3)
                            generarEnemigosAzul(listaEnemigosAzul, imgEnemigo4)
                            generarEnemigosAzulFuerte(listaEnemigosAzulFuerte, imgEnemigo5)
                            salida.write("Puntuación anterior: ")
                            salida.write(str(score))
                            salida.write('\n')
                            #Cambiar de ventana
                            estado = "menu"


                if estado == "next":
                    xr3, yr3, anchoR3, altoR3 = botonContinuar.rect
                    if xm >= xr3 and xm <= xr3 + anchoR3:
                        if ym >= yr3 and ym <= yr3 + altoR3:
                            dx = randint(3, 5)
                            dy = randint(5, 7)
                            x = ANCHO // 2
                            y = ALTO // 2
                            xRAQUETA = ANCHO // 2
                            yRAQUETA = ALTO - 20
                            listaEnemigosRojo = []
                            listaEnemigosAmarillo = []
                            listaEnemigosVerde = []
                            listaEnemigosAzul = []
                            listaEnemigosAzulFuerte = []
                            generarEnemigosRojo(listaEnemigosRojo, imgEnemigo1)
                            generarEnemigosAmarillo(listaEnemigosAmarillo, imgEnemigo2)
                            generarEnemigosVerde(listaEnemigosVerde, imgEnemigo3)
                            generarEnemigosAzul(listaEnemigosAzul, imgEnemigo4)
                            generarEnemigosAzulFuerte(listaEnemigosAzulFuerte, imgEnemigo5)
                            #Cambiar de ventana
                            estado = "jugando"


            # Raqueta movimiento
            if evento.type ==pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    moverRaqueta = True
                    DX_RAQUETA = -10
                elif evento.key == pygame.K_RIGHT:
                    moverRaqueta = True
                    DX_RAQUETA = +10
            if evento.type == pygame.KEYUP:
                moverRaqueta = False

        # Borrar pantalla
        ventana.fill(GRIS)

        if estado == "menu":
            fuente1 = pygame.font.SysFont("calibri", 62)
            texto1 = fuente1.render("Breakout", 1, NEGRO)
            ventana.blit(texto1, (300, 50))
            dibujarMenu(ventana,botonJugar,botonPuntuaciones)

        elif estado == "puntuaciones":
            fuente2 = pygame.font.SysFont("calibri", 62)
            texto2 = fuente2.render(contenido, 1, NEGRO)
            ventana.blit(texto2, (100, 200))
            ventana.blit(botonRegresar.image, botonRegresar.rect)

        elif estado == "jugando":

            fuente3 = pygame.font.SysFont("calibri", 30)
            texto3 = fuente3.render(str(score), 1, ROJO)
            ventana.blit(texto3, (ANCHO-80, 10))

            fuente4 = pygame.font.SysFont("calibri", 30)
            texto4 = fuente4.render("Score: ", 1, ROJO)
            ventana.blit(texto4, (ANCHO-170, 10))

            dibujarJuego(ventana, listaEnemigosRojo, listaEnemigosAmarillo, listaEnemigosVerde, listaEnemigosAzul, listaEnemigosAzulFuerte,listaVidas)

            # Bordes de juego
            pygame.draw.line(ventana,NEGRO,(0,50),(ANCHO,50),2)
            pygame.draw.line(ventana, NEGRO,(0,50),(0,ALTO),2)
            pygame.draw.line(ventana, NEGRO,(ANCHO-2,50),(ANCHO-2,ALTO),2)

            # Dibujar raqueta
            raqueta = pygame.draw.rect(ventana, BLANCO,(xRAQUETA,yRAQUETA,ANCHO_RAQUETA,ALTO_RAQUETA))

            # Dibujar pelota
            pelota = pygame.draw.circle(ventana,BLANCO,(x,y),radio)

            x += dx
            y += dy

            if y<=radio+50:
                dy = -dy

            if x>=ANCHO-radio or x <=radio:
                dx = -dx

            # Colision con raqueta
            if x>=xRAQUETA and y>= yRAQUETA and x<=xRAQUETA + ANCHO_RAQUETA:
                pong.play()
                dy = -dy


            if xRAQUETA>=ANCHO:
                DX_RAQUETA =0

            if moverRaqueta:
                xRAQUETA += DX_RAQUETA

            # Eliminar enemigos
            colisionAzulFuerte = eliminarEnemigosAzulFuerte(pelota,listaEnemigosAzulFuerte)
            colisionAzul = eliminarEnemigosAzul(pelota, listaEnemigosAzul)
            colisionVerde = eliminarEnemigosVerde(pelota, listaEnemigosVerde)
            colisionAmarillo = eliminarEnemigosAmarillo(pelota, listaEnemigosAmarillo)
            colisionRojo = eliminarEnemigosRojo(pelota, listaEnemigosRojo)

            if colisionAzulFuerte == True:
                dy = -dy
                score += 10

            if colisionAzul == True:
                dy = -dy
                score += 20

            if colisionVerde == True:
                dy = -dy+1
                score += 30

            if colisionAmarillo == True:
                dy = -dy+1
                score += 40

            if colisionRojo == True:
                dy = -dy+2
                score += 50


            # Eliminar Vidas
            vidasRestantes = eliminarVidas(y,listaVidas)

            if vidasRestantes == True:
                dx = randint(3, 5)
                dy = randint(5, 7)
                x = ANCHO//2
                y = ALTO//2

            if len(listaVidas) == 0:
                estado = "fin"


            if len(listaEnemigosAzulFuerte) == 0 and len(listaEnemigosAzul) == 0 and len(listaEnemigosVerde) == 0 and len(listaEnemigosAmarillo) == 0 and len(listaEnemigosRojo) == 0:
                estado = "next"


        elif estado == "fin":
            fuente5 = pygame.font.SysFont("calibri", 60)
            texto5 = fuente5.render(str(score), 1, NEGRO)
            ventana.blit(texto5, (ANCHO//2+200, ALTO//2-100))

            fuente6 = pygame.font.SysFont("calibri", 60)
            texto6 = fuente6.render("Tu puntuación fue: ", 1, NEGRO)
            ventana.blit(texto6, (ANCHO//2-300, ALTO//2-100))
            ventana.blit(botonInicio.image, botonInicio.rect)


        elif estado == "next":
            fuente7 = pygame.font.SysFont("calibri", 60)
            texto7 = fuente7.render(str(score), 1, NEGRO)
            ventana.blit(texto7, (ANCHO//2+70, ALTO//2-100))

            fuente8 = pygame.font.SysFont("calibri", 60)
            texto8 = fuente8.render("Score: ", 1, NEGRO)
            ventana.blit(texto8, (ANCHO//2-100, ALTO//2-100))

            fuente10 = pygame.font.SysFont("calibri", 60)
            texto10 = fuente10.render("Siguiente nivel", 1, NEGRO)
            ventana.blit(texto10, (ANCHO//2-160, ALTO//2+50))
            ventana.blit(botonContinuar.image, botonContinuar.rect)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(80)          # 40 fps

    salida.close()
    pygame.quit()   # termina pygame


def main():

    dibujar()

main()