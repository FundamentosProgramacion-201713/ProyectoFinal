#encoding: UTF-8
#Autor: Omar Israel Galván García
#A01745810
#Videojuego

import pygame
from random import randint

ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


def dibujarMenu(ventana, boton):
    ventana.blit(boton.img, boton.rect)


def dibujarJuego(ventana, fondoMar):
    ventana.fill(BLANCO)
    ventana.blit(fondoMar, (0, 0))

def generarEnemigosAzar(listaEnemigos,enemigoImagen):

    cx = randint(20,ANCHO-128)
    cy = randint(50,ALTO)
    enemigo = pygame.sprite.Sprite()
    enemigo.img = enemigoImagen
    enemigo.rect = enemigoImagen.get_rect()
    enemigo.rect.left =cx
    enemigo.rect.top = cy
    listaEnemigos.append(enemigo)


def dibujarObjetos(ventana,listaEnemigos,listaProyectiles):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.img,enemigo.rect)

    for fuego in listaProyectiles:
        ventana.blit(fuego.img,fuego.rect)

def moverEnemigos(ventana,listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 10
        if enemigo.rect.left <0:
            listaEnemigos.remove(enemigo)


def actualizarDisparos(listaProyectiles,listaEnemigos):
    for fuego in listaProyectiles:
        fuego.rect.left += 20
        if fuego.rect.left >= ANCHO:
            listaProyectiles.remove(fuego)
            continue
        borrarDisparo = False
        for k in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[k]
            if fuego.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarDisparo = True
                break
            if borrarDisparo:
                listaProyectiles.remove(fuego )

def dibujar():
    # Ejemplo del uso de pygame

    mov = 0
    estado = 0
    movPezx = 0
    movPezy = 0
    direcc = True
    listaProyectiles = []
    listaEnemigos = []
    timer = 0

    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    jugar = pygame.image.load("boton.png")  # imagen obtenida de: https://dabuttonfactory.com/

    boton = pygame.sprite.Sprite()
    boton.img = jugar
    boton.rect = jugar.get_rect()
    boton.rect.left = ANCHO // 2 - boton.rect.width // 2
    boton.rect.top = ALTO // 2 - boton.rect.height // 2

    p = pygame.image.load("pezN.jpg")
    pez = pygame.sprite.Sprite()
    pez.img = p
    pez.rect = p.get_rect()
    pez.rect.left = movPezy
    pez.rect.top = movPezx

    inversionPez = pygame.transform.flip(pez.img,True,False)


    enemigoImagen = pygame.image.load("enemigo01.jpg")
    fuegoImagen = pygame.image.load("fuegoR.jpg")
    fondoMar = pygame.image.load("fm.jpg")  # imagen obtenida de: https://www.google.com.mx/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiS5YCY6OLXAhUIPCYKHS8fB1YQjBwIBA&url=http%3A%2F%2Fimagenes.4ever.eu%2Fdata%2Fdownload%2Fanimados%2Ffondo-del-mar-189765.jpg&psig=AOvVaw0LUxhn4Atm04XYli1BMFPp&ust=1512011564789671


    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb, yb, anchoB, altoB = boton.rect
                if xm >= xb and xm <= xb + anchoB:
                    if ym >= yb and ym <= yb + altoB:
                        estado = 1

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movPezy -= 10
                    pygame.mixer.music.load("burbujas.mp3")  # sonidos obtenidos de: http://www.sonidosmp3gratis.com
                    pygame.mixer.music.play()

                elif evento.key == pygame.K_DOWN:
                    movPezy += 10
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()

                elif evento.key == pygame.K_LEFT:
                    movPezx -= 10
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()
                    direcc = True

                elif evento.key == pygame.K_RIGHT:
                    movPezx += 10
                    pygame.mixer.music.load("burbujas.mp3")
                    pygame.mixer.music.play()
                    direcc = False

                elif evento.key == pygame.K_SPACE:
                    pygame.mixer.music.load("disparo.mp3")  # sonidos obtenidos de: http://www.sonidosmp3gratis.com
                    pygame.mixer.music.play()
                    fuego = pygame.sprite.Sprite()
                    fuego.img = fuegoImagen
                    fuego.rect = fuegoImagen.get_rect()
                    fuego.rect.left = movPezx
                    fuego.rect.top = movPezy+10
                    listaProyectiles.append(fuego)

        if estado == 0:
            fondo = pygame.image.load( "fondo.jpg")  # imagen obtenida de: https://professor-falken.com/wp-content/uploads/2017/01/noche-estrellas-espacio-constelacion-galaxia-universo-Fondos-de-Pantalla-HD-professor-falken.com_.jpg
            ventana.blit(fondo, (mov, 0))
            dibujarMenu(ventana, boton)
            mov -= 1

        if estado == 1:
            dibujarJuego(ventana, fondoMar)
            if direcc == True:
                ventana.blit(pez.img,(movPezx,movPezy))
            elif direcc == False:
                ventana.blit(inversionPez,(movPezx,movPezy))

            generarEnemigosAzar(listaEnemigos,enemigoImagen)
            actualizarDisparos(listaProyectiles,listaEnemigos)

            dibujarObjetos(ventana, listaEnemigos, listaProyectiles)
            moverEnemigos(ventana, listaEnemigos)



        timer += 1/40
        print(int(timer))


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    dibujar()


main()