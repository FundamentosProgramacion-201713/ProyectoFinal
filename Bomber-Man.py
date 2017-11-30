#AUTOR: Luis Enrique Neri Pérez
#DESCRIPCIÓN: Juego Bomber-Man

import pygame, pygame.mixer

# DIMENSIONES DE LA PANTALLA
ANCHO = 800
ALTO = 600

# COORDENADAS PERMITIDAS
coordenadasPosRick= ['(590,350)','(40,100)', '(40,50)', '(-10,100)', '(90,100)', '(140,100)', '(140,50)', '(190,100)', '(240,100)', '(240,150)', '(290,150)', '(340,150)', '(340,100)', '(340,50)', '(390,50)', '(440,50)', '(440,100)', '(440,150)', '(390,150)', '(390,200)', '(440,200)', '(490,200)', '(540,200)', '(540,150)', '(540,100)', '(490,100)', '(540,50)', '(590,50)', '(590,100)', '(590,200)', '(640,200)', '(640,150)', '(690,150)', '(690,100)', '(740,100)', '(740,50)', '(690,200)', '(740,200)', '(690,250)', '(690,300)', '(740,300)', '(640,300)', '(590,300)', '(590,250)', '(540,300)', '(490,300)', '(490,250)', '(540,350)', '(540,400)', '(540,450)', '(540,500)', '(590,500)', '(640,500)', '(690,500)', '(740,500)', '(640,450)', '(640,400)', '(690,400)', '(740,400)', '(690,350)', '(440,300)', '(390,300)', '(340,300)', '(340,350)', '(340,400)', '(290,400)', '(240,400)', '(290,450)', '(340,450)', '(390,450)', '(390,400)', '(440,400)', '(290,300)', '(240,300)', '(190,300)', '(140,300)', '(140,350)', '(140,400)', '(140,450)', '(140,500)', '(90,500)', '(90,450)', '(40,450)', '(40,400)', '(-10,400)', '(-10,350)', '(40,350)', '(40,300)', '(90,300)', '(90,250)', '(90,200)', '(140,200)', '(190,200)', '(240,200)', '(290,200)', '(140,150)', '(40,200)', '(-10,200)', '(40,150)', '(340,500)', '(290,250)']
coordenadasPosMorty = ['(330,520)','(30,70)', '(30,120)', '(-20,120)', '(80,120)', '(130,120)', '(130,70)', '(180,120)', '(230,120)', '(230,170)', '(280,170)', '(330,170)', '(330,120)', '(330,70)', '(380,70)', '(430,70)', '(430,120)', '(480,120)', '(530,120)', '(580,120)', '(580,70)', '(530,70)', '(530,170)', '(530,220)', '(580,220)', '(630,220)', '(680,220)', '(730,220)', '(680,170)', '(680,120)', '(730,120)', '(730,70)', '(630,170)', '(380,170)', '(380,220)', '(430,220)', '(480,220)', '(480,270)', '(480,320)', '(530,320)', '(580,320)', '(580,270)', '(630,320)', '(680,320)', '(680,270)', '(730,320)', '(680,370)', '(680,420)', '(730,420)', '(630,420)', '(630,470)', '(630,520)', '(680,520)', '(730,520)', '(580,520)', '(530,520)', '(530,470)', '(530,420)', '(530,370)', '(580,370)', '(430,320)', '(380,320)', '(330,320)', '(330,370)', '(330,420)', '(380,420)', '(430,420)', '(280,420)', '(230,420)', '(280,470)', '(330,470)', '(380,470)', '(280,320)', '(230,320)', '(180,320)', '(130,320)', '(130,370)', '(130,420)', '(130,470)', '(130,520)', '(80,520)', '(80,470)', '(30,470)', '(30,420)', '(-20,420)', '(-20,370)', '(30,370)', '(30,320)', '(80,320)', '(280,270)', '(280,220)', '(230,220)', '(180,220)', '(130,220)', '(80,220)', '(80,270)', '(30,220)', '(-20,220)', '(30,170)', '(130,170)', '(430,170)']
coordenadasBombas = {'(740,50)': '(740,50)&(740,100)', '(740,100)': '(740,100)&(690,100)&(740,50)', '(690,100)': '(690,100)&(740,100)&(690,150)', '(690,150)': '(690,150)&(640,150)&(690,200)&(690,100)', '(690,200)': '(690,200)&(740,200)&(640,200)&(690,250)&(690,150)', '(740,200)': '(740,200)&(690,200)', '(690,250)': '(690,250)&(690,300)&(690,200)', '(690,300)': '(690,300)&(740,300)&(640,300)&(690,350)&(690,250)', '(740,300)': '(740,300)&(690,300)', '(690,350)': '(690,350)&(690,400)&(690,300)', '(690,400)': '(690,400)&(740,400)&(640,400)&(690,350)', '(740,400)': '(740,400)&(690,400)', '(640,400)': '(640,400)&(690,400)&(640,450)', '(640,450)': '(640,450)&(640,500)&(640,400)', '(640,500)': '(640,500)&(690,500)&(590,500)&(640,450)', '(690,500)': '(690,500)&(740,500)&(640,500)', '(740,500)': '(740,500)&(690,500)', '(590,500)': '(590,500)&(640,500)&(540,500)', '(540,500)': '(540,500)&(590,500)&(540,450)', '(540,450)': '(540,450)&(540,500)&(540,400)', '(540,400)': '(540,400)&(540,450)&(540,350)', '(540,350)': '(540,350)&(590,350)&(540,400)&(540,300)', '(590,350)': '(590,350)&(540,350)&(590,300)', '(590,300)': '(590,300)&(640,300)&(540,300)&(590,350)&(590,250)', '(540,300)': '(540,300)&(590,300)&(490,300)&(540,350)', '(640,300)': '(640,300)&(690,300)&(590,300)', '(640,200)': '(640,200)&(690,200)&(590,200)&(640,150)', '(590,200)': '(590,200)&(640,200)&(540,200)&(590,250)', '(640,150)': '(640,150)&(690,150)&(640,200)', '(590,250)': '(590,250)&(590,300)&(590,200)', '(540,200)': '(540,200)&(590,200)&(490,200)&(540,150)', '(540,150)': '(540,150)&(540,200)&(540,100)', '(540,100)': '(540,100)&(590,100)&(490,100)&(540,150)&(540,50)', '(540,50)': '(540,50)&(590,50)&(540,100)', '(590,50)': '(590,50)&(540,50)&(590,100)', '(590,100)': '(590,100)&(540,100)&(590,50)', '(490,200)': '(490,200)&(540,200)&(440,200)&(490,250)', '(490,250)': '(490,250)&(490,300)&(490,200)', '(490,300)': '(490,300)&(540,300)&(440,300)&(490,250)', '(440,300)': '(440,300)&(490,300)&(390,300)', '(390,300)': '(390,300)&(440,300)&(340,300)', '(340,300)': '(340,300)&(390,300)&(290,300)&(340,350)', '(340,350)': '(340,350)&(340,400)&(340,300)', '(340,400)': '(340,400)&(390,400)&(290,400)&(340,450)&(340,350)', '(390,400)': '(390,400)&(440,400)&(340,400)&(390,450)', '(440,400)': '(440,400)&(390,400)', '(390,450)': '(390,450)&(340,450)&(390,400)', '(340,450)': '(340,450)&(390,450)&(290,450)&(340,500)&(340,400)', '(290,450)': '(290,450)&(340,450)&(290,400)', '(290,400)': '(290,400)&(340,400)&(240,400)&(290,450)', '(240,400)': '(240,400)&(290,400)', '(340,500)': '(340,500)&(340,450)', '(290,300)': '(290,300)&(340,300)&(240,300)&(290,250)', '(240,300)': '(240,300)&(290,300)&(190,300)', '(290,250)': '(290,250)&(290,300)&(290,200)', '(290,200)': '(290,200)&(240,200)&(290,250)&(290,150)', '(290,150)': '(290,150)&(340,150)&(240,150)&(290,200)', '(340,150)': '(340,150)&(390,150)&(290,150)&(340,100)', '(390,150)': '(390,150)&(440,150)&(340,150)&(390,200)', '(390,200)': '(390,200)&(440,200)&(390,150)', '(440,200)': '(440,200)&(490,200)&(390,200)&(440,150)', '(440,150)': '(440,150)&(390,150)&(440,200)&(440,100)', '(440,100)': '(440,100)&(490,100)&(440,150)&(440,50)', '(490,100)': '(490,100)&(540,100)&(440,100)', '(440,50)': '(440,50)&(390,50)&(440,100)', '(390,50)': '(390,50)&(440,50)&(340,50)', '(340,50)': '(340,50)&(390,50)&(340,100)', '(340,100)': '(340,100)&(340,150)&(340,50)', '(190,300)': '(190,300)&(240,300)&(140,300)', '(140,300)': '(140,300)&(190,300)&(90,300)&(140,350)', '(140,350)': '(140,350)&(140,400)&(140,300)', '(140,400)': '(140,400)&(140,450)&(140,350)', '(140,450)': '(140,450)&(90,450)&(140,500)&(140,400)', '(140,500)': '(140,500)&(90,500)&(140,450)', '(90,500)': '(90,500)&(140,500)&(90,450)', '(90,450)': '(90,450)&(140,450)&(40,450)&(90,500)', '(40,450)': '(40,450)&(90,450)&(40,400)', '(40,400)': '(40,400)&(-10,400)&(40,450)&(40,350)', '(-10,400)': '(-10,400)&(40,400)&(-10,350)', '(-10,350)': '(-10,350)&(40,350)&(-10,400)', '(40,350)': '(40,350)&(-10,350)&(40,400)&(40,300)', '(40,300)': '(40,300)&(90,300)&(40,350)', '(90,300)': '(90,300)&(140,300)&(40,300)&(90,250)', '(90,250)': '(90,250)&(90,300)&(90,200)', '(90,200)': '(90,200)&(140,200)&(40,200)&(90,250)', '(40,200)': '(40,200)&(90,200)&(-10,200)&(40,150)', '(-10,200)': '(-10,200)&(40,200)', '(140,200)': '(140,200)&(190,200)&(90,200)&(140,150)', '(190,200)': '(190,200)&(240,200)&(140,200)', '(240,200)': '(240,200)&(290,200)&(190,200)&(240,150)', '(240,150)': '(240,150)&(290,150)&(240,200)&(240,100)', '(240,100)': '(240,100)&(190,100)&(240,150)', '(190,100)': '(190,100)&(240,100)&(140,100)', '(140,100)': '(140,100)&(190,100)&(90,100)&(140,150)&(140,50)', '(140,150)': '(140,150)&(140,200)&(140,100)', '(40,150)': '(40,150)&(40,200)&(40,100)', '(40,100)': '(40,100)&(90,100)&(-10,100)&(40,150)&(40,50)', '(-10,100)': '(-10,100)&(40,100)', '(90,100)': '(90,100)&(140,100)&(40,100)', '(140,50)': '(140,50)&(140,100)', '(40,50)': '(40,50)&(40,100)', '(30,70)': '(30,70)&(30,120)','(30,70)': '(30,70)&(30,120)', '(30,120)': '(30,120)&(80,120)&(-20,120)&(30,170)&(30,70)', '(30,170)': '(30,170)&(30,220)&(30,120)', '(30,220)': '(30,220)&(80,220)&(-20,220)&(30,170)', '(-20,220)': '(-20,220)&(30,220)', '(-20,120)': '(-20,120)&(30,120)', '(80,120)': '(80,120)&(130,120)&(30,120)', '(130,120)': '(130,120)&(180,120)&(80,120)&(130,170)&(130,70)', '(130,70)': '(130,70)&(130,120)', '(130,170)': '(130,170)&(130,220)&(130,120)', '(130,220)': '(130,220)&(180,220)&(80,220)&(130,170)', '(80,220)': '(80,220)&(130,220)&(30,220)&(80,270)', '(180,220)': '(180,220)&(230,220)&(130,220)', '(230,220)': '(230,220)&(280,220)&(180,220)&(230,170)', '(230,170)': '(230,170)&(280,170)&(230,220)&(230,120)', '(230,120)': '(230,120)&(180,120)&(230,170)', '(180,120)': '(180,120)&(230,120)&(130,120)', '(280,220)': '(280,220)&(230,220)&(280,270)&(280,170)', '(280,170)': '(280,170)&(330,170)&(230,170)&(280,220)', '(280,270)': '(280,270)&(280,320)&(280,220)', '(280,320)': '(280,320)&(330,320)&(230,320)&(280,270)', '(230,320)': '(230,320)&(280,320)&(180,320)', '(180,320)': '(180,320)&(230,320)&(130,320)', '(130,320)': '(130,320)&(180,320)&(80,320)&(130,370)', '(80,320)': '(80,320)&(130,320)&(30,320)&(80,270)', '(80,270)': '(80,270)&(80,320)&(80,220)', '(30,320)': '(30,320)&(80,320)&(30,370)', '(30,370)': '(30,370)&(-20,370)&(30,420)&(30,320)', '(-20,370)': '(-20,370)&(30,370)&(-20,420)', '(-20,420)': '(-20,420)&(30,420)&(-20,370)', '(30,420)': '(30,420)&(-20,420)&(30,470)&(30,370)', '(30,470)': '(30,470)&(80,470)&(30,420)', '(80,470)': '(80,470)&(130,470)&(30,470)&(80,520)', '(80,520)': '(80,520)&(130,520)&(80,470)', '(130,520)': '(130,520)&(80,520)&(130,470)', '(130,470)': '(130,470)&(80,470)&(130,520)&(130,420)', '(130,420)': '(130,420)&(130,470)&(130,370)', '(130,370)': '(130,370)&(130,420)&(130,320)', '(330,320)': '(330,320)&(380,320)&(280,320)&(330,370)', '(330,370)': '(330,370)&(330,420)&(330,320)', '(330,420)': '(330,420)&(380,420)&(280,420)&(330,470)&(330,370)', '(280,420)': '(280,420)&(330,420)&(230,420)&(280,470)', '(230,420)': '(230,420)&(280,420)', '(280,470)': '(280,470)&(330,470)&(280,420)', '(330,470)': '(330,470)&(380,470)&(280,470)&(330,520)&(330,420)', '(380,470)': '(380,470)&(330,470)&(380,420)', '(380,420)': '(380,420)&(430,420)&(330,420)&(380,470)', '(430,420)': '(430,420)&(380,420)', '(330,520)': '(330,520)&(330,470)', '(380,320)': '(380,320)&(430,320)&(330,320)', '(430,320)': '(430,320)&(480,320)&(380,320)', '(480,320)': '(480,320)&(530,320)&(430,320)&(480,270)', '(530,320)': '(530,320)&(580,320)&(480,320)&(530,370)', '(530,370)': '(530,370)&(580,370)&(530,420)&(530,320)', '(530,420)': '(530,420)&(530,470)&(530,370)', '(530,470)': '(530,470)&(530,520)&(530,420)', '(530,520)': '(530,520)&(580,520)&(530,470)', '(580,520)': '(580,520)&(630,520)&(530,520)', '(630,520)': '(630,520)&(680,520)&(580,520)&(630,470)', '(680,520)': '(680,520)&(730,520)&(630,520)', '(730,520)': '(730,520)&(680,520)', '(630,470)': '(630,470)&(630,520)&(630,420)', '(630,420)': '(630,420)&(680,420)&(630,470)', '(680,420)': '(680,420)&(730,420)&(630,420)&(680,370)', '(730,420)': '(730,420)&(680,420)', '(680,370)': '(680,370)&(680,420)&(680,320)', '(680,320)': '(680,320)&(730,320)&(630,320)&(680,370)&(680,270)', '(730,320)': '(730,320)&(680,320)', '(630,320)': '(630,320)&(680,320)&(580,320)', '(580,320)': '(580,320)&(630,320)&(530,320)&(580,370)&(580,270)', '(330,170)': '(330,170)&(380,170)&(280,170)&(330,120)', '(330,120)': '(330,120)&(330,170)&(330,70)', '(330,70)': '(330,70)&(380,70)&(330,120)', '(380,70)': '(380,70)&(430,70)&(330,70)', '(430,70)': '(430,70)&(380,70)&(430,120)', '(430,120)': '(430,120)&(480,120)&(430,170)&(430,70)', '(430,170)': '(430,170)&(380,170)&(430,220)&(430,120)', '(380,170)': '(380,170)&(430,170)&(330,170)&(380,220)', '(380,220)': '(380,220)&(430,220)&(380,170)', '(430,220)': '(430,220)&(480,220)&(380,220)&(430,170)', '(480,220)': '(480,220)&(530,220)&(430,220)&(480,270)', '(530,220)': '(530,220)&(580,220)&(480,220)&(530,170)', '(530,170)': '(530,170)&(530,220)&(530,120)', '(530,120)': '(530,120)&(580,120)&(480,120)&(530,170)&(530,70)', '(480,120)': '(480,120)&(530,120)&(430,120)', '(580,120)': '(580,120)&(530,120)&(580,70)', '(580,70)': '(580,70)&(530,70)&(580,120)', '(530,70)': '(530,70)&(580,70)&(530,120)', '(480,270)': '(480,270)&(480,320)&(480,220)', '(580,220)': '(580,220)&(630,220)&(530,220)&(580,270)', '(630,220)': '(630,220)&(680,220)&(580,220)&(630,170)', '(680,220)': '(680,220)&(730,220)&(630,220)&(680,270)&(680,170)', '(730,220)': '(730,220)&(680,220)', '(630,170)': '(630,170)&(680,170)&(630,220)', '(680,170)': '(680,170)&(630,170)&(680,220)&(680,120)', '(680,120)': '(680,120)&(730,120)&(680,170)', '(730,120)': '(730,120)&(680,120)&(730,70)', '(730,70)': '(730,70)&(730,120)', '(680,270)': '(680,270)&(680,320)&(680,220)', '(580,370)': '(580,370)&(530,370)&(580,320)', '(580,270)': '(580,270)&(580,320)&(580,220)'}

