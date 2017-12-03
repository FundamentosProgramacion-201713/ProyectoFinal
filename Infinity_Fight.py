# encoding: UTF-8
# Autor: Edgar Alexis González Amador - A01746540.
# Bienvenido, este el codigo del videojuego "Infinity Fight", creado por Edgar Alexis.

import pygame
from random import randint

Ancho = 800
Alto = 600

Blanco = (255,255,255)
Negro = (0,0,0)
Azul = (51, 221, 255)

estado = "menu"

num_imagenes_golpe1 = 41
tiempoEntreFramesGolpe1 = 0.02
tiempoTotalGolpe1 = num_imagenes_golpe1 * tiempoEntreFramesGolpe1
num_imagenes_golpe2 = 41
tiempoEntreFramesGolpe2 = 0.02
tiempoTotalGolpe2 = num_imagenes_golpe2 * tiempoEntreFramesGolpe2
num_imagenes_golpe3 = 41
tiempoEntreFramesGolpe3 = 0.02
tiempoTotalGolpe3 = num_imagenes_golpe3 * tiempoEntreFramesGolpe3
num_imagenes_golpe4 = 41
tiempoEntreFramesGolpe4 = 0.02
tiempoTotalGolpe4 = num_imagenes_golpe4 * tiempoEntreFramesGolpe4

xpersonaje1 = 150
ypersonaje1 = 150
xpersonaje2 = 450
ypersonaje2 = 150

def crearListaSpritesGolpe1():
    listaGolpe1 = []

    for i in range(num_imagenes_golpe1):
        nombre = "Recursos/Imagenes/Personaje1/Golpe1/Golpe1 ("+str(i+1)+").png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = xpersonaje1
        sprAnimacion.rect.top = ypersonaje1
        listaGolpe1.append(sprAnimacion)

    return listaGolpe1

def crearListaSpritesGolpe2():
    listaGolpe2 = []

    for i in range(num_imagenes_golpe1):
        nombre = "Recursos/Imagenes/Personaje1/Golpe2/Golpe2 ("+str(i+1)+").png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = xpersonaje1
        sprAnimacion.rect.top = ypersonaje1
        listaGolpe2.append(sprAnimacion)

    return listaGolpe2

def crearListaSpritesGolpe3():
    listaGolpe3 = []

    for i in range(num_imagenes_golpe3):
        nombre = "Recursos/Imagenes/Personaje2/Golpe1/Golpe1 ("+str(i+1)+").png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = xpersonaje2
        sprAnimacion.rect.top = ypersonaje2
        listaGolpe3.append(sprAnimacion)

    return listaGolpe3

def crearListaSpritesGolpe4():
    listaGolpe4 = []

    for i in range(num_imagenes_golpe4):
        nombre = "Recursos/Imagenes/Personaje2/Golpe2/Golpe2 ("+str(i+1)+").png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = xpersonaje2
        sprAnimacion.rect.top = ypersonaje2
        listaGolpe4.append(sprAnimacion)

    return listaGolpe4

def obtenerFrameGolpe1(timerAnimacionGolpe1, listaSpritesGolpe1):
    indice = int(timerAnimacionGolpe1/tiempoEntreFramesGolpe1)
    return listaSpritesGolpe1[indice]

def obtenerFrameGolpe2(timerAnimacionGolpe2, listaSpritesGolpe2):
    indice = int(timerAnimacionGolpe2/tiempoEntreFramesGolpe2)
    return listaSpritesGolpe2[indice]

def obtenerFrameGolpe3(timerAnimacionGolpe3, listaSpritesGolpe3):
    indice = int(timerAnimacionGolpe3/tiempoEntreFramesGolpe3)
    return listaSpritesGolpe3[indice]

def obtenerFrameGolpe4(timerAnimacionGolpe4, listaSpritesGolpe4):
    indice = int(timerAnimacionGolpe4/tiempoEntreFramesGolpe4)
    return listaSpritesGolpe4[indice]


