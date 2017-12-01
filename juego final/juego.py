#encoding: UTF-8
#Autor: Omar Israel Galván García
#A01745810
#Videojuego

import pygame   #se importa la librerìa de pygame
from random import randint  #se importa la libreria de aleatorio

ANCHO = 800 #se define el ancho de la pantala
ALTO = 600  #se define el alto de la pantalla
BLANCO = (255, 255, 255)    #se genera el color blanco en RGB
NEGRO = (0, 0, 0)   #se genera el color negro en RGB


def dibujarMenu(ventana, boton,botonDos):       #dibuja el menú
    ventana.blit(boton.img, boton.rect) #dibuja el boton de jugar
    ventana.blit(botonDos.img,botonDos.rect)    #dibuja el boton de instrucciones


def dibujarJuego(ventana, fondoMar):    #dibuja el juego
    ventana.fill(BLANCO)    #limpia la pantalla
    ventana.blit(fondoMar, (0, 0))  #dibuja el mar

def generarEnemigosAzar(listaEnemigos,enemigoImagen):   #genera los enemigos

    cx = randint(20,ANCHO-128)  #genera coordenadas aleatorias en el eje x
    cy = randint(50,ALTO-50)    #genera coordenadas aleatorias en el eje y
    enemigo = pygame.sprite.Sprite()    #crea el sprite del enemigo
    enemigo.img = enemigoImagen     #crea la imagen en sprite
    enemigo.rect = enemigoImagen.get_rect() #obtiene los bordes de la imagen
    enemigo.rect.left =ANCHO    #coordenada en el eje x
    enemigo.rect.top = cy   #coordenada en el eje y
    listaEnemigos.append(enemigo)   #agrega los elemntos a la lista


def dibujarObjetos(ventana,listaEnemigos,listaProyectiles): #dibuja los objetos
    for enemigo in listaEnemigos:   #visita cada uno de los elementos en la lista
        ventana.blit(enemigo.img,enemigo.rect)  #dibuja los enemigos

    for fuego in listaProyectiles:  #visita cada uno de los elementos de la lista
        ventana.blit(fuego.img,fuego.rect)  #dibuja los elementos

def moverEnemigos(ventana,listaEnemigos):   #desplaza a los enemigos por el eje x
    for enemigo in listaEnemigos:   #visita los elementos de la lista
        enemigo.rect.left -= 10 #lo mueve 10 unidades a la izquierda
        if enemigo.rect.left <0:    #si es menor a 0 de la pantalla
            listaEnemigos.remove(enemigo)   #lo elimina de la lista

        if enemigo.rect.left ==100: #si pasa la "barrera"
            return 1    #regresa 1
        else:
            return 0    #regresa 0

def actualizarDisparos(listaProyectiles,listaEnemigos): #actualiza los disparos
    estatus = False #variable de control
    for fuego in listaProyectiles:  #recorre la lista de proyectiles
        fuego.rect.left += 20   #mueve el proyectil 20 unidades
        if fuego.rect.left >= ANCHO:    #si el proyectil sale de la pantalla
            listaProyectiles.remove(fuego)  #borra el proyectil
            continue    #continua analizando
        borrarDisparo = False   #variable de control


        for k in range(len(listaEnemigos)-1,-1,-1): #visita la lista de enemigos
            enemigo = listaEnemigos[k]  #enemigo en indice k

            if fuego.rect.colliderect(enemigo): #si choca con el enemigo
                listaEnemigos.remove(enemigo)   #lo elimina de la lista
                estatus = True  #el estatus se vuelve verdadero
                borrarDisparo = True    #borrar disparo se vuelve verdadero
                break   #termina el ciclo

        if borrarDisparo:   #si es verdadera la variable
            listaProyectiles.remove(fuego)  #elimina el fuego de la lista

        if estatus == True: #revisa el estatus
            return 1    #regresa 1
        else:
            return 0    #regresa 0

