#AUTOR: Luis Enrique Neri Pérez
#DESCRIPCIÓN: Juego Bomber-Man

import pygame, pygame.mixer

# DIMENSIONES DE LA PANTALLA
ANCHO = 800
ALTO = 600

# COORDENADAS PERMITIDAS
coordenadasPosRick= ['(590,350)','(40,100)', '(40,50)', '(-10,100)', '(90,100)', '(140,100)', '(140,50)', '(190,100)', '(240,100)', '(240,150)', '(290,150)', '(340,150)', '(340,100)', '(340,50)', '(390,50)', '(440,50)', '(440,100)', '(440,150)', '(390,150)', '(390,200)', '(440,200)', '(490,200)', '(540,200)', '(540,150)', '(540,100)', '(490,100)', '(540,50)', '(590,50)', '(590,100)', '(590,200)', '(640,200)', '(640,150)', '(690,150)', '(690,100)', '(740,100)', '(740,50)', '(690,200)', '(740,200)', '(690,250)', '(690,300)', '(740,300)', '(640,300)', '(590,300)', '(590,250)', '(540,300)', '(490,300)', '(490,250)', '(540,350)', '(540,400)', '(540,450)', '(540,500)', '(590,500)', '(640,500)', '(690,500)', '(740,500)', '(640,450)', '(640,400)', '(690,400)', '(740,400)', '(690,350)', '(440,300)', '(390,300)', '(340,300)', '(340,350)', '(340,400)', '(290,400)', '(240,400)', '(290,450)', '(340,450)', '(390,450)', '(390,400)', '(440,400)', '(290,300)', '(240,300)', '(190,300)', '(140,300)', '(140,350)', '(140,400)', '(140,450)', '(140,500)', '(90,500)', '(90,450)', '(40,450)', '(40,400)', '(-10,400)', '(-10,350)', '(40,350)', '(40,300)', '(90,300)', '(90,250)', '(90,200)', '(140,200)', '(190,200)', '(240,200)', '(290,200)', '(140,150)', '(40,200)', '(-10,200)', '(40,150)', '(340,500)', '(290,250)']
coordenadasPosMorty = ['(330,520)','(30,70)', '(30,120)', '(-20,120)', '(80,120)', '(130,120)', '(130,70)', '(180,120)', '(230,120)', '(230,170)', '(280,170)', '(330,170)', '(330,120)', '(330,70)', '(380,70)', '(430,70)', '(430,120)', '(480,120)', '(530,120)', '(580,120)', '(580,70)', '(530,70)', '(530,170)', '(530,220)', '(580,220)', '(630,220)', '(680,220)', '(730,220)', '(680,170)', '(680,120)', '(730,120)', '(730,70)', '(630,170)', '(380,170)', '(380,220)', '(430,220)', '(480,220)', '(480,270)', '(480,320)', '(530,320)', '(580,320)', '(580,270)', '(630,320)', '(680,320)', '(680,270)', '(730,320)', '(680,370)', '(680,420)', '(730,420)', '(630,420)', '(630,470)', '(630,520)', '(680,520)', '(730,520)', '(580,520)', '(530,520)', '(530,470)', '(530,420)', '(530,370)', '(580,370)', '(430,320)', '(380,320)', '(330,320)', '(330,370)', '(330,420)', '(380,420)', '(430,420)', '(280,420)', '(230,420)', '(280,470)', '(330,470)', '(380,470)', '(280,320)', '(230,320)', '(180,320)', '(130,320)', '(130,370)', '(130,420)', '(130,470)', '(130,520)', '(80,520)', '(80,470)', '(30,470)', '(30,420)', '(-20,420)', '(-20,370)', '(30,370)', '(30,320)', '(80,320)', '(280,270)', '(280,220)', '(230,220)', '(180,220)', '(130,220)', '(80,220)', '(80,270)', '(30,220)', '(-20,220)', '(30,170)', '(130,170)', '(430,170)']

# COLORES
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

# IMAGENES
imagenMenu = pygame.image.load("Fondo Menú.jpg")
imagenFondo = pygame.image.load("Laberinto.jpg")
imagenIntro = pygame.image.load("Casa.png")
imagenCreditos = pygame.image.load("Creditos.jpg")
imagenScore = pygame.image.load("Fondo High Scores.jpg")
imagenInstrucciones = pygame.image.load("Instrucciones.jpg")
rick = ["RickDerecha.png","RickIzquierda.png"]
morty = ["MortyDerecha.png","MortyIzquierda.png"]
corazones = ["0Corazones.png","1Corazón.png","2Corazones.png","3Corazones.png","4Corazones.png"]