# COLORES
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

valorTimer = 10
timer = 0
# IMAGENES
imagenMenu = pygame.image.load("Fondo Menú.jpg")
imagenFondo = pygame.image.load("Laberinto.jpg")
imagenIntro = pygame.image.load("Casa.png")
imagenCreditos = pygame.image.load("Creditos.jpg")
imagenScore = pygame.image.load("Fondo High Scores.jpg")
imagenInstrucciones = pygame.image.load("Instrucciones.jpg")
imagenGameOver = pygame.image.load("Game Over Ventana.jpg")
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

def dibujarPuntajeR(ventana, puntajeRick):
    fuente = pygame.font.Font('freesansbold.ttf', 115)
    puntajeRick = str(puntajeRick).split()
    while not len(puntajeRick) == 4:
        puntajeRick.insert(0,"0")
    pRick = ""
    pRick.join(puntajeRick)


def dibujarCajas(ventana, btnCajas, pruebaCajas):
    for u in range (len(pruebaCajas)):
        heynow = pruebaCajas[u].split("&")
        btnCajas.rect.left = int(heynow[0]) # LEFT ES EL EJE X
        btnCajas.rect.top = int(heynow[1])-10  # HEIGHT ES EL EJE Y
        ventana.blit(btnCajas.image, btnCajas.rect)

def dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa,vidasRick, vidasMorty, puntajeRick, puntajeMorty, btnCajas, pruebaCajas):
    dibujarVidasMorty(ventana,btnVidasMorty)
    dibujarVidasRick(ventana, btnVidasRick)
    dibujarCajas(ventana, btnCajas, pruebaCajas)
    #dibujarPuntajeR(ventana, puntajeRick)
    #dibujarPuntajeM(ventana, puntajeMorty)
    if vidasRick>0:
        dibujarRick(ventana,imagenRick, xRick, yRick)
    if vidasMorty>0:
        dibujarMorty(ventana, imagenMorty, xMorty, yMorty)
    dibujarPausa(ventana, btnPausa)

def dibujarRick(ventana, imagenMorty, x, y):
    ventana.blit(imagenMorty, (x, y))

def dibujarMorty(ventana, imagenRick, x, y):
    ventana.blit(imagenRick, (x, y))

def dibujarScores(ventana, btnScores, nombresOrdenados, puntajesOrdenados):
    font = pygame.font.SysFont("eras bold itc", 60)
    primer = "1.-" + nombresOrdenados[0]
    texto1L = font.render(primer, True, (244, 244, 244))
    segundo = "2.-" + nombresOrdenados [1]
    texto2L = font.render(segundo, True, (244, 244, 244))
    tercero = "3.-" + nombresOrdenados[2]
    texto3L = font.render(tercero, True, (244, 244, 244))
    cuarto = "4.-" + nombresOrdenados[3]
    texto4L = font.render(cuarto, True, (244, 244, 244))
    quinto = "5.-" + nombresOrdenados [4]
    texto5L = font.render(quinto, True, (244, 244, 244))
    ventana.blit(texto1L, (ANCHO//4 - 60,195 + 56*0))
    ventana.blit(texto2L, (ANCHO//4 - 60, 195 + 56 * 1))
    ventana.blit(texto3L, (ANCHO//4 - 60, 195 + 56 * 2))
    ventana.blit(texto4L, (ANCHO//4 - 60, 195 + 56 * 3))
    ventana.blit(texto5L, (ANCHO//4 - 60, 195 + 56 * 4))
    puntaje1 = font.render(puntajesOrdenados[0], True, (244, 244, 244))
    puntaje2 = font.render(puntajesOrdenados[1], True, (244, 244, 244))
    puntaje3 = font.render(puntajesOrdenados[2], True, (244, 244, 244))
    puntaje4 = font.render(puntajesOrdenados[3], True, (244, 244, 244))
    puntaje5 = font.render(puntajesOrdenados[4], True, (244, 244, 244))
    ventana.blit(puntaje1, (ANCHO - ANCHO//4, 195 + 56 * 0))
    ventana.blit(puntaje2, (ANCHO - ANCHO//4, 195 + 56 * 1))
    ventana.blit(puntaje3, (ANCHO - ANCHO//4, 195 + 56 * 2))
    ventana.blit(puntaje4, (ANCHO - ANCHO//4, 195 + 56 * 3))
    ventana.blit(puntaje5, (ANCHO - ANCHO//4, 195 + 56 * 4))
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

def dibujarBombaM(ventana, btnBomba,x,y):
    x = x +btnBomba.rect.width // 2
    y = y + btnBomba.rect.height // 2  # HEIGHT ES EL EJE Y
    ventana.blit(btnBomba.image, (x,y))

def dibujarBombaR(ventana, btnBomba,x,y):
    x = x + btnBomba.rect.width // 2 - 10
    y = y + btnBomba.rect.height - 4
    ventana.blit(btnBomba.image, (x,y))
    return x,y

def dibujarTextoIntro2(ventana, btnTextoIntro2):
    ventana.blit(btnTextoIntro2.image, btnTextoIntro2.rect)

def dibujarListo1(ventana, btnListo1):
    ventana.blit(btnListo1.image, btnListo1.rect)

def dibujarListo2(ventana, btnListo2):
    ventana.blit(btnListo2.image, btnListo2.rect)

def dibujarPausa(ventana, btnPausa):
    ventana.blit(btnPausa.image, btnPausa.rect)

def dibujarFuegoM(ventana, btnFuego, x, y, explosion):
    xBombaPrueba1 = x + 50
    xBombaPrueba2 = x - 50
    yBombaPrueba1 = y + 50
    yBombaPrueba2 = y - 50
    ventana.blit(btnFuego.image, (x + 10, y + 15))
    explosion.play()
    cadena1 = "(" + str(xBombaPrueba1) + "," + str(y) + ")"
    if cadena1 in coordenadasPosMorty:
        explosion.play()
        ventana.blit(btnFuego.image, (xBombaPrueba1+10,y+15))
        explosion.play()
    cadena2 = "(" + str(xBombaPrueba2) + "," + str(y) + ")"
    if cadena2 in coordenadasPosMorty:
        explosion.play()
        ventana.blit(btnFuego.image, (xBombaPrueba2+10,y+15))
        explosion.play()
    cadena3 = "(" + str(x) + "," + str(yBombaPrueba1) + ")"
    if cadena3 in coordenadasPosMorty:
        explosion.play()
        ventana.blit(btnFuego.image, (x+10,yBombaPrueba1+20))
        explosion.play()
    cadena4 = "(" + str(x) + "," + str(yBombaPrueba2) + ")"
    if cadena4 in coordenadasPosMorty:
        explosion.play()
        ventana.blit(btnFuego.image, (x+10,yBombaPrueba2+20))
        explosion.play()

def dibujarFuegoR(ventana, btnFuego, x, y, explosion):
    xBombaPrueba1 = x + 50
    xBombaPrueba2 = x - 50
    yBombaPrueba1 = y + 50
    yBombaPrueba2 = y - 50
    ventana.blit(btnFuego.image, (x, y +40))
    explosion.play()
    cadena1 = "(" + str(xBombaPrueba1) + "," + str(y) + ")"
    if cadena1 in coordenadasPosRick:
        explosion.play()
        ventana.blit(btnFuego.image, (xBombaPrueba1,y + 40))
        explosion.play()
    cadena2 = "(" + str(xBombaPrueba2) + "," + str(y) + ")"
    if cadena2 in coordenadasPosRick:
        explosion.play()
        ventana.blit(btnFuego.image, (xBombaPrueba2,y + 40))
        explosion.play()
    cadena3 = "(" + str(x) + "," + str(yBombaPrueba1) + ")"
    if cadena3 in coordenadasPosRick:
        explosion.play()
        ventana.blit(btnFuego.image, (x,yBombaPrueba1 + 40))
        explosion.play()
    cadena4 = "(" + str(x) + "," + str(yBombaPrueba2) + ")"
    if cadena4 in coordenadasPosRick:
        explosion.play()
        ventana.blit(btnFuego.image, (x,yBombaPrueba2 + 40))
        explosion.play()

def dibujar():
    pruebaCajas = ['152&100', '402&100', '602&100', '152&150', '202&150', '152&200', '302&200', '352&200', '452&200', '702&200', '2&250', '52&250', '102&250', '252&250', '302&250', '502&250', '552&250', '652&250', '502&300', '52&350', '152&350', '202&350', '302&350', '552&350', '602&350', '702&350', '152&400', '352&400', '552&400', '52&450', '252&450', '302&450', '352&450', '402&450', '452&450', '552&450', '652&450', '752&450', '52&500', '152&500', '302&500', '352&500', '402&500', '652&500']
    cajasX = [152,402,602,152,202,152,302,352,452,702,2,52,102,252,302,502,552,652,502,52,152,202,302,552,602,702,152,352,552,52,252,303,352,402,452,552,652,752,52,152,302,352,402,652]
    cajasY = [100,100,100,150,150,200,200,200,200,200,250,250,250,250,250,250,250,250,300,350,350,350,350,350,350,350,400,400,400,450,450,450,450,450,450,450,450,450,500,500,500,500,500,500]
    cajasDestruidas = {'152&100': True, '402&100': True, '602&100': True, '152&150': True, '202&150': True, '152&200': True, '302&200': True, '352&200': True, '452&200': True, '702&200': True, '2&250': True, '52&250': True, '102&250': True, '252&250': True, '302&250': True, '502&250': True, '552&250': True, '652&250': True, '502&300': True, '52&350': True, '152&350': True, '202&350': True, '302&350': True, '552&350': True, '602&350': True, '702&350': True, '152&400': True, '352&400': True, '552&400': True, '52&450': True, '252&450': True, '302&450': True, '352&450': True, '402&450': True, '452&450': True, '552&450': True, '652&450': True, '752&450': True, '52&500': True, '152&500': True, '302&500': True, '352&500': True, '402&500': True, '652&500': True}

    print("RICK & MORTY: BOMBER-MAN 2 PLAYERS")
    print("----------------------------------------------------")
    print("Acompaña a Rick y a Morty para decidir quén estará al mando durante su próxima aventura")
    print("Ingresa tu nombre gamer (UNA SOLA PALABRA) en el personaje con el que quieras jugar (Rick o Morty)")
    nombreJ1 = input("MORTY: ")
    nombreJ2 = input("RICK: ")
    print("----------------------------------------------------")
    print("COMENCEMOS...")

    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    timerM = 0
    timerR = 0
    puntajeRick = 0
    puntajeMorty = 0

    # ESTADOS DEL JUEGO
    estado = "menu"

    click = pygame.mixer.Sound("minecraft_click.wav")
    explosion = pygame.mixer.Sound("Explosion.wav")

    # REPRODUCIR TEMA PRINCIPAL
    pygame.mixer.init()
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

    # BOMBAS
    imgBomba = pygame.image.load("Bomba.png")
    btnBomba = pygame.sprite.Sprite()  # SPRITE
    btnBomba.image = imgBomba
    btnBomba.rect = imgBomba.get_rect()  # rect(x,y,width,lenght)

    # FUEGO
    imgFuego = pygame.image.load("Fire.png")
    btnFuego = pygame.sprite.Sprite()  # SPRITE
    btnFuego.image = imgFuego
    btnFuego.rect = imgFuego.get_rect()  # rect(x,y,width,lenght)

    # CAJAS
    imgCajas = pygame.image.load("Caja.png")
    btnCajas = pygame.sprite.Sprite()  # SPRITE
    btnCajas.image = imgCajas
    btnCajas.rect = imgCajas.get_rect()  # rect(x,y,width,lenght)

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
    bombaMorty = False
    bombaRick = False
    seleccionPausa = ""

    entradaP = open("puntajes.txt", "r")
    puntajes = entradaP.readlines()
    entradaP.close()
    entradaN = open("nombres.txt", "r")
    nombres = entradaN.readlines()
    entradaN.close()
    diccionarioNombre = {}
    for k in range(len(puntajes)):
        nombre = nombres[k]
        puntaje = puntajes[k]
        diccionarioNombre[nombre] = puntaje
    puntajes.sort()
    puntajes.reverse()
    puntajesOrdenados = []
    nombresOrdenados = []

    for k in puntajes:  # Promedios
        for f in diccionarioNombre:  # Nombres
            if k == diccionarioNombre[f]:
                if f not in nombresOrdenados:
                    nombresOrdenados.append(f)
                    puntajesOrdenados.append(k)
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
                            click.play()
                            estado = "intro"
                    xb, yb, anchoB, altoB = btnScores.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            click.play()
                            estado = "scores"
                    xb, yb, anchoB, altoB = btnCreditos.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            click.play()
                            estado = "creditos"
                elif estado == "creditos":
                    xb, yb, anchoB, altoB = btnRegresar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            click.play()
                            estado = "menu"
                elif estado == "scores":
                    xb, yb, anchoB, altoB = btnRegresar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            click.play()
                            estado = "menu"
                elif estado == "intro":
                    xb, yb, anchoB, altoB = btnIntro.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(canciones["Jazz"])
                            pygame.mixer.music.play(-1)
                            click.play()
                            estado = "instrucciones"
                elif estado == "jugando":
                    x1, y1, ancho1, alto1 = btnContinuarJuego.rect
                    x2, y2, ancho2, alto2 = btnReiniciar.rect
                    x3, y3, ancho3, alto3 = btnVolverMenu.rect
                    xb, yb, anchoB, altoB = btnPausa.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            clicPausa = True
                            mover = False
                    if clicPausa == True:
                        if xm >= x1 and xm <= x1 + ancho1:
                            if ym >= y1 and ym <= y1 + alto1:
                                click.play()
                                seleccionPausa = "Continuar"
                                mover = True
                        if xm >= x2 and xm <= x2 + ancho2:
                            if ym >= y2 and ym <= y2 + alto2:
                                vidasMorty = 3
                                vidasRick = 3
                                xRick = 740
                                yRick = 50
                                xMorty = 30
                                yMorty = 70
                                click.play()
                                seleccionPausa = "Reiniciar"
                                cajasDestruidas = {'152&100': True, '402&100': True, '602&100': True, '152&150': True, '202&150': True, '152&200': True, '302&200': True, '352&200': True, '452&200': True, '702&200': True, '2&250': True, '52&250': True, '102&250': True, '252&250': True, '302&250': True, '502&250': True, '552&250': True, '652&250': True, '502&300': True, '52&350': True, '152&350': True, '202&350': True, '302&350': True, '552&350': True, '602&350': True, '702&350': True, '152&400': True, '352&400': True, '552&400': True, '52&450': True, '252&450': True, '302&450': True, '352&450': True, '402&450': True, '452&450': True, '552&450': True, '652&450': True, '752&450': True, '52&500': True, '152&500': True, '302&500': True, '352&500': True, '402&500': True, '652&500': True}
                                pruebaCajas = ['152&100', '402&100', '602&100', '152&150', '202&150', '152&200', '302&200', '352&200', '452&200', '702&200', '2&250', '52&250', '102&250', '252&250', '302&250', '502&250', '552&250', '652&250', '502&300', '52&350', '152&350', '202&350', '302&350', '552&350', '602&350', '702&350', '152&400', '352&400', '552&400', '52&450', '252&450', '302&450', '352&450', '402&450', '452&450', '552&450', '652&450', '752&450', '52&500', '152&500', '302&500', '352&500', '402&500', '652&500']
                                mover = True

                        if xm >= x3 and xm <= x3 + ancho3:
                            if ym >= y3 and ym <= y3 + alto3:
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load(canciones["Tema"])
                                pygame.mixer.music.play(-1)
                                vidasMorty = 3
                                vidasRick = 3
                                xRick = 740
                                yRick = 50
                                xMorty = 30
                                yMorty = 70
                                click.play()
                                seleccionPausa = "Menu"
                                mover = True
            elif evento.type == pygame.KEYDOWN:
                if estado == "instrucciones":
                    if evento.key == pygame.K_KP_ENTER:
                        jugador2 = "ready"
                    elif evento.key == pygame.K_RETURN:
                        jugador2 = "ready"
                    elif evento.key == pygame.K_SPACE:
                        jugador1 = "ready"
                    elif jugador1 == jugador2:
                        estado = "jugando"
                elif estado == "jugando":
                    ventana.blit(imagenFondo, (0, 0))
                    dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa,vidasRick, vidasMorty, puntajeRick, puntajeMorty,btnCajas, pruebaCajas)
                if estado == "jugando":
                    if mover == True:
                        if vidasRick>0:
                            # MOVIMIENTOS RICK
                            if evento.key == pygame.K_UP:  # ARRIBA RICK
                                yRickPrueba = yRick - 50
                                cadena = "(" + str(xRick) + "," + str(yRickPrueba) + ")"
                                if cadena in coordenadasPosRick:
                                    c1 = str(xRick + 12) + "&" + str(yRick)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    yRick -= 50
                                    else:
                                        yRick -= 50
                            elif evento.key == pygame.K_DOWN:  # ABAJO RICK
                                yRickPrueba = yRick + 50
                                cadena = "(" + str(xRick) + "," + str(yRickPrueba) + ")"
                                if cadena in coordenadasPosRick:
                                    c1 = str(xRick + 12) + "&" + str(yRick + 100)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    yRick += 50
                                    else:
                                        yRick += 50
                                if cadena == "(340,500)":
                                    estado = "gameover"
                            elif evento.key == pygame.K_LEFT:  # IZQUIERDA RICK
                                xRickPrueba = xRick - 50
                                cadena = "(" + str(xRickPrueba) + "," + str(yRick) + ")"
                                if cadena in coordenadasPosRick:
                                    c1 = str(xRickPrueba + 12) + "&" + str(yRick+50)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    xRick -= 50
                                    else:
                                        xRick -= 50
                                r = 1
                            elif evento.key == pygame.K_RIGHT:  # DERECHA RICK
                                xRickPrueba = xRick + 50
                                cadena = "(" + str(xRickPrueba) + "," + str(yRick) + ")"
                                if cadena in coordenadasPosRick:
                                    c1 = str(xRickPrueba + 12) + "&" + str(yRick+50)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    xRick += 50
                                    else:
                                        xRick += 50
                                r = 0
                            # PONER BOMBA
                            elif evento.key == pygame.K_RETURN: #BOMBA RICK
                                if timerR == 0:
                                    bombaRick = True
                                    xBombaR = xRick
                                    yBombaR = yRick
                            elif evento.key == pygame.K_KP_ENTER: #BOMBA RICK PC
                                if timerR == 0:
                                    bombaRick = True
                                    xBombaR = xRick
                                    yBombaR = yRick

                        if vidasMorty>0:
                            # MOVIMIENTOS MORTY
                            if evento.key == pygame.K_w:  # ARRIBA MORTY
                                yMortyPrueba = yMorty - 50
                                cadena = "(" + str(xMorty) + "," + str(yMortyPrueba) + ")"
                                if cadena in coordenadasPosMorty:
                                    c1 = str(xMorty + 22) + "&" + str(yMorty-20)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    yMorty -= 50
                                    else:
                                        yMorty -= 50
                            elif evento.key == pygame.K_s:  # ABAJO MORTY
                                yMortyPrueba = yMorty + 50
                                cadena = "(" + str(xMorty) + "," + str(yMortyPrueba) + ")"
                                if cadena in coordenadasPosMorty:
                                    c1 = str(xMorty + 22) + "&" + str(yMorty + 30 + 50)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    yMorty += 50
                                    else:
                                        yMorty += 50
                                if cadena == "(330,520)":
                                    estado = "gameover"
                            elif evento.key == pygame.K_d:  # DERECHA MORTY
                                xMortyPrueba = xMorty + 50
                                cadena = "(" + str(xMortyPrueba) + "," + str(yMorty) + ")"
                                if cadena in coordenadasPosMorty:
                                    c1 = str(xMortyPrueba + 12 +10) + "&" + str(yMorty + 50-20)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    xMorty += 50
                                    else:
                                        xMorty += 50
                                m = 0
                            elif evento.key == pygame.K_a:  # IZQUIERDA MORTY
                                xMortyPrueba = xMorty - 50
                                cadena = "(" + str(xMortyPrueba) + "," + str(yMorty) + ")"
                                if cadena in coordenadasPosMorty:
                                    c1 = str(xMortyPrueba + 12 +10) + "&" + str(yMorty+50-20)
                                    if c1 in pruebaCajas:
                                        for explotado in cajasDestruidas:
                                            if explotado == c1:
                                                if cajasDestruidas[c1] == False:
                                                    xMorty -= 50
                                    else:
                                        xMorty -= 50
                                m = 1
                            elif evento.key == pygame.K_SPACE: #BOMBA MORTY
                                if timerM == 0:
                                    bombaMorty = True
                                    xBombaM = xMorty
                                    yBombaM = yMorty
                    imagenRick = pygame.image.load(rick[r])
                    imagenMorty = pygame.image.load(morty[m])

        # DIBUJAR VENTANAS
        if estado == "menu": # MENÚ PRINCIPAL
            ventana.blit(imagenMenu, (0, 0))
            dibujarMenu(ventana, btnJugar)
            dibujarScores(ventana, btnScores, nombresOrdenados, puntajesOrdenados)
            dibujarCreditos(ventana, btnCreditos)
        elif estado == "scores": # PUNTAJES
            ventana.blit(imagenScore, (0,0))
            dibujarScores(ventana, btnRegresar, nombresOrdenados, puntajesOrdenados)
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
                mover = True
        elif estado == "jugando": #JUEGO
            ventana.blit(imagenFondo, (0,0))
            dibujarJuego(ventana, imagenRick, xRick, yRick, imagenMorty, xMorty, yMorty, btnVidasMorty, btnVidasRick, btnPausa,vidasRick, vidasMorty, puntajeRick, puntajeMorty, btnCajas, pruebaCajas)
            if clicPausa == True:
                dibujarMenuPausa(ventana, btnMenuPausa, btnContinuarJuego, btnReiniciar, btnVolverMenu)
                if seleccionPausa == "Continuar":
                    clicPausa = False
                    seleccionPausa = ""
                elif seleccionPausa == "Reiniciar":
                    clicPausa = False
                    puntajeRick = 0
                    puntajeMorty = 0
                    seleccionPausa = ""
                    estado = "instrucciones"
                    jugador1 = "1"
                    jugador2 = "2"
                elif seleccionPausa == "Menu":
                    clicPausa = False
                    seleccionPausa = ""
                    estado = "menu"
            #BOMBAS
            if bombaMorty == True:
                if timerM<30:
                    dibujarBombaM(ventana, btnBomba, xBombaM, yBombaM)
                    timerM += 1
                elif timerM == 30:
                    verifR = "(" + str(xRick) + "," + str(yRick) + ")"
                    verifM = "(" + str(xMorty) + "," + str(yMorty) + ")"
                    verifBM = "(" + str(xBombaM) + "," + str(yBombaM) + ")"
                    xPruebaR = xBombaM + 10
                    yPruebaR = yBombaM - 20
                    verifBR = "(" + str(xPruebaR) + "," + str(yPruebaR) + ")"
                    coordsR = coordenadasBombas[verifBR].split("&")
                    coordsM = coordenadasBombas[verifBM].split("&")
                    for prueba in coordsR:
                        if verifR == prueba:
                            vidasRick -= 1
                            puntajeRick -= 20
                            puntajeMorty += 100
                    for prueba in coordsM:
                        if verifM == prueba:
                            vidasMorty -= 1
                            puntajeMorty -= 20
                    for pruebadM in pruebaCajas:
                        c1 = str(xBombaM + 22 -50) + "&" + str(yBombaM + 30) # IZQUIERDA
                        c2 = str(xBombaM + 22) + "&" + str(yBombaM + 30) # ENMEDIO
                        c3 = str(xBombaM + 22 + 50) + "&" + str(yBombaM + 30) # DERECHA
                        c4 = str(xBombaM + 22) + "&" + str(yBombaM + 30 - 50) # ARRIBA
                        c5 = str(xBombaM + 22) + "&" + str(yBombaM + 30 + 50) # ABAJO
                        if c1 in pruebaCajas:
                            pruebaCajas.remove(c1)
                            cajasDestruidas[c1] = False
                            puntajeMorty += 50
                        if c2 in pruebaCajas:
                            pruebaCajas.remove(c2)
                            cajasDestruidas[c2] = False
                            puntajeMorty += 50
                        if c3 in pruebaCajas:
                            pruebaCajas.remove(c3)
                            cajasDestruidas[c3] = False
                            puntajeMorty += 50
                        if c4 in pruebaCajas:
                            pruebaCajas.remove(c4)
                            cajasDestruidas[c4] = False
                            puntajeMorty += 50
                        if c5 in pruebaCajas:
                            pruebaCajas.remove(c5)
                            cajasDestruidas[c5] = False
                            puntajeMorty += 50
                    dibujarFuegoM(ventana, btnFuego, xBombaM,yBombaM,explosion)
                    bombaMorty = False
                    timerM = 0
            if bombaRick == True:
                if timerR<30:
                    dibujarBombaR(ventana, btnBomba, xBombaR, yBombaR)
                    timerR += 1
                elif timerR == 30:
                    verifR = "(" + str(xRick) + "," + str(yRick) + ")"
                    verifM = "(" + str(xMorty) + "," + str(yMorty) + ")"
                    verifBR = "(" + str(xBombaR) + "," + str(yBombaR) + ")"
                    xPruebaM = xBombaR-10
                    yPruebaM = yBombaR +20
                    verifBM = "(" + str(xPruebaM) + "," + str(yPruebaM) + ")"
                    coordsR = coordenadasBombas[verifBR].split("&")
                    coordsM = coordenadasBombas[verifBM].split("&")
                    for prueba in coordsR:
                        if verifR == prueba:
                            vidasRick -= 1
                            puntajeRick -= 20
                    for pruebadR in pruebaCajas:
                        c1 = str(xBombaR + 12 - 50) + "&" + str(yBombaR + 50) # IZQUIERDA
                        c2 = str(xBombaR + 12) + "&" + str(yBombaR + 50) # ENMEDIO
                        c3 = str(xBombaR + 12 + 50) + "&" + str(yBombaR + 50) # DERECHA
                        c4 = str(xBombaR + 12) + "&" + str(yBombaR) # ARRIBA
                        c5 = str(xBombaR + 12) + "&" + str(yBombaR + 100) # ABAJO
                        if c1 in pruebaCajas:
                            pruebaCajas.remove(c1)
                            cajasDestruidas[c1] = False
                            puntajeRick += 50
                        if c2 in pruebaCajas:
                            pruebaCajas.remove(c2)
                            cajasDestruidas[c2] = False
                            puntajeRick += 50
                        if c3 in pruebaCajas:
                            pruebaCajas.remove(c3)
                            cajasDestruidas[c3] = False
                            puntajeRick += 50
                        if c4 in pruebaCajas:
                            pruebaCajas.remove(c4)
                            cajasDestruidas[c4] = False
                            puntajeRick += 50
                        if c5 in pruebaCajas:
                            pruebaCajas.remove(c5)
                            cajasDestruidas[c5] = False
                            puntajeRick += 50
                    for prueba in coordsM:
                        if verifM == prueba:
                            vidasMorty -= 1
                            puntajeMorty -= 20
                            puntajeRick += 100
                    dibujarFuegoR(ventana, btnFuego, xBombaR, yBombaR, explosion)
                    bombaRick = False
                    timerR = 0
        elif estado == "gameover":
            ventana.blit(imagenGameOver, (0,0))
            dibujarRegresar(ventana, btnRegresar)
            xb, yb, anchoB, altoB = btnRegresar.rect
            if xm >= xb and xm <= xb + anchoB:
                if ym >= yb and ym <= yb + altoB:
                    click.play()
                    vidasMorty = 3
                    vidasRick = 3
                    xRick = 740
                    yRick = 50
                    xMorty = 30
                    yMorty = 70
                    click.play()
                    seleccionPausa = "Reiniciar"
                    cajasDestruidas = {'152&100': True, '402&100': True, '602&100': True, '152&150': True, '202&150': True, '152&200': True, '302&200': True, '352&200': True, '452&200': True, '702&200': True, '2&250': True, '52&250': True, '102&250': True, '252&250': True, '302&250': True, '502&250': True, '552&250': True, '652&250': True, '502&300': True, '52&350': True, '152&350': True, '202&350': True, '302&350': True, '552&350': True, '602&350': True, '702&350': True, '152&400': True, '352&400': True, '552&400': True, '52&450': True, '252&450': True, '302&450': True, '352&450': True, '402&450': True, '452&450': True, '552&450': True, '652&450': True, '752&450': True, '52&500': True, '152&500': True, '302&500': True, '352&500': True, '402&500': True, '652&500': True}
                    pruebaCajas = ['152&100', '402&100', '602&100', '152&150', '202&150', '152&200', '302&200', '352&200', '452&200', '702&200', '2&250', '52&250', '102&250', '252&250', '302&250', '502&250', '552&250', '652&250', '502&300', '52&350', '152&350', '202&350', '302&350', '552&350', '602&350', '702&350', '152&400', '352&400', '552&400', '52&450', '252&450', '302&450', '352&450', '402&450', '452&450', '552&450', '652&450', '752&450', '52&500', '152&500', '302&500', '352&500', '402&500', '652&500']
                    mover = True
                    estado = "scores"
                    salidaN = open("nombres.txt", "a")
                    salidaP = open("puntajes.txt", "a")
                    f1 ="\n" + str(nombreJ1)
                    f2 ="\n" + str(puntajeMorty)
                    f3 ="\n" + str(nombreJ2)
                    f4 ="\n" + str(puntajeRick)
                    salidaN.write(f1)
                    salidaP.write(f2)
                    salidaN.write(f3)
                    salidaP.write(f4)
                    salidaN.close()
                    salidaP.close()

                    entradaP = open("puntajes.txt", "r")
                    puntajes = entradaP.readlines()
                    entradaP.close()
                    entradaN = open("nombres.txt", "r")
                    nombres = entradaN.readlines()
                    entradaN.close()
                    for k in range(len(puntajes)):
                        nombre = nombres[k]
                        puntaje = puntajes[k]
                        diccionarioNombre[nombre] = puntaje
                    puntajes.sort()
                    puntajes.reverse()
                    puntajesOrdenados = []
                    nombresOrdenados = []

                    for k in puntajes:  # Promedios
                        for f in diccionarioNombre:  # Nombres
                            if k == diccionarioNombre[f]:
                                if f not in nombresOrdenados:
                                    nombresOrdenados.append(f)
                                    puntajesOrdenados.append(k)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(valorTimer)          # 40 fpsS
    print("PUNTAJE RICK:",puntajeRick)
    print("PUNTAJE MORTY:", puntajeMorty)
    pygame.quit()   # termina pygame


def main():
    dibujar()

main()