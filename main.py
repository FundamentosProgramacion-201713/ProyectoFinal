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
imgNave = pygame.image.load("Imagenes/nave.png")
imgAsteroide = pygame.image.load("Imagenes/asteroide.png")
imgAsteroideD = pygame.image.load("Imagenes/asteroideM.png")
imgAsteroideA = pygame.image.load("Imagenes/asteroideG.png")
imgAsteroideI = pygame.image.load("Imagenes/asteroideM.png")
imgLookMorty = pygame.image.load("Imagenes/look.png")
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
showMe = pygame.mixer.Sound("Sonidos/showMe.wav")
wubba = pygame.mixer.Sound("Sonidos/wubba.wav")
wubba.set_volume(.3)

imgDisparo = pygame.image.load("Imagenes/disparo.png")
imgGameOver = pygame.image.load("Imagenes/gameover.png")

# Mostrar un mensaje en pantalla
def mensajeEnPantalla(m, ventana, x, y, tamano):
    font = pygame.font.SysFont("Arial", tamano)
    texto = font.render(m ,True, (255,255,255))
    ventana.blit(texto, [x,  y])

# Actualiza la posición de los disparos
def actualizarDisparos(disparos):
    for disparo in disparos:
        if disparo.rect.x > 800:
            disparos.remove(disparo)
        disparo.rect.x += 15

# Actualiza la posición de los asteroides
def actualizarAsteroides(asteroides, tiempoInicial, universo):
    for asteroide in asteroides:
        if asteroide.rect.x < 0-asteroide.rect.width:
            asteroide.rect.y = random.randint(asteroide.rect.height, ALTO -asteroide.rect.height )
            asteroide.rect.x = random.randint(800, 2000)
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
        asteroide.rect.x -= asteroide.velocidad

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

        # Disparo
        disparo = pygame.sprite.Sprite()
        disparo.image = imgDisparo
        disparo.rect = imgDisparo.get_rect()
        disparo.rect.x = nave.rect.x + nave.rect.width - 10
        disparo.rect.y = nave.rect.y + nave.rect.height // 2
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

# Función para validar el puntaje y en todo caso escribirlo en el archivo
def validarPuntuacion(puntuacion):
    entrada = open("Archivos/informacion.txt", "r")
    datos = entrada.readlines()
    entrada.close()
    puntuaciones = []
    nombres = []
    nuevasP = []
    for x in range(len(datos)):
        datos[x] = datos[x].rstrip()
        lista = datos[x].split(":")
        puntuaciones.append(int(lista[1]))
        nombres.append(lista[0])

    if puntuacion > min(puntuaciones):
        puntuaciones[puntuaciones.index(min(puntuaciones))] = puntuacion
        nombre = input("¡Entras en los primeros tres lugares! Escribe tu nombre: ")
        if puntuacion > puntuaciones[0]:
            intermedio = puntuaciones[0]
            intermedioN = nombres[0]
            puntuaciones[0] = puntuacion
            nombres[0] = nombre
            puntuaciones[2] = puntuaciones[1]
            nombres[2] = nombres[1]
            puntuaciones[1] = intermedio
            nombres[1] = intermedioN
        elif puntuacion > puntuaciones[1]:
            intermedio = puntuaciones[1]
            intermedioN = nombres[1]
            puntuaciones[1] = puntuacion
            nombres[1] = nombre
            puntuaciones[2] = intermedio
            nombres[2] = intermedioN
        else:
            nombres[2] = nombre
        datos = ""
        for x in range(3):
            datos += nombres[x] + ":" + str(puntuaciones[x]) + "\n"
        salida = open("Archivos/informacion.txt", "w")
        salida.write(datos)
        salida.close()

