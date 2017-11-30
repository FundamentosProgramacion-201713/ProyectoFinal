# encoding: UTF-8
# Autor: Ana María López Soto
#Desarrollo del juego Pollos Locos
from random import randint

import pygame

# Dimensiones de la pantalla
ANCHO = 1065
ALTO = 600

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]

def dibujarMenu(ventana, botonJugar, botonCreditos, botonControles):
    COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonCreditos.image, botonCreditos.rect)
    ventana.blit(botonControles.image, botonControles.rect)

    fuente = pygame.font.SysFont("monospace", 90) # Título del juego
    texto = fuente.render("POLLOS LOCOS", 1, COLORLOCO)
    texto2 = fuente.render("EL JUEGO MÁS GENIAL", 1, COLORLOCO)
    ventana.blit(texto, ((ANCHO // 2) - 300, 100))
    ventana.blit(texto2, ((ANCHO // 2) - 500, 500))

def dibujarControles(ventana, botonMenu):
    COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
    fuente = pygame.font.SysFont("monospace", 38)
    titulo = fuente.render("Controles: ", 1, COLORLOCO)
    up = fuente.render("FLECHA ARRIBA ~~~~~~~ ARRIBA/ADELANTE", 1, COLORLOCO)
    left = fuente.render("FLECHA IZQUIERDA ~~~~~~~ IZQUIERDA(LATERAL)", 1, COLORLOCO)
    down = fuente.render("FLECHA ABAJO ~~~~~~~ ABAJO/ATRAS", 1, COLORLOCO)
    right = fuente.render("FLECHA DERECHA ~~~~~~~ DERECHA(LATERAL)", 1, COLORLOCO)
    vidas = fuente.render("TIENES TRES VIDAS, INTENTA NO MORIR TANTO", 1, COLORLOCO)
    ventana.blit(titulo, (60, 60))
    ventana.blit(up, (60, 120))
    ventana.blit(left, (60, 180))
    ventana.blit(down, (60, 240))
    ventana.blit(right, (60, 300))
    ventana.blit(vidas, (60, 360))
    ventana.blit(botonMenu.image, botonMenu.rect)  # boton menú

def dibujarCreditos(ventana, botonMenu):
    COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("Créditos: ", 1, COLORLOCO)
    autor = fuente.render("Autor: Ana María López Soto ", 1, COLORLOCO)
    matricula = fuente.render("Matrícula: A01746134 ", 1, COLORLOCO)
    apoyo = fuente.render("¡SÍ SE PUDO!", 1, BLANCO)
    ventana.blit(texto, (60, 100))
    ventana.blit(autor, (120, 170))
    ventana.blit(matricula, (120, 230))
    ventana.blit(apoyo, ((ANCHO//2)-220, 300))
    ventana.blit(botonMenu.image, botonMenu.rect)  # boton menú

def dibujarGanar(ventana, botonMenu, botonReintentar,pollo_muerto,astro):
    COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("ERES EL MEJOR ASTRONAUTA", 1, COLORLOCO)
    texto2 = fuente.render("DE TODA LA HISTORIA", 1, COLORLOCO)
    ventana.blit(texto, (40, 100))
    ventana.blit(texto2, (100, 200))
    ventana.blit(pollo_muerto.image, pollo_muerto.rect)
    ventana.blit(astro.image, astro.rect)
    ventana.blit(botonMenu.image, botonMenu.rect)
    ventana.blit(botonReintentar.image, botonReintentar.rect)

def dibujarPerdida(ventana, botonMenu, botonReintentar,pollo_TRF,huevo):
    COLORLOCO = (randint(0, 255), randint(0, 255), randint(0, 255))
    fuente = pygame.font.SysFont("monospace", 70)
    texto = fuente.render("AHORA ERES HUEVO ASADO", 1, COLORLOCO)
    texto2 = fuente.render("EL APOLO 24 HA EXPLOTADO", 1, COLORLOCO)
    ventana.blit(texto, (70, 100))
    ventana.blit(texto2, ((ANCHO // 2) - 500, 200))
    ventana.blit(botonMenu.image, botonMenu.rect)
    ventana.blit(botonReintentar.image, botonReintentar.rect)
    ventana.blit(pollo_TRF.image, pollo_TRF.rect)
    ventana.blit(huevo.image, huevo.rect)

def dibujarJuego(ventana, listaEnemigos, listaBalas, principal, vidas, cronometro):
    ventana.blit(principal.image,principal.rect)
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

    fuente = pygame.font.SysFont("monospace", 20)
    tiempo = fuente.render("Tiempo: %.2f" % cronometro, 1, BLANCO)
    vidas_sob = fuente.render("Vidas: " + str(vidas), 1, BLANCO)
    ventana.blit(tiempo, (ANCHO - 200, 540))
    ventana.blit(vidas_sob, (ANCHO - 200, 560))

def actualizarBalas(listaBalas, listaEnemigos):
    for bala in listaBalas: # NO DEBEN modificar
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue    # REGRESA al inicio del ciclo
        borrarBala = False
        for k in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala = True
                break   # TERMINA el ciclo
        if borrarBala:
            listaBalas.remove(bala)

def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    cx = randint(0, ANCHO - enemigo.rect.width)
    cy = -enemigo.rect.height
    enemigo.rect.left = cx
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)

def actualizarEnemigos(listaEnemigos,principal,vidas):
    DX = 1
    DY = 7
    derecha = True
    abajo = True

    # Actualiza la posición del enemigo
    for enemigo in listaEnemigos:
        if derecha:
            enemigo.rect.left += DX  # x = x + 3
        else:
            enemigo.rect.left -= DX

        if abajo:
            enemigo.rect.top += DY
        else:
            enemigo.rect.top -= DY


        if enemigo.rect.left < -enemigo.rect.width or enemigo.rect.colliderect(principal) or enemigo.rect.right == ANCHO:
            listaEnemigos.remove(enemigo)
        if enemigo.rect.colliderect(principal):
            vidas -= 1
    return vidas

def dibujar():
    moverJugadorLateralx = False
    moverJugadorVerticaly = False
    dx = 20
    dy = 20

    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución


   #Condiciones principales
    estado = "menu"    # jugando, ganar, perder, creditos, crontroles
    vidas = 3

    # Fondo
    imagenFondo = pygame.image.load("FONDO1.jpg")

    # Cargar imágenes
    imgBtnJugar = pygame.image.load("BtnJugar.png")
    imgBtnCreditos = pygame.image.load("BtnCreditos.png")
    imgBtnControles = pygame.image.load("BtnControles.png")
    imgBtnRMenú = pygame.image.load("BtnMenu.png")
    imgBtnReintentar = pygame.image.load("BtnReintentar.png")

    # Jugador
    imgJugador = pygame.image.load("NAVE.png")

    # Enemigos
    listaEnemigos = []
    imgEnemigo1 = pygame.image.load("PIERNA_Y.png")
    imgEnemigo2 = pygame.image.load("POLLO NAVIDAD.png")
    imgEnemigo3 = pygame.image.load("POLLO_2.png")
    imgEnemigo4 = pygame.image.load("asteroide.png")
    imgPolloMuerto = pygame.image.load("Pollo_muerto.png")
    imgPollo_triunfador = pygame.image.load("POLLO_GANAR.png")
    imgHuevo_loco =  pygame.image.load("Huevo_loco.png")
    imgAstro = pygame.image.load("ASTRO.png")

    # Balas
    listaBalas = []
    imgBala = pygame.image.load("BALA SIN FONDO 2.png")

    # Tiempos
    timer = 0

    # Sprites
        #Btn Jugar
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - (botonJugar.rect.height // 3 + 30)

        #Btn Creditos
    botonCreditos = pygame.sprite.Sprite()
    botonCreditos.image = imgBtnCreditos
    botonCreditos.rect = imgBtnCreditos.get_rect()
    botonCreditos.rect.left = ANCHO // 2 - botonCreditos.rect.width // 2
    botonCreditos.rect.top = ALTO //2 - (botonCreditos.rect.height // 3 - botonJugar.rect.height+10)

        #Btn Controles
    botonControles = pygame.sprite.Sprite()
    botonControles.image = imgBtnControles
    botonControles.rect = imgBtnControles.get_rect()
    botonControles.rect.left = ANCHO // 2 - botonControles.rect.width // 2
    botonControles.rect.top =  ALTO //2 - (botonControles.rect.height // 3 - botonCreditos.rect.height-80)

        # Btn Regresar al Menu
    botonRMenu = pygame.sprite.Sprite()
    botonRMenu.image = imgBtnRMenú
    botonRMenu.rect = imgBtnRMenú.get_rect()
    botonRMenu.rect.left = ANCHO // 2 - botonRMenu.rect.width // 2
    botonRMenu.rect.top = ALTO // 2 - (botonRMenu.rect.height // 3 - botonCreditos.rect.height-80)

        # Btn Reintentar
    botonReintentar = pygame.sprite.Sprite()
    botonReintentar.image = imgBtnReintentar
    botonReintentar.rect = imgBtnReintentar.get_rect()
    botonReintentar.rect.left = ANCHO // 2 - botonReintentar.rect.width // 2
    botonReintentar.rect.top = ALTO //2 - (botonCreditos.rect.height // 3 - botonJugar.rect.height+10)

        #Jugador Principal (Nave)
    principal = pygame.sprite.Sprite()
    principal.image = imgJugador
    principal.rect = imgJugador.get_rect()
    principal.rect.left = ANCHO // 2 - principal.rect.width // 2
    principal.rect.top = ALTO - principal.rect.height

    # Pollo Morido Ganamos
    pollo_muerto = pygame.sprite.Sprite()
    pollo_muerto.image = imgPolloMuerto
    pollo_muerto.rect = imgPolloMuerto.get_rect()
    pollo_muerto.rect.left = 150 - pollo_muerto.rect.width // 2
    pollo_muerto.rect.top = 500 - pollo_muerto.rect.height

    # Pollo Nos Ganó
    pollo_TRF = pygame.sprite.Sprite()
    pollo_TRF.image = imgPollo_triunfador
    pollo_TRF.rect = imgPollo_triunfador.get_rect()
    pollo_TRF.rect.left = 150 - pollo_TRF.rect.width // 2
    pollo_TRF.rect.top = 500 - pollo_TRF.rect.height

    # Huevo Nos Ganó
    huevo = pygame.sprite.Sprite()
    huevo.image = imgHuevo_loco
    huevo.rect = imgHuevo_loco.get_rect()
    huevo.rect.left = 900 - huevo.rect.width // 2
    huevo.rect.top = 500 - huevo.rect.height

        # Astro Ganamos
    astro = pygame.sprite.Sprite()
    astro.image = imgAstro
    astro.rect = imgAstro.get_rect()
    astro.rect.left = 900 - huevo.rect.width // 2
    astro.rect.top = 500 - huevo.rect.height - 70


    # MUSICA de fondo
    pygame.mixer.init()
    pygame.mixer.music.load("MAIN_THEME.mp3")
    pygame.mixer.music.play(-1)

    #Efecto de sonido del disparo
    efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN: # El usuario hizo click
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    xBtnJ, yBtnJ, anchoBtnJ, altoBtnJ = botonJugar.rect
                    xBtnC, yBtnC, anchoBtnC, altoBtnC = botonCreditos.rect
                    xBtnCTR, yBtnCTR, anchoBtnCTR, altoBtnCTR = botonControles.rect

                    if xm>=xBtnJ and xm<=xBtnJ+anchoBtnJ:
                        if ym>=yBtnJ and ym<=yBtnJ+altoBtnJ:
                            # Cambiar de ventana
                            estado = "jugando"

                    if xm>=xBtnC and xm<=xBtnC+anchoBtnC:
                        if ym>= yBtnC and ym<=yBtnC+altoBtnC:
                            # Cambiar de ventana
                            estado = "creditos"

                    if xm>=xBtnCTR and xm<=xBtnCTR+anchoBtnCTR:
                        if ym>=yBtnCTR and ym<=yBtnCTR+altoBtnCTR:
                            # Cambiar de ventana
                            estado = "controles"



                elif estado == "creditos" or estado == "controles":
                    xBtnRM, yBtnRM, anchoBtnRM, altoBtnRM = botonRMenu.rect

                    if xBtnRM <= xm <= xBtnRM+anchoBtnRM:
                        if yBtnRM <= ym <= yBtnRM+altoBtnRM:
                            # Regresar al menu
                            estado = "menu"

                elif estado == "perder":
                    xBtnR, yBtnR, anchoBtnR, altoBtnR = botonReintentar.rect
                    xBtnRM, yBtnRM, anchoBtnRM, altoBtnRM = botonRMenu.rect

                    if xBtnR <= xm <= xBtnR+anchoBtnR:
                        if yBtnR <= ym <= yBtnR+altoBtnR:
                            # Reintentar
                            estado = "jugando"

                    if xBtnRM <= xm <= xBtnRM+anchoBtnRM:
                        if yBtnRM <= ym <= yBtnRM+altoBtnRM:
                            # Regresar al menú
                            estado = "menu"

                elif estado == "ganar":
                    xBtnRM, yBtnRM, anchoBtnRM, altoBtnRM = botonRMenu.rect

                    if xBtnRM <= xm <= xBtnRM + anchoBtnRM:
                        if yBtnRM <= ym <= yBtnRM + altoBtnRM:
                            # Regresar a menú
                            estado = "menu"

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    efecto.play()
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = principal.rect.left + bala.rect.width // 3
                    bala.rect.top = principal.rect.top - bala.rect.height
                    listaBalas.append(bala)

            # Jugador
                if evento.key == pygame.K_DOWN:  # flecha abajo
                    dy = +20
                    moverJugadorVerticaly = True

                if evento.key == pygame.K_UP:  # flecha arriba
                    dy = -10
                    moverJugadorVerticaly = True

                if evento.key == pygame.K_RIGHT:  # flecha derecha
                    dx = +10
                    moverJugadorLateralx = True

                if evento.key == pygame.K_LEFT:  # flecha izquierda
                    dx = -10
                    moverJugadorLateralx = True


            elif evento.type == pygame.KEYUP:  # se suelta la tecla
                moverJugadorLateralx = False
                moverJugadorVerticaly = False

        # Borrar pantalla
        ventana.blit(imagenFondo, (0, 0))

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, botonJugar,botonCreditos,botonControles)
            timer = 0
            cronometro = 90
            vidas = 3
            moverJugadorLateralx = False
            moverJugadorVerticaly = False

        elif estado == "jugando":
            vidas = actualizarEnemigos(listaEnemigos,principal,vidas)
            actualizarBalas(listaBalas, listaEnemigos)
            dibujarJuego(ventana, listaEnemigos, listaBalas,principal,vidas,cronometro)

            # Generar enemigos cada 2 segundos
            timer += 2 / 20
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
            elif timer >= 1.5 and 0 < cronometro <= 30: # Generar enemigos cada dos segundos
                timer = 0
                generarEnemigoAzar(listaEnemigos,imgEnemigo2)
                generarEnemigoAzar(listaEnemigos,imgEnemigo4)

            if moverJugadorVerticaly:
                principal.rect.top += dy
            if moverJugadorLateralx:
                principal.rect.left += dx


                #Ganó o perdió
            if vidas == 0:
                estado = "perder"
            if cronometro <= 0:
                estado = "ganar"


        elif estado == "creditos":
            dibujarCreditos(ventana,botonRMenu)

        elif estado == "controles":
            dibujarControles(ventana,botonRMenu)

        elif estado == "perder":
            dibujarPerdida(ventana,botonRMenu,botonReintentar, pollo_TRF,huevo)
            vidas = 3
            cronometro = 90


        elif estado == "ganar":
            dibujarGanar(ventana,botonRMenu, botonReintentar,pollo_muerto, astro)



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

def main():
    dibujar()


main()