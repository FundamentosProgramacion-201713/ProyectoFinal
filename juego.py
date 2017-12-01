#encoding: UTF-8
#Autor: Maria Fernanda Torres Velazquez A01746537
#PROYECTO: VIDEOJUEGO-PONG

#INSTRUCCIONES: PARA MOVER A JUGADOR 1: PRESIONAR TECLAS "W" y "S"
#PARA MOVER A JUGADOR 2, PRESIONAR FLECHAS DE DIRECCION, ARRIBA Y ABAJO


import random #Importar libreria random
import pygame, sys #Importar pygame y sys
from pygame.locals import * #Importar constantes de pygame



pygame.init() #Iniciar pygame
fps = pygame.time.Clock()

#colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (153,204,255)
ROSA= (255,0,128)
MORADO= (153,255,51)
NARANJA= (255,142,55)
NEGRO= (0,0,0)

#Declaracion de variables globales
ANCHO= 800
ALTO= 600
RADIO_PELOTA= 20
ANCHO_TABLERO= 10
ALTO_TABLERO= 100
MITAD_ANCHO_TABLERO= ANCHO_TABLERO//2
MITAD_ALTO_TABLERO= ALTO_TABLERO//2
POS_PELOTA=[0, 0]
VEL_PELOTA= [0, 0]
RAQUETA1_VEL= 0
RAQUETA2_VEL= 0
JUGADOR1_PUNTAJE= 0
JUGADOR2_PUNTAJE= 0

#pantalla
ventana=pygame.display.set_mode((ANCHO, ALTO), 0, 32) #crear ventana
pygame.display.set_caption('JUEGO PONG') #Titulo de la ventana