# Función para iniciar el juego
def iniciar():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    menu = True

    # -----------------------------MENÚ---------------------------
    x = 0
    nivel = 0
    pygame.mixer.music.load("Sonidos/menuMusic.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(0)
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

            entrada = open("Archivos/informacion.txt", "r")
            datos = entrada.readlines()
            nombres = []
            puntuaciones = []

            for linea in datos:
                linea = linea.rstrip()
                linea = linea.split(":")
                nombres.append(linea[0])
                puntuaciones.append(linea[1])

            mensajeEnPantalla(nombres[0], ventana, 140, 170, 70)
            mensajeEnPantalla(nombres[1], ventana, 140, 250, 70)
            mensajeEnPantalla(nombres[2], ventana, 140, 330, 70)

            mensajeEnPantalla(puntuaciones[0], ventana, 500, 170, 70)
            mensajeEnPantalla(puntuaciones[1], ventana, 500, 250, 70)
            mensajeEnPantalla(puntuaciones[2], ventana, 500, 330, 70)

            opcion = boton("Regresar", 325, 520, 150, 50, BLANCO, NEGRO, ventana, "")
            if opcion == False:
                nivel = 0
        elif nivel == 2:
            ventana.blit(imgTeclas, (100,80))
            ventana.blit(imgLookMorty, (-50, 289))
            mensajeEnPantalla("Mover", ventana, 130, 250, 50)
            ventana.blit(imgBE, (480,100))
            mensajeEnPantalla("Disparar", ventana, 510, 250, 50)
            mensajeEnPantalla("Las imágenes y el contenido es propiedad ", ventana, 300, 400, 20)
            mensajeEnPantalla("de Rick and Morty (creado por Justin Roilland y Dan Harmon)", ventana, 300, 420, 20)
            opcion = boton("Regresar", 325, 520, 150, 50, BLANCO, NEGRO, ventana, "")
            if opcion == False:
                nivel = 0
        pygame.display.update()
        reloj.tick(40)
    jugando = True
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sonidos/stranger.wav")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(0)
    showMe.play()
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

    # Generación de asteroides
    def crearAsteroides(n, vMax, puntuacion):
        puntuacion = puntuacion // 100
        vMax += puntuacion
        vMin = 0 + puntuacion
        for x in range(n):
            asteroide = pygame.sprite.Sprite()
            asteroide.image = imgAsteroide
            asteroide.rect = imgAsteroide.get_rect()
            asteroide.rect.x = random.randint(800, 2000)
            asteroide.rect.y = random.randint(asteroide.rect.height, ALTO - asteroide.rect.height)
            asteroide.velocidad = random.randint(1, vMax)
            asteroide.timer = (random.randint(1,59))
            asteroides.add(asteroide)
            universo.add(asteroide)
    n = 30
    crearAsteroides(n, 5, 0)
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

        # Muestra el fondo de pantalla
        ventana.blit(imgFondo, (0,0))
        ventana.blit(imgFondo, (x, 0))
        ventana.blit(imgFondo, (ANCHO + x, 0))
        x -= 5
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
        crearAsteroides(nuevos, random.randint(1,5), puntuacion)

        # Actualiza los disparos
        actualizarDisparos(disparos)

        # Actualiza el movimiento de los asteroides
        asteroides, universo = actualizarAsteroides(asteroides, tiempoInicial, universo)

        # Muestra en la pantalla todos los sprites
        universo.draw(ventana)

        # Muestra en pantalla información adicional
        mensajeEnPantalla("Puntuación: %d" % puntuacion, ventana, 550, 30, 40)
        mensajeEnPantalla("Vidas: %d" % vidas, ventana, 30, 30, 40)
        if puntuacion % 500  == 0 and puntuacion > 0:
            wubba.play()
        pygame.display.update()
        reloj.tick(60)
    final = True
    while final:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                final = False


        ventana.blit(imgFondo, (0, 0))
        ventana.blit(imgFondo, (x, 0))
        ventana.blit(imgFondo, (ANCHO + x, 0))
        x -= 5
        if x <= -ANCHO:
            x = 0
        ventana.blit(imgGameOver, (200,93))
        mensajeEnPantalla("Tu puntuación:", ventana, 150, 300, 60)
        mensajeEnPantalla(str(puntuacion), ventana, 500, 300, 60)


        pygame.display.update()
        reloj.tick(60)

    pygame.quit()
    validarPuntuacion(puntuacion)


def main():
    iniciar()
main()