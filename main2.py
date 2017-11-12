# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import pygame
import random

ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
NEGRO = (0,0,0)
imgFondo = pygame.image.load("fondo.png")
imgNave = pygame.image.load("nave.PNG")
imgAsteroide = pygame.image.load("asteroide.png")
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
def actualizarAsteroides(asteroides):
    for asteroide in asteroides:
        asteroide.rect.y += asteroide.velocidad

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
        disparo = pygame.sprite.Sprite()
        disparo.image = imgDisparo
        disparo.rect = imgDisparo.get_rect()
        disparo.rect.x = nave.rect.x + nave.rect.width // 2 - 5
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

    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                menu = False
        ventana.blit(imgFondo, (0, 0))
        mensajeEnPantalla("Space Invaders", ventana, 150, 50, 100)
        pygame.display.update()
        reloj.tick(40)
    jugando = True

    # ---------------------------Sprites--------------------------

    # Grupos de Sprites
    universo = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    disparos = pygame.sprite.Group()

    # Nave
    nave = pygame.sprite.Sprite()
    nave.image = imgNave
    nave.rect = imgNave.get_rect()
    nave.rect.x = ANCHO // 2 - nave.rect.width // 2
    nave.rect.y = ALTO // 2 - nave.rect.height // 2
    universo.add(nave)

    # Datos iniciales
    puntuacion = 0

    # Asteroides
    for x in range(50):
        asteroide = pygame.sprite.Sprite()
        asteroide.image = imgAsteroide
        asteroide.rect = imgAsteroide.get_rect()
        asteroide.rect.x = random.randint(0, ANCHO - asteroide.rect.width)
        asteroide.rect.y = random.randint(-1000, -50)
        asteroide.velocidad = random.randint(1, 5)
        asteroides.add(asteroide)
        universo.add(asteroide)

    # ---------------------------JUEGO----------------------------
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        nave, disparos = validarControlesNave(nave, disparos, universo)
        pygame.sprite.spritecollide(nave, asteroides, True)
        ventana.blit(imgFondo, (0, 0))
        puntuacion = validarChoqueDisparoAsteroide(disparos, asteroides, universo, puntuacion)
        actualizarDisparos(disparos)
        actualizarAsteroides(asteroides)
        universo.draw(ventana)
        mensajeEnPantalla("Puntuación: %d" % puntuacion, ventana, 450, 30, 40)
        pygame.display.update()
        reloj.tick(40)
    pygame.quit()

def main():
    iniciar()
main()