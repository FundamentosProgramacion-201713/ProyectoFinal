# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import pygame
import random
import time

ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
NEGRO = (0,0,0)
imgFondo = pygame.image.load("fondo.png")
imgNave = pygame.image.load("nave8bit.png")
imgAsteroide = pygame.image.load("asteroide8bit.png")
imgAsteroideD = pygame.image.load("asteroide8bitD.png")
imgAsteroideA = pygame.image.load("asteroide8bitA.png")
imgAsteroideI = pygame.image.load("asteroide8bitI.png")



imgDisparo = pygame.image.load("disparo.png")

# Mostrar un mensaje en pantalla
def mensajeEnPantalla(m, ventana, x, y, tamano):
    font = pygame.font.SysFont("Arial", tamano)
    texto = font.render(m ,True, (255,255,255))
    ventana.blit(texto, [x,  y])

# Actualiza la posición de los disparos
def actualizarDisparos(disparos):
    for disparo in disparos:
        if disparo.rect.y < 0:
            disparos.remove(disparo)
        disparo.rect.y -= 10

# Actualiza la posición de los asteroides
def actualizarAsteroides(asteroides, tiempoInicial):
    tiempoActual = int(time.time())
    mod = (tiempoActual - tiempoInicial) % 4
    for asteroide in asteroides:
        asteroide.rect.y += asteroide.velocidad
        asteroide.inicio += 1
        if mod == 0:
            asteroide.image = imgAsteroide
        elif mod == 1:
            asteroide.image = imgAsteroideD
        elif mod == 2:
            asteroide.image = imgAsteroideA
        elif mod == 3:
            asteroide.image = imgAsteroideI


# Borra los disparos que estén fuera de rango y comprueba que haya colisiones
def validarChoqueDisparoAsteroide(disparos, asteroides, universo, puntuacion):
    for disparo in disparos:
        if disparo.rect.y <= 0:
            disparos.remove(disparo)
            universo.remove(disparo)

    aciertos = pygame.sprite.groupcollide(disparos, asteroides, True, True)
    for acierto in aciertos:
        puntuacion += 10
    return puntuacion


# Valida los controles de la nave
def validarControlesNave(nave, disparos, universo):
    # Teclas presionadas
    teclasPresionadas = pygame.key.get_pressed()
    # Verificar si alguna tecla del control fue presionada
    if teclasPresionadas[pygame.K_LEFT] and nave.rect.x > 0:
        nave.rect.x -= 10
    if teclasPresionadas[pygame.K_RIGHT] and nave.rect.x < ANCHO - nave.rect.width:
        nave.rect.x += 10
    if teclasPresionadas[pygame.K_UP] and nave.rect.y > 0:
        nave.rect.y -= 10
    if teclasPresionadas[pygame.K_DOWN] and nave.rect.y < ALTO - nave.rect.height:
        nave.rect.y += 10
    if teclasPresionadas[pygame.K_a]:
        # Disparo Izquierdo
        disparo = pygame.sprite.Sprite()
        disparo.image = imgDisparo
        disparo.rect = imgDisparo.get_rect()
        disparo.rect.x = nave.rect.x - 3
        disparo.rect.y = nave.rect.y
        disparos.add(disparo)
        universo.add(disparo)

        # Disparo Derecho
        disparo = pygame.sprite.Sprite()
        disparo.image = imgDisparo
        disparo.rect = imgDisparo.get_rect()
        disparo.rect.x = nave.rect.x + nave.rect.width - 10
        disparo.rect.y = nave.rect.y
        disparos.add(disparo)
        universo.add(disparo)
    return nave, disparos

# Función para iniciar el juego
def iniciar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    menu = True

    # -----------------------------MENÚ---------------------------
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(0)

    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                menu = False
        ventana.blit(imgFondo, (0, 0))
        mensajeEnPantalla("Space Invaders", ventana, 150, 100, 100)
        mensajeEnPantalla("Hecho por Luis Alcántara", ventana, 150, 200, 50)
        mensajeEnPantalla("Presiona SPACE para Comenzar", ventana, 150, 400, 50)
        mensajeEnPantalla("Presiona Q para Salir", ventana, 150, 450, 50)

        pygame.display.update()
        reloj.tick(40)
    jugando = True

    # ---------------------------Sprites--------------------------

    # Grupos de Sprites
    universo = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    naveG = pygame.sprite.Group()

    # Nave
    nave = pygame.sprite.Sprite()
    nave.image = imgNave
    nave.rect = imgNave.get_rect()
    nave.rect.x = ANCHO // 2 - nave.rect.width // 2
    nave.rect.y = ALTO // 2 - nave.rect.height // 2
    naveG.add(nave)
    universo.add(nave)

    # Datos iniciales
    puntuacion = 0
    vidas = 3

    # Asteroides
    for x in range(50):
        asteroide = pygame.sprite.Sprite()
        asteroide.image = imgAsteroide
        asteroide.rect = imgAsteroide.get_rect()
        asteroide.rect.x = random.randint(0, ANCHO - asteroide.rect.width)
        asteroide.rect.y = random.randint(-1000, -50)
        asteroide.inicio = random.randint(0, 3)
        asteroide.velocidad = random.randint(1, 5)
        asteroides.add(asteroide)
        universo.add(asteroide)

    # ---------------------------JUEGO----------------------------
    tiempoInicial = int(time.time())
    print(tiempoInicial)
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
        if vidas <= 0:
            jugando = False
        # Muestra el fondo de pantalla
        #ventana.blit(imgFondo, (0, 0))
        ventana.fill(NEGRO)
        # Verifica si hay choques entre los asteroides y las naves
        choques = pygame.sprite.spritecollide(nave, asteroides, True)
        for choque in choques:
            vidas -= 1
        # Verifica controles de la nave
        nave, disparos = validarControlesNave(nave, disparos, universo)

        # Checa por cambios en la puntuación
        puntuacion = validarChoqueDisparoAsteroide(disparos, asteroides, universo, puntuacion)

        # Actualiza los disparos
        actualizarDisparos(disparos)

        # Actualiza el movimiento de los asteroides
        actualizarAsteroides(asteroides, tiempoInicial)

        # Muestra en la pantalla todos los sprites
        universo.draw(ventana)

        # Muestra en pantalla información adicional
        mensajeEnPantalla("Puntuación: %d" % puntuacion, ventana, 550, 30, 40)
        mensajeEnPantalla("Vidas: %d" % vidas, ventana, 30, 30, 40)

        pygame.display.update()
        reloj.tick(40)

    pygame.quit()

def main():
    iniciar()
main()