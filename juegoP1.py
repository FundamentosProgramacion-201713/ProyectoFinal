#encoding: UTF-8

#OSCAR ZUÑIGA LARA

#A01654827




from random import randint

import pygame


ANCHO = 800

ALTO = 600

BLANCO = (255,255,255)

wea = True

tiempo = 0

avance = 0

def dibujarMenu(ventana,btnJugar,fondo):
    ventana.blit(fondo.image,fondo.rect)
    ventana.blit(btnJugar.image,btnJugar.rect)

def dibujarJuego(ventana, rana, disparo, rasho, municionCargador, listaBolas, fondo, listaListaBolas,estado,avance):
    estado = ("jugando")

    ventana.blit(fondo.image,fondo.rect)
    ventana.blit(rana.image,rana.rect)

    for a in listaListaBolas:

        for enemigo in listaBolas:

            ventana.blit(enemigo.image, enemigo.rect)
            xb1,yb1,xb2,yb2 = enemigo.rect
            xr1,yr1,xr2,yr2 = rana.rect

            if xb1 - 20 <= xr1 and xb1 + 20 >= xr1:
                listaListaBolas = []
                avance = 0
                estado = ("menu")

            elif yb1 - 20 >= yr1 and yb1 + 20 <=  yr1:
                listaListaBolas = []
                avance = 0
                estado = ("menu")

    if disparo == True and municionCargador > 0:

        ventana.blit(rasho.image,rana.rect)
        detectarColision(listaBolas, rasho)

    return estado

def generarBolas(imgBola, listaBolas,listaY1,listaX1):

    cantidadLB = len(listaBolas)
    len(listaY1)
    if cantidadLB < 3:
        for b in range(len(listaY1)):
            #for a in listaListaBolas:
            cx = ANCHO -20 - listaX1[b]
            cy = listaY1[-b]
            nuevo = pygame.sprite.Sprite()
            nuevo.image = imgBola
            nuevo.rect = imgBola.get_rect()
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaBolas.append(nuevo)

def detectarColision(bolas, rasho):

    #x1,y1,x2,y2 = rasho.get_rect()

    for a in bolas:
        pass

def dibujar():

    tiempo = 1

    estado = "menu"

    disparo = False

    recarga = False

    municionTotal = 100

    municionCargador = 10

    avance = 0

    listaListaBolas = []

    imgFondo = pygame.image.load("fonfo.jpg")
    fondo = pygame.sprite.Sprite()
    fondo.image = imgFondo
    fondo.rect = imgFondo.get_rect()
    fondo.rect.left = 0
    fondo.rect.top = 0

    imgBotonJugar = pygame.image.load("button_jugar.png")

    btnJugar = pygame.sprite.Sprite()  # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height // 2

    imgRana = pygame.image.load("ranita.png")
    rana = pygame.sprite.Sprite()
    rana.image = imgRana
    rana.rect = imgRana.get_rect()
    rana.rect.left = ANCHO//2
    rana.rect.top = ALTO//2

    imgRasho = pygame.image.load("rasho.png")
    rasho = pygame.sprite.Sprite()
    rasho.image = imgRasho
    rasho.rect = imgRasho.get_rect()

    imgBola = pygame.image.load("bola.png")
    bola = pygame.sprite.Sprite
    bola.image = imgBola
    bola.rect = imgBola.get_rect()

    listaBolas = []
    listaX1 = []
    listaY1 = []

    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    while not termina:
        # Procesa loseventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm,ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb,yb,anchoB,altoB = btnJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <=yb+altoB:
                            estado = "jugando"
        ventana.fill(BLANCO)
#//////////////////////////////////////////////////////////////
        if estado == "menu":
            dibujarMenu(ventana , btnJugar,fondo)
        elif estado == "jugando":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    rana.rect.top -= 5
                elif evento.key == pygame.K_a:
                    rana.rect.left -= 5
                elif evento.key == pygame.K_s:
                    rana.rect.top += 5
                elif evento.key == pygame.K_d:
                    rana.rect.left += 5
                elif evento.key == pygame.K_SPACE:
                    disparo = True
                elif evento.key == pygame.K_r:
                    recarga = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    xm, ym = pygame.mouse.get_pos()
                if rana.rect.left > ANCHO - 20:
                    rana.rect.left = ANCHO - 20
                if rana.rect.left < 0:
                    rana.rect.left = 0
                if rana.rect.top < 0:
                    rana.rect.top = 0
                if rana.rect.top > ALTO - 20:
                    rana.rect.top = ALTO - 20
            estado = dibujarJuego(ventana,rana,disparo,rasho,municionCargador,listaBolas,fondo,listaListaBolas,estado,avance)
            if disparo == True and municionCargador >= 0 :
                municionCargador -= 1/30
            elif recarga == True and municionTotal >= 0:
                municionCargador = 5
                tiempo += 1/10
                municionTotal -= int(tiempo)
                if tiempo > 1:
                    tiempo = 0
            disparo = False
            recarga = False
            wea = False


            tiempo += 1/32

            if avance == int(avance):
                listaBolas = []
                listaListaBolas.append(listaListaBolas)


                for a in range(3):
                    listaY1.append((randint(0,ALTO)))
                    listaX1.append(avance * 50)

                #print(listaListaBolas)///////////////////////


            generarBolas(imgBola, listaBolas,listaY1,listaX1)

            avance = avance + 1 / 32


        #////////////////////////////////////////////////////////////

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir

                termina = True


#/////////////////////////////////////////////////////////////////
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 60 fps
    pygame.quit()   # termina pygame
def main():

    dibujar()


main()