# EFECTOS DE SONIDO
canciones = {"Tema":'IntroSong.mp3',"Jazz":"RickJazz.mp3","Click":'Click.mp3', "Explosion":'Explosion.wav', "Alerta":'Alerta.wav'}


def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)

def dibujarIntro(ventana, btnIntro):
    ventana.blit(btnIntro.image, btnIntro.rect)

def dibujarVidasMorty(ventana, btnVidasMorty):
    ventana.blit(btnVidasMorty.image, btnVidasMorty.rect)

def dibujarVidasRick(ventana, btnVidasRick):
    ventana.blit(btnVidasRick.image, btnVidasRick.rect)

def dibujarMenuPausa(ventana, btnMenuPausa, btnContinuarJuego, btnReiniciar, btnVolverMenu):
    ventana.blit(btnMenuPausa.image, btnMenuPausa.rect)
    dibujarContinuarJuego(ventana, btnContinuarJuego)  # 1
    dibujarReiniciarJuego(ventana, btnReiniciar)  # 2
    dibujarVolverMenu(ventana, btnVolverMenu)  # 3

def dibujarContinuarJuego(ventana, btnContinuarJuego):
    ventana.blit(btnContinuarJuego.image, btnContinuarJuego.rect)


def dibujarReiniciarJuego(ventana, btnReiniciarJuego):
    ventana.blit(btnReiniciarJuego.image, btnReiniciarJuego.rect)


def dibujarVolverMenu(ventana, btnVolverMenu):
    ventana.blit(btnVolverMenu.image, btnVolverMenu.rect)


def dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa, btnMenuPausa, btnVolverMenu,btnContinuarJuego, btnReiniciar):
    dibujarRick(ventana,imagenRick, xRick, yRick)
    dibujarMorty(ventana, imagenMorty, xMorty, yMorty)
    dibujarVidasMorty(ventana,btnVidasMorty)
    dibujarVidasRick(ventana, btnVidasRick)
    dibujarPausa(ventana, btnPausa)


def dibujarRick(ventana, imagenMorty, x, y):
    ventana.blit(imagenMorty, (x, y))

def dibujarMorty(ventana, imagenRick, x, y):
    ventana.blit(imagenRick, (x, y))

def dibujarScores(ventana, btnScores):
    ventana.blit(btnScores.image, btnScores.rect)

def dibujarMadMorty(ventana, btnMadMorty):
    ventana.blit(btnMadMorty.image, btnMadMorty.rect)

def dibujarMadRick(ventana, btnMadRick):
    ventana.blit(btnMadRick.image, btnMadRick.rect)

def dibujarRegresar(ventana, btnRegresar):
    ventana.blit(btnRegresar.image, btnRegresar.rect)


def dibujarCreditos(ventana, btnCreditos):
    ventana.blit(btnCreditos.image, btnCreditos.rect)


def dibujarTextoIntro1(ventana, btnTextoIntro):
    ventana.blit(btnTextoIntro.image, btnTextoIntro.rect)


def dibujarTextoIntro2(ventana, btnTextoIntro2):
    ventana.blit(btnTextoIntro2.image, btnTextoIntro2.rect)

def dibujarListo1(ventana, btnListo1):
    ventana.blit(btnListo1.image, btnListo1.rect)

def dibujarListo2(ventana, btnListo2):
    ventana.blit(btnListo2.image, btnListo2.rect)

