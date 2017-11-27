# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Videojuego proyecto final

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)

def generarColor():
    return (randint(0,255),randint(0,255),randint(0,255))

def dibujarMenu(ventana, botonJugar,botonRecords,botonCreditos):
    ventana.blit(botonJugar.image,botonJugar.rect) # boton jugar
    ventana.blit(botonRecords.image,botonRecords.rect) # boton records
    ventana.blit(botonCreditos.image,botonCreditos.rect) # boton créditos

    colorAleatorio = generarColor()
    fuente = pygame.font.SysFont("monospace", 80) # título del juego
    texto = fuente.render("El último viajero", 1,colorAleatorio)
    ventana.blit(texto, ((ANCHO//2)-220, 100))

def dibujarJuego(ventana, listaEnemigos, pantuflas):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)
    ventana.blit(pantuflas.image,pantuflas.rect)
    # limitar dentro de la pantalla
    if pantuflas.rect.left <= 0:
        pantuflas.rect.left = 0
    elif pantuflas.rect.left >= ANCHO - pantuflas.rect.width:
        pantuflas.rect.left = ANCHO - pantuflas.rect.width
    elif pantuflas.rect.top <= 0:
        pantuflas.rect.top = 0
    elif pantuflas.rect.top >= ALTO-pantuflas.rect.height:
        pantuflas.rect.top = ALTO-pantuflas.rect.height

def imprimirTexto(ventana, timer,danio):
    fuente = pygame.font.SysFont("monospace",24)
    temporizador = fuente.render("Tiempo: " + str(timer),1,BLANCO)
    danio = fuente.render(str(danio),1,BLANCO)
    ventana.blit(temporizador,(ANCHO-150,20))
    ventana.blit(danio, (ANCHO-150,50))

def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    cy = randint(enemigo.rect.height, ALTO-enemigo.rect.height)
    enemigo.rect.left = ANCHO
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)

def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 10
        if enemigo.rect.left < -enemigo.rect.width:
            listaEnemigos.remove(enemigo)
            continue

def dibujarRecords(ventana,botonMenu):
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("Récords: ", 1, BLANCO)
    ventana.blit(texto, ((ANCHO//2)-220, 100))
    ventana.blit(botonMenu.image,botonMenu.rect) # boton créditos

def dibujarCreditos(ventana,botonMenu):
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("Créditos: ", 1, BLANCO)
    ventana.blit(texto, ((ANCHO//2)-220, 100))
    ventana.blit(botonMenu.image,botonMenu.rect) # boton créditos

def dibujar():
    # Inicio de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Condiciones iniciales
    estado = "menu" # jugando, fin
    x = 0  # inicio fondo
    timer = 0
    danio = 0

    # Cargar imagen fondo
    imgFondo = pygame.image.load("images/imagen-fondo.jpg")

    # Cargar imágenes botones
    imgBtnJugar = pygame.image.load("images/button_jugar.png")
    imgBtnRecords = pygame.image.load("images/button_records.png")
    imgBtnCreditos = pygame.image.load("images/button_creditos.png")
    imgBtnMenu = pygame.image.load("images/button_menu.png")

    # Cargar imagen Pantuflas
    imgPantuflas = pygame.image.load("images/pantuflas-el-perro.jpg") # cambiar a .png cuando Dany

    # Sprites
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width//2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height//2

    botonRecords = pygame.sprite.Sprite()
    botonRecords.image = imgBtnRecords
    botonRecords.rect = imgBtnRecords.get_rect()
    botonRecords.rect.left = ANCHO // 2 - botonRecords.rect.width - 20
    botonRecords.rect.top = ALTO // 2 + botonJugar.rect.height//2 + botonRecords.rect.height

    botonCreditos = pygame.sprite.Sprite()
    botonCreditos.image = imgBtnCreditos
    botonCreditos.rect = imgBtnCreditos.get_rect()
    botonCreditos.rect.left = ANCHO // 2 + 20
    botonCreditos.rect.top = ALTO // 2 + botonJugar.rect.height//2 + botonCreditos.rect.height

    botonMenu = pygame.sprite.Sprite()
    botonMenu.image = imgBtnMenu
    botonMenu.rect = imgBtnMenu.get_rect()
    botonMenu.rect.left = 50
    botonMenu.rect.top = 50

    pantuflas = pygame.sprite.Sprite()
    pantuflas.image = imgPantuflas
    pantuflas.rect = imgPantuflas.get_rect()
    pantuflas.rect.left = 50
    pantuflas.rect.top = ALTO // 2 - pantuflas.rect.height//2

    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("images/nave-malvada.png")

    # Balas
    listaBalas = []
    #imgBala = pygame.image.load("bullet.jpg")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xbJ, ybJ, anchoBJ, altoBJ = botonJugar.rect
                    xbR, ybR, anchoBR, altoBR = botonRecords.rect
                    xbC, ybC, anchoBC, altoBC = botonCreditos.rect
                    if xbJ <= xm <= xbJ+anchoBJ:
                        if ybJ <= ym <= ybJ+altoBJ:
                            # Cambiar de ventana
                            estado = "jugando"
                    elif xbR <= xm <= xbR + anchoBR:
                        if ybR <= ym <= ybR + altoBR:
                            # Cambiar de ventana
                            estado = "records"
                    elif xbC <= xm <= xbC + anchoBC:
                        if ybC <= ym <= ybC + altoBC:
                            # Cambiar de ventana
                            estado = "creditos"
                elif estado == "records" or estado == "creditos":
                    xbM, ybM, anchoBM, altoBM = botonMenu.rect
                    if xbM <= xm <= xbM+anchoBM:
                        if ybM <= ym <= ybM+altoBM:
                            # Regresar a menu
                            estado = "menu"

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    pantuflas.rect.top -= 20
                if evento.key == pygame.K_s:
                    pantuflas.rect.top += 20
                if evento.key == pygame.K_a:
                    pantuflas.rect.left -= 20
                if evento.key == pygame.K_d:
                    pantuflas.rect.left += 20

        # Borrar pantalla
        ventana.fill(BLANCO)
        ventana.blit(imgFondo,(x,0))
        ventana.blit(imgFondo,(ANCHO+x,0))
        x -= 1
        if x <= -ANCHO:
            x = 0

        # Mover enemigos
        moverEnemigos(listaEnemigos)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana,botonJugar,botonRecords,botonCreditos)
        elif estado == "jugando":
        #    actualizarBalas(listaBalas,listaEnemigos)
            dibujarJuego(ventana,listaEnemigos,pantuflas)
            imprimirTexto(ventana, timer,danio) # Imprimir texto
            timer += 1 / 40
            if timer >= 0.5: # Generar enemigos cada segundo
                timer = 0
                generarEnemigoAzar(listaEnemigos, imgEnemigo)
        elif estado == "records":
            dibujarRecords(ventana,botonMenu)
        elif estado == "creditos":
            dibujarCreditos(ventana,botonMenu)
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def main():
    dibujar()

main()