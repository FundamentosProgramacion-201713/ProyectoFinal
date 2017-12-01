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
NEGRO = (0,0,0)

def generarColor():
    return (randint(0,255),randint(0,255),randint(0,255))

def dibujarMenu(ventana, botonJugar,botonRecords,botonCreditos,botonControles):
    ventana.blit(botonJugar.image,botonJugar.rect) # boton jugar
    ventana.blit(botonRecords.image,botonRecords.rect) # boton records
    ventana.blit(botonCreditos.image,botonCreditos.rect) # boton créditos
    ventana.blit(botonControles.image,botonControles.rect) # botón controles

    colorAleatorio = generarColor()
    fuente = pygame.font.SysFont("monospace", 80) # título del juego
    texto1 = fuente.render("Pantuflas,", 1,colorAleatorio)
    texto2 = fuente.render("el viajero espacial",1,colorAleatorio)
    ventana.blit(texto1, ((ANCHO//2)-220, 80))
    ventana.blit(texto2, ((ANCHO//2)-220, 130))

def dibujarJuego(ventana, listaEnemigos, pantuflas,timer,vidas,cronometro,puntaje):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)
    ventana.blit(pantuflas.image,pantuflas.rect)

    fuente = pygame.font.SysFont("monospace",24)
    temporizador = fuente.render("%.2f" % timer,1,BLANCO)
    tiempo = fuente.render("Tiempo restante: %.d" % cronometro, 1, BLANCO)
    lifes = fuente.render("Vidas: " +str(vidas),1,BLANCO)
    score = fuente.render("Puntaje: " +str(puntaje),1,BLANCO)
    ventana.blit(temporizador,(ANCHO-200,20))
    ventana.blit(tiempo, (ANCHO-200,50))
    ventana.blit(lifes, (ANCHO-200,80))
    ventana.blit(score, (ANCHO-200,110))

def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    cy = randint(0, ALTO-enemigo.rect.height)
    enemigo.rect.left = ANCHO
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)

def actualizarEnemigos(listaEnemigos,pantuflas,vidas):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 10
        if enemigo.rect.left < -enemigo.rect.width or enemigo.rect.colliderect(pantuflas):
            listaEnemigos.remove(enemigo)
        if enemigo.rect.colliderect(pantuflas):
            vidas -= 1
    return vidas

def activarPoder(puntaje,listaEnemigos,pantuflas):
    for enemigo in listaEnemigos:
        if enemigo.rect.colliderect(pantuflas):
            puntaje += 1
    return puntaje

def dibujarRecords(ventana,botonMenu):
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("Récords: ", 1, BLANCO)
    ventana.blit(texto, ((ANCHO//2)-220, 100))
    ventana.blit(botonMenu.image,botonMenu.rect) # boton menú

def dibujarCreditos(ventana,botonMenu):
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("Créditos: ", 1, BLANCO)

    ventana.blit(texto, ((ANCHO//2)-220, 100))
    ventana.blit(botonMenu.image,botonMenu.rect) # boton menú

def dibujarControles(ventana, botonMenu):
    fuente = pygame.font.SysFont("monospace", 70)
    titulo = fuente.render("Controles: ", 1, BLANCO)
    w = fuente.render("W --------- ARRIBA",1,BLANCO)
    a = fuente.render("A --------- ATRÁS",1,BLANCO)
    s = fuente.render("S --------- ABAJO",1,BLANCO)
    d = fuente.render("D --------- DELANTE",1,BLANCO)
    ventana.blit(titulo, ((ANCHO // 2), 100))
    ventana.blit(w, ((ANCHO // 2), 200))
    ventana.blit(a, ((ANCHO // 2), 250))
    ventana.blit(s, ((ANCHO // 2), 300))
    ventana.blit(d, ((ANCHO // 2), 350))
    ventana.blit(botonMenu.image, botonMenu.rect)  # boton menú

def dibujarFinMalo(ventana,botonMenu,botonReintentar):
    fuente = pygame.font.SysFont("monospace", 50)
    texto = fuente.render("Pantuflas no pudo llegar a casa. :-(",1,BLANCO)
    ventana.blit(texto,((ANCHO//2)-220, 150))
    ventana.blit(botonMenu.image,botonMenu.rect)
    ventana.blit(botonReintentar.image,botonReintentar.rect)

def dibujarFinBueno(ventana, botonMenu):
    fuente = pygame.font.SysFont("monospace", 50)
    texto = fuente.render("Pantuflas llegó a casa. :-D",1,BLANCO)
    ventana.blit(texto,((ANCHO//2)-220,150))
    ventana.blit(botonMenu.image,botonMenu.rect)

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
    poder = False
    cargaPoder = 0
    tiempoPoder = 10
    vidas = 3
    puntaje = 0
    moverPantuflasLateral = False
    moverPantuflasVertical = False
    dx = 0
    dy = 0

    # Música fondo
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/musicaFondo.mp3")
    pygame.mixer.music.play(-1)

    # Cargar imagen fondo
    imgFondo = pygame.image.load("images/imagen-fondo.jpg")

    # Cargar imágenes botones
    imgBtnJugar = pygame.image.load("images/button_jugar.png")
    imgBtnRecords = pygame.image.load("images/button_records.png")
    imgBtnCreditos = pygame.image.load("images/button_creditos.png")
    imgBtnMenu = pygame.image.load("images/button_menu.png")
    imgBtnReintentar = pygame.image.load("images/button_reintentar.png")
    imgBtnControles = pygame.image.load("images/button_controles.png")

    # Cargar imagen Pantuflas
    imgPantuflas = pygame.image.load("images/pantuflas-el-perro.png") # cambiar a .png cuando Dany

    # Enemigos
    listaEnemigos = []
    imgEnemigo1 = pygame.image.load("images/nave-malvada-1.png")
    imgEnemigo2 = pygame.image.load("images/nave-malvada-2.png")
    imgEnemigo3 = pygame.image.load("images/nave-malvada-3.png")
    imgEnemigo4 = pygame.image.load("images/nave-malvada-4.png")
    imgEnemigo5 = pygame.image.load("images/nave-malvada-5.png")

    # Sprites
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width//2
    botonJugar.rect.top = ALTO // 2 - 3*botonJugar.rect.height//2

    botonControles = pygame.sprite.Sprite()
    botonControles.image = imgBtnControles
    botonControles.rect = imgBtnControles.get_rect()
    botonControles.rect.left = ANCHO // 2 - botonControles.rect.width//2
    botonControles.rect.top = ALTO // 2 + 3*botonControles.rect.height//2

    botonRecords = pygame.sprite.Sprite()
    botonRecords.image = imgBtnRecords
    botonRecords.rect = imgBtnRecords.get_rect()
    botonRecords.rect.left = ANCHO // 2 - botonRecords.rect.width - 20
    botonRecords.rect.top = ALTO // 2

    botonCreditos = pygame.sprite.Sprite()
    botonCreditos.image = imgBtnCreditos
    botonCreditos.rect = imgBtnCreditos.get_rect()
    botonCreditos.rect.left = ANCHO // 2 + 20
    botonCreditos.rect.top = ALTO // 2

    botonMenu = pygame.sprite.Sprite()
    botonMenu.image = imgBtnMenu
    botonMenu.rect = imgBtnMenu.get_rect()
    botonMenu.rect.left = 50
    botonMenu.rect.top = 50

    botonReintentar = pygame.sprite.Sprite()
    botonReintentar.image = imgBtnReintentar
    botonReintentar.rect = imgBtnReintentar.get_rect()
    botonReintentar.rect.left = 50
    botonReintentar.rect.top = 100

    pantuflas = pygame.sprite.Sprite()
    pantuflas.image = imgPantuflas
    pantuflas.rect = imgPantuflas.get_rect()
    pantuflas.rect.left = 50
    pantuflas.rect.top = ALTO // 2 - pantuflas.rect.height//2

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
                    xBcontrol, ybcontrol, anchoBcontrol, altoBcontrol = botonControles.rect

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

                    elif xBcontrol <= xm <= xBcontrol + anchoBcontrol:
                        if ybcontrol <= ym <= ybcontrol + altoBcontrol:
                            # Cambiar ventana
                            estado = "controles"

                elif estado == "records" or estado == "creditos" or estado == "controles":
                    xbM, ybM, anchoBM, altoBM = botonMenu.rect

                    if xbM <= xm <= xbM+anchoBM:
                        if ybM <= ym <= ybM+altoBM:
                            # Regresar a menu
                            estado = "menu"

                elif estado == "finMalo":
                    xbRe, ybRe, anchoBRe, altoBRe = botonReintentar.rect
                    xbM, ybM, anchoBM, altoBM = botonMenu.rect

                    if xbRe <= xm <= xbRe+anchoBRe:
                        if ybRe <= ym <= ybRe+altoBRe:
                            # intentar otra vez
                            estado = "jugando"

                    if xbM <= xm <= xbM+anchoBM:
                        if ybM <= ym <= ybM+altoBM:
                            # Regresar a menú
                            estado = "menu"

                elif estado == "finBueno":
                    xbM, ybM, anchoBM, altoBM = botonMenu.rect

                    if xbM <= xm <= xbM+anchoBM:
                        if ybM <= ym <= ybM+altoBM:
                            # Regresar a menú
                            estado = "menu"


            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    moverPantuflasVertical = True
                    dy = -10
                if evento.key == pygame.K_s:
                    moverPantuflasVertical = True
                    dy = +10
                if evento.key == pygame.K_a:
                    moverPantuflasLateral = True
                    dx = -10
                if evento.key == pygame.K_d:
                    moverPantuflasLateral = True
                    dx = +10
                if evento.key == pygame.K_SPACE:
                    poder = True

            elif evento.type == pygame.KEYUP:
                moverPantuflasLateral = False
                moverPantuflasVertical = False

        # Borrar pantalla
        ventana.fill(BLANCO)
        ventana.blit(imgFondo,(x,0))
        ventana.blit(imgFondo,(ANCHO+x,0))
        x -= 1
        if x <= -ANCHO:
            x = 0

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana,botonJugar,botonRecords,botonCreditos,botonControles)
            timer = 0
            cronometro = 90
            vidas = 3
            moverPantuflasLateral = False
            moverPantuflasVertical = False

        elif estado == "jugando":
            vidas = actualizarEnemigos(listaEnemigos,pantuflas,vidas) # Mover enemigos
            dibujarJuego(ventana,listaEnemigos,pantuflas,timer,vidas,cronometro,puntaje)
            timer += 1 / 40
            cronometro -= 1 / 40
            if timer >= 1 and cronometro > 80: # Generar enemigos cada segundo
                timer = 0
                generarEnemigoAzar(listaEnemigos, imgEnemigo1)
            elif timer >= 1 and 60 < cronometro <= 80: # Generar enemigos cada segundo
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo1)
                generarEnemigoAzar(listaEnemigos,imgEnemigo2)
            elif timer >= 1.5 and 45 < cronometro <= 60: # Generar enemigos cada dos segundos
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo1)
                generarEnemigoAzar(listaEnemigos,imgEnemigo2)
                generarEnemigoAzar(listaEnemigos,imgEnemigo3)
            elif timer >= 1.5 and 30 < cronometro <= 45: # Generar enemigos cada dos segundos
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo3)
                generarEnemigoAzar(listaEnemigos,imgEnemigo4)
            elif timer >= 1.5 and 20 < cronometro <= 30: # Generar enemigos cada dos segundos
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo2)
                generarEnemigoAzar(listaEnemigos,imgEnemigo5)
            elif timer >= 1.5 and 10 < cronometro <= 20: # Generar enemigos cada dos segundos
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo1)
                generarEnemigoAzar(listaEnemigos,imgEnemigo5)
            elif timer >= 0.5 and 0 < cronometro <= 10: # Generar enemigos cada medio segundo
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo1)

            if poder:
                if tiempoPoder > 0:
                    tiempoPoder -= 1 / 40
                    puntaje = activarPoder(puntaje, listaEnemigos, pantuflas)
                elif tiempoPoder == 0:
                    cargaPoder = 30
                    tiempoPoder = 10
                    poder = False

            if moverPantuflasLateral:
                pantuflas.rect.left += dx
            if moverPantuflasVertical:
                pantuflas.rect.top += dy

            # limitar dentro de la pantalla
            if pantuflas.rect.left <= 0 or pantuflas.rect.left >= ANCHO - pantuflas.rect.width:
                moverPantuflasLateral = False
                dx = 0
            if pantuflas.rect.top <= 0 or pantuflas.rect.top >= ALTO - pantuflas.rect.height:
                moverPantuflasVertical = False
                dy = 0
                
            if vidas == 0:
                estado = "finMalo"
            if cronometro <= 0:
                estado = "finBueno"

        elif estado == "records":
            dibujarRecords(ventana,botonMenu)
        elif estado == "creditos":
            dibujarCreditos(ventana,botonMenu)
        elif estado == "controles":
            dibujarControles(ventana,botonMenu)
        elif estado == "finMalo":
            dibujarFinMalo(ventana,botonMenu,botonReintentar)
            vidas = 3
            cronometro = 90
        elif estado == "finBueno":
            dibujarFinBueno(ventana,botonMenu)
            vidas = 3
            cronometro = 90

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def main():
    dibujar()

main()