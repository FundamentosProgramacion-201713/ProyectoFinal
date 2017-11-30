#Encoding: UTF-8
#Autor: Roberto Téllez Perezyera
"""
Atrapa los libros y evita las pantallas azules para que te vaya de maravilla en los finales y puedas disfrutar de tus
vacaciones como todo un campeón en su silla de acampar.
"""

import pygame
from random import randrange,randint

pygame.mixer.init()
badHit = pygame.mixer.Sound("hitFinal.wav")
alonsoGameOver = pygame.mixer.Sound("alonsoGameOverFinal.wav")

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # (R,G,B) / rango [0,255]
NEGRO = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREENISH = (135, 194, 113)
LIGHTORANGE = (255,204,153)



def dibujarMenu(ventana, botonJugar, botonHi):
    #Dibuja los botones del menu principal
    ventana.blit(botonJugar.image,botonJugar.rect)
    ventana.blit(botonHi.image,botonHi.rect)


def dibujarJuego(ventana, timer, personaje, listaLibros, listaBlscr, listaVidas, score):
    #Dibuja y anima a los sprites. Contiene las condiciones cuando uno choca con el otro
    ventana.blit(personaje.image, personaje.rect)

    generaVida = False

    #Ahora, añadimos los libros
    for libro in listaLibros:
        ventana.blit(libro.image, libro.rect)

    #Añadimos las blue screens
    for blscr in listaBlscr:
        ventana.blit(blscr.image, blscr.rect)

    #Animar objetos cayendo:
    for libro in listaLibros:
        libro.rect.top += 15
        if libro.rect.top >= ALTO:
            libro.rect.top = 6
            libro.rect.left = randrange(0,607,1)

    for screen in listaBlscr:
        screen.rect.top += 17
        if screen.rect.top >= ALTO:
            screen.rect.top = 6
            screen.rect.left = randrange(0,607,1)

    #Verificar colisiones:
    for libro in listaLibros:
        if libro.rect.colliderect(personaje):
            score += 10
            libro.rect.top = 6
            libro.rect.left = randrange(0,607,1)


    for screen in listaBlscr:
        if screen.rect.colliderect(personaje):
            screen.rect.top = 6
            screen.rect.left = randrange(0,607,1)
            badHit.play()


    if timer > 28:
        print("vida!")
        generaVida = True

    if generaVida:
        for vida in listaVidas:
            ventana.blit(vida.image,vida.rect)
            vida.rect.top += 14
            if vida.rect.top >= ALTO:
                listaVidas.remove(vida)

    return score



def generarLibros(listaLibros, imgLibro):
    #Genera 5 libros en una pos x aleatoria en parteSuperiorPantalla
    for x in range(5):
        xCoord = randrange(0,607,1)
        yCoord = 7
        nuevo = pygame.sprite.Sprite()
        nuevo.image = imgLibro
        nuevo.rect = imgLibro.get_rect()
        nuevo.rect.left = xCoord
        nuevo.rect.top = yCoord
        listaLibros.append(nuevo)


def generarBlscr(listaBlscr, imgBlscr):
    #Genera 5 pantallas azules en una pos x aleatoria en parteSuperiorPantalla
    for x in range(5):
        xCoord = randrange(0,607,1)
        yCoord = 7
        nuevo = pygame.sprite.Sprite()
        nuevo.image = imgBlscr
        nuevo.rect = imgBlscr.get_rect()
        nuevo.rect.left = xCoord
        nuevo.rect.top = yCoord
        listaBlscr.append(nuevo)



def generarVida(imgVida, listaVidas):
    for x in range(1):
        xCoord = randrange(0,607,1)
        yCoord = 7
        nuevo = pygame.sprite.Sprite()
        nuevo.image = imgVida
        nuevo.rect = imgVida.get_rect()
        nuevo.rect.left = xCoord
        nuevo.rect.top = yCoord
        listaVidas.append(nuevo)


