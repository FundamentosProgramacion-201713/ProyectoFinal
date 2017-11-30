#Autor: Irving Fuentes Aguilera
#Juego: Adaptación de Brick Breaker con la caricatura Rick and Morty
#Sprites animados de Rick y Morty, al igual que la canción utilizada se acreditan al juego Pocket Morty, sus creadores y a la serie como tal


import pygame
from random import *

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
aleatorio=(randint(0,255),randint(0,255),randint(0,255))



def generarLadrillos(listaLadrillos,imgLadrillo):
    for i in range(15):  # dibuja los ladrillos
        for j in range(6):
            cx= 35+i*50
            cy= 55+j*20
            nuevo = pygame.sprite.Sprite()
            nuevo.image = imgLadrillo
            nuevo.rect = imgLadrillo.get_rect()
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaLadrillos.append(nuevo)


def dibujarJuego(ventana,raqueta,listaLadrillos,pelota,tamañoLetra,puntuacion,xPuntuacion,yPuntuacion):
    ventana.blit(raqueta.image, raqueta.rect)
    font = pygame.font.SysFont("ComicSansMS", tamañoLetra)
    puntuacion=str(puntuacion)
    texto = font.render(puntuacion, True, (255, 255, 255))
    for ladrillo in listaLadrillos:
        ventana.blit(ladrillo.image, ladrillo.rect)
    ventana.blit(pelota.image, pelota.rect)
    mensaje = font.render("Score:", True, BLANCO)
    ventana.blit(mensaje, [xPuntuacion - 150, yPuntuacion])

def movimientoPelota(derecha,abajo,pelota,raqueta,DX,DY,vidas,listaLadrillos,puntuacion):
    if derecha:
        pelota.rect.left += DX  # x = x+3
    else:
        pelota.rect.left -= DX


    if pelota.rect.left <= 0:
        derecha = True

    if abajo:
        pelota.rect.top += DY
    else:
        pelota.rect.top -= DY

    if pelota.rect.left >= ANCHO - pelota.rect.width // 2:
        derecha = not derecha

    if pelota.rect.top < 0:
        abajo = True

    if pelota.rect.top >ALTO:
        vidas-=1


    if pelota.rect.colliderect(raqueta):
        abajo = False
        DY += 1

    for k in range(len(listaLadrillos) - 1, -1, -1):
        ladrillo = listaLadrillos[k]
        if pelota.rect.colliderect(ladrillo):
            listaLadrillos.remove(ladrillo)
            abajo = True
            puntuacion += 10
    return derecha, abajo, vidas, puntuacion, pelota.rect.top

def dibujarMenu(ventana, btnJugar,btnHS,titulo):
    imagenFondo = pygame.image.load("imagenes_fondo.jpg")
    ventana.blit(imagenFondo, (0, 0))
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnHS.image, btnHS.rect)
    ventana.blit(titulo.image,titulo.rect)

def reiniciarPosicion(pelota,raqueta):
    pelota.rect.left = 400 - pelota.rect.width // 2  # X
    pelota.rect.top = 600 - pelota.rect.height - 13  # Y
    raqueta.rect.left = 400 - raqueta.rect.width // 2  # X
    raqueta.rect.top = 600 - raqueta.rect.height  # Y

def juegoTerminado(gameOver,ventana):
    ventana.blit(gameOver.image,gameOver.rect)


def mostrarPuntuación(puntuacion, ventana, xPuntuacion, yPuntuacion, tamañoLetra):
    puntuacion=str(puntuacion)
    font = pygame.font.SysFont("ComicSansMS", tamañoLetra)
    texto = font.render(puntuacion ,True, BLANCO)
    ventana.blit(texto, [xPuntuacion,  yPuntuacion])


