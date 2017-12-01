# encoding: UTF-8
# Autor: Edgar Alexis González Amador - A01746540.
# Bienvenido, este el codigo del videojuego "Infinity Fight", creado por Edgar Alexis.

import pygame

Ancho = 800
Alto = 600

Blanco = (255,255,255)
Negro = (0,0,0)

num_imagenes_golpe1 = 41
tiempoEntreFramesGolpe1 = 0.02
tiempoTotalGolpe1 = num_imagenes_golpe1 * tiempoEntreFramesGolpe1
num_imagenes_golpe2 = 41
tiempoEntreFramesGolpe2 = 0.02
tiempoTotalGolpe2 = num_imagenes_golpe2 * tiempoEntreFramesGolpe2

xpersonaje1 = 150
ypersonaje1 = 150
xpersonaje2 = 0
ypersonaje2 = 0

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

def obtenerFrameGolpe1(timerAnimacionGolpe1, listaSpritesGolpe1):
    indice = int(timerAnimacionGolpe1/tiempoEntreFramesGolpe1)
    return listaSpritesGolpe1[indice]

def obtenerFrameGolpe2(timerAnimacionGolpe2, listaSpritesGolpe2):
    indice = int(timerAnimacionGolpe2/tiempoEntreFramesGolpe2)
    return listaSpritesGolpe2[indice]

def mostrarPantalla():

    # BOTONES

    # Cargar imagenes
    imgBtnJugar = pygame.image.load("Recursos/Imagenes/Botones/btn_jugar.png")
    imgBtnScore = pygame.image.load("Recursos/Imagenes/Botones/btn_score.png")
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


    Estatico = True
    atacar1 = False
    atacar2 = False
    moverp1 = False

    global xpersonaje1
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))
    reloj = pygame.time.Clock()
    terminar = False
    imagenFondoMenu=pygame.image.load("Recursos/Imagenes/Fondos/Menu.png")
    imagenFondo=pygame.image.load("Recursos/Imagenes/Fondos/RingPelea.png")
    juegador=pygame.image.load("Recursos/Imagenes/Personaje1/Estatico/Personaje.png")

    listaSpritesGolpe1 = crearListaSpritesGolpe1()
    timerAnimacionGolpe1 = 0

    listaSpritesGolpe2 = crearListaSpritesGolpe2()
    timerAnimacionGolpe2 = 0

    dxpersonaje = 0
    estado = "menu"

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
                    Estatico = False
                    atacar1 = True
                    atacar2 = False
                if evento.key == pygame.K_a:   # flecha arriba
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

        ventana.fill(Blanco)


        if estado == "menu":
            ventana.blit(imagenFondoMenu,(0,0))
            ventana.blit(botonJugar.image, botonJugar.rect)
            ventana.blit(botonScore.image, botonScore.rect)
            pygame.display.flip()   # Actualiza trazos
            reloj.tick(40)          # 40 fps

        elif estado == "juego":
            ventana.blit(imagenFondo,(0,0))

            frameActualGolpe1 = obtenerFrameGolpe1(timerAnimacionGolpe1, listaSpritesGolpe1)
            frameActualGolpe2 = obtenerFrameGolpe2(timerAnimacionGolpe2, listaSpritesGolpe2)

            if moverp1:
                xpersonaje1 += dxpersonaje
                listaSpritesGolpe1 = crearListaSpritesGolpe1()
                listaSpritesGolpe2 = crearListaSpritesGolpe2()
                timerAnimacionGolpe2 = 0
                timerAnimacionGolpe1 = 0

            if Estatico:
                ventana.blit(juegador,(xpersonaje1,ypersonaje1))
            elif atacar1:
                ventana.blit(frameActualGolpe1.image, frameActualGolpe1.rect)
            elif atacar2:
                ventana.blit(frameActualGolpe2.image, frameActualGolpe2.rect)

            pygame.display.flip()  # Actualiza trazos
            timerAnimacionGolpe1 += reloj.tick(40) / 1000  # 40 fps
            if timerAnimacionGolpe1 >= tiempoTotalGolpe1:
                timerAnimacionGolpe1 = 0
                timerAnimacionGolpe2 = 0
                atacar1 = False
                Estatico = True

            timerAnimacionGolpe2 += reloj.tick(40) / 1000  # 40 fps
            if timerAnimacionGolpe2 >= tiempoTotalGolpe2:
                timerAnimacionGolpe2 = 0
                timerAnimacionGolpe1 = 0
                atacar2 = False
                Estatico = True
    pygame.quit()

def main():
    mostrarPantalla()

main()