def mostrarPantalla():
    global estado
    timerSegundos = 60

    #Lista segundos
    listaSegundos = []
    for seg in range (61):
        listaSegundos.append(seg)

    # BOTONES

    # Cargar imagenes
    imgBtnJugar = pygame.image.load("Recursos/Imagenes/Botones/btn_jugar.png")
    Win1 = pygame.image.load("Recursos/Imagenes/Fondos/Win1.png")
    Lose1 = pygame.image.load("Recursos/Imagenes/Fondos/Lose1.png")
    imgBtnScore = pygame.image.load("Recursos/Imagenes/Botones/btn_score.png")
    imgBtnr = pygame.image.load("Recursos/Imagenes/Botones/btn_r.png")

    # Sprite
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = (Ancho//2)
    botonJugar.rect.top = (Alto//2)
    #-------------------------------
    botonScore = pygame.sprite.Sprite()
    botonScore.image = imgBtnScore
    botonScore.rect = imgBtnScore.get_rect()
    botonScore.rect.left = (Ancho//2)
    botonScore.rect.top = (Alto//2) + 100

    botonRegresar = pygame.sprite.Sprite()
    botonRegresar.image = imgBtnr
    botonRegresar.rect = imgBtnr.get_rect()
    botonRegresar.rect.left = (Ancho)-350
    botonRegresar.rect.top = (Alto)-100

    PVJugador1 = 100
    PVJugador2 = 100

    numRound = 1

    min = 1

    Estatico = True
    atacar1 = False
    atacar2 = False
    moverp1 = False
    golpeAzar = 0
    movimientoAtras = False
    movimientoAdelante = False
    detenido = False

    global xpersonaje1
    global xpersonaje2
    pygame.init()
    pygame.mixer.music.load("Recursos/Sonidos/Musica1.mp3")
    pygame.mixer.music.play(-1)
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    terminar = False
    imagenFondoMenu=pygame.image.load("Recursos/Imagenes/Fondos/Menu.png")
    score=pygame.image.load("Recursos/Imagenes/Fondos/Score.png")
    imagenFondo=pygame.image.load("Recursos/Imagenes/Fondos/RingPelea.png")
    juegador=pygame.image.load("Recursos/Imagenes/Personaje1/Estatico/Personaje.png")

    personaje1 = pygame.sprite.Sprite()
    personaje1.image = juegador
    personaje1.rect = juegador.get_rect()
    personaje1.rect.left = xpersonaje1
    personaje1.rect.top = ypersonaje1

    juegador2=pygame.image.load("Recursos/Imagenes/Personaje2/Estatico/Personaje02.png")

    personaje2 = pygame.sprite.Sprite()
    personaje2.image = juegador2
    personaje2.rect = juegador2.get_rect()
    personaje2.rect.left = xpersonaje2+57
    personaje2.rect.top = ypersonaje2

    numberOne = pygame.image.load("Recursos/Imagenes/Numeros/numero1.png")
    numberTwo = pygame.image.load("Recursos/Imagenes/Numeros/numero2.png")
    numberThree = pygame.image.load("Recursos/Imagenes/Numeros/numero3.png")

    listaSpritesGolpe1 = crearListaSpritesGolpe1()
    timerAnimacionGolpe1 = 0

    listaSpritesGolpe2 = crearListaSpritesGolpe2()
    timerAnimacionGolpe2 = 0

    listaSpritesGolpe3 = crearListaSpritesGolpe3()
    timerAnimacionGolpe3 = 0

    listaSpritesGolpe4 = crearListaSpritesGolpe4()
    timerAnimacionGolpe4 = 0

    dxpersonaje = 0
    dxpersonaje2 = 0
    tiempo = 0
    tiempoEspera = 0
    inicioRound = 0
    timerGolpes = 0
    timerMovimiento2 = 0
    tiempoAzarMovimiento = 5

    listaGolpes = []
    for numGolpe in range(13):
        if numGolpe == 0:
            listaGolpes.append(randint(1, 5))
        else:
            listaGolpes.append(randint((0+(numGolpe*5)),((3+(numGolpe*5)))))
    #pygame.mixer.music.load("Recursos/Sonidos/Musica1.mp3")
    #pygame.mixer.music.play(1)
    while not terminar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT: # flecha abajo
                    Estatico = True
                    atacar1 = False
                    atacar2 = False
                    dxpersonaje = -20
                    moverp1 = True
                if evento.key == pygame.K_RIGHT:   # flecha arriba
                    Estatico = True
                    atacar1 = False
                    atacar2 = False
                    dxpersonaje = +20
                    moverp1 = True
                if evento.key == pygame.K_s:   # flecha arriba
                    personaje1.sonidoPuno = pygame.mixer.Sound("Recursos/Sonidos/Pow.wav")
                    personaje1.sonidoPuno.play()
                    Estatico = False
                    atacar1 = True
                    atacar2 = False
                if evento.key == pygame.K_a:   # flecha arriba
                    personaje1.sonidoPuno = pygame.mixer.Sound("Recursos/Sonidos/Pow.wav")
                    personaje1.sonidoPuno.play()
                    Estatico = False
                    atacar1 = False
                    atacar2 = True

            if evento.type == pygame.KEYUP:     # se suelta la tecla
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    moverp1 = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchob, altob = botonJugar.rect
                    if xm >= xb and xm <= xb+anchob and ym >= yb and ym <= yb+altob:
                        estado = "juego"
                if estado == "menu":
                    xb, yb, anchob, altob = botonScore.rect
                    if xm >= xb and xm <= xb+anchob and ym >= yb and ym <= yb+altob:
                        estado = "score"
                if estado == "score":
                    xb, yb, anchob, altob = botonRegresar.rect
                    if xm >= xb and xm <= xb+anchob and ym >= yb and ym <= yb+altob:
                        estado = "menu"

        ventana.fill(Blanco)

        txtseg = listaSegundos[timerSegundos]

        if estado == "menu":
            ventana.blit(imagenFondoMenu,(0,0))
            ventana.blit(botonJugar.image, botonJugar.rect)
            ventana.blit(botonScore.image, botonScore.rect)
            pygame.display.flip()   # Actualiza trazos

        elif estado == "score":
            ventana.blit(score,(0,0))

            ventana.blit(botonRegresar.image, botonRegresar.rect)
            fuente = pygame.font.SysFont("Verdana", 20)
            numeroPeleas = open("Recursos/Peleas.txt", "r")
            textoNumeroPeleas = numeroPeleas.read()
            listaPuntajes = textoNumeroPeleas.split("\n")
            parrafo = ""
            for x in range (len(listaPuntajes)):
                parrafo = (listaPuntajes[x])
                txtRound = fuente.render(parrafo, 1, Blanco)
                ventana.blit(txtRound,(20, (100)+(x*20)))

            pygame.display.flip()   # Actualiza trazos
            reloj.tick(40)          # 40 fps

        elif estado == "juego":
            ventana.blit(imagenFondo,(0,0))

            frameActualGolpe1 = obtenerFrameGolpe1(timerAnimacionGolpe1, listaSpritesGolpe1)
            frameActualGolpe2 = obtenerFrameGolpe2(timerAnimacionGolpe2, listaSpritesGolpe2)
            frameActualGolpe3 = obtenerFrameGolpe3(timerAnimacionGolpe3, listaSpritesGolpe3)
            frameActualGolpe4 = obtenerFrameGolpe4(timerAnimacionGolpe4, listaSpritesGolpe4)

            #
            fuente = pygame.font.SysFont("Verdana", 25)
            txtRound = fuente.render("Round "+str(numRound)+"", 1, Blanco)
            ventana.blit(txtRound,(20, 42))
            txtRound = fuente.render("%02d:%02d"%(min,txtseg), 1, Blanco)
            ventana.blit(txtRound,((Ancho//2)-40, 15))
            #

            # Mostra barra de puntos de vida
            for pv in range (PVJugador1):
                pygame.draw.line(ventana, Azul, (50+(3*pv), 20), (50+(3*pv), 40), 3)
            for pv in range (PVJugador2):
                pygame.draw.line(ventana, Azul, (450+(3*pv), 20), (450+(3*pv), 40), 3)

            if moverp1:
                xpersonaje1 += dxpersonaje
                listaSpritesGolpe1 = crearListaSpritesGolpe1()
                listaSpritesGolpe2 = crearListaSpritesGolpe2()
                timerAnimacionGolpe2 = 0
                timerAnimacionGolpe1 = 0

            if Estatico:
                personaje1.rect.left = xpersonaje1
                personaje1.rect.top = ypersonaje1
                ventana.blit(personaje1.image, personaje1.rect)
            elif atacar1:
                ventana.blit(frameActualGolpe1.image, frameActualGolpe1.rect)
            elif atacar2:
                ventana.blit(frameActualGolpe2.image, frameActualGolpe2.rect)

            if (tiempoEspera > 0 and tiempoEspera < 1000):
                ventana.blit(numberThree, (336, 254))
            elif (tiempoEspera > 1000 and tiempoEspera < 2000):
                ventana.blit(numberTwo, (336, 254))
            elif (tiempoEspera > 2000 and tiempoEspera <3000):
                ventana.blit(numberOne, (336, 254))
            elif (tiempoEspera > 3000):
                inicioRound = 1

            if timerGolpes in listaGolpes:
                personaje2.sonidoPuno = pygame.mixer.Sound("Recursos/Sonidos/Pow.wav")
                personaje2.sonidoPuno.play()
                if golpeAzar == 0:
                    ventana.blit(frameActualGolpe3.image, frameActualGolpe3.rect)
                    golpeAzar = 0
                elif golpeAzar == 1:
                    ventana.blit(frameActualGolpe4.image, frameActualGolpe4.rect)
                    golpeAzar = 1
                if frameActualGolpe3.rect.colliderect(personaje1) or frameActualGolpe4.rect.colliderect(personaje1):
                    PVJugador1 -= 1
            else:
                if inicioRound == 1:
                    personaje2.rect.left = xpersonaje2+57
                    personaje2.rect.top = ypersonaje2
                    ventana.blit(personaje2.image, personaje2.rect)

                    xpersonaje2 += dxpersonaje2
                    listaSpritesGolpe3 = crearListaSpritesGolpe3()
                    listaSpritesGolpe4 = crearListaSpritesGolpe4()
                    timerAnimacionGolpe3 = 0
                    timerAnimacionGolpe4 = 0
                    if golpeAzar == 0:
                        golpeAzar = 1
                    elif golpeAzar == 1:
                        golpeAzar = 0
                    if movimientoAdelante == True:
                        dxpersonaje2 = 20
                    elif movimientoAtras == True:
                        dxpersonaje2 = -20
                    elif detenido == True:
                        dxpersonaje2 = 0
                else:
                    ventana.blit(personaje2.image, personaje2.rect)

            if atacar1 or atacar2:
                if frameActualGolpe1.rect.colliderect(personaje2) or frameActualGolpe2.rect.colliderect(personaje2):
                    PVJugador2 -= 1

            if PVJugador1 <= 0:
                estado = "Lose1"
            if PVJugador2 <= 0:
                numeroPeleas = open("Recursos/Peleas.txt", "r")
                textoNumeroPeleas = numeroPeleas.read()
                listaPuntajes = textoNumeroPeleas.split("\n")
                numeroDePeleas = len(listaPuntajes)
                numeroPeleas.close()
                numeroPeleas = open("Recursos/Peleas.txt", "w")
                for x in range(numeroDePeleas):
                    numeroPeleas.write(listaPuntajes[x]+"\n")
                numeroPeleas.write("Pelea " + str(numeroDePeleas) + " - " + str(60 - timerSegundos) + " segundos")
                numeroPeleas.close()
                estado = "Win1"

            pygame.display.flip()  # Actualiza trazos

            cuarentavoDeSegundo = reloj.tick(40)

            timerAnimacionGolpe1 += cuarentavoDeSegundo / 1000  # 40 fps
            if timerAnimacionGolpe1 >= tiempoTotalGolpe1:
                timerAnimacionGolpe1 = 0
                timerAnimacionGolpe2 = 0
                atacar1 = False
                Estatico = True

            timerAnimacionGolpe2 += cuarentavoDeSegundo / 1000  # 40 fps
            if timerAnimacionGolpe2 >= tiempoTotalGolpe2:
                timerAnimacionGolpe2 = 0
                timerAnimacionGolpe1 = 0
                atacar2 = False
                Estatico = True

            timerAnimacionGolpe3 += cuarentavoDeSegundo / 1000  # 40 fps
            if timerAnimacionGolpe3 >= tiempoTotalGolpe3:
                timerAnimacionGolpe3 = 0

            timerAnimacionGolpe4 += cuarentavoDeSegundo / 1000  # 40 fps
            if timerAnimacionGolpe4 >= tiempoTotalGolpe4:
                timerAnimacionGolpe4 = 0

            if inicioRound == 0:
                tiempoEspera += cuarentavoDeSegundo

            elif inicioRound == 1:
                tiempo += cuarentavoDeSegundo
                if (tiempo > 1000):
                    timerSegundos -= 1
                    timerGolpes += 1
                    tiempo = 0
            if timerMovimiento2 >= 850:
                tiempoAzarMovimiento = randint(3, 5)
            timerMovimiento2 += cuarentavoDeSegundo
            if tiempoAzarMovimiento == 3:
                movimientoAdelante = True
                movimientoAtras = False
                detenido = False
            elif tiempoAzarMovimiento == 4:
                movimientoAtras = True
                movimientoAdelante = False
                detenido = False
            elif tiempoAzarMovimiento == 5:
                detenido = True
                movimientoAdelante = False
                movimientoAtras = False

        elif estado == "Win1":
            ventana.blit(Win1, (0, 0))
            pygame.display.flip()   # Actualiza trazos

            cuarentavoDeSegundo = reloj.tick(40)
            tiempo += cuarentavoDeSegundo
            if (tiempo > 5000):
                estado = "menu"
            PVJugador1 = 100
            PVJugador2 = 100
            tiempoEspera = 0
            inicioRound = 0

        elif estado == "Lose1":
            ventana.blit(Lose1, (0, 0))
            pygame.display.flip()   # Actualiza trazos

            cuarentavoDeSegundo = reloj.tick(40)
            tiempo += cuarentavoDeSegundo
            if (tiempo > 5000):
                estado = "menu"
            PVJugador1 = 100
            PVJugador2 = 100
            tiempoEspera = 0
            inicioRound = 0


    pygame.quit()


def main():
    mostrarPantalla()

main()