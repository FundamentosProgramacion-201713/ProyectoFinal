#Autor: Mónica Monserrat Palacios Rodríguez
#encoding-UTF-8
#Video Juego de Acertijos

import pygame
from random import randint
from random import shuffle

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def mostrarAcertijo(acertijo, opcion1, opcion2, correcta,ventana):
    fuente1 = pygame.font.SysFont("Times New Roman", 20)
    fuente = pygame.font.SysFont("Times New Roman", 40)
    texto = fuente1.render(str(acertijo), 1, BLANCO)
    texto2 = fuente.render(str(opcion1), 1, BLANCO)
    texto3 = fuente.render(str(opcion2), 1, BLANCO)
    texto4 = fuente.render(str(correcta), 1, BLANCO)
    texto5 = fuente.render('Escribe a, b o c', 1, BLANCO)



    ventana.blit(texto, (0, 14))
    ventana.blit(texto2, (150, 100))
    ventana.blit(texto3, (150, 200))
    ventana.blit(texto4, (150, 300))
    ventana.blit(texto5, (150, 400))





def crearArchivo(ventana, evento, num):
    entrada = open("respuestas.txt", "r", encoding='UTF-8')  # Especificaciones para leer archivos y escribirlos
    lista = entrada.readlines()
    entrada.close()

    datos = (lista[num]).split(";")


    acertijo = datos[0]
    opcion1 = datos[1]
    opcion2 = datos[2]
    correcta = str(datos[3])

    mostrarAcertijo(acertijo, opcion1, opcion2, correcta, ventana)




    '''if evento.type == pygame.MOUSEBUTTONDOWN:#El usuario hizo click con el mouse
        xm, ym = pygame.mouse.get_pos()
        xb, yb, anchoB, altoB = botonNext.rect
        if xm >= xb and xm <= xb + anchoB:
            if ym >= yb and ym <= yb + altoB:'''







def dibujarWin(ventana, fondo, imgWin):
    ventana.blit(fondo, (0, 0))
    ventana.blit(imgWin, (0,0))
    fuente1 = pygame.font.SysFont("Times New Roman", 75)
    texto = fuente1.render(str('FELICIDADES'), 1, BLANCO)
    texto2 = fuente1.render(str('CIERRA E INTENTA DE NUEVO'), 1, BLANCO)


    ventana.blit(texto, (0, 400))
    ventana.blit(texto2, (0, 500))





def dibujarFail(ventana, fondoFail, imgFail):
    ventana.blit(fondoFail, (0, 0))
    ventana.blit(imgFail, (50, 0))
    fuente1 = pygame.font.SysFont("Times New Roman", 75)
    texto = fuente1.render(str('CIERRA E INTENTA DE NUEVO'), 1, BLANCO)

    ventana.blit(texto, (0, 500))


def dibujarMenu(ventana,botonJugar, back):
    ventana.blit(back, (0, 0))
    ventana.blit(botonJugar.image,botonJugar.rect)

    fuente1 = pygame.font.SysFont("Times New Roman", 200)
    fuente2 = pygame.font.SysFont("Arial", 40)
    texto = fuente1.render('Bienvenido', 1, NEGRO)
    texto2 = fuente2.render('Oprime Jugar', 1, NEGRO)
    texto3 = fuente2.render('Adivina el acertijo', 1, NEGRO)


    ventana.blit(texto, (10, 10))
    ventana.blit(texto2, (10, 200))
    ventana.blit(texto3, (10, 300))




def dibujarJuego(ventana, listaEnemigos,back,x,listaCerebro,evento):
    ventana.blit(back, (x, 0))

    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
        enemigo = listaEnemigos[0]

    for cerebro in listaCerebro:
        ventana.blit(cerebro.image, cerebro.rect)





def generarEnemigos(listaEnemigos, imgEnemigo):
    for x in range(5):
        for y in range(1):
            cx = 60 + x * 450
            cy = 30 + y * 140
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)




