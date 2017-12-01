# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González
# Videojuego proyecto final Fundamentos de programación 201713

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]

def generarColor():
    return (randint(0,255),randint(0,255),randint(0,255))

def dibujarMenu(ventana, botonJugar,botonCreditos):
    ventana.blit(botonJugar.image,botonJugar.rect) # boton jugar
    ventana.blit(botonCreditos.image,botonCreditos.rect) # boton créditos

    fuente = pygame.font.SysFont("monospace", 24)
    titulo = fuente.render("Controles: ", 1, BLANCO)
    w = fuente.render("W ----------------- ARRIBA", 1, BLANCO)
    a = fuente.render("A ----------------- ATRÁS", 1, BLANCO)
    s = fuente.render("S ----------------- ABAJO", 1, BLANCO)
    d = fuente.render("D ----------------- DELANTE", 1, BLANCO)
    space = fuente.render("BARRA ESPACIADORA ----------------- PODER ESPECIAL",1,BLANCO)
    ventana.blit(titulo, ((ANCHO // 2 - 40), ALTO//2 + 60))
    ventana.blit(w, (ANCHO // 2 - 62, ALTO//2 + 80))
    ventana.blit(a, (ANCHO // 2 - 60, ALTO//2 + 100))
    ventana.blit(s, (ANCHO // 2 - 60, ALTO//2 + 120))
    ventana.blit(d, (ANCHO // 2 - 60, ALTO//2 + 140))
    ventana.blit(space, (ANCHO // 2 - 236, ALTO // 2 + 160))

    colorAleatorio = generarColor()
    fuente = pygame.font.SysFont("monospace", 80) # título del juego
    fuenteb = pygame.font.SysFont("monospace", 40)
    texto1 = fuente.render("Pantuflas,", 1,colorAleatorio)
    texto2 = fuente.render("el viajero espacial",1,colorAleatorio)
    inst = fuenteb.render("AYUDA A PANTUFLAS A VOLVER A CASA",1,colorAleatorio)
    ventana.blit(texto1, ((ANCHO//2)-250, 80))
    ventana.blit(texto2, ((ANCHO//2)-250, 130))
    ventana.blit(inst, (ANCHO // 2 - 280, ALTO//2 + 200))


def dibujarJuego(ventana,listaEnemigos,pantuflas,vidas,cronometro,puntaje,tiempoPoder,cargaPoder):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)
    ventana.blit(pantuflas.image,pantuflas.rect)

    fuente = pygame.font.SysFont("monospace",24)
    tiempo = fuente.render("Tiempo restante: %.d" % cronometro, 1, BLANCO)
    lifes = fuente.render("Vidas: " +str(vidas),1,BLANCO)
    score = fuente.render("Puntaje: " +str(puntaje),1,BLANCO)
    powertime = fuente.render("Invencible por: %.d s" % tiempoPoder,1,BLANCO)
    powercharge = fuente.render("Tiempo de carga: %.d s" % cargaPoder,1,BLANCO)
    ventana.blit(tiempo, (ANCHO-200,50))
    ventana.blit(lifes, (ANCHO-200,80))
    ventana.blit(score, (ANCHO-200,110))
    ventana.blit(powercharge,(ANCHO-200,140))
    if cargaPoder < 1:
        ventana.blit(powertime,(ANCHO-200,170))

def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    cy = randint(0, ALTO-enemigo.rect.height)
    enemigo.rect.left = ANCHO
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)

def actualizarEnemigos(listaEnemigos,pantuflas,vidas,poder,tiempoPoder,puntaje,cargaPoder):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 10
        if enemigo.rect.left < -enemigo.rect.width or enemigo.rect.colliderect(pantuflas):
            listaEnemigos.remove(enemigo)

        if poder:
            cargaPoder = 0
            if enemigo.rect.colliderect(pantuflas):
                puntaje += 1

            if tiempoPoder >= 0:
                tiempoPoder -= 1 / 40
            elif tiempoPoder < 0:
                poder = False

        if not poder:
            cargaPoder += 1 / 40
            tiempoPoder = cargaPoder
            if enemigo.rect.colliderect(pantuflas):
                vidas -= 1
    return vidas,puntaje,tiempoPoder,cargaPoder

def dibujarCreditos(ventana,botonMenu):
    fuentet = pygame.font.SysFont("monospace",70)
    fuentec = pygame.font.SysFont("monospace",30)
    titulo = fuentet.render("Créditos: ", 1, BLANCO)
    dany = fuentec.render('Daniela Hernández Méndez -------- Diseño y coloreado "Pantuflas"',1,BLANCO)
    benji = fuentec.render('Benjamín Rodríguez Vázquez -------- Música de fondo',1,BLANCO)
    extras = fuentec.render('pixabay.com -------- Naves e imagen de fondo',1,BLANCO)
    io = fuentec.render('Ángel Guillermo Ortiz González -------- Programación y compilado',1,BLANCO)
    py = fuentec.render('Hecho en pygame',1,BLANCO)

    ventana.blit(titulo, (ANCHO//2 - 350,110))
    ventana.blit(dany, (ANCHO//2 - 350,180))
    ventana.blit(benji, (ANCHO//2 - 350,210))
    ventana.blit(extras, (ANCHO//2 - 350,240))
    ventana.blit(io, (ANCHO//2 - 350,270))
    ventana.blit(py, (ANCHO//2 - 350,330))

    ventana.blit(botonMenu.image,botonMenu.rect) # boton menú

def dibujarFinMalo(ventana,botonMenu,botonReintentar,pantuflasT):
    fuente = pygame.font.SysFont("monospace", 50)
    texto = fuente.render("Pantuflas no pudo llegar a casa. :-(",1,BLANCO)
    ventana.blit(texto,((ANCHO//2)-220, 150))
    ventana.blit(botonMenu.image,botonMenu.rect)
    ventana.blit(botonReintentar.image,botonReintentar.rect)
    ventana.blit(pantuflasT.image,pantuflasT.rect)

def dibujarFinBueno(ventana, botonMenu,pantuflasG,planeta):
    fuente = pygame.font.SysFont("monospace", 50)
    texto = fuente.render("Pantuflas llegó a casa. :-D",1,BLANCO)
    ventana.blit(texto,((ANCHO//2)-220,150))
    ventana.blit(botonMenu.image,botonMenu.rect)

    ventana.blit(pantuflasG.image,pantuflasG.rect)
    ventana.blit(planeta.image,planeta.rect)

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
    cargaPoder = 1
    tiempoPoder = 0
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
    imgBtnCreditos = pygame.image.load("images/button_creditos.png")
    imgBtnMenu = pygame.image.load("images/button_menu.png")
    imgBtnReintentar = pygame.image.load("images/button_reintentar.png")

    # Cargar imagen Pantuflas
    imgPantuflas = pygame.image.load("images/pantuflas-el-perro.png") # nave
    imgPantuflasG = pygame.image.load("images/pantuflas-ganador.png") # al ganar sale
    imgPantuflasT = pygame.image.load("images/pantuflas-triste.png") # al ganar sale

    # Cargar imagen planeta
    imgPlaneta = pygame.image.load("images/planeta.png")

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
    botonJugar.rect.left = ANCHO // 2 - 20 - botonJugar.rect.width
    botonJugar.rect.top = ALTO // 2

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

    pantuflasG = pygame.sprite.Sprite()
    pantuflasG.image = imgPantuflasG
    pantuflasG.rect = imgPantuflasG.get_rect()
    pantuflasG.rect.left = ANCHO // 2 - 5*pantuflasG.rect.width//4
    pantuflasG.rect.top = 200

    pantuflasT = pygame.sprite.Sprite()
    pantuflasT.image = imgPantuflasT
    pantuflasT.rect = imgPantuflasT.get_rect()
    pantuflasT.rect.left = ANCHO // 2 - pantuflasT.rect.width//2
    pantuflasT.rect.top = ALTO // 2 - pantuflasT.rect.height//2

    planeta = pygame.sprite.Sprite()
    planeta.image = imgPlaneta
    planeta.rect = imgPlaneta.get_rect()
    planeta.rect.left = ANCHO // 2 + 50
    planeta.rect.top = 200

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    xbJ, ybJ, anchoBJ, altoBJ = botonJugar.rect
                    xbC, ybC, anchoBC, altoBC = botonCreditos.rect

                    if xbJ <= xm <= xbJ+anchoBJ:
                        if ybJ <= ym <= ybJ+altoBJ:
                            # Cambiar de ventana
                            estado = "jugando"

                    elif xbC <= xm <= xbC + anchoBC:
                        if ybC <= ym <= ybC + altoBC:
                            # Cambiar de ventana
                            estado = "creditos"

                elif estado == "creditos":
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
            dibujarMenu(ventana,botonJugar,botonCreditos)
            timer = 0
            cronometro = 93
            vidas = 3
            puntaje = 0
            poder = False
            cargaPoder = 1
            tiempoPoder = 0
            moverPantuflasLateral = False
            moverPantuflasVertical = False

        elif estado == "jugando":
            vidas,puntaje,tiempoPoder,cargaPoder = actualizarEnemigos(listaEnemigos,pantuflas,vidas,poder,tiempoPoder,puntaje,cargaPoder) # Mover enemigos
            dibujarJuego(ventana,listaEnemigos,pantuflas,vidas,cronometro,puntaje,tiempoPoder,cargaPoder)
            timer += 1 / 40
            cronometro -= 1 / 40
            if timer >= 1 and 80 < cronometro < 90: # Generar enemigos cada segundo
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
            elif timer >= 0.3 and 0 < cronometro <= 10: # Generar enemigos cada medio segundo
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo1)

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

        elif estado == "creditos":
            dibujarCreditos(ventana,botonMenu)
        elif estado == "finMalo":
            dibujarFinMalo(ventana,botonMenu,botonReintentar,pantuflasT)
            vidas = 3
            cronometro = 93
            puntaje = 0
            poder = False
            cargaPoder = 1
            tiempoPoder = 0
        elif estado == "finBueno":
            dibujarFinBueno(ventana,botonMenu,pantuflasG,planeta)
            vidas = 3
            cronometro = 93
            puntaje = 0
            poder = False
            cargaPoder = 1
            tiempoPoder = 0

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def main():
    dibujar()

main()