def mostrarPuntos(ventana, puntos): #muestra los puntos obtenidos
    fuente = pygame.font.SysFont("monospace",80)    #crea la fuente
    texto = fuente.render("Puntos: ",1,BLANCO)  #crea el texto
    points = fuente.render(str(puntos),1,BLANCO)    #guarda los puntos
    ventana.blit(texto,(ANCHO//2+80,0)) #dibuja el texto
    ventana.blit(points,(ANCHO//2+300,0))   #dibuja los puntos


def hasPerdido(ventana,imagenMenu): #cuando pierde
    ventana.fill(BLANCO)    #se limpia la pantalla
    perder = pygame.image.load("derrota.png")   #carga la imagen
    fuente = pygame.font.SysFont("monospace",80)    #crea una fuente
    texto = fuente.render("LOS PECES HAN",1,NEGRO)  #crea el texto 1
    texto2 = fuente.render("INVADIDO MI CASA",1,NEGRO)  #crea el texto 2
    texto3 = fuente.render("VUELVE A INTENTARLO",1,NEGRO)   #crea el texto 3
    ventana.blit(texto,(0,0))   #dibuja los textos
    ventana.blit(texto2,(0,100))
    ventana.blit(texto3,(0,200))
    ventana.blit(perder,(ANCHO//2,ALTO//2))

    im = pygame.sprite.Sprite() #crea un sprite
    im.img = imagenMenu
    im.rect = imagenMenu.get_rect()
    im.rect.left = ANCHO - im.rect.width - 10
    im.rect.top = ALTO - im.rect.height - 10

    ventana.blit(im.img, (im.rect.left, im.rect.top))   #dibuja el sprite

def dibujarVidas(ventana, VIDAS,imagenMenu):    #dibuja las vidas
    vida = pygame.image.load("vida.png")    #carga la imagen
    fuente = pygame.font.SysFont("monospace", 60)   #crea la fuente
    texto = fuente.render("VIDAS: ", 1, BLANCO) #crea el texto
    ventana.blit(texto, (10, 10))   #dibuja el texto

    if VIDAS == 5:  #analiza las vidas
        ventana.blit(vida,(150,5))
        ventana.blit(vida,(190,5))
        ventana.blit(vida,(230,5))
        ventana.blit(vida,(270,5))
        ventana.blit(vida,(310,5))
    elif VIDAS == 4:
        ventana.blit(vida, (150, 5))
        ventana.blit(vida, (190, 5))
        ventana.blit(vida, (230, 5))
        ventana.blit(vida, (270, 5))
    elif VIDAS == 3:
        ventana.blit(vida, (150, 5))
        ventana.blit(vida, (190, 5))
        ventana.blit(vida, (230, 5))
    elif VIDAS == 2:
        ventana.blit(vida, (150, 5))
        ventana.blit(vida, (190, 5))
    elif VIDAS == 1:
        ventana.blit(vida, (150, 5))
    elif VIDAS <= 0:
        hasPerdido(ventana,imagenMenu)


def dibujarIntro(ventana, iPez,imagenMenu): #dibuja la historia
    ventana.fill(BLANCO)    #limpia la pantalla
    ventana.blit(iPez,(ANCHO-300,100))  #dibuja pez azul
    fuente = pygame.font.SysFont("monospace",40)    #crea la fuente
    texto = fuente.render("Hola!, Soy Azulín, mi casa ha sido invadida",1,NEGRO)    #crea los textos
    texto2 = fuente.render("por peces malos,ayudame a eliminarlos",1,NEGRO)
    texto3 = fuente.render("usando las flechas de tu teclado para",1,NEGRO)
    texto4 = fuente.render("moverme y la barra espaciadora para",1,NEGRO)
    texto5 = fuente.render("disparar.No dejes que pasen! Sino se",1,NEGRO)
    texto6 = fuente.render("comerán mi comida",1,NEGRO)

    ventana.blit(texto,(10,25)) #dibuja los textos
    ventana.blit(texto2,(10,50))
    ventana.blit(texto3,(10,75))
    ventana.blit(texto4,(10,100))
    ventana.blit(texto5,(10,125))
    ventana.blit(texto6,(10,150))

    im = pygame.sprite.Sprite() #crea un sprite para regresar
    im.img = imagenMenu
    im.rect = imagenMenu.get_rect()
    im.rect.left = ANCHO - im.rect.width-10
    im.rect.top = ALTO - im.rect.height-10

    ventana.blit(im.img,(im.rect.left,im.rect.top)) #dibuja el sprite


def felicitaciones(ventana):    #felicitaciones
    fuente = pygame.font.SysFont("monospace",80)    #crea una funete
    texto = fuente.render("VAS MUY BIEN!",1,BLANCO)
    texto2 = fuente.render("SIGUE ASI!", 1, BLANCO)
    ventana.blit(texto,(100,100))
    ventana.blit(texto2,(100,150))



def dibujar():  #funcion principal
    mov = 0 #variables
    estado = 0
    movPezx = 10
    movPezy = 100
    direcc = True
    listaProyectiles = []
    listaEnemigos = []
    timer = 0
    timer2 = 0
    avance = 50
    resultado = 0
    puntos = 0
    VIDAS = 5

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    jugar = pygame.image.load("boton.png")  # imagen obtenida de: https://dabuttonfactory.com/
    intrucciones = pygame.image.load("instruccion.png")
    iPez = pygame.image.load("introPez.png")

    boton = pygame.sprite.Sprite()
    boton.img = jugar
    boton.rect = jugar.get_rect()
    boton.rect.left = ANCHO // 2 - boton.rect.width // 2
    boton.rect.top = ALTO // 2 - 150

    botonDos = pygame.sprite.Sprite()
    botonDos.img = intrucciones
    botonDos.rect = intrucciones.get_rect()
    botonDos.rect.left = ANCHO //2 - botonDos.rect.width //2
    botonDos.rect.top = ALTO //2-botonDos.rect.height+150




    p = pygame.image.load("imagenpez.png")
    pez = pygame.sprite.Sprite()
    pez.img = p
    pez.rect = p.get_rect()
    pez.rect.left = movPezy
    pez.rect.top = movPezx

    inversionPez = pygame.transform.flip(pez.img,True,False)

    enemigoImagen = pygame.image.load("enemigoAzul.png")
    fuegoImagen = pygame.image.load("Fuego01.png")
    fondoMar = pygame.image.load("fm.jpg")  # imagen obtenida de: https://www.google.com.mx/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiS5YCY6OLXAhUIPCYKHS8fB1YQjBwIBA&url=http%3A%2F%2Fimagenes.4ever.eu%2Fdata%2Fdownload%2Fanimados%2Ffondo-del-mar-189765.jpg&psig=AOvVaw0LUxhn4Atm04XYli1BMFPp&ust=1512011564789671
    imagenComida = pygame.image.load("comida.png")
    imagenMenu = pygame.image.load("principal.png")

    im = pygame.sprite.Sprite()
    im.img = imagenMenu
    im.rect = imagenMenu.get_rect()
    im.rect.left = ANCHO - im.rect.width
    im.rect.top = ALTO - im.rect.height


    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play()

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN: #pregunta si el usuario hizo click
                xm, ym = pygame.mouse.get_pos() #obtiene la posición del mouse
                xb, yb, anchoB, altoB = boton.rect
                if xm >= xb and xm <= xb + anchoB:
                    if ym >= yb and ym <= yb + altoB:
                        estado = 1

                x2,y2,a2,al2 = botonDos.rect
                if xm>= x2 and xm <= x2 + a2:
                    if ym >= y2 and ym <= y2+al2:
                        estado = 2

                x3,y3,a3,al3 = im.rect
                if xm>= x3 and xm <= x3 + a3:
                    if ym >= y3 and ym <= y3+al3:
                        estado = 0

            elif evento.type == pygame.KEYDOWN: #si la tecla es pulsada
                if evento.key == pygame.K_UP:
                    movPezy -= avance   #incrementa la variable de movimiento del pez
                    pygame.mixer.music.load("burbujas.mp3")  # sonidos obtenidos de: http://www.sonidosmp3gratis.com
                    pygame.mixer.music.play()   #reproduce el sonido

                elif evento.key == pygame.K_DOWN:
                    movPezy += avance
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()

                elif evento.key == pygame.K_LEFT:
                    movPezx -= avance
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()
                    direcc = True

                elif evento.key == pygame.K_RIGHT:
                    movPezx += avance
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()
                    direcc = False

                elif evento.key == pygame.K_SPACE:
                    pygame.mixer.music.load("disparo.mp3")  # sonidos obtenidos de: http://www.sonidosmp3gratis.com
                    pygame.mixer.music.play()   #reproduce el sonido
                    fuego = pygame.sprite.Sprite()  #crea un sprite nuevo
                    fuego.img = fuegoImagen
                    fuego.rect = fuegoImagen.get_rect()
                    fuego.rect.left = movPezx   #mueve el fuego en el eje x
                    fuego.rect.top = movPezy+5  #mueve el fuego en el eje y
                    listaProyectiles.append(fuego)  #agrega el proyectil a la lista

        if estado == 0:
            fondo = pygame.image.load( "fondo.jpg")  # imagen obtenida de: https://professor-falken.com/wp-content/uploads/2017/01/noche-estrellas-espacio-constelacion-galaxia-universo-Fondos-de-Pantalla-HD-professor-falken.com_.jpg
            ventana.blit(fondo, (mov, 0))   #dibuja el fondo
            dibujarMenu(ventana, boton,botonDos)    #dibuja los botones
            mov -= 1    #movimiento del fondo
            if mov<= -ANCHO+300:    #si es mayor al al ancho +300
                mov = 0 #se reinicia el contador

        if estado == 1:
            dibujarJuego(ventana, fondoMar) #dibuja los elementos
            if direcc == True:
                ventana.blit(pez.img,(movPezx,movPezy)) #dibuja al pez
            elif direcc == False:
                ventana.blit(inversionPez,(movPezx,movPezy))    #dibuja el pez invertido

            resultado = (actualizarDisparos(listaProyectiles, listaEnemigos))   #si el disparo alcanzó un enemigo
            dibujarObjetos(ventana, listaEnemigos, listaProyectiles)    #dibuja los objetos
            salud = (moverEnemigos(ventana, listaEnemigos)) #dibuja las vidas

            if timer >= 2:  #si el timer es mayor o igual a 2
                generarEnemigosAzar(listaEnemigos,enemigoImagen)    #genera los enemigos
                timer = 0   #se reinicia el timer

            if resultado == 1:  #si chocó con un enemigo
                puntos += 10    #suma 10 puntos

            mostrarPuntos(ventana,puntos)   #dibuja los puntos obtenidos

            if salud == 1:  #si un enemigo pasa la barrera
                VIDAS -= 1  #se resta una vida
            dibujarVidas(ventana,VIDAS,imagenMenu)  #dibuja las vidas

            if puntos/100 == 1: #si obtiene 100 puntos
                felicitaciones(ventana) #felicita al usuario

        if estado == 2:
            dibujarIntro(ventana,iPez,imagenMenu)   #dibuja la historia

        timer += 1/40   #se crea el timer

        pygame.display.flip()   #actualiza pygame
        reloj.tick(40)  #40fps

    pygame.quit()   #sale de pygame


def main(): #funcion main
    dibujar()   #funcion principal


main()