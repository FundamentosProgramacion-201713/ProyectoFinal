# encoding: UTF-8
# Autor: Gabriela Mariel Vargas Franco
# A01745775
#Videojuego: esquivar cuantos meteoritos puedas
from random import randint
import time

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)
puntos=[]
puntajeArchivo=[]
maximoPuntaje=[]


def dibujarMenu(ventana, botonJugar):
    ventana.blit(botonJugar.image,botonJugar.rect)


def dibujarJuego(ventana, listaMeteoros, dino):
    #para que salgan uno por uno con el ciclo for
    for meteoro in listaMeteoros:
        ventana.blit(meteoro.image, meteoro.rect)
    ventana.blit(dino.image,dino.rect)


def dibujarGameOver(ventana,imgGameOver,botonRestart):
    ventana.blit(imgGameOver,((ANCHO//2)-270,(ALTO//2)-170))
    ventana.blit(botonRestart.image,botonRestart.rect)

def generarMeteorosAzar(listaMeteoros, imgMeteoro):
    cx = randint(20,ANCHO-128)  # cada 150 pixeles va a haber un enemigo
    cy = 0
    meteoro = pygame.sprite.Sprite()
    meteoro.image = imgMeteoro
    meteoro.rect = imgMeteoro.get_rect()
    meteoro.rect.left = cx
    meteoro.rect.top = cy
    listaMeteoros.append(meteoro)


def actualizarMeteoros(listaMeteoros,dino,efecto):
    for meteoros in listaMeteoros:
        meteoros.rect.top+=20
        efecto.play()
        if meteoros.rect.top>=ALTO: #si ya se salio de la pantalla

            listaMeteoros.remove(meteoros) #elimino la bala
            continue #reinicia el ciclo, vuelve a preguntar por las pruebas del ciclo REGRESA AL INICIO DEL CICLO
        borrarMeteoro=False
        for m in range(len(listaMeteoros)-1,-1,-1):
            meteoros=listaMeteoros[m]
            if meteoros.rect.colliderect(dino):
                borrarMeteoro=True
                break
        if borrarMeteoro:
            listaMeteoros.remove(meteoros)


def dibujar():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    estado="menu"
    #Cargar imagenes
    boton=pygame.image.load("button_jugar.png")
    imgGameOver=pygame.image.load("GameOver.png")
    dinosaurio=pygame.image.load("Raptor.png")
    restart=pygame.image.load("button_reiniciar.png")
    #Cargar música
    pygame.mixer.init()
    pygame.mixer.music.load("FondoMusical.mp3")
    pygame.mixer.music.play(-1)
    #https://es.melodyloops.com/music/free/
    efecto=pygame.mixer.Sound("bomb-04.wav")
    #http://www.mediacollege.com/downloads/sound-effects/explosion/
    gameOverSound=pygame.mixer.Sound("GameOverArcade.wav")

    #FONDO
    fondo=pygame.image.load("fondoJurasico.png")
    x=0
    #Meteoros
    listaMeteoros=[]
    imgMeteoro=pygame.image.load("Meteorito.png")
    generarMeteorosAzar(listaMeteoros,imgMeteoro)
    #PUNTOS
    puntaje=[]
    puntos=0
    #Sprite
    botonJugar=pygame.sprite.Sprite()
    botonJugar.image=boton
    botonJugar.rect=boton.get_rect()
    botonJugar.rect.left=ANCHO//2-botonJugar.rect.width//2
    botonJugar.rect.top=ALTO//2-botonJugar.rect.height//2

    #REINICIAR
    botonRestart=pygame.sprite.Sprite()
    botonRestart.image=restart
    botonRestart.rect=restart.get_rect()
    botonRestart.rect.left=(ANCHO//2)-50
    botonRestart.rect.top=(ALTO//2)+100

    #DINOSAURIO
    xDino=0
    yDino=2*ALTO//3
    dino = pygame.sprite.Sprite()
    dino.image = dinosaurio
    dino.rect = dinosaurio.get_rect()#devuelve el ancho y el alto de la imagen
    dino.rect.left = xDino
    dino.rect.top = yDino

    #TIEMPO
    timer=0
    #velocidad
    vx=0
    #Puntaje
    puntajeMax=0
    puntosActuales=0

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # EL USUARIO HIZO CLICK CON EL MAOUSE
                xm, ym = pygame.mouse.get_pos()  # saber donde dio click
                if estado=="menu":
                    xb,yb,anchoB,altoB=botonJugar.rect
                    if xm>=xb and xm<=xb+anchoB:  #DELIMITANDO
                        if ym>=yb and ym<=yb+altoB: #estoy entre abajo ya arriba
                            #Cambiar de ventana(cambio de estado)
                            estado="jugando" #se cambia del estado menu a estado jugando
                elif estado=="jugando":
                    meteoro = pygame.sprite.Sprite()
                    meteoro.image = imgMeteoro
                    meteoro.rect = imgMeteoro.get_rect()
                    meteoro.rect=imgMeteoro.get_rect()
                    meteoro.rect.left=xm
                    meteoro.rect.top=ym
                    listaMeteoros.append(meteoro)
                    dino = pygame.sprite.Sprite()
                    dino.image = dinosaurio
                    dino.rect = dinosaurio.get_rect()
                    dino.rect.left = ANCHO-dino.rect.width-10
                    dino.rect.right = ALTO-dino.rect.widht+10
            elif evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_RIGHT:
                    vx +=10
                if evento.key==pygame.K_LEFT:
                    vx -=10
            elif evento.type==pygame.KEYUP:
                if evento.key==pygame.K_RIGHT:
                    vx +=0
                if evento.key==pygame.K_LEFT:
                    vx -=0


        # Borrar pantalla
        if estado=="menu":
            ventana.blit(fondo,(0,0))
        elif estado=="jugando":
            ventana.blit(fondo,(x,0))
            ventana.blit(fondo,(ANCHO+x,0))
            x -=3
            if x<= -ANCHO:
                x=0

        #Meteoros cada 2 Segundos
        timer+=reloj.tick(40)/1000
        if timer>=3: #ya acumuló tres segundos?
            timer=0
            generarMeteorosAzar(listaMeteoros,imgMeteoro)
        #Movimiento dino
        dino.rect.move_ip(vx,0)
        #Puntuacion

        #dibujar
        if estado=="menu":
            dibujarMenu(ventana, botonJugar)
            fuente = pygame.font.SysFont("None", 35)
            texto=fuente.render("¡Esquiva los meteoros!",1,NEGRO)
            ventana.blit(texto, ((ANCHO//2)-120, (ALTO//2)-250))


        elif estado=="jugando":
            dibujarJuego(ventana,listaMeteoros,dino)
            actualizarMeteoros(listaMeteoros,dino,efecto)
            for meteoros in listaMeteoros:
                meteoros.rect.top+=20
                if meteoros.rect.top>=ALTO: #si ya se salio de la pantalla
                    puntosActuales+=1
                    if puntosActuales>10:
                        timer+=1


            fuente = pygame.font.SysFont("None", 40)
            msg = fuente.render("Puntos: " + str(puntosActuales), 1, BLANCO)
            ventana.blit(msg, ((ANCHO // 3)-250, (ALTO//2)-250))

            for m in range(len(listaMeteoros)-1,-1,-1):
                meteoros=listaMeteoros[m]
            if meteoros.rect.colliderect(dino):
                estado = "Game Over"
                pygame.mixer.music.stop()

        elif estado == "Game Over":
            dibujarGameOver(ventana,imgGameOver,botonRestart)
            gameOverSound.play()
            gameOverSound.set_volume(0.4)
            puntuacionAlta=0
            highScore=open("High Score.txt","w")
            if puntosActuales>puntuacionAlta:
                puntuacionAlta=puntosActuales
                puntajeArchivo.append(puntuacionAlta)
                hS=max(puntajeArchivo)
                maximoPuntaje.append(hS)
            highScore.write(str(maximoPuntaje))
            highScore.close()
            datos=open("High Score.txt","r")
            lineas=datos.read()
            for l in lineas:
                list(l)
                newLine=l.split(",")
                imprimirHs=newLine[0]
                fuente = pygame.font.SysFont("None", 35)
                high=fuente.render("High Score:"+ str(imprimirHs),1,NEGRO)
                ventana.blit(high, ((ANCHO)-300, (ALTO//2)-250))
                datos.close()

            fuente = pygame.font.SysFont("None", 40)
            texto = fuente.render("Pulsa Escape para salir ", 1, BLANCO)
            ventana.blit(texto, ((ANCHO // 3)-250, (ALTO//3)+300))
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_ESCAPE:
                    termina=True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
            # EL USUARIO HIZO CLICK CON EL MAOUSE
                xmr, ymr = pygame.mouse.get_pos()  # saber donde dio click
                if estado=="Game Over":
                    xbr,ybr,anchoBr,altoBr=botonRestart.rect
                    if xmr>=xbr and xmr<=xbr+anchoBr:  #DELIMITANDO
                        if ymr>=ybr and ymr<=ybr+altoBr: #estoy entre abajo ya arriba
                            #Cambiar de ventana(cambio de estado)
                            dibujar()



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps


    pygame.quit()   # termina pygame



def main():
    dibujar()
main()
