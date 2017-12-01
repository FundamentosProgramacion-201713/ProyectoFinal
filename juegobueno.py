# encoding: UTF-8
# Autor: Yerish Valdes Bernes
#juego que emula space invaders

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO=(0,0,0)
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
def dibujarMenu(ventana, botonJugar):
    ventana.blit(botonJugar.image, botonJugar.rect)

def dibujarMenu1(ventana, botonContinuar):
    ventana.blit(botonContinuar.image, botonContinuar.rect)

def dibujarJuego(ventana,listaMarcianoGrande,listMarcianChico,listaBalas,listaBalasMarciano,listavidas):
    for marciano in listaMarcianoGrande:
        ventana.blit(marciano.image, marciano.rect)
    for marciano in listMarcianChico:
        ventana.blit(marciano.image, marciano.rect)
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)
    for BalaMarciano in listaBalasMarciano:
        ventana.blit(BalaMarciano.image, BalaMarciano.rect)
    for vidas in listavidas:
        ventana.blit(vidas.image, vidas.rect)

def actualizarBalasMarciano(listaBalasMaciano):
    for balamars in listaBalasMaciano:
        balamars.rect.top += 35
        if balamars.rect.top >= ALTO:
            listaBalasMaciano.remove(balamars)

            continue


def actualizarBalas(listaBalas,listaMarcianoGrande,listMarcianChico,score):
    for bala in listaBalas:
        bala.rect.top -= 35
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue
        borrarBala = False
        for k in range((len(listaMarcianoGrande))-1,-1,-1):
            enemigogrande = listaMarcianoGrande[k]
            if bala.rect.colliderect(enemigogrande):
                listaMarcianoGrande.remove(enemigogrande)
                score+=20
                borrarBala = True
                break

        for k in range((len(listMarcianChico))-1,-1,-1):
            enemigo = listMarcianChico[k]
            if bala.rect.colliderect(enemigo):
                listMarcianChico.remove(enemigo)
                score += 10
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)
    return score

def generarMarcianoChico(listMarcianChico,imgMarcianoChico):
    for x in range(7):
        for y in range(1):

            cx = 12 + x*111
            cy = 179
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgMarcianoChico
            enemigo.rect = imgMarcianoChico.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listMarcianChico.append(enemigo)



def generarMarcianoGrande(listaMarcianoGrande, imgMarcianoGrande):
    for x in range(7):
        for y in range(1):

            cx = 12 + x*111
            cy = 80
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgMarcianoGrande
            enemigo.rect = imgMarcianoGrande.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaMarcianoGrande.append(enemigo)


def generarvidas(listavidas, vida):
    for x in range (3):
        for y in range (1):
            cx=20+x*26
            cy=13
            vidas=pygame.sprite.Sprite()
            vidas.image=vida
            vidas.rect=vida.get_rect()
            vidas.rect.left=cx
            vidas.rect.top=cy
            listavidas.append(vidas)

def matar(nave,listaBalasMarciano):
    for k in range((len(listaBalasMarciano))):
        bala = listaBalasMarciano[k]
        if bala.rect.colliderect(nave):
            listaBalasMarciano.remove(bala)
            return True


def restarVidas(listavidas, nave,listaBalasMarciano):
    wasd=0

    for i in range((len(listavidas)) - 1, -1, -1):
        restar = matar(nave, listaBalasMarciano)
        if restar==True:
            vida = listavidas[wasd]
            listavidas.remove(vida)
            wasd+=1
            return True






