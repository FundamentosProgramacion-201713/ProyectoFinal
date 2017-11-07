# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import pygame
from random import randint

ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)

#Inicia el pygame con la pantalla y el menú
def iniciar():
    pygame.init()
    imagenFondo = pygame.image.load("fondo.png")
    nave = pygame.image.load("nave.PNG")
    alien = pygame.image.load("alien2.png")

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Galaluich")
    reloj = pygame.time.Clock()
    termina = False

    # Las dimensiones de la nave
    xNave = 150
    yNave = 120

    # Las dimensiones del enemigo
    xAlien = 37
    yAlien = 37

    # Posición de la nave inicial
    dx = 400
    dy = 400

    # Posición del enemigo inicial
    dAlien = randint(100, 200)
    dAlien2 = randint(100, 200)
    factorA1 = 1

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        # Teclas presionadas
        teclasPresionadas = pygame.key.get_pressed()

        # Verificar si alguna tecla del control fue presionada
        if teclasPresionadas[pygame.K_LEFT] and dx > 0:
            dx -= 10
        if teclasPresionadas[pygame.K_RIGHT] and dx < ANCHO - xNave:
            dx += 10
        if teclasPresionadas[pygame.K_UP] and dy > 0:
            dy -= 10
        if teclasPresionadas[pygame.K_DOWN] and dy < ALTO - yNave:
            dy += 10

        # Comprobar la dirección del enemgio y cambiarla de ser necesarop
        if dAlien > 600 -yAlien or dAlien < 0:
            factorA1 = factorA1 * -1

        # Actualización de la nave y el enemigo
        ventana.blit(imagenFondo, (0, 0))
        ventana.blit(nave, (dx, dy))
        ventana.blit(alien, (100,dAlien))

        # Suma aleatoria de la velocidad del alien
        dAlien +=  factorA1* 15


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    iniciar()
main()