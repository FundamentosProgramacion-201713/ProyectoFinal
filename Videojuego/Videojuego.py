# encoding: UTF-8
# Autor: Eduardo Gallegos Solís
# Videojuego Examen Final Introducción a la Programación

from random import randint
import pygame
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
NUM_IMAGENES = 10
TIEMPO_ENTRE_FRAMES = .007
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES


def dibujarMenu(ventana, botonJugar, botonCreditos, imagenFondo, botonScores, imagenTitulo):
    ventana.blit(imagenFondo, (0, 0))
    ventana.blit(imagenTitulo, (ANCHO//3, 30))
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonCreditos.image, botonCreditos.rect)
    ventana.blit(botonScores.image, botonScores.rect)


def dibujarJuego(ventana, imagenFondoJuego, listaEnemigos, listasBalas, imagenJuego, xPersonaje):
    ventana.blit(imagenJuego, (xPersonaje,ALTO-110))
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listasBalas:
        ventana.blit(bala.image, bala.rect)

def dibujarCreditos(ventana, imagenFondoCreditos, botonRegresar):
    ventana.blit(imagenFondoCreditos, (0,0))
    ventana.blit(botonRegresar.image, botonRegresar.rect)

def dibujarScores(ventana, imagenFondoScores, botonRegresar):
    ventana.blit(imagenFondoScores, (0,0))
    ventana.blit(botonRegresar.image, botonRegresar.rect)

def actualizarBalas(listasBalas,listaEnemigos):
    for bala in listasBalas: #NO DEBEN MODIFICAR ESA COLECCION
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listasBalas.remove(bala)
            continue
        borrarBala = False
        for k in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala = True
                break #Termina el ciclo (For/While)
        if borrarBala:
            listasBalas.remove(bala)

def generarEnemigosAzar(listaEnemigos, imgEnemigo):
    cx= randint(20, ANCHO-128)
    cy = randint(20,ALTO//2)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    enemigo.rect.left = cx #- enemigo.rect.width // 2
    enemigo.rect.top = cy #- enemigo.rect.height // 2
    listaEnemigos.append(enemigo)


def dibujarInstrucciones(ventana, imagenFondoInstrucciones, botonAndroid, botonApple, botonJugar):
    ventana.blit(imagenFondoInstrucciones, (0,0))
    ventana.blit(botonApple.image, botonApple.rect)
    ventana.blit(botonAndroid.image, botonAndroid.rect)

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    timerAnimacion = 0
    estado = "menu"
    # Cargar imagenes
    imgBtnJugar = pygame.image.load("Imagenes/button_jugar.png")
    # Sprite
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 4 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2.5

    imgBtnCreditos = pygame.image.load("Imagenes/button_creditos.png")
    # Sprite
    botonCreditos = pygame.sprite.Sprite()
    botonCreditos.image = imgBtnCreditos
    botonCreditos.rect = imgBtnCreditos.get_rect()
    botonCreditos.rect.left = ANCHO // 4 - botonCreditos.rect.width // 2
    botonCreditos.rect.top = ALTO // 2.25 + botonCreditos.rect.height

    imgBtnScores = pygame.image.load("Imagenes/button_highscore.png")
    # Sprite
    botonScores = pygame.sprite.Sprite()
    botonScores.image = imgBtnScores
    botonScores.rect = imgBtnScores.get_rect()
    botonScores.rect.left = ANCHO // 4 - botonScores.rect.width // 2
    botonScores.rect.top = ALTO // 2 + (2*botonScores.rect.height )

    imgBtnRegresar = pygame.image.load("Imagenes/button_regresar.png")
    # Sprite
    botonRegresar = pygame.sprite.Sprite()
    botonRegresar.image = imgBtnRegresar
    botonRegresar.rect = imgBtnRegresar.get_rect()
    botonRegresar.rect.left = ANCHO - (2*botonRegresar.rect.width)
    botonRegresar.rect.top = ALTO - (2*botonRegresar.rect.height)

    imgBtnApple = pygame.image.load("Imagenes/personaje2.png")
    # Sprite
    botonApple = pygame.sprite.Sprite()
    botonApple.image = imgBtnApple
    botonApple.rect = imgBtnRegresar.get_rect()
    botonApple.rect.left = ANCHO//2 +  botonApple.rect.width
    botonApple.rect.top = ALTO//3 + (botonApple.rect.height)

    imgBtnAndroid = pygame.image.load("Imagenes/personaje1.png")
    # Sprite
    botonAndroid = pygame.sprite.Sprite()
    botonAndroid.image = imgBtnAndroid
    botonAndroid.rect = imgBtnRegresar.get_rect()
    botonAndroid.rect.left = ANCHO//3 + (botonApple.rect.width)
    botonAndroid.rect.top = ALTO//3 + (botonAndroid.rect.height)

    #Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Imagenes/Enemigo.png")
    generarEnemigosAzar(listaEnemigos, imgEnemigo)

    # Balas
    listasBalas = []
    imgBala = pygame.image.load("Imagenes/bala.png")

    #Fondo
    imagenFondo = pygame.image.load("Imagenes/Inicio.png")
    imagenFondoJuego = pygame.image.load("Imagenes/Imagen fondo.png")
    imagenFondoCreditos = pygame.image.load("Imagenes/Creditos.png")
    imagenTitulo = pygame.image.load("Imagenes/Titulo.png")
    imagenFondoScores = pygame.image.load("Imagenes/scores.png")
    imagenFondoInstrucciones = pygame.image.load("Imagenes/instrucciones.png")

    y = 0
    timer = 0
    xPersonaje = ANCHO//2


    pygame.mixer.init()
    pygame.mixer.music.load("Imagenes/musicaJuego.mp3")
    pygame.mixer.music.play(-1)


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN: #El usuario hizo click
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xc, yc, anchoC, altoC = botonCreditos.rect
                    xh, yh, anchoH, altoH = botonScores.rect
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb+anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            #Cambiar ventana
                            estado = "instrucciones"
                    if xm >= xc and xm <= xc+anchoC:
                        if ym >= yc and ym <= yc+ altoC:
                            #Cambiar ventana
                            estado = "creditos"
                    if xm >= xh and xm <= xh+anchoH:
                        if ym >= yh and ym <= yh+ altoH:
                            estado = "scores"
                elif estado == "creditos":
                    xr, yr, anchoR, altoR = botonRegresar.rect
                    if xm >= xr and xm <= xr+anchoR:
                        if ym >= yr and ym <= yr + altoR:
                            #Cambiar ventana
                            estado = "menu"
                elif estado == "scores":
                    xr, yr, anchoR, altoR = botonRegresar.rect
                    if xm >= xr and xm <= xr+anchoR:
                        if ym >= yr and ym <= yr + altoR:
                            #Cambiar ventana
                            estado = "menu"
                elif estado == "instrucciones":
                    xa, ya, anchoa, altoa = botonApple.rect
                    xA, yA, anchoA, altoA = botonAndroid.rect
                    if xm >= xa and xm <= xa + anchoa:
                        if ym >= ya and ym <= ya + altoa:
                            # Cambiar ventana
                            estado = "jugando"
                            personajeBien = "Imagenes/personaje2.png"
                            imagenPersonaje = pygame.image.load(personajeBien)
                    elif xm >= xA and xm <= xA + anchoA:
                        if ym >= yA and ym <= yA + altoA:
                            # Cambiar ventana
                            estado= "jugando"
                            personajeBien = "Imagenes/personaje1.png"
                            imagenPersonaje = pygame.image.load(personajeBien)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    xPersonaje -= 30
                elif evento.key == pygame.K_RIGHT:
                    xPersonaje += 30
                if evento.key == pygame.K_SPACE:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = xPersonaje
                    bala.rect.top = ALTO -100
                    listasBalas.append(bala)
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        if estado == "menu":
            dibujarMenu(ventana, botonJugar, botonCreditos, imagenFondo, botonScores, imagenTitulo)
        elif estado == "instrucciones":
            dibujarInstrucciones(ventana, imagenFondoInstrucciones,botonAndroid, botonApple, botonJugar)
        elif estado == "jugando":
            ventana.blit(imagenFondoJuego,(0, y))
            ventana.blit(imagenFondoJuego, (0, ALTO + y))
            y -= 1
            if y <= -ALTO:
                y = 0
            actualizarBalas(listasBalas, listaEnemigos)
            dibujarJuego(ventana, imagenFondoJuego, listaEnemigos, listasBalas, imagenPersonaje, xPersonaje)
            timer += 1/40
            if timer >= 2:
                timer=0
                generarEnemigosAzar(listaEnemigos, imgEnemigo)
        elif estado == "creditos":
            dibujarCreditos(ventana, imagenFondoCreditos, botonRegresar)
        elif estado == "scores":
            dibujarScores(ventana,imagenFondoScores, botonRegresar)

        # Musica de fondo

        pygame.display.flip()   # Actualiza trazos
        timerAnimacion += reloj.tick(40)/1000
        if timerAnimacion>= TIEMPO_TOTAL:
            timerAnimacion = 0

    pygame.quit()   # termina pygame

def main():
    dibujar()

main()