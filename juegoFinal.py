# encoding: UTF-8
# Autor: Angel Roberto Pesado Bartolo A01374942
# Es un juego de tiros de penal de futbol, en el cual el usuario tiene que elegir uno de los 6 rectangulos rojos para ver si anota gol o falla el penal, cada que meta un gol, se le aumentará 1 punto y cada que falle se le restará 1 punto
#Es un juego de azar así que lo disfruten.

import pygame#importamos la librería de pygame
import random#importamos la libreria random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


NUM_IMAGENES = 8                    # Para los balones cambien de forma
TIEMPO_ENTRE_FRAMES = 0.1           # Tiempo entre cada imagen de la animación
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES
NUM_IMAGENES2=10                    #Para el movimiento de del portero

def crearListaSprites():
    lista = []

    for i in range(NUM_IMAGENES2):
        nombre = "imagenes/anima-"+str(i)+".png"        # anima- para los porteros
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = ANCHO//2-sprAnimacion.rect.width//2
        sprAnimacion.rect.top = ALTO//2-sprAnimacion.rect.height//2-25
        lista.append(sprAnimacion)

    return lista

def crearListaSprites2():
    lista2 = []

    for i in range(NUM_IMAGENES):
        nombre = "imagenes2/anima-"+str(i)+".png"        # anima- para el balón
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = ANCHO//2-sprAnimacion.rect.width//2
        sprAnimacion.rect.top = ALTO//2-sprAnimacion.rect.height//2+170
        lista2.append(sprAnimacion)

    return lista2

def obtenerFrame(timerAnimacion, listaSprites):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]

def obtenerFrame2(timerAnimacion, listaSprites2):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites2[indice]

def dibujarMenu(ventana,btnJugar):
    ventana.blit(btnJugar.image,btnJugar.rect)


def generarLugares(listaEnemigos,lugarTiro):#
    for x in range(3):
        for y in range(2):
            cx=130+x*190
            cy=ALTO//2-y*100-75
            nuevo = pygame.sprite.Sprite()
            nuevo.image = lugarTiro
            nuevo.rect = lugarTiro.get_rect()
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaEnemigos.append(nuevo)

def obtenerLTR(lugarTiro):
    ltr=pygame.sprite.Sprite
    ltr.image=lugarTiro
    ltr.rect=lugarTiro.get_rect()
    ltr.rect.left=ANCHO//2-ltr.rect.width//2
    ltr.rect.top = ANCHO // 2 - ltr.rect.height // 2


def dibujarInstrucciones(ventana, jugar):
    ventana.blit(jugar.image, jugar.rect)

def dibujarJuego(ventana, listaPosicion, listaBalas):
    for enemigo in listaPosicion:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    #defines estados
    estados="Menu"#jugando, termina
    #botones y fondos
    imgbotonJugar=pygame.image.load("jugar.png")
    Fondo=pygame.image.load("Fondo.jpg")
    instrucciones=pygame.image.load("titulo.png")
    lugarTiro=pygame.image.load("lugarTiro.png")
    final=pygame.image.load("final.png")
    ball=pygame.image.load("ball.png")
    perder = pygame.image.load("perder.png")

    btnJugar=pygame.sprite.Sprite
    btnJugar.image=imgbotonJugar
    btnJugar.rect=imgbotonJugar.get_rect()
    btnJugar.rect.left=ANCHO//2-btnJugar.rect.width//2+250
    btnJugar.rect.top=ALTO//2-btnJugar.rect.height//2+250


    #listas
    listaLugares = []
    contadores = []
    cont = 0
    listaBalas=[]
    listaPosicion = []
    listaSprites = crearListaSprites()
    listaSprites2 = crearListaSprites2()
    timerAnimacion = 0

    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)
    efecto = pygame.mixer.Sound("gool.wav")
    efecto1 = pygame.mixer.Sound("abucheo.wav")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEBUTTONDOWN:

                xm, ym = pygame.mouse.get_pos()
                if estados=="Menu":
                    xb,yb,anchoB,altoB=btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estados="jugando"
                elif estados=="jugando":
                    enemigo = pygame.sprite.Sprite()
                    enemigo.image = ball
                    enemigo.rect = ball.get_rect()
                    enemigo.rect.left = xm
                    enemigo.rect.top = ym
                    listaPosicion.append(enemigo)
                    xm, ym = pygame.mouse.get_pos()
                    contadores=[]
                    for tiros in range(len(listaLugares)-5):
                        xb, yb, anchoB, altoB = listaLugares[tiros].rect
                    contadores.append((cont))
                    contadores.sort()
                    i=random.randint(1,6)
                    if xm >= xb and xm <= xb + anchoB:
                            if i==i:
                                cont+=1
                                efecto.play()
                            elif not i ==1:
                                cont-=1
                                efecto1.play()
                            if ym >= yb and ym <= yb + altoB:
                                estados="jugando"
                    contadores=[]
                    for tiros in range(len(listaLugares)-2):
                        xb, yb, anchoB, altoB = listaLugares[tiros].rect
                        contadores.append((cont))
                    i = random.randint(1, 6)
                    if xm >= xb and xm <= xb + anchoB:
                        if i == 3:
                            cont += 1
                            efecto.play()
                        elif not i == 3:
                            cont -= 1
                            efecto1.play()
                        if ym >= yb and ym <= yb + altoB:
                            estados = "jugando"
                    contadores = []
                    for tiros in range(len(listaLugares)):
                        xb, yb, anchoB, altoB = listaLugares[tiros].rect
                    i = random.randint(1, 6)
                    if xm >= xb and xm <= xb + anchoB:
                        if i == 6:
                            cont += 1
                            efecto.play()
                        elif not i == 6:
                            cont -= 1
                            efecto1.play()
                        if ym >= yb and ym <= yb + altoB:
                            estados = "jugando"
                    contadores.append((cont))

        #Crear texto en pantalla

        fuente = pygame.font.SysFont("monospace", 48)
        texto = fuente.render("Tus goles son :) " + str(cont), 1, BLANCO)
        texto1=fuente.render("Tu mayor puntaje fue de "+str(contadores),1,ROJO)

        ventana.blit(texto, (ANCHO // 2 -250, 0))


        frameActual = obtenerFrame(timerAnimacion, listaSprites)
        frameActual2 = obtenerFrame2(timerAnimacion, listaSprites2)


        pygame.display.flip()  # Actualiza trazos
        timerAnimacion += reloj.tick(40) / 1000  # Tiempo exacto entre frames
        if timerAnimacion >= TIEMPO_TOTAL:
            timerAnimacion = 0
                # Dibujar, aquí haces todos los trazos que requieras

        if estados=="Menu":
            ventana.blit(instrucciones, (0, 0))
            dibujarMenu(ventana,btnJugar)

        elif estados=="jugando":
            ventana.blit(Fondo, (0, 0))
            dibujarJuego(ventana, listaPosicion, listaBalas)

            generarLugares(listaLugares,lugarTiro)

            for lugares in listaLugares:
                ventana.blit(lugares.image,lugares.rect)
            ventana.blit(frameActual.image, frameActual.rect)
            ventana.blit(frameActual2.image, frameActual2.rect)

            if cont>=25:
                ventana.blit(final, (0, 0))
                ventana.blit(texto1, (ANCHO // 2 -385,100))
            if cont<=-10:
                ventana.blit(perder, (0, 0))
                ventana.blit(texto1, (ANCHO // 2  -385, 100))

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()