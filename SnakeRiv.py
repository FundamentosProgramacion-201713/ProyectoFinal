#Rodrigo Rivera Salinas
#A01375000
#Snake de la cumbia



import pygame,sys
from pygame.locals import *
from random import randint

ALTO= 600
ANCHO = 800
Naranja = (55, 12, 200)
Verde = (33, 235, 200)
Raro = (250, 100, 50)
Negro=(0,0,0)
Cosa=(0,250,30)

def dibujarMenu(ventana,btnJugar):  #dubujar primera ventana
    ventana.blit(btnJugar.image, btnJugar.rect)

def dibujarVivora(vivora, ventana):    #Dibujar vivora
    for a in range(len(vivora)):
        if a == 0:
            pygame.draw.rect(ventana, Verde,(vivora[a][1] * 20, vivora[a][0] * 20, 20, 20), 10)
            imgcaVivora = pygame.image.load("cabezavivora.png")
            cabeza = pygame.sprite.Sprite
            cabeza.image = imgcaVivora
        else:
            pygame.draw.rect(ventana, (Raro),(vivora[a][1] * 20, vivora[a][0] * 20, 20, 20), 10)
            imgcuVivora = pygame.image.load("cuerpoViv.png")
            cuerpo = pygame.sprite.Sprite
            cuerpo.image = imgcuVivora


def mover(vivora, nuevaPos):    #actualizar tamaño de la serpiente
    for i in reversed(range(1, len(vivora))):
        vivora[i] = vivora[i - 1]
    vivora[0] = nuevaPos
    return vivora


def puntuacion(objeto1, objeto2, Extra, ventana):      #Cada que la cabeza coliciona con los objetos sumar
    if Extra:
        pygame.draw.rect(ventana, (Verde), (objeto1 * 20 + 4, objeto2 * 20 + 4, 13, 13), 9)
    else:
        pygame.draw.rect(ventana, (Cosa), (objeto1 * 20 + 4, objeto2 * 20 + 4, 13, 13), 9)


def largo(tamaño):        #Contar tamaño de la serpinte
    if int(tamaño) > 99 and int(tamaño) < 1000:
        dig = 460
    elif int(tamaño) > 9 and int(tamaño) < 100:
        dig = 500
    elif int(tamaño) > 1000:
        dig = 430
    else:
        dig = 530
    return dig


def lados(vivora):      #Limitar pantalla
    ANCHO
    ALTO

    return vivora

def generarEnemigos(listaObstaculos, imgObstaculo):  #Generar enemigos
    for x in range(5):
        for y in range(4):
            # Generar el enemigo en x,y
            cx = 50 + x*150
            cy = 50 + y*100
            obstaculo = pygame.sprite.Sprite()
            obstaculo.image = imgObstaculo
            obstaculo.rect = imgObstaculo.get_rect()
            obstaculo.rect.left = cx
            obstaculo.rect.top = cy
            listaObstaculos.append(obstaculo)

def generarEnemigoAzar(listaObjetos, imgObstaculo):   #Generar enemigos al azar
    cx = randint(20,ANCHO-128)
    cy = randint(50,ALTO)
    obstaculo = pygame.sprite.Sprite()
    obstaculo.image = imgObstaculo
    obstaculo.rect = imgObstaculo.get_rect()
    obstaculo.rect.left = cx
    obstaculo.rect.top = cy
    listaObjetos.append(obstaculo)

def dibujar():     #Dibujar el juego
    pygame.init()


    #PROCURA COQUETEARME MAS.mp3
    pygame.mixer.init()
    pygame.mixer.music.load("PROCURA COQUETEARME MAS.mp3")
    pygame.mixer.music.play(-1)

    # Poner todos los sprites

    imgbotonJugar = pygame.image.load("button_Jugar.png")
    btnJugar = pygame.sprite.Sprite
    btnJugar.image = imgbotonJugar
    btnJugar.rect = imgbotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height // 2

    imgPunto1=pygame.image.load("1punto.png")
    punto1=pygame.sprite.Sprite
    punto1.image=imgPunto1

    imgpunto2=pygame.image.load("2puntos.png")
    punto2=pygame.sprite.Sprite
    punto2.image=imgpunto2

    imgcaVivora=pygame.image.load("cabezavivora.png")
    cabeza=pygame.sprite.Sprite
    cabeza.image=imgcaVivora

    imgcuVivora=pygame.image.load("cuerpoViv.png")
    cuerpo=pygame.sprite.Sprite
    cuerpo.image=imgcuVivora

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    Extra = False
    vivora = [[5, 7], [5, 6], [5, 5]]
    Capital = pygame.font.Font(None, 100)
    dibujarMenu(ventana, btnJugar)
    objeto1 = 10
    objeto2 = 10
    direccion = 2
    termina = False
    estados = "menu"

    #obstaculos
    listaObstaculos=[]
    imgObstaculo=pygame.image.load("bloque.png")
    generarEnemigos(listaObstaculos,imgObstaculo)


    while not termina:


        tamaño = str(len(vivora))
        dig=largo(tamaño)
        puntiacion = Capital.render(tamaño, 2, Negro)
        ventana.fill((255, 255, 255))
        ventana.blit(puntiacion, (dig, 20))
        timer=0
        timer += 1 / 40
        if timer >= 2:
            generarEnemigoAzar(listaObstaculos,imgObstaculo)
        ventana.blit(puntiacion,(dig,20))

        dibujarVivora(vivora, ventana)
        puntuacion(objeto1, objeto2, Extra, ventana)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                sys.exit()
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estados=="menu":
                    xb,yb,anchoB,altoB=btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estados=="jugando"

                    #3:abajo
                    #1:arriba
                    #4:izq
                    #2:derecha
            elif evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    direccion = 3
                elif evento.key == K_UP:
                    direccion = 1
                elif evento.key == K_LEFT:
                    direccion = 4
                elif evento.key == K_RIGHT:
                    direccion = 2

            if direccion == 2:    #Mover a la vivora completa en la 4 direcciones segun se le indique
                vivora = mover(vivora, [vivora[0][0], vivora[0][1] + 1])
            elif direccion == 4:
                vivora = mover(vivora, [vivora[0][0], vivora[0][1] - 1])
            elif direccion == 1:
                vivora = mover(vivora, [vivora[0][0] - 1, vivora[0][1]])
            elif direccion == 3:
                vivora = mover(vivora, [vivora[0][0] + 1, vivora[0][1]])


            if vivora[0][0] == objeto2 and vivora[0][1] == objeto1:   #ir sumando la puntuacion
                if Extra:
                    vivora.append([-6, -5])
                vivora.append([-2, -3])
                objeto1=randint(1, 30)
                objeto2 =randint(1, 23)
                if Extra:
                    Extra = False
            vivora = lados(vivora)

            for i in range(1, len(vivora)):
                if vivora[0][0] == vivora[i][0] and vivora[0][1] == vivora[i][1]:

                    sys.exit()


        reloj.tick(40)
        pygame.display.flip()
    pygame.quit()


def main():
    dibujar()




main()