def dibujar():
    #Uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Timer
    timer = 0

    #Estados
    estado = "menu"


    #Backgrounds
    imgBg = pygame.image.load("pantallaJugando.png")


    #Botones
    imgBotonJugar = pygame.image.load("boton_jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBotonJugar
    botonJugar.rect = imgBotonJugar.get_rect()
    botonJugar.rect.left = ANCHO//2 - botonJugar.rect.width//2
    botonJugar.rect.top = ALTO//2 + 100   # - botonJugar.rect.height//2 <-- no lo quiero centrado >:v

    imgBotonVolver = pygame.image.load("boton_menu.png")
    botonVolver = pygame.sprite.Sprite()
    botonVolver.image = imgBotonVolver
    botonVolver.rect = imgBotonVolver.get_rect()
    #ahorita el botón está centrado
    botonVolver.rect.left = ANCHO//2 - botonVolver.rect.width//2
    botonVolver.rect.top = ALTO//2 - botonVolver.rect.height//2

    imgBotonHi = pygame.image.load("boton_hiScores.png")
    botonHi = pygame.sprite.Sprite()
    botonHi.image = imgBotonHi
    botonHi.rect = imgBotonHi.get_rect()
    botonHi.rect.left = ANCHO//2 - botonHi.rect.width//2
    botonHi.rect.top = ALTO//2 + 13


    #Personaje
    imgPersonaje = pygame.image.load("personaje.png")
    personaje = pygame.sprite.Sprite()
    personaje.image = imgPersonaje
    personaje.rect = imgPersonaje.get_rect()
    personaje.rect.left = ANCHO//2 - personaje.rect.width//2 - 50
    personaje.rect.top = ALTO - personaje.rect.height - 11

    dxPersonaje = 0
    moverPersonaje = False


    #objetoBueno
    listaLibros = []
    imgLibro = pygame.image.load("atrapar.png")
    generarLibros(listaLibros, imgLibro)
    #Aquí no creamos sprites, sino hasta después


    #objetoMalo
    listaBlscr = []
    imgBlscr = pygame.image.load("atraparNot.png")
    generarBlscr(listaBlscr, imgBlscr)


    #spriteVida
    listaVidas = []
    imgVida = pygame.image.load("vida.png")
    generarVida(imgVida,listaVidas)

    #initialD
    score = 0
    lives = 3


    #***-EL CICLO PRINCIPAL-***
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            moverPersonaje = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    termina = True

                if evento.key == pygame.K_LEFT:
                    dxPersonaje = -15
                    moverPersonaje = True
                if evento.key == pygame.K_RIGHT:
                    dxPersonaje = +15
                    moverPersonaje = True
                if evento.key == pygame.KEYUP:
                    dxPersonaje = 0
                    moverPersonaje = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xM, yM = pygame.mouse.get_pos()
                if estado == "menu":
                    xM, yM = pygame.mouse.get_pos()
                    xB, yB, anchoB, altoB = botonJugar.rect
                    #El mouse está sobre botonJugar:
                    if xM >= xB and xM <= xB + anchoB:
                        if yM >= yB and yM <= yB + altoB:
                            estado = "jugando"
                elif estado == "jugando":
                    pass

        # Borrar pantalla
        ventana.blit(imgBg,(0,0))
        #ventana.fill(BLANCO)

        timer += 1/40       #1 / fps    <--- checar reloj.tick, abajo
        if timer > 30:
            timer = 0

        # ---> Dibujar, aquí haces todos los trazos que requieras <---
        if estado == "menu":
            ventana.fill(GREENISH)
            dibujarMenu(ventana, botonJugar, botonHi)
        elif estado == "jugando":
            dibujarJuego(ventana, timer, personaje, listaLibros, listaBlscr, listaVidas, score)



        if moverPersonaje == True:
            personaje.rect.left += dxPersonaje


        elif estado == "jugandoTermina":
            ventana.fill(LIGHTORANGE)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

        #print(enemyHit)
        print(score)

    pygame.quit()               # termina pygame    ///     Termina el ciclo principal


def main():
    dibujar()


main()