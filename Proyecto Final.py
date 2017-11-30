# encoding: UTF-8
# Autor: Neftalí Rodríguez Martínez.
# Se muestra un juego donde el objetivo es cazar a bugs bunny.

#Importamos las librerías a utilizar.
import pygame
from random import randrange

# Dimensiones de la pantalla.
ANCHO = 800
ALTO = 600
# Colores.
BLANCO = (255, 255, 255)
ROJO = (230, 0, 38)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
MORADO = (120, 40, 140)
#Datos importantes
vida=100
score=0
estado="menu"
contadorColisiones = 0


def dibujarMenu(ventana, btnJugar): # Dibuja en pantalla los botones del menu.
    ventana.blit(btnJugar.image, btnJugar.rect)

    fuente = pygame.font.SysFont("monospace", 40)
    texto = fuente.render("¡Bienvenido, es hora de jugar!", 1, AZUL)
    ventana.blit(texto, (ANCHO // 2 - 365, ALTO // 2 - 250))

    mejorPuntaje = open("score.txt", "r")
    linea = mejorPuntaje.read()
    mejorPuntaje.close()

    if linea == "" or int(linea) == 0:
        linea = "0"
    elif int(linea) > 0:
        linea = str(linea)

    fuente2 = pygame.font.SysFont("semibold", 40)
    texto2 = fuente2.render("Mejor Puntaje: "+linea, 1, NEGRO)
    ventana.blit(texto2, (ANCHO // 2 - 120, ALTO - (btnJugar.rect.height + 50)))


def dibujarJuego(ventana, elmer, listaEnemigos, listaBalas, imgBugs): #Dibujo de objetos y efectos a lo largo del juego.
    global vida
    global score
    global estado
    global contadorColisiones

    efecto = pygame.mixer.Sound("punch.wav")

    # Dibujar objetos en pantalla
    ventana.blit(elmer.image, elmer.rect)

    for bugs in listaEnemigos:
        ventana.blit(bugs.image, bugs.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


    #Verificar si bugs se sale de la pantalla.
    for bugs in listaEnemigos:
        bugs.rect.left -= 8
        if bugs.rect.left <= -100 or bugs.rect.top >= ALTO:
            bugs.rect.left = ANCHO - 100
            bugs.rect.top = randrange(0, 500, 1)
            vida -= 10

    #Verificar Colisiones elmer vs bugs.
    for bugs in listaEnemigos:
        if bugs.rect.colliderect(elmer):
            bugs.rect.left = ANCHO - 100
            bugs.rect.top = randrange(0, 500, 1)
            vida -= 10

    # Verificar Colisiones bala vs bugs.
    for bala in listaBalas:
        for bugs in listaEnemigos:
            if bugs.rect.colliderect(bala):
                bugs.rect.left = ANCHO - 100
                bugs.rect.top = randrange(0, 500, 1)
                listaBalas.remove(bala)
                efecto.play()
                score += 10
                contadorColisiones += 1
                if contadorColisiones % 5 == 0:
                    vida += 5
                break


    #Letreros en pantalla
    scoreStr = str(score)
    vidaStr = str(vida)
    fuente = pygame.font.SysFont("monospace", 20)
    texto = fuente.render("Score: " + scoreStr + " Vida: " + vidaStr, 1, BLANCO)
    ventana.blit(texto, (ANCHO - 250, 0))
    texto2 = fuente.render("Bunnies atrapados: "+str(contadorColisiones), 1, BLANCO)
    ventana.blit(texto2, (0, 0))

    if vida <= 0:
        estado="sin_vida"


def generarEnemigos(listaEnemigos, imgBugs): #Generamos a BUGS BUNNY.
    for k in range(4):
        xCoord = ANCHO - 100
        yCoord = randrange(0, 500, 1)
        bugs = pygame.sprite.Sprite()
        bugs.image = imgBugs
        bugs.rect = imgBugs.get_rect()
        bugs.rect.left = xCoord
        bugs.rect.top = yCoord
        listaEnemigos.append(bugs)



def generarBalas(listaBalas, listaEnemigos, imgBugs): #Generamos las balas

    for bala in listaBalas:
        bala.rect.left += 5

    for e in listaEnemigos:
        e.rect.top += 1
        #Eliminar balas fuera de la pantalla.
        for k in range(-1, len(listaBalas)-1, -1):
            if listaBalas[k].rect.left <= -16:
                listaBalas.remove(listaBalas[k])


def dibujarSinVida(ventana): #Función para dibujar la pantalla de estado "sin_vida".
    global score
    mejorPuntaje = open("score.txt", "r")
    linea = mejorPuntaje.read()
    mejorPuntaje.close()

    if linea == "" or int(score) > (int(linea)):
        nuevoPuntaje = open("score.txt", "w")
        nuevoPuntaje.write(str(score))
        nuevoPuntaje.close()

    fuente = pygame.font.SysFont("monospace", 32)
    texto = fuente.render("Lo siento, te has quedado sin vida.", 1, AZUL)
    ventana.blit(texto, (65, 30))
    texto2= fuente.render("Mejor puntaje: "+linea, 1, AZUL)
    ventana.blit(texto2, (220, 500))


def dibujarInstrucciones(ventana, btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)

    fuente = pygame.font.SysFont("semibold", 40)
    texto = fuente.render("INSTRUCCIONES", 1, ROJO)
    ventana.blit(texto, (ANCHO // 2 - 115, 0))

    fuente2 = pygame.font.SysFont("semibold", 30)
    texto2 = fuente2.render(" Flecha arriba y abajo para moverte", 1, ROJO)
    ventana.blit(texto2, (0, 60))

    texto3 = fuente2.render(" Barra de espacio para disparar", 1, ROJO)
    ventana.blit(texto3, (0, 110))

    texto4 = fuente2.render(" Consigue la mayor cantidad de puntos derrotando a Bugs Bunny", 1, ROJO)
    ventana.blit(texto4, (0, 160))

    texto5 = fuente2.render(" Derrota a Bugs Bunny antes de que salga de la pantalla o te toque", 1, ROJO)
    ventana.blit(texto5, (0, 210))

    texto6 = fuente2.render(" Pierdes vida si Bugs Bunny logra escapar o te toca", 1, ROJO)
    ventana.blit(texto6, (0, 260))

    texto7 = fuente2.render(" Por cada 5 disparos acertados obtienes 5 puntos de vida", 1, ROJO)
    ventana.blit(texto7, (0, 310))

    texto8 = fuente2.render(" El juego termina si te quedas sin vida", 1, ROJO)
    ventana.blit(texto8, (0, 360))

    texto9 = fuente2.render(" ¡Establece una nueva marca con el mayor puntaje!", 1, ROJO)
    ventana.blit(texto9, (0, 410))

    mejorPuntaje = open("score.txt", "r")
    linea = mejorPuntaje.read()
    mejorPuntaje.close()
    if linea == "" or int(linea) == 0:
        linea = "0"
    elif int(linea) > 0:
        linea = str(linea)
    texto10 = fuente2.render("Mejor Puntaje: " + linea, 1, ROJO)
    ventana.blit(texto10, (0, 460))



def jugar (): # Función dónde se está programando el juego.
    global estado


    #Imagenes.
    imgFondoJuego = pygame.image.load("juego.png")  #Imagen  de fondo jugando
    imgFondoGanaste = pygame.image.load("ganaste.png")  #Imagen de fondo ganaste
    imgElmer = pygame.image.load("elmer.png")   #Imagen personaje bueno
    imgBugs = pygame.image.load("bugs.png")     #Imagen personaje enemigo
    imgBala = pygame.image.load("bullet.png")   #Imagen de la bala
    imgBotonJugar = pygame.image.load("button_jugar.png")
    imgFondoMenu = pygame.image.load("menu.png")
    imgPerdiste = pygame.image.load("sin_vida.png")

    #Botones.
    btnJugar = pygame.sprite.Sprite()  # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO - (btnJugar.rect.height + 20)

    #Personaje bueno.
    elmer = pygame.sprite.Sprite()
    elmer.image = imgElmer
    elmer.rect = imgElmer.get_rect()
    elmer.rect.left = 0
    elmer.rect.top = ALTO // 2 - elmer.rect.height // 2

    dyPersonaje = 0
    moverPersonaje = False

    #Bala.
    listaBalas = []

    #Enemigo.
    listaEnemigos = []
    generarEnemigos(listaEnemigos, imgBugs)

    #Score y Vida.
    #score = 0
    #vida = 100


    pygame.init()   #Se inicia el juego.
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana
    pygame.display.set_caption("Caza Bugs")
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Estados.
    estado = "menu"

    pygame.mixer.music.load("opening.mp3")
    pygame.mixer.music.play(-1)



    while not termina:
        #Procesa los eventos que ocurren en la ventana de pygame.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm >= xb and xm <= xb+anchoB:
                        if ym >= yb and ym <= yb+altoB:
                            estado = "instrucciones"

                elif estado == "instrucciones":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugando1"



            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                        dyPersonaje = -20
                        moverPersonaje = True

                elif evento.key == pygame.K_DOWN:
                    dyPersonaje = +20
                    moverPersonaje = True

                elif evento.key == pygame.K_SPACE:
                    #Crear bala.
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = 50
                    bala.rect.top = elmer.rect.top + 50
                    listaBalas.append(bala)

            elif evento.type == pygame.KEYUP:
                dyPersonaje = 0
                moverPersonaje = False


        #Borra la pantalla.
        if estado == "menu":
            ventana.blit(imgFondoMenu, (0,0))
        elif estado == "instrucciones":
            ventana.fill(NEGRO)
        elif estado == "jugando1":
            ventana.blit(imgFondoJuego, (0,0))
        elif estado == "sin_vida":
            ventana.blit(imgPerdiste, (0,0))




        #Dibujar.
        if estado == "menu":
            dibujarMenu(ventana, btnJugar)

        elif estado == "instrucciones":
            dibujarInstrucciones(ventana, btnJugar)

        elif estado == "jugando1":
            dibujarJuego(ventana, elmer, listaEnemigos, listaBalas, imgBugs)
            generarBalas(listaBalas, listaEnemigos, imgBugs)
            if moverPersonaje:
                if elmer.rect.top + dyPersonaje < ALTO - elmer.rect.height and elmer.rect.top + dyPersonaje > 0:
                    elmer.rect.top += dyPersonaje

        elif estado == "sin_vida":
            dibujarSinVida(ventana)
        #elif estado == "ganaste":
            #dibujarGanaste(ventana)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit() #termina pygame



def main ():
    jugar()

main()