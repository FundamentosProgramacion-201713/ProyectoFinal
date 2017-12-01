#encoding UTF-8
#Autor:Nazdira Abigail Cerda del Prado
#Proyecto: Juego ByeBlock

#Importar librerias
import pygame
from random import randint
from pygame import *

#Dimensiones de pantalla
ANCHO=800
ALTO=600

#Colores en escala RGB
BLANCO = (255, 255, 255)
MORADO= (203, 0, 255)
NEGRO=(0,0,0)

#Actualiza la lista de balas para que cuando colisionen con el enemigo se eliminen
def actualizarBalas(listaBalas, listaEnem):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue
        borrarBala = False
        for k in range(len(listaEnem) - 1, -1, -1):
            enemigo = listaEnem[k]

            if bala.rect.colliderect(enemigo):
                listaEnem.remove(enemigo)
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)

#Genera enemigos
def generarEnemigos(listaEnem, imgEnem):
    for x in range(8):
        for y in range(3):
            # Generar el enemigo en x, y
            cx = 50 + x * 100
            cy = 50 + y * 120
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnem
            enemigo.rect = imgEnem.get_rect()
            enemigo.rect.left = (cx - enemigo.rect.width // 2)
            # Generea bloques enemigos aparecen arriba de la mitad de la pantalla
            enemigo.rect.top = (cy - enemigo.rect.height // 2) // 2
            listaEnem.append(enemigo)

#Genera enemigos en coordenadas al azar
def generarEnemigoAzar(listaEnem, imgEnem):
    cx = randint(0, ANCHO)
    cy = randint(0, ALTO)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnem
    enemigo.rect = imgEnem.get_rect()
    enemigo.rect.left = cx - enemigo.rect.width // 2
    # Bloques enemigos se dibujan arriba de la mitad de la pantalla
    enemigo.rect.top = (cy - enemigo.rect.height // 2) // 2
    listaEnem.append(enemigo)

#Dibuja menu
def dibujarMenu(ventana, boton):
    ventana.blit(boton.image, boton.rect)

#Dibujo fondo
def dibujarFondo(ventana, imagenFondoINICIO):
    ventana.blit(imagenFondoINICIO, (0, 0))

#Dibuja juego (enemigos y balas)
def dibujarJuego(ventana, listaEnemigos, listaBalas):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

#Suma puntos ganados
def actualizarPUNTAJE(listaBalas, listaEnemigos, PUNTAJE):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            PUNTAJE=PUNTAJE-5

        for k in range(len(listaEnemigos) - 1, -1,-1):
            enemigo = listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                PUNTAJE = PUNTAJE + 10

    return PUNTAJE

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado= "menu" #Estado menu, estado incial donde el usuario elige la opción a ejecutar

    # Cargar Fondos
    imagenFondo = pygame.image.load("fondoJuegoInicio.png")
    imagenFondoFIN = pygame.image.load("fondoJuegoFin.png")
    imagenFondoPuntajes = pygame.image.load("fondoJuegoPuntaje.png")
    fondoMovimiento=pygame.image.load("fondoJuego.png")
    y=0

    # Cargar imagen/Sprite = ButonJugar
    imgBtnJugar = pygame.image.load("button_jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2 + 50

    # Cargar imagen/Sprite = ButonPuntajes
    imgBtnPuntajes = pygame.image.load("button_puntajes.png")
    botonPuntajes = pygame.sprite.Sprite()
    botonPuntajes.image = imgBtnPuntajes
    botonPuntajes.rect = imgBtnPuntajes.get_rect()
    botonPuntajes.rect.left = ANCHO // 2 - botonPuntajes.rect.width // 2 - 250
    botonPuntajes.rect.top = ALTO // 2 - botonPuntajes.rect.height // 2 + 150

    # Cargar imagen/Sprite = Menú
    imgBtPrincipal = pygame.image.load("button_menu.png")
    botonPrincipal = pygame.sprite.Sprite()
    botonPrincipal.image = imgBtPrincipal
    botonPrincipal.rect = imgBtPrincipal.get_rect()
    botonPrincipal.rect.left = ANCHO // 2 - botonPrincipal.rect.width // 2 - 300
    botonPrincipal.rect.top = ALTO // 2 - botonPrincipal.rect.height // 2 + 278

    # Enemigos
    listaEnem = []
    imgEnem = pygame.image.load("enemigo1.png")
    imgEnemigo2 = pygame.image.load("enemigo2.png")
    imgEnemigo3 = pygame.image.load("enemigo3.png")
    generarEnemigos(listaEnem, imgEnem)
    generarEnemigos(listaEnem, imgEnemigo2)
    generarEnemigos(listaEnem, imgEnemigo3)

    # Bloque bueno
    imgPersonaje = pygame.image.load("bloquebueno.png")
    xPersonaje = 0

    # Balas/Pelotas
    listaBalas = []
    imgBala = pygame.image.load("pelotaj.png")

    timerEnemigo2 = 0
    timerEnemigo3 = 0
    timerTIEMPO = 0

    # Puntos

    listaPuntajes = []
    puntajes = open("Puntajes.txt")
    puntajes2 = puntajes.readlines()

    for linea in puntajes2:
        listaPuntajes.append(linea)

    puntajeMax = max(listaPuntajes)

    PUNTAJE = 0

    pygame.mixer.init()
    pygame.mixer.music.load("CANCIONMENU.mp3")
    pygame.mixer.music.play(-1)

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Mouse en los diferentes estados...
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click
                # Posición del mouse
                xm, ym = pygame.mouse.get_pos()

                if estado == "menu":
                    # Posición del botón
                    xb, yb, anchoB, altoB = botonJugar.rect
                    xbP, ybP, anchoBP, altoBP = botonPuntajes.rect

                    if xm > xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana/estado
                            estado = "jugando"

                    if xm > xbP and xm <= xbP + anchoBP:
                        if ym >= ybP and ym <= ybP + altoBP:
                            # Cambiar de ventana/estado
                            estado = "Puntajes"

                if estado == "Fin" or "Acerca":
                    xb, yb, anchoB, altoB = botonPrincipal.rect
                    if xm > xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana/estado
                            estado = "menu"


                # Ventana jugando, dibujar enemigos
                elif estado == "jugando":
                    enemigo = pygame.sprite.Sprite()
                    enemigo.image = imgEnem
                    enemigo.rect = imgEnem.get_rect()
                    enemigo.rect.left = xm - enemigo.rect.width // 2
                    enemigo.rect.top = ym - enemigo.rect.height // 2
                    listaEnem.append(enemigo)

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    #efecto.play() efecto de musica
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = xNave + 18
                    bala.rect.top = ALTO - bala.rect.height - 50
                    listaBalas.append(bala)

                if evento.type ==pygame.K_LEFT: #Oprime la flecha de la izquierda
                    dxPersonaje = +20
                    moverPersonaje = True
                if evento.key == pygame.K_RIGHT:  #Oprime la flecha de la derecha
                    dxPersonaje= -20
                    moverPersonaje = True
            elif evento.type == pygame.KEYUP:  # se suelta la tecla
                    moverPersonaje = False

            elif moverPersonaje: #Actualizar pos.
                xPersonaje += dxPersonaje

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Generar enemigos cada 2 segundos
        timerEnemigo2 += 1 / 40
        timerEnemigo3 += 1 / 40
        timerTIEMPO += 1 / 40

        if timerEnemigo2 >= 2:
            generarEnemigoAzar(listaEnem, imgEnem)
            timerEnemigo2 = 0

        if timerEnemigo3 >= 5:
            generarEnemigoAzar(listaEnem, imgEnemigo2)
            timerEnemigo3 = 0

        if estado == "menu":
            dibujarFondo(ventana, imagenFondo)
            dibujarMenu(ventana, botonJugar)
            dibujarMenu(ventana, botonPuntajes)

        elif estado == "jugando":

            # DibujarFondoConAnimacion
            ventana.blit(fondoMovimiento, (0, y))
            ventana.blit(fondoMovimiento, (0, ALTO + y))
            y -= 1

            if y <= -ALTO:
                y = 0

            # Continuar con Juego
            dibujarJuego(ventana, listaEnem, listaBalas)
            actualizarBalas(listaBalas, listaEnem)
            PUNTAJE = actualizarPUNTAJE(listaBalas, listaEnem, PUNTAJE)

            # Personaje
            ventana.blit(imgPersonaje, (xNave, ALTO - 75))
            xNave, yNave = pygame.mouse.get_pos()

            # Datos en pantalla, calculando las coordenadas para que no se traslapen
            pygame.draw.rect(ventana, NEGRO, (0, ALTO - 25, ANCHO, 200), 0)
            fuente = pygame.font.SysFont("Helvetica", 20)

            tiempo = fuente.render("Tiempo: " + str(("%.2f") % timerTIEMPO), 1, MORADO)
            ventana.blit(tiempo, (ANCHO - 140, ALTO - 25))

            TSCORE = fuente.render("SCORE: " + str(PUNTAJE) + " |", 1, MORADO)
            ventana.blit(TSCORE, (ANCHO - 275, ALTO - 25))

            Cenemigos = fuente.render("Cantidad de Enemigos: " + str(len(listaEnem)) + " |", 1,MORADO)

            #El objetivo ideal sería que ganara eliminando todos los enemigos pero como se generan muy rápido será
            #imposible
            if (len(listaEnem) == 10):
                estado = "Ganar"
                # Saca archivo nuevo con puntaje nuevo
                salida = open("Puntajes.txt", "a+", encoding="UTF-8")
                salida.write(str(PUNTAJE) + '\n')

            ventana.blit(Cenemigos, (ANCHO - 550, ALTO - 25))

        if (len(listaEnem) == 0):
            estado = "Fin"

        elif estado == "Fin":
            dibujarFondo(ventana, imagenFondoFIN)
            dibujarMenu(ventana, botonPrincipal)

        elif estado == "Puntajes":
            dibujarFondo(ventana, imagenFondoPuntajes)
            fuente = pygame.font.SysFont("Helvetica", 20)
            listaPuntajesFinal = fuente.render(puntajeMax, 1, BLANCO)
            ventana.blit(listaPuntajesFinal, (ANCHO // 2 - 30, ALTO // 2 + 10))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame

def main():
    dibujar()

main()