def dibujar():
    BLANCO = (255, 255, 255)

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    estado ="menu" # Bandera para saber si termina la ejecución
    termina=False
    moverNave=False
    # Cargar imágenes
    imgBtnJugar = pygame.image.load("button_nuevo-juego.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2

    # Cargar imágenes 2
    imgBtncontinuar = pygame.image.load("button_continuar.png")
    botonContinuar = pygame.sprite.Sprite()
    botonContinuar.image = imgBtncontinuar
    botonContinuar.rect = imgBtncontinuar.get_rect()
    botonContinuar.rect.left = ANCHO // 2 - botonContinuar.rect.width // 2
    botonContinuar.rect.top = ALTO // 2 - botonContinuar.rect.height // 2

    abc=0
    #nave

    ALTO_NAVE = 30
    ANCHO_NAVE = 50
    xNAVE = ANCHO // 2
    yNAVE = ALTO - 20
    moverNAVE = False
    DXNAVE = 25
    #timer
    timer=0


    #Enemigos
    listMarcianChico = []
    listaMarcianoGrande = []
    imgMarcianoChico = pygame.image.load("marcianopequeño.png")
    imgMarcianoGrande= pygame.image.load("marcianogrande.png")

    # Generar enemigos
    generarMarcianoChico(listMarcianChico,imgMarcianoChico)
    generarMarcianoGrande(listaMarcianoGrande, imgMarcianoGrande)

    # Balas
    listaBalas = []
    imgBala = pygame.image.load("green.png")
    # Balasmarciano

    listaBalasMaciano = []
    imgBalaMarciano = pygame.image.load("Red_laser.png")

    efecto = pygame.mixer.Sound("shoot.wav")

    listavidas=[]
    vida= pygame.image.load("corazon-de-8-bits.png")
    generarvidas(listavidas,vida)
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True


            elif evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click con el mouse
                xm, ym = pygame.mouse.get_pos()


                if estado=="menu1":

                    listaBalas = []
                    listaBalasMaciano = []
                    listMarcianChico = []
                    listaMarcianoGrande = []

                    generarMarcianoChico(listMarcianChico, imgMarcianoChico)
                    generarMarcianoGrande(listaMarcianoGrande, imgMarcianoGrande)
                    xNAVE = ANCHO // 2
                    yNAVE = ALTO - 20


                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana
                            estado = "jugando"

                if estado == "menu":

                    listavidas = []
                    listaBalas = []
                    listaBalasMaciano = []
                    listMarcianChico = []
                    listaMarcianoGrande = []
                    generarvidas(listavidas, vida)
                    generarMarcianoChico(listMarcianChico, imgMarcianoChico)
                    generarMarcianoGrande(listaMarcianoGrande, imgMarcianoGrande)
                    xNAVE = ANCHO // 2
                    yNAVE = ALTO - 20


                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            score = 0
                            # Cambiar de ventana
                            estado = "jugando"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    moverNave = True
                    DXNave = -10
                elif evento.key == pygame.K_RIGHT:
                    moverNave = True
                    DXNave = +10
                if evento.key == pygame.K_SPACE:
                    efecto.play()
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = xNAVE
                    bala.rect.top = yNAVE
                    listaBalas.append(bala)

                for abc in range (1):
                    BalaMarciano = pygame.sprite.Sprite()
                    BalaMarciano.image = imgBalaMarciano
                    BalaMarciano.rect = imgBalaMarciano.get_rect()
                    BalaMarciano.rect.left =xNAVE
                    BalaMarciano.rect.top = 30
                    listaBalasMaciano.append(BalaMarciano)

            if evento.type == pygame.KEYUP:
                moverNave = False

        ventana.fill(NEGRO)

        if estado == "menu":
            fuente = pygame.font.SysFont("calibri", 40)
            texto2 = fuente.render(str("Los enemigos reponden a tus ataques"), 1, BLANCO)
            ventana.blit(texto2, (130, ALTO // 3))

            dibujarMenu(ventana, botonJugar)
        elif estado=="menu1":
            fuente = pygame.font.SysFont("calibri", 40)
            texto1 = fuente.render(str("Pulsa para continuar"), 1, BLANCO)
            ventana.blit(texto1, (260, ALTO // 4))
            dibujarMenu1(ventana, botonContinuar)

        elif estado == "jugando":

            fuente = pygame.font.SysFont("calibri",40)
            texto = fuente.render(str(score),1,BLANCO)
            ventana.blit(texto,(ANCHO-100,10))



            nave = pygame.draw.rect(ventana, BLANCO, (xNAVE, yNAVE, ANCHO_NAVE, ALTO_NAVE))
            dibujarJuego(ventana,listaMarcianoGrande,listMarcianChico,listaBalas,listaBalasMaciano,listavidas)
            if moverNave:
                xNAVE += DXNave
            score=actualizarBalas(listaBalas,listaMarcianoGrande,listMarcianChico,score)
            actualizarBalasMarciano(listaBalasMaciano)
            eliminarvidas = restarVidas(listavidas,nave,listaBalasMaciano)

            if len(listavidas)==0:
                estado="menu"

            if (len(listaMarcianoGrande))+(len(listMarcianChico))==0:
                estado="menu1"


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()