def dibujarPausa(ventana, btnPausa):
    ventana.blit(btnPausa.image, btnPausa.rect)

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # ESTADOS DEL JUEGO
    estado = "menu"

    # REPRODUCIR TEMA PRINCIPAL
    pygame.mixer.music.load(canciones["Tema"])
    pygame.mixer.music.play(-1)

    # VIDAS
    vidasRick = 3
    vidasMorty = 3

    # BOTON INICIAR
    imgBotonJugar = pygame.image.load("Iniciar.png")
    btnJugar = pygame.sprite.Sprite()  # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()  # rect(x,y,width,lenght)
    btnJugar.rect.left = ANCHO - btnJugar.rect.width - 60 # LEFT ES EL EJE X
    btnJugar.rect.top = ALTO - btnJugar.rect.height - 15  # HEIGHT ES EL EJE Y

    # BOTON PUNTAJES
    imgBotonScores = pygame.image.load("HIGH SCORES.png")
    btnScores = pygame.sprite.Sprite()  # SPRITE
    btnScores.image = imgBotonScores
    btnScores.rect = imgBotonScores.get_rect()  # rect(x,y,width,lenght)
    btnScores.rect.left =  40 +  btnJugar.rect.width // 2 + btnScores.rect.width // 2 + 40 # LEFT ES EL EJE X
    btnScores.rect.top = ALTO - btnJugar.rect.height - 15  # HEIGHT ES EL EJE Y

    # BOTON CRÉDITOS
    imgBotonCreditos = pygame.image.load("CREDITOS.png")
    btnCreditos = pygame.sprite.Sprite()  # SPRITE
    btnCreditos.image = imgBotonCreditos
    btnCreditos.rect = imgBotonCreditos.get_rect()  # rect(x,y,width,lenght)
    btnCreditos.rect.left = 40   + 20   # LEFT ES EL EJE X
    btnCreditos.rect.top = ALTO - btnCreditos.rect.height - 15  # HEIGHT ES EL EJE Y

    # BOTON REGRESAR
    imgBotonRegresar = pygame.image.load("REGRESAR.png")
    btnRegresar = pygame.sprite.Sprite()  # SPRITE
    btnRegresar.image = imgBotonRegresar
    btnRegresar.rect = imgBotonRegresar.get_rect()  # rect(x,y,width,lenght)
    btnRegresar.rect.left = 40 + btnRegresar.rect.width // 2 + btnScores.rect.width // 2 + 40  # LEFT ES EL EJE X
    btnRegresar.rect.top = ALTO - btnRegresar.rect.height - 15  # HEIGHT ES EL EJE Y

    # BOTÓN INTRO
    imgBotonIntro = pygame.image.load("CONTINUAR.png")
    btnIntro = pygame.sprite.Sprite()  # SPRITE
    btnIntro.image = imgBotonIntro
    btnIntro.rect = imgBotonIntro.get_rect()  # rect(x,y,width,lenght)
    btnIntro.rect.left = ANCHO - btnJugar.rect.width - 60  # LEFT ES EL EJE X
    btnIntro.rect.top = ALTO - btnIntro.rect.height - 15  # HEIGHT ES EL EJE Y

    # MAD MORTY INTRO
    imgMadMorty = pygame.image.load("Mad Morty.png")
    btnMadMorty = pygame.sprite.Sprite()  # SPRITE
    btnMadMorty.image = imgMadMorty
    btnMadMorty.rect = imgMadMorty.get_rect()  # rect(x,y,width,lenght)
    btnMadMorty.rect.left = 0  # LEFT ES EL EJE X
    btnMadMorty.rect.top = ALTO - btnMadMorty.rect.height  # HEIGHT ES EL EJE Y

    # MAD MORTY INTRO
    imgMadRick = pygame.image.load("Mad Rick.png")
    btnMadRick = pygame.sprite.Sprite()  # SPRITE
    btnMadRick.image = imgMadRick
    btnMadRick.rect = imgMadRick.get_rect()  # rect(x,y,width,lenght)
    btnMadRick.rect.left = ANCHO - btnMadRick.rect.width  # LEFT ES EL EJE X
    btnMadRick.rect.top = ALTO - btnMadRick.rect.height  # HEIGHT ES EL EJE Y

    # TITULO INTRO
    imgTextoIntro = pygame.image.load("Texto Intro 1.png")
    btnTextoIntro = pygame.sprite.Sprite()  # SPRITE
    btnTextoIntro.image = imgTextoIntro
    btnTextoIntro.rect = imgTextoIntro.get_rect()  # rect(x,y,width,lenght)
    btnTextoIntro.rect.left = 25  # LEFT ES EL EJE X
    btnTextoIntro.rect.top = 25  # HEIGHT ES EL EJE Y

    # TEXTO INTRO
    imgTextoIntro2 = pygame.image.load("Texto Intro 2.png")
    btnTextoIntro2 = pygame.sprite.Sprite()  # SPRITE
    btnTextoIntro2.image = imgTextoIntro2
    btnTextoIntro2.rect = imgTextoIntro2.get_rect()  # rect(x,y,width,lenght)
    btnTextoIntro2.rect.left = ANCHO//2 - btnTextoIntro2.rect.width// 2 - 40  # LEFT ES EL EJE X
    btnTextoIntro2.rect.top = ALTO - btnTextoIntro2.rect.height - 5  # HEIGHT ES EL EJE Y

    # BOTÓN PAUSA
    imgPausa = pygame.image.load("Pausa.png")
    btnPausa = pygame.sprite.Sprite()  # SPRITE
    btnPausa.image = imgPausa
    btnPausa.rect = imgPausa.get_rect()  # rect(x,y,width,lenght)
    btnPausa.rect.left = ANCHO // 2 - btnPausa.rect.width // 2  # LEFT ES EL EJE X
    btnPausa.rect.top = 67  # HEIGHT ES EL EJE Y

    # BOTÓN LISTO
    imgListo1 = pygame.image.load("Ready.png")
    btnListo1 = pygame.sprite.Sprite()  # SPRITE
    btnListo1.image = imgListo1
    btnListo1.rect = imgListo1.get_rect()  # rect(x,y,width,lenght)
    btnListo1.rect.left = 297   # LEFT ES EL EJE X
    btnListo1.rect.top = ALTO - 60  # HEIGHT ES EL EJE Y

    imgListo2 = pygame.image.load("Ready.png")
    btnListo2 = pygame.sprite.Sprite()  # SPRITE
    btnListo2.image = imgListo2
    btnListo2.rect = imgListo2.get_rect()  # rect(x,y,width,lenght)
    btnListo2.rect.left = 483  # LEFT ES EL EJE X
    btnListo2.rect.top = ALTO - 60  # HEIGHT ES EL EJE Y

    # MENÚ PAUSA
    imgMenuPausa = pygame.image.load("MenuPausa.png")
    btnMenuPausa = pygame.sprite.Sprite()  # SPRITE
    btnMenuPausa.image = imgMenuPausa
    btnMenuPausa.rect = imgMenuPausa.get_rect()  # rect(x,y,width,lenght)
    btnMenuPausa.rect.left = ANCHO // 2 - btnMenuPausa.rect.width // 2  # LEFT ES EL EJE X
    btnMenuPausa.rect.top = ALTO//2 - btnMenuPausa.rect.height//2  # HEIGHT ES EL EJE Y

    # MENÚ PAUSA: CONTINUAR
    imgContinuarJuego = pygame.image.load("ContinuarJuego.png")
    btnContinuarJuego = pygame.sprite.Sprite()  # SPRITE
    btnContinuarJuego.image = imgContinuarJuego
    btnContinuarJuego.rect = imgContinuarJuego.get_rect()  # rect(x,y,width,lenght)
    btnContinuarJuego.rect.left = ANCHO // 2 - btnContinuarJuego.rect.width // 2  # LEFT ES EL EJE X
    btnContinuarJuego.rect.top = ALTO // 2 - btnContinuarJuego.rect.height  - 28  # HEIGHT ES EL EJE Y

    # MENÚ PAUSA: REINICIAR
    imgReiniciar = pygame.image.load("Reiniciar.png")
    btnReiniciar = pygame.sprite.Sprite()  # SPRITE
    btnReiniciar.image = imgReiniciar
    btnReiniciar.rect = imgReiniciar.get_rect()  # rect(x,y,width,lenght)
    btnReiniciar.rect.left = ANCHO // 2 - btnReiniciar.rect.width // 2  # LEFT ES EL EJE X
    btnReiniciar.rect.top = ALTO // 2 - btnReiniciar.rect.height //2 + 28  # HEIGHT ES EL EJE Y

    # MENÚ PAUSA: VolverMenu
    imgVolverMenu = pygame.image.load("VolverMenu.png")
    btnVolverMenu = pygame.sprite.Sprite()  # SPRITE
    btnVolverMenu.image = imgVolverMenu
    btnVolverMenu.rect = imgVolverMenu.get_rect()  # rect(x,y,width,lenght)
    btnVolverMenu.rect.left = ANCHO // 2 - btnVolverMenu.rect.width // 2  # LEFT ES EL EJE X
    btnVolverMenu.rect.top = ALTO // 2 + btnVolverMenu.rect.height  + 28  # HEIGHT ES EL EJE Y

    # SELECTOR DE IMÁGENES DE LOS PERSONAJES
    r = 1
    m = 0
    imagenRick = pygame.image.load(rick[r])
    imagenMorty = pygame.image.load(morty[m])
    jugador1 = 0
    jugador2 = 4
    # COORDENADAS INICIALES RICK & MORTY
    xRick = 740
    yRick = 50
    xMorty = 30
    yMorty = 70


    clicPausa = False
    seleccionPausa = 0

    x = 0
    y = 0
    contador = 0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():


            # VIDAS PERSONAJES
            imgVidasMorty = pygame.image.load(corazones[vidasMorty])
            btnVidasMorty = pygame.sprite.Sprite()  # SPRITE
            btnVidasMorty.image = imgVidasMorty
            btnVidasMorty.rect = imgVidasMorty.get_rect()  # rect(x,y,width,lenght)
            btnVidasMorty.rect.left = 37  # LEFT ES EL EJE X
            btnVidasMorty.rect.top = 36  # HEIGHT ES EL EJE Y

            imgVidasRick = pygame.image.load(corazones[vidasRick])
            btnVidasRick = pygame.sprite.Sprite()  # SPRITE
            btnVidasRick.image = imgVidasRick
            btnVidasRick.rect = imgVidasRick.get_rect()  # rect(x,y,width,lenght)
            btnVidasRick.rect.left = ANCHO - btnVidasMorty.rect.width - 30  # LEFT ES EL EJE X
            btnVidasRick.rect.top = 37  # HEIGHT ES EL EJE Y

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()  # Obtener coordenadas mouse
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "intro"
                    xb, yb, anchoB, altoB = btnScores.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "scores"
                    xb, yb, anchoB, altoB = btnCreditos.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "creditos"
                elif estado == "creditos":
                    xb, yb, anchoB, altoB = btnRegresar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "menu"
                elif estado == "scores":
                    xb, yb, anchoB, altoB = btnRegresar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "menu"
                elif estado == "intro":
                    xb, yb, anchoB, altoB = btnIntro.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "instrucciones"
                elif estado == "jugando":
                    x1, y1, ancho1, alto1 = btnContinuarJuego.rect
                    x2, y2, ancho2, alto2 = btnReiniciar.rect
                    x3, y3, ancho3, alto3 = btnVolverMenu.rect
                    xb, yb, anchoB, altoB = btnPausa.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            clicPausa = True
                    if xm >= x1 and xm <= x1 + ancho1:
                        if ym >= y1 and ym <= y1 + alto1:
                            seleccionPausa = "Continuar"
                    if xm >= x2 and xm <= x2 + ancho2:
                        if ym >= y2 and ym <= y2 + alto2:
                            seleccionPausa = "Reiniciar"
                    if xm >= x3 and xm <= x3 + ancho3:
                        if ym >= y3 and ym <= y3 + alto3:
                            seleccionPausa = "Menu"
            elif evento.type == pygame.KEYDOWN:
                if estado == "instrucciones":
                    if evento.key == pygame.K_BACKSPACE:
                        jugador2 = "ready"
                    elif evento.key == pygame.K_SPACE:
                        jugador1 = "ready"
                    elif jugador1 == jugador2:
                        estado = "jugando"
                elif estado == "jugando":
                    ventana.blit(imagenFondo, (0, 0))
                    dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa, btnMenuPausa, btnVolverMenu,btnContinuarJuego, btnReiniciar)

                if estado == "jugando":
                    # MOVIMIENTOS RICK
                    if evento.key == pygame.K_UP:  # ARRIBA RICK
                        yRickPrueba = yRick - 50
                        cadena = "("+str(xRick) + "," + str(yRickPrueba) + ")"
                        if cadena in coordenadasPosRick:
                            yRick -= 50
                    elif evento.key == pygame.K_DOWN:  # ABAJO RICK
                        yRickPrueba = yRick + 50
                        cadena = "(" + str(xRick) + "," + str(yRickPrueba) + ")"
                        if cadena in coordenadasPosRick:
                            yRick += 50
                    elif evento.key == pygame.K_LEFT:  # DERECHA RICK
                        xRickPrueba = xRick - 50
                        cadena = "(" + str(xRickPrueba) + "," + str(yRick) + ")"
                        if cadena in coordenadasPosRick:
                            xRick -= 50
                        r = 1
                    elif evento.key == pygame.K_RIGHT:  # IZQUIERDA RICK
                        xRickPrueba = xRick + 50
                        cadena = "(" + str(xRickPrueba) + "," + str(yRick) + ")"
                        if cadena in coordenadasPosRick:
                            xRick += 50
                        r = 0
                    # MOVIMIENTOS MORTY
                    elif evento.key == pygame.K_w:  # ARRIBA MORTY
                        yMortyPrueba = yMorty - 50
                        cadena = "(" + str(xMorty) + "," + str(yMortyPrueba) + ")"
                        if cadena in coordenadasPosMorty:
                            yMorty -= 50
                    elif evento.key == pygame.K_s:  # ABAJO MORTY
                        yMortyPrueba = yMorty + 50
                        cadena = "(" + str(xMorty) + "," + str(yMortyPrueba) + ")"
                        if cadena in coordenadasPosMorty:
                            yMorty += 50
                    elif evento.key == pygame.K_d:  # DERECHA MORTY
                        xMortyPrueba = xMorty + 50
                        cadena = "(" + str(xMortyPrueba) + "," + str(yMorty) + ")"
                        if cadena in coordenadasPosMorty:
                            xMorty += 50
                        m = 0
                    elif evento.key == pygame.K_a:  # IZQUIERDA MORTY
                        xMortyPrueba = xMorty - 50
                        cadena = "(" + str(xMortyPrueba) + "," + str(yMorty) + ")"
                        if cadena in coordenadasPosMorty:
                            xMorty -= 50
                        m = 1
                    imagenRick = pygame.image.load(rick[r])
                    imagenMorty = pygame.image.load(morty[m])

        # DIBUJAR VENTANAS
        if estado == "menu": # MENÚ PRINCIPAL
            ventana.blit(imagenMenu, (0, 0))
            dibujarMenu(ventana, btnJugar)
            dibujarScores(ventana, btnScores)
            dibujarCreditos(ventana, btnCreditos)
        elif estado == "scores": # PUNTAJES
            ventana.blit(imagenScore, (0,0))
            dibujarScores(ventana, btnRegresar)
        elif estado == "creditos": # CRÉDITOS
            ventana.blit(imagenCreditos, (0, 0))
            dibujarRegresar(ventana, btnRegresar)
        elif estado == "intro": # INTRODUCCIÓN
            jugador1 = 0
            jugador2 = 5
            # ANIMACIÓN FONDO EN MOVIMIENTO
            if contador == 0:
                if x> -200:
                    ventana.blit(imagenIntro, (x,y))
                    dibujarMadMorty(ventana, btnMadMorty)
                    dibujarMadRick(ventana, btnMadRick)
                    dibujarTextoIntro1(ventana, btnTextoIntro)
                    dibujarTextoIntro2(ventana, btnTextoIntro2)
                    dibujarIntro(ventana, btnIntro)
                    x -= 1
                elif x == -200:
                    contador = 1
            elif contador == 1:
                if x < 0:
                    ventana.blit(imagenIntro, (x,y))
                    dibujarMadMorty(ventana, btnMadMorty)
                    dibujarMadRick(ventana, btnMadRick)
                    dibujarTextoIntro1(ventana, btnTextoIntro)
                    dibujarTextoIntro2(ventana, btnTextoIntro2)
                    dibujarIntro(ventana, btnIntro)
                    x += 1
                elif x == 0:
                    contador = 0
        elif estado == "instrucciones": # INSTRUCCIONES
            ventana.blit(imagenInstrucciones, (0, 0))
            if jugador1 == "ready":
                dibujarListo1(ventana, btnListo1)
            elif jugador2 == "ready":
                dibujarListo2(ventana, btnListo2)
            if jugador1 == jugador2:
                dibujarListo1(ventana, btnListo1)
                dibujarListo2(ventana, btnListo2)
                estado = "jugando"
        elif estado == "jugando": #JUEGO
            ventana.blit(imagenFondo, (0,0))
            dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa, btnMenuPausa, btnVolverMenu,btnContinuarJuego, btnReiniciar)
            if clicPausa == True:
                dibujarMenuPausa(ventana, btnMenuPausa, btnContinuarJuego, btnReiniciar, btnVolverMenu)
                if seleccionPausa == "Continuar":
                    clicPausa = False
                elif seleccionPausa == "Reiniciar":
                    clicPausa = False
                    estado = "instrucciones"
                elif seleccionPausa == "Menu":
                    clicPausa = False
                    estado = "menu"

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(10)          # 40 fpsS
    pygame.quit()   # termina pygame


def main():
    dibujar()

main()