def genrearCerebro(listaCerebro, imgCerebro):
    for x in range(1):
        for y in range(1):

            cerebro = pygame.sprite.Sprite()
            cerebro.image = imgCerebro
            cerebro.rect = imgCerebro.get_rect()
            cerebro.rect.left = ANCHO//2 -50
            cerebro.rect.top = ALTO//2+100
            listaCerebro.append(cerebro)


def generarEnemigosClick(listaEnemigos, imgEnemigo):
    cx = randint(20, ANCHO - 128)
    cy = randint(50, ALTO - 300)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    enemigo.rect.left = cx
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)




def eliminarEnemigos(listaEnemigos, evento, imgEnemigo, ventana, fondoWin, imgWin, fondoFail, imgFail, botonJugar):
    num = randint(0,26)
    if len(listaEnemigos) >= 1:
        enemigo = (listaEnemigos[0])
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:
                listaEnemigos.remove(enemigo)

            elif evento.key == pygame.K_a or evento.key == pygame.K_b:
                generarEnemigosClick(listaEnemigos, imgEnemigo)


        elif len(listaEnemigos) > 7:
            dibujarFail(ventana, fondoFail, imgFail)

    elif len(listaEnemigos) == 0:
        dibujarWin(ventana, fondoWin, imgWin)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución


    estado = "menu"  # jugando, fin

    # cargar imágenes
    imgBtnJugar = pygame.image.load("start1.png")
    backgroundImage = pygame.image.load("fondo.jpg")
    imgWin = pygame.image.load("win.png")
    fondoWin = pygame.image.load("heaven.jpg")
    imgFail = pygame.image.load("fail.jpg")
    fondoFail = pygame.image.load("hell.jpg")
    file = ('A_labio_dulce.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


    num = randint(0, 26)

    x=0
    # boton
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2


    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("enemigo.png")
    generarEnemigos(listaEnemigos, imgEnemigo)

    listaCerebro = []
    imgCerebro = pygame.image.load("cerebro1.png")

    genrearCerebro(listaCerebro,imgCerebro)



    # Tiempos
    timer = 0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN: #El usuario hizo click con el mouse
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana
                            estado = "jugando"


                elif estado == "jugando":
                    if (len(listaEnemigos)) == 0:
                        estado = "win"
                        if evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click con el mouse
                            xm, ym = pygame.mouse.get_pos()
                            xb, yb, anchoB, altoB = botonJugar.rect
                            if xm >= xb and xm <= xb + anchoB:
                                if ym >= yb and ym <= yb + altoB:
                                    # Cambiar de ventana
                                    estado = "menu"

                    elif (len(listaEnemigos)) >10:
                        estado = "fail"
                        if evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click con el mouse
                            xm, ym = pygame.mouse.get_pos()
                            xb, yb, anchoB, altoB = botonJugar.rect
                            if xm >= xb and xm <= xb + anchoB:
                                if ym >= yb and ym <= yb + altoB:
                                    # Cambiar de ventana
                                    estado = "menu"


        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras

        if estado == "menu":
            dibujarMenu(ventana, botonJugar, backgroundImage)

        elif estado == "jugandoagain":
            dibujarJuego(ventana, listaEnemigos, backgroundImage, x, listaCerebro, evento)
            eliminarEnemigos(listaEnemigos, evento, imgEnemigo, ventana, fondoWin, imgWin, fondoFail, imgFail,
                             botonJugar)



        elif estado == "jugando":

            dibujarJuego(ventana, listaEnemigos,backgroundImage,x, listaCerebro,evento)
            eliminarEnemigos(listaEnemigos,evento, imgEnemigo, ventana, fondoWin, imgWin, fondoFail, imgFail, botonJugar)
            crearArchivo(ventana, evento, num)

            'pygame.draw.rect(ventana, BLANCO, ((0, ANCHO), (20, ANCHO)))'


        elif estado == "win":
            dibujarWin(ventana, fondoWin, imgWin)
            dibujarMenu(ventana, botonJugar, backgroundImage)

        elif estado == "fail":
            dibujarFail(ventana, fondoFail, imgFail, listaEnemigos)
            dibujarMenu(ventana, botonJugar, backgroundImage)



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(100)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()