# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import pygame
import random
import time

ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255, 0, 0)
# Imagenes para el juego
imgFondo = pygame.image.load("Fondos/fondo.png")
imgNave = pygame.image.load("Sprites/nave8bit.png")
imgAsteroide = pygame.image.load("Sprites/asteroide8bit.png")
imgAsteroideD = pygame.image.load("Sprites/asteroide8bitD.png")
imgAsteroideA = pygame.image.load("Sprites/asteroide8bitA.png")
imgAsteroideI = pygame.image.load("Sprites/asteroide8bitI.png")
pygame.mixer.init()

# Imágenes para el menú
imgTeclas = pygame.image.load("Archivos/teclas.png")
imgFlechas = pygame.image.load("Archivos/flechas.png")
imgBE = pygame.image.load("Archivos/space_bar.png")

# Efectos de sonido y música
disparofx = pygame.mixer.Sound("Sonidos/disparosLaser.wav")
disparofx.set_volume(.3)
disparofxFin = pygame.mixer.Sound("Sonidos/disparosLaserFin.wav")
disparofxFin.set_volume(.3)

imgDisparo = pygame.image.load("Sprites/disparo.png")

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
        disparo.rect.y -= 15

# Actualiza la posición de los asteroides
def actualizarAsteroides(asteroides, tiempoInicial, universo):
    for asteroide in asteroides:
        if asteroide.rect.y > 600:
            asteroide.rect.y = random.randint(-500, -100)
            asteroide.rect.x = random.randint(10, 790)
        if asteroide.timer == 15:
            asteroide.image = imgAsteroide
        elif asteroide.timer == 30:
            asteroide.image = imgAsteroideD
        elif asteroide.timer == 45:
            asteroide.image = imgAsteroideA
        elif asteroide.timer == 60:
            asteroide.image = imgAsteroideI
        elif asteroide.timer > 60:
            asteroide.timer = 0

        asteroide.timer += 1
        asteroide.velocidad = random.randint(1, 10)
        asteroide.rect.y += asteroide.velocidad

    return asteroides, universo

# Borra los disparos que estén fuera de rango y comprueba que haya colisiones
def validarChoqueDisparoAsteroide(disparos, asteroides, universo, puntuacion):
    for disparo in disparos:
        if disparo.rect.y <= 0:
            disparos.remove(disparo)
            universo.remove(disparo)

    aciertos = pygame.sprite.groupcollide(disparos, asteroides, True, True)
    contador = 0
    for acierto in aciertos:
        puntuacion += 10
        contador += 1
    return puntuacion, contador


# Valida los controles de la nave
def validarControlesNave(nave, disparos, universo, timer):
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
    if teclasPresionadas[pygame.K_SPACE] and timer > 4/60:
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
        timer = 0
    return nave, disparos, timer

# Devuelve dos objetos, la superficie del texto y el rectangulo
def texto_objeto(texto, font, color):
    ventanaTexto = font.render(texto, True, color)
    return ventanaTexto, ventanaTexto.get_rect()

# Función para crear un botón
def boton (msg, x, y, ancho, alto, ic, ac, ventana, accion):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+ancho > mouse[0] > x) and (y+alto > mouse[1] > y):
        pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto))
        texto = pygame.font.Font("freesansbold.ttf", 20)
        ventanaTexto, textoRect = texto_objeto(msg, texto, BLANCO)
        textoRect.center = ((x + (ancho / 2)), (y + (alto / 2)))
        ventana.blit(ventanaTexto, textoRect)
        if click[0] == 1:
            return False
        else:
            return True
    else:
        pygame.draw.rect(ventana, ic, (x, y, ancho, alto))
        texto = pygame.font.Font("freesansbold.ttf", 20)
        ventanaTexto, textoRect = texto_objeto(msg, texto, NEGRO)
        textoRect.center = ( (x+(ancho/2)), (y+(alto/2)) )
        ventana.blit(ventanaTexto, textoRect)
        return True

# Función para iniciar el juego
def validarPuntuacion(puntuacion):
    entrada = open("Archivos/informacion.txt", "r")