def moverPelota(derecha): #Funcion que genera la pelota y devuelve su posicion y su velocidad en una lista
    global POS_PELOTA, VEL_PELOTA
    POS_PELOTA= [ANCHO // 2, ALTO // 2]
    x= random.randrange(2,4)
    y= random.randrange(1,3)

    if derecha == False: #Si derecha es verdadero, va a la derecha, si no a la izquierda
        x = - x

    VEL_PELOTA = [x, -y]


def definirJugadores():
    global RAQUETA1_POS, RAQUETA2_POS, RAQUETA1_VEL, RAQUETA2_VEL, JUGADOR1_PUNTAJE, JUGADOR2_PUNTAJE  #variables flotantes
    global puntaje1, puntaje2 #Variables enteras
    RAQUETA1_POS= [MITAD_ANCHO_TABLERO - 1, ALTO // 2] #posicion de raqueta 1
    RAQUETA2_POS= [ANCHO + 1 - MITAD_ANCHO_TABLERO, ALTO // 2] #posicion raqueta 2
    JUGADOR1_PUNTAJE=0
    JUGADOR2_PUNTAJE=0

    if random.randrange(0, 6) == 0:
        moverPelota(True)
    else:
        moverPelota(False)


def dibujarEsenario(tablero):
    global RAQUETA1_POS, RAQUETA2_POS, POS_PELOTA, VEL_PELOTA, JUGADOR1_PUNTAJE, JUGADOR2_PUNTAJE
    tablero.fill(AZUL)
    pygame.draw.line(tablero, BLANCO, [ANCHO // 2, 0], [ANCHO // 2, ALTO], 6)
    pygame.draw.line(tablero, BLANCO, [ANCHO_TABLERO, 0], [ANCHO_TABLERO, ALTO], 6)
    pygame.draw.line(tablero, BLANCO, [ANCHO - ANCHO_TABLERO, 0], [ANCHO - ANCHO_TABLERO, ALTO], 6)
    pygame.draw.circle(tablero, BLANCO, [ANCHO // 2, ALTO // 2], 70, 6)

#para actualizar las raquetas en la posicion vertical y se mantengan en pantalla
    if RAQUETA1_POS[1] > MITAD_ALTO_TABLERO and RAQUETA1_POS[1] < ALTO - MITAD_ALTO_TABLERO:
        RAQUETA1_POS[1] += RAQUETA1_VEL
    elif RAQUETA1_POS[1] == MITAD_ALTO_TABLERO and RAQUETA1_VEL > 0:
        RAQUETA1_POS[1] += RAQUETA1_VEL
    elif RAQUETA1_POS[1] == ALTO - MITAD_ALTO_TABLERO and RAQUETA1_VEL < 0:
        RAQUETA1_POS[1] += RAQUETA1_VEL

    if RAQUETA2_POS[1] > MITAD_ALTO_TABLERO and RAQUETA2_POS[1] < ALTO - MITAD_ALTO_TABLERO:
        RAQUETA2_POS[1] += RAQUETA2_VEL
    elif RAQUETA2_POS[1] == MITAD_ALTO_TABLERO and RAQUETA2_VEL > 0:
        RAQUETA2_POS[1] += RAQUETA2_VEL
    elif RAQUETA2_POS[1] == ALTO - MITAD_ALTO_TABLERO and RAQUETA2_VEL < 0:
        RAQUETA2_POS[1] += RAQUETA2_VEL

#para actualizar pelota
    POS_PELOTA[0] += int(VEL_PELOTA[0])
    POS_PELOTA[1] += int(VEL_PELOTA[1])

#dibujar raquetas y pelota
    pygame.draw.circle(tablero, NARANJA, POS_PELOTA, 20, 0) #PELOTA
    pygame.draw.polygon(tablero, MORADO, [[RAQUETA1_POS[0] - MITAD_ANCHO_TABLERO, RAQUETA1_POS[1] - MITAD_ALTO_TABLERO],
                                        [RAQUETA1_POS[0] - MITAD_ANCHO_TABLERO, RAQUETA1_POS[1] + MITAD_ALTO_TABLERO],
                                        [RAQUETA1_POS[0] + MITAD_ANCHO_TABLERO, RAQUETA1_POS[1] + MITAD_ALTO_TABLERO],
                                        [RAQUETA1_POS[0] + MITAD_ANCHO_TABLERO, RAQUETA1_POS[1] - MITAD_ALTO_TABLERO]], 0) #RAQUETA1
    pygame.draw.polygon(tablero, ROSA, [[RAQUETA2_POS[0] - MITAD_ANCHO_TABLERO, RAQUETA2_POS[1] - MITAD_ALTO_TABLERO],
                                        [RAQUETA2_POS[0] - MITAD_ANCHO_TABLERO, RAQUETA2_POS[1] + MITAD_ALTO_TABLERO],
                                        [RAQUETA2_POS[0] + MITAD_ANCHO_TABLERO, RAQUETA2_POS[1] + MITAD_ALTO_TABLERO],
                                        [RAQUETA2_POS[0] + MITAD_ANCHO_TABLERO, RAQUETA2_POS[1] - MITAD_ALTO_TABLERO]], 0) #RAQUETA2



#colisiones de pelota con borde superior e inferior
    if int(POS_PELOTA[1]) <= RADIO_PELOTA:
        VEL_PELOTA[1] = - VEL_PELOTA[1]
    if int(POS_PELOTA[1]) >= ALTO + 1 - RADIO_PELOTA:
        VEL_PELOTA[1] = -VEL_PELOTA[1]


#colisiones de pelota con raquetas
    if int(POS_PELOTA[0]) <= RADIO_PELOTA + ANCHO_TABLERO and int(POS_PELOTA[1]) in range(RAQUETA1_POS[1] - MITAD_ALTO_TABLERO,
                                                                                 RAQUETA1_POS[1] + MITAD_ALTO_TABLERO, 1):
        VEL_PELOTA[0] = -VEL_PELOTA[0]
        VEL_PELOTA[0] *= 1.1
        VEL_PELOTA[1] *= 1.1
    elif int(POS_PELOTA[0]) <= RADIO_PELOTA + ANCHO_TABLERO:
        JUGADOR2_PUNTAJE += 1
        moverPelota(True)

    if int(POS_PELOTA[0]) >= ANCHO + 1 - RADIO_PELOTA - ANCHO_TABLERO and int(POS_PELOTA[1]) in range(
                    RAQUETA2_POS[1] - MITAD_ALTO_TABLERO, RAQUETA2_POS[1] + MITAD_ALTO_TABLERO, 1):
        VEL_PELOTA[0] = -VEL_PELOTA[0]
        VEL_PELOTA[0] *= 1.1
        VEL_PELOTA[1] *= 1.1
    elif int(POS_PELOTA[0]) >= ANCHO + 1 - RADIO_PELOTA - ANCHO_TABLERO:
        JUGADOR1_PUNTAJE += 1
        moverPelota(False)

#actualizar puntajes
    fuente1 = pygame.font.SysFont("Century Gothic", 20)
    puntaje1 = fuente1.render("JUGADOR 1:  " + str(JUGADOR1_PUNTAJE), 10, NEGRO)
    tablero.blit(puntaje1, (50, 20))

    fuente2 = pygame.font.SysFont("Century Gothic", 20)
    puntaje2 = fuente2.render("JUGADOR 2:  " + str(JUGADOR2_PUNTAJE), 10, NEGRO)
    tablero.blit(puntaje2, (470, 20))

#control teclas presionadas
def presionarTecla(evento):
    global RAQUETA1_VEL, RAQUETA2_VEL

    if evento.key == K_UP:
        RAQUETA2_VEL = -12
    elif evento.key == K_DOWN:
        RAQUETA2_VEL = 12
    elif evento.key == K_w:
        RAQUETA1_VEL = -12
    elif evento.key == K_s:
        RAQUETA1_VEL = 12

#control teclas sin presionar
def teclaArriba(evento):
    global RAQUETA1_VEL, RAQUETA2_VEL

    if evento.key in (K_w, K_s):
        RAQUETA1_VEL = 0
    elif evento.key in (K_UP, K_DOWN):
        RAQUETA2_VEL = 0

def main():
    definirJugadores()


main()

#ciclo del juego
while True:

    dibujarEsenario(ventana)

    for evento in pygame.event.get():

        if evento.type == KEYDOWN:
            presionarTecla(evento)
        elif evento.type == KEYUP:
            teclaArriba(evento)
        elif evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    fps.tick(80)
