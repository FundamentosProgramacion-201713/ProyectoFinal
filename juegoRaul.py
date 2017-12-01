# encoding: UTF-8
# Autor: Raul Ortiz Mateos
# Sprites para la creacion de un juego
from random import randint

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarMenu(ventana, botonJugar,botoninfo):
    ventana.blit(botonJugar.image,botonJugar.rect)
    ventana.blit(botoninfo.image, botoninfo.rect)


def dibujarJuegpo(ventana, listaEnemigos,listaBalas):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)


    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)

def actualizarBalas(listaBalas,listaEnemigos):
    for bala in listaBalas:
        bala.rect.left+=20
        if bala.rect.left<=0:
            listaBalas.remove(bala)
            continue#reiniciar el ciclo, no tod volver a preguntar las instrucciones del ciclo
        borrarBala=False
        for k in range(len(listaEnemigos)-1,-1,-1):
            enemigo=listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala=True
                break  #lo que hace es terminar el ciclo se puede utilizar dentro de un for o un while lo rompemos porque ya colisionamos on e enemigo

        if borrarBala:
            listaBalas.remove(bala)

def NivelVida(ventana, letra, nivel, vidas):

    nivel=str(nivel)
    vidas=str(vidas)

    nivelPantalla=letra.render(nivel,0,(VERDE_BANDERA))
    vidasPantalla=letra.render(vidas,0,(VERDE_BANDERA))
    ventana.blit(nivelPantalla,(20,50))
    ventana.blit(vidasPantalla,(730,50))
    nivelTexto = letra.render("nivel", 0, (VERDE_BANDERA))
    vidasTexto = letra.render('vidas', 0, (VERDE_BANDERA))
    ventana.blit(nivelTexto, (20, 70))
    ventana.blit(vidasTexto, (730,70))

def reiniciar(estado,btnVolver,fuente,ventana,botonJugar,botoninfo):
    if estado=="ganaste":
        ventana.blit(btnVolver.image, btnVolver.rect)
        textoGanaste = fuente.render("Ganaste", 0, (VERDE_BANDERA))
        ventana.blit(textoGanaste, (400, 400))
    elif estado=="menu":
        ventana.blit(botonJugar.image, botonJugar.rect)
        ventana.blit(botoninfo.image, botoninfo.rect)


def generarEnemigos(listaEnemigos,imgEnemigo):
    for x in range(3):
        cx = randint(100,ANCHO-128)
        enemigo = pygame.sprite.Sprite()
        enemigo.image = imgEnemigo
        enemigo.rect = imgEnemigo.get_rect()
        enemigo.rect.left =cx
        enemigo.rect.top=580
        listaEnemigos.append((enemigo))


def generarEnemigoAzar(listaEnemigos, imgEnemigo):
    cx = randint(20, ANCHO - 128)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    enemigo.rect.left = cx
    enemigo.rect.top = 580
    listaEnemigos.append((enemigo))

def vidas(listaenemigos, spriteMario,vidas):
    for impacto in listaenemigos:
        if spriteMario.rect.colliderect(impacto):
            spriteMario.rect.left=6
            spriteMario.rect.top=650
            return vidas-1


    return vidas

def reiniciarJuego(nivel,vidas,estado):
    if vidas == 0:
        estado="menu"
    if nivel >= 4:
        estado="ganaste"

    return estado


def dibujarInformacion(ventana, botonSalir):
    ventana.blit(botonSalir.image, botonSalir.rect)


def dibujarSalidaMenu(ventanaJ, botonSalidaJugar):
    ventanaJ.blit(botonSalidaJugar.image, botonSalidaJugar.rect)