def iniciar():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    menu = True

    # -----------------------------MENÚ---------------------------
    pygame.mixer.music.load('Sonidos/music.mp3')

    # pygame.mixer.music.play(0)
    x = 0
    nivel = 0
    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                menu = False

        ventana.fill(BLANCO)
        ventana.blit(imgFondo, (x, 0))
        ventana.blit(imgFondo, (ANCHO + x, 0))
        x -= 1
        if x <= -ANCHO:
            x = 0
        if nivel == 0:
            mensajeEnPantalla("Space Invaders", ventana, 150, 100, 100)
            mensajeEnPantalla("Hecho por Luis Alcántara", ventana, 200, 200, 50)
            menu = boton("Inicio", 300, 300, 200, 50, BLANCO, NEGRO, ventana, "jugar")
            opcion = boton("Puntuación Alta", 300, 375, 200, 50, BLANCO, NEGRO, ventana, "")
            opcionA = boton("Ayuda", 300, 450, 200, 50, BLANCO, NEGRO, ventana,  "ayuda")
            if opcion == False:
                nivel = 1
            elif opcionA == False:
                nivel = 2
        elif nivel == 1:
            mensajeEnPantalla("Puntuaciones Altas", ventana, 130, 40, 80)
            mensajeEnPantalla("Jugadores:", ventana, 70, 120, 50)
            opcion = boton("Regresar", 325, 520, 150, 50, BLANCO, NEGRO, ventana, "")
            if opcion == False:
                nivel = 0
        elif nivel == 2:
            ventana.blit(imgTeclas, (70,100))
            mensajeEnPantalla("Mover", ventana, 115, 300, 50)
            ventana.blit(imgBE, (450,130))
            mensajeEnPantalla("Disparar", ventana, 510, 300, 50)
            opcion = boton("Regresar", 325, 520, 150, 50, BLANCO, NEGRO, ventana, "")
            if opcion == False:
                nivel = 0
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
    def crearAsteroides(n, vMax):
        for x in range(n):
            asteroide = pygame.sprite.Sprite()
            asteroide.image = imgAsteroide
            asteroide.rect = imgAsteroide.get_rect()
            asteroide.rect.x = random.randint(0, ANCHO - asteroide.rect.width)
            asteroide.rect.y = random.randint(-1000, -250)
            asteroide.velocidad = random.randint(1, vMax)
            asteroide.timer = (random.randint(1,59))
            asteroides.add(asteroide)
            universo.add(asteroide)
    n = 30
    crearAsteroides(n, 5)
    # ---------------------------JUEGO----------------------------
    tiempoInicial = int(time.time())
    timer = 4/60
    while jugando:

        timer += 1 / 60
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    disparofx.play()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    disparofx.fadeout(1)
                    disparofxFin.play()
        if vidas <= 0:
            jugando = False
        if len(asteroides) <= 0 and n <= 200:
            n += 50
            crearAsteroides(n, 5)

        # Muestra el fondo de pantalla
        ventana.blit(imgFondo, (0,0))
        ventana.blit(imgFondo, (x, 0))
        ventana.blit(imgFondo, (ANCHO + x, 0))
        x -= 1
        if x <= -ANCHO:
            x = 0

        # Verifica si hay choques entre los asteroides y las naves
        choques = pygame.sprite.spritecollide(nave, asteroides, True)
        for choque in choques:
            vidas -= 1
        # Verifica controles de la nave
        nave, disparos, timer = validarControlesNave(nave, disparos, universo, timer)

        # Checa por cambios en la puntuación
        puntuacion, nuevos = validarChoqueDisparoAsteroide(disparos, asteroides, universo, puntuacion)

        # Crear nuevos asteroides si han sido destruidos
        crearAsteroides(nuevos, random.randint(1,5))

        # Actualiza los disparos
        actualizarDisparos(disparos)

        # Actualiza el movimiento de los asteroides
        asteroides, universo = actualizarAsteroides(asteroides, tiempoInicial, universo)

        # Muestra en la pantalla todos los sprites
        universo.draw(ventana)

        # Muestra en pantalla información adicional
        mensajeEnPantalla("Puntuación: %d" % puntuacion, ventana, 550, 30, 40)
        mensajeEnPantalla("Vidas: %d" % vidas, ventana, 30, 30, 40)
        pygame.display.update()
        reloj.tick(60)
    pygame.quit()

    validarPuntuacion(puntuacion)

def main():
    iniciar()
main()