def dibujar():
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
      # Bandera para saber si termina la ejecución
    # Estado
    menu = True
    jugando= False
    highScore=False

    #Botones
    imgBotonJugar = pygame.image.load("PlayGameBtn.png")
    btnJugar = pygame.sprite.Sprite()
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2  # X
    btnJugar.rect.top = ALTO // 2 - 40  # Y
    imgBotonHS= pygame.image.load("HighScores.png")
    btnHS= pygame.sprite.Sprite()
    btnHS.image= imgBotonHS
    btnHS.rect = imgBotonHS.get_rect()
    btnHS.rect.left = ANCHO // 2 - btnJugar.rect.width // 2  # X
    btnHS.rect.top = ALTO // 2 + 50  # Y
    imgAdorno= pygame.image.load("Adorno.png")
    adorno= pygame.sprite.Sprite()
    adorno.image= imgAdorno
    adorno.rect= imgAdorno.get_rect()
    adorno.rect.left= 25
    adorno.rect.top=100

    #Sprites, objetos del juego
    imgPelota = pygame.image.load("Pelota.png")
    pelota = pygame.sprite.Sprite()
    pelota.image = imgPelota
    pelota.rect = imgPelota.get_rect()
    pelota.rect.left = 400 - pelota.rect.width // 2  # X
    pelota.rect.top = 600 - pelota.rect.height - 13  # Y
    imgRaqueta = pygame.image.load("Raqueta.png")
    raqueta = pygame.sprite.Sprite()
    raqueta.image = imgRaqueta
    raqueta.rect = imgRaqueta.get_rect()
    raqueta.rect.left = 400 - raqueta.rect.width // 2  # X
    raqueta.rect.top = 600 - raqueta.rect.height  # Y
    imgLadrillo = pygame.image.load("LadrilloEspecial.png")
    imgGameOver = pygame.image.load("GameOver.png")
    gameOver = pygame.sprite.Sprite()
    gameOver.image = imgGameOver
    gameOver.rect = imgGameOver.get_rect()
    gameOver.rect.left = ANCHO // 2 - btnJugar.rect.width // 2  # X
    gameOver.rect.top = ALTO // 2 - 40  # Y
    imgYouWin = pygame.image.load("YouWin.png")
    youWin = pygame.sprite.Sprite()
    youWin.image = imgYouWin
    youWin.rect = imgYouWin.get_rect()
    youWin.rect.left = ANCHO // 2 - btnJugar.rect.width // 2  # X
    youWin.rect.top = ALTO // 2 - 40  # Y
    imgVida1= pygame.image.load("Vida1.png")
    imgVida2= pygame.image.load("Vida2.png")
    imgVida3= pygame.image.load("Vida3.png")
    vida1 = pygame.sprite.Sprite()
    vida1.image = imgVida1
    vida1.rect = imgVida1.get_rect()
    vida1.rect.left = 5  # X
    vida1.rect.top = 10  # Y
    vida2 = pygame.sprite.Sprite()
    vida2.image = imgVida2
    vida2.rect = imgVida2.get_rect()
    vida2.rect.left = 50  # X
    vida2.rect.top = 10  # Y
    vida3 = pygame.sprite.Sprite()
    vida3.image = imgVida3
    vida3.rect = imgVida3.get_rect()
    vida3.rect.left = 100  # X
    vida3.rect.top = 10  # Y
    listaVidas=[]
    listaVidas.append(vida3)
    listaVidas.append(vida2)
    listaVidas.append(vida1)
    imgTitulo = pygame.image.load("Titulo.png")
    titulo = pygame.sprite.Sprite()
    titulo.image = imgTitulo
    titulo.rect = imgTitulo.get_rect()
    titulo.rect.left = ANCHO // 2 - titulo.rect.width // 2  # X
    titulo.rect.top = ALTO // 2 - 350  # Y


    # Ladrillos
    listaLadrillos = []
    generarLadrillos(listaLadrillos,imgLadrillo)
    #Variables
    DX = 15
    DY = 7.5
    derecha = True
    abajo = False
    moverRaqueta= True
    moverPelota= False
    moverPelotaInicial= True
    dxRaqueta=0
    xPuntuacion=730
    yPuntuacion=10
    tamañoLetra=50
    #Estadísitcas
    puntuacion=0
    vidas=3
    # Musica e imagen de fondo
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)
    imagenFondo = pygame.image.load("imagenes_fondo.jpg")
    imagenHighScores= pygame.image.load("FondoHighScores.png")
    y = 0

    efecto1 = pygame.mixer.Sound("GameOver.wav")
    efecto2 = pygame.mixer.Sound("Efecto2.wav")


    while menu:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                menu = False
                jugando=False
            elif  evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if menu==True:
                    xb, yb, anchoB, altoB = btnJugar.rect
                    xb2, yb2, anchoB2, altoB2= btnHS.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            menu=False
                            jugando=True
                    if xm>=xb2 and xm<=xb2+anchoB2:
                        if ym>=yb2 and ym<=yb2+altoB2:
                            menu=False
                            highScore=True

        ventana.blit(imagenFondo, (0,0))
        dibujarMenu(ventana, btnJugar,btnHS,titulo)
        ventana.blit(adorno.image, adorno.rect)
        pygame.display.flip()
        reloj.tick(60)

    while highScore:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                highScore = False
                jugando=False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    jugando=True
                    highScore=False

        entrada = open("HighScores.txt", "r")
        datos = entrada.readlines()
        nombres = []
        puntuaciones = []

        for linea in datos:
            linea = linea.rstrip()
            linea = linea.split(":")
            nombres.append(linea[0])
            puntuaciones.append(linea[1])


        ventana.blit(imagenHighScores, (0, 0))

        mostrarPuntuación(nombres[0], ventana, 200, 170, 45)
        mostrarPuntuación(nombres[1], ventana, 200, 250, 45)
        mostrarPuntuación(nombres[2], ventana, 200, 330, 45)

        mostrarPuntuación(puntuaciones[0], ventana, 600, 170, 45)
        mostrarPuntuación(puntuaciones[1], ventana, 600, 250, 45)
        mostrarPuntuación(puntuaciones[2], ventana, 600, 330, 45)
        font = pygame.font.SysFont("ComicSansMS", tamañoLetra)
        texto = font.render("HighScores", True, BLANCO)
        ventana.blit(texto, [ANCHO // 2-75,50 ])
        texto = font.render("Presiona ESC para comenzar a jugar", True, BLANCO)
        ventana.blit(texto, [100, 550])
        pygame.display.flip()
        reloj.tick(30)


    while jugando:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                jugando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dxRaqueta= -20
                    moverRaqueta= True
                    if moverPelota == False:
                        moverPelotaInicial= True
                if evento.key == pygame.K_RIGHT:
                    dxRaqueta= 20
                    moverRaqueta = True
                    if moverPelota == False:
                        moverPelotaInicial= True
            if evento.type == pygame.KEYUP:
                moverRaqueta = False
                moverPelotaInicial= False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    moverPelota = True
                    efecto2.play()

        ventana.fill(BLANCO)
        ventana.blit(imagenFondo, (0, y))
        ventana.blit(imagenFondo, (0, ALTO + y))

        y -= 1
        if y <= -ALTO:
            y = 0

        if moverRaqueta:
            raqueta.rect.left += dxRaqueta
        if moverPelotaInicial:
            pelota.rect.left += dxRaqueta
        if moverPelota:
            derecha, abajo, vidas, puntuacion, posicion=movimientoPelota(derecha,abajo,pelota,raqueta,DX,DY,vidas,listaLadrillos,puntuacion)
            if posicion>600:
                reiniciarPosicion(pelota,raqueta)
                moverPelota=False
                moverRaqueta=False
                abajo=False
                vidas=int((vidas-0.01)+0.01)
                for vida in range (0,len(listaVidas)):
                    listaVidas.remove(listaVidas[vida])
                    break

        if vidas==0:
            moverPelota=False
            moverRaqueta=False
            moverPelotaInicial=False
            juegoTerminado(gameOver,ventana)
            efecto1.play()


        if len(listaLadrillos)==0:
            moverPelota = False
            moverRaqueta = False
            moverPelotaInicial = False
            juegoTerminado(youWin, ventana)




        dibujarJuego(ventana, raqueta, listaLadrillos, pelota,tamañoLetra,puntuacion,xPuntuacion,yPuntuacion)
        mostrarPuntuación(puntuacion, ventana, xPuntuacion, yPuntuacion, tamañoLetra)
        for vida in listaVidas:
            ventana.blit(vida.image, vida.rect)
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()

    return puntuacion

def buscarMejorPuntuacion(puntuacion):
    entrada = open("HighScores.txt", "r")
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
        print(puntuaciones)
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
        datos = ""
        for x in range(3):
            datos += nombres[x] + ":" + str(puntuaciones[x]) + "\n"
        salida = open("HighScores.txt", "w")
        salida.write(datos)
        salida.close()


def main():
    puntuacion=dibujar()
    buscarMejorPuntuacion(puntuacion)


main()