def dibujar():
    pygame.mixer.init()
    pygame.mixer.music.load("TS/mario.mp3")
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.10)



    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    ventanaJ=pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución



    estado="menu"#jugando,fin

    #cargar imagenes
    imagenBtnJugar=pygame.image.load("TS/boton.png")
    imagenBtnSalida=pygame.image.load("TS/salir1.png")
    imagenBtnInfo=pygame.image.load("TS/info.png")
    imagenFondo=pygame.image.load("TS/fondo.jpg")
    imgF=pygame.image.load("TS/fondo.png")
    imgf=pygame.image.load("TS/fondoinfo.jpg")
    imgFSJ=pygame.image.load("TS/salirJuego.png")
    #sprite
    botonJugar=pygame.sprite.Sprite()
    botonJugar.image=imagenBtnJugar
    botonJugar.rect=imagenBtnJugar.get_rect()
    botonJugar.rect.left=ANCHO//2-botonJugar.rect.width//2
    botonJugar.rect.top = ALTO // 2


    botonInfo=pygame.sprite.Sprite()
    botonInfo.image=imagenBtnInfo
    botonInfo.rect=imagenBtnInfo.get_rect()
    botonInfo.rect.left = ANCHO//3
    botonInfo.rect.top = ALTO//3

    botonsalida = pygame.sprite.Sprite()
    botonsalida.image = imagenBtnSalida
    botonsalida.rect = imagenBtnSalida.get_rect()
    botonsalida.rect.left = 600
    botonsalida.rect.top = 750

    botonSalidaJugar = pygame.sprite.Sprite()
    botonSalidaJugar.image = imgFSJ
    botonSalidaJugar.rect = imgFSJ.get_rect()
    botonSalidaJugar.rect.left = 600
    botonSalidaJugar.rect.top = 750

    vidas1=3
    nivel=1
    timer=0

    #enemigos
    listaEnemigos=[]
    imgEnemigo=pygame.image.load("TS/malo.png")
    generarEnemigos(listaEnemigos,imgEnemigo)

    #balas
    listaBalas=[]
    listaBalasN=[]
    imgBala=pygame.image.load("TS/bala.png")

    #personaje
    imgMario = pygame.image.load("TS/mn.png")
    sM = pygame.sprite.Sprite()
    sM.image = imgMario
    sM.rect = imgMario.get_rect()
    sM.rect.left = 6
    sM.rect.top = 650




    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                #el usuario hizo click con el mouse
                xm, ym = pygame.mouse.get_pos()
                if estado=="menu":
                    xB,yB,anchoB,altoB=botonJugar.rect
                    if xm>=xB and xm<=xB+anchoB:
                        if ym>=yB and ym<=yB+altoB:
                            #cambiar a ventana
                            estado="jugando"

                if estado=="menu":
                    xB, yB, anchoB, altoB = botonInfo.rect
                    if xm >= xB and xm <= xB + anchoB:
                        if ym >= yB and ym <= yB + altoB:
                            # cambiar a ventana
                            estado = "informacion"

                elif estado=="informacion":
                    xB, yB, anchoB, altoB = botonsalida.rect
                    if xm >= xB and xm <= xB + anchoB:
                        if ym >= yB and ym <= yB + altoB:
                            # cambiar a ventana
                            estado = "menu"
                elif estado=="jugando":
                    xB, yB, anchoB, altoB = botonSalidaJugar.rect
                    if xm >= xB and xm <= xB + anchoB:
                        if ym >= yB and ym <= yB + altoB:
                            # cambiar a ventana
                            estado = "menu"#hacer 2 botonbes que me marque el si o el no y hacer otra captura de pantalla.
                elif estado=="Jugando":
                    enemigo = pygame.sprite.Sprite()
                    enemigo.image = imgEnemigo
                    enemigo.rect = imgEnemigo.get_rect()
                    enemigo.rect.left=xm-enemigo.rect.width//2
                    enemigo.rect.top=ym-enemigo.rect.height//2
                    listaEnemigos.append((enemigo))


            elif evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_w:
                    sM.image = pygame.image.load("TS/mnf.png")
                    bala=pygame.sprite.Sprite()
                    bala.image=imgBala
                    bala.rect=imgBala.get_rect()
                    bala.rect.left=sM.rect.left
                    bala.rect.top=sM.rect.top
                    listaBalas.append(bala)

        else:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                sM.image = pygame.image.load("TS/mn.png")
                sM.rect.left -= 6
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                sM.image = pygame.image.load("TS/mnd.png")
                sM.rect.left += 6


            elif estado == "ganaste":
                xB, yB, anchoB, altoB = botonsalida.rect
                if xm >= xB and xm <= xB + anchoB:
                    if ym >= yB and ym <= yB + altoB:
                        # cambiar a ventana
                        estado = "menu"



        # Borrar pantalla
        ventana.blit(imagenFondo,(0,0))
        #cronometro de cuanto tiempo te tardaste en pasar el juego

        #tipo de letra
        letra=pygame.font.SysFont("monospace", 30)
        lettraPF=pygame.font.SysFont("monospace",90)

        #tiempo
        aux=1
        time=pygame.time.get_ticks()/1000
        if aux==time:
            aux+1

        timer += 1 / 40
        if timer >= 1:
            timer = 0
            generarEnemigoAzar(listaEnemigos, imgEnemigo)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado=="menu":
            dibujarMenu(ventana,botonJugar,botonInfo)

        elif estado=="informacion":
            ventanaJ.blit(imgf, (0, 0))
            dibujarInformacion(ventanaJ,botonsalida)

        elif estado=="jugando":
            ventanaJ.blit(imgF, (0, 0))
            actualizarBalas(listaBalas,listaEnemigos)
            dibujarJuegpo(ventanaJ, listaEnemigos,listaBalas)
            fuente = pygame.font.SysFont("monospace", 48)
            texto2=fuente.render("tiempo de juego:"+"  "+str(time),1,VERDE_BANDERA)
            ventana.blit(texto2, (200, 1))
            dibujarSalidaMenu(ventanaJ,botonSalidaJugar)
            v=vidas(listaEnemigos,sM,vidas1)
            NivelVida(ventana, letra, nivel,v)
            ventana.blit(sM.image, sM.rect)
            if sM.rect.left>=ANCHO-20:
                nivel+=1
                sM.rect.left=0
            if sM.rect.left<0:
                sM.rect.left=0
            if sM.rect.left>=ANCHO:
                sM.rect.left=ANCHO-sM.rect.width
            if sM.rect.top>=ALTO:
                sM.rect.top=ALTO-sM.rect.height
        estado = reiniciarJuego(nivel, vidas, estado)
        if estado == "menu" or estado == "ganaste":
            reiniciar(estado,botonsalida,lettraPF,ventana,botonJugar,botonInfo)
            # vista de score

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)
        # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()