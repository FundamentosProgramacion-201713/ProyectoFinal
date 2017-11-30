#encoding UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa realiza corre un juego donde una gacela debe llegar al otro lado de la pantalla, sin ser tocado por lo leones.

ANCHO= 800
ALTO=600
BLANCO= (255,255,255)
NEGRO=(0,0,0)
ROJO= (230,0,38)
rebote= 1
segundo=0
minuto=0
timer = 0

from pygame import mixer
import pygame
def dibujarMenu(ventana, btnJugar, fondoDePantalla):#Muestra los elementos relacionados al menú.
    mejorTiempo = open("MejorTiempo", 'r')
    lista1 = mejorTiempo.readlines()
    mejorTiempo.close()
    tiempo1= lista1[1]
    ventana.blit(fondoDePantalla.image, fondoDePantalla.rect)
    fuente = pygame.font.SysFont("monospace", 40)
    texto = fuente.render("El mejor tiempo es: " + tiempo1+"s.", 1, ROJO)
    texto2= fuente.render("Usa las flechas para moverte",1,ROJO)
    ventana.blit(texto2,(100,100))
    ventana.blit(texto, (100, 200))

    ventana.blit( btnJugar.image, btnJugar.rect)



def dibujarJuego(ventana, listaLeones, portal, gacela, barraDeVida, fondoDePantalla, segundo, minuto): #Muestra todos los elementos del nivel 1.
    ventana.blit(fondoDePantalla.image, fondoDePantalla.rect)
    fuente= pygame.font.SysFont("freesansbold.ttf", 40)
    texto= fuente.render (minuto + ":" + segundo, 1, ROJO)
    ventana.blit(texto, (10,10))
    for leon in listaLeones:
        ventana.blit(leon.image, leon.rect)
    ventana.blit(portal.image, portal.rect)
    ventana.blit(gacela.image, gacela.rect)
    ventana.blit(barraDeVida.image, barraDeVida.rect)





def generarLeones(listaLeones, imgLeon):#Genera los leones y los agrega a la lista "listaLeones".
    for x in range(3):
        if x==0:
            cx=150
            cy=0
        if x==1:

            cx = 301
            cy = 250
        if x==2:
            cx=452
            cy=400
        leon = pygame.sprite.Sprite()
        leon.image = imgLeon
        leon.rect = imgLeon.get_rect()
        leon.rect.left = cx
        leon.rect.top = cy
        listaLeones.append(leon)


def dibujarJuego2(ventana, listaLeones, lineaDeMeta, gacela, barraDeVida, fondoDePantalla, segundo, minuto):#Muestra todos elementos relacionados al nivel 2.
    segundo=str(segundo)
    ventana.blit(fondoDePantalla.image, fondoDePantalla.rect)
    fuente = pygame.font.SysFont("freesansbold.ttf", 40)
    texto = fuente.render(minuto + ":" + segundo+"s.", 1, ROJO)
    ventana.blit(texto, (10, 10))
    for leon in listaLeones:
        ventana.blit(leon.image, leon.rect)
    ventana.blit(lineaDeMeta.image, lineaDeMeta.rect)
    ventana.blit(gacela.image, gacela.rect)
    ventana.blit(barraDeVida.image, barraDeVida.rect)


def dibujarMensajePerdido(ventana, minuto, segundo, fondoDePantalla, formaDePerder ):#Muestra todos los elementos relacionados a la ventana del mensaje, donde se muestra que el usuario perdió.
    mejorTiempo = open("MejorTiempo", 'r')
    lista1 = mejorTiempo.readlines()
    mejorTiempo.close()
    tiempo1 = lista1[1]
    ventana.blit(fondoDePantalla.image,fondoDePantalla.rect)
    fuente=pygame.font.SysFont("freesansbold.ttf",40)
    texto1 =fuente.render("¡Has perdido!",1, ROJO)
    ventana.blit(texto1 ,(ANCHO//2-90, 50))
    texto2 = fuente.render("Tu tiempo es:"+minuto+":"+segundo+"s", 1, ROJO)
    ventana.blit(texto2, (ANCHO // 2 - 110, 100))
    texto3 = fuente.render("El mejor tiempo es: " + tiempo1 + "s", 1, ROJO)
    ventana.blit(texto3,(ANCHO//2-120,150 ))



def mostrarMensajeGanador(ventana, minuto, segundo, fondoDePantalla, mejorTiempo): #Muestra todas los elementos relacionadas a la ventana que muestra el mensaje ganador.
    mejorTiempo=str(mejorTiempo)
    ventana.blit(fondoDePantalla.image, fondoDePantalla.rect)
    fuente=pygame.font.SysFont("freesansbold.ttf", 40)
    texto1= fuente.render("¡Felicidades, has ganado!", 1, ROJO)
    ventana.blit(texto1, (ANCHO//2 -300, 50))
    texto2= fuente.render("Tu tiempo es:"+minuto+":"+segundo+"s",1, ROJO)
    ventana.blit(texto2, (ANCHO//2-300,100))
    texto3 = fuente.render("El mejor es: "+ mejorTiempo, 1, ROJO)
    ventana.blit(texto3, (ANCHO // 2 - 300, 150))


def checarMejorTiempo(minuto, segundo):#Revisa el archivo de "MejorTiempo", para saber si es un tiempo menor y lo modifica si es el caso
    mejorTiempo=open("MejorTiempo",'r')
    lista1= mejorTiempo.readlines()
    mejorTiempo.close()
    segundo=float(segundo)
    tiempo1= float(lista1[1])
    if segundo<=tiempo1:
        escribirTiempo = open("MejorTiempo", "w")
        escribirTiempo.write("Mejor Tiempo")
        escribirTiempo.write("\n")
        segundo=str(segundo)
        escribirTiempo.write(str(segundo))
        escribirTiempo.close()
        return segundo
    return tiempo1
def dibujar(): #Dibuja los trazos principales del juego
    formaDePerder=0
    contador = 0
    abajo3 = True
    abajo = True
    abajo2 = False
    segundo = 0
    minuto = 0
    timer = 0
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    # Estados
    estado = "menu"
    # Botonoes

    imgBotonJugar = pygame.image.load("botonJugar.png")
    botonJugar = pygame.sprite.Sprite()  # Sprite
    botonJugar.image = imgBotonJugar
    botonJugar.rect = imgBotonJugar.get_rect()

    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2

    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.top // 2

    imgFondoDePantalla= pygame.image.load("sabana.png")
    fondoDePantalla= pygame.sprite.Sprite()
    fondoDePantalla.image= imgFondoDePantalla
    fondoDePantalla.rect= imgFondoDePantalla.get_rect()
    fondoDePantalla.rect.top=0
    fondoDePantalla.rect.left=0
    #Personajes
    imgLeon = pygame.image.load("leonO.png")
    leon = pygame.sprite.Sprite()  # Sprite
    leon.image = imgLeon
    leon.rect = imgLeon.get_rect()
    #Elementos
    #Portal
    imgPortal= pygame.image.load("portal.png")
    portal=pygame.sprite.Sprite()
    portal.image=imgPortal
    portal.rect = imgPortal.get_rect()
    portal.rect.left = ANCHO-100
    portal.rect.top = 250
    #Línea de Meta
    imgLineaDeMeta= pygame.image.load("lineaDeMeta.png")
    lineaDeMeta= pygame.sprite.Sprite()
    lineaDeMeta.image=imgLineaDeMeta
    lineaDeMeta.rect=imgLineaDeMeta.get_rect()
    lineaDeMeta.rect.left =20
    lineaDeMeta.rect.top= 250

    #Barra de Vida
    imgBarraDeVidaCompleta=pygame.image.load("barraDeVidaCompleta.jpg")
    barradeVidaCompleta=pygame.sprite.Sprite()
    barradeVidaCompleta.image=imgBarraDeVidaCompleta
    barradeVidaCompleta.rect=imgBarraDeVidaCompleta.get_rect()
    barradeVidaCompleta.rect.left=20
    barradeVidaCompleta.rect.top=ALTO-100
    barraDeVida=barradeVidaCompleta

    imgBarraDeVidaDosTercios=pygame.image.load("barraDeVidaDosTercios.jpg")
    barraDeVidaDosTercios=pygame.sprite.Sprite()
    barraDeVidaDosTercios.image=imgBarraDeVidaDosTercios
    barraDeVidaDosTercios.rect=imgBarraDeVidaDosTercios.get_rect()
    barraDeVidaDosTercios.rect.left=20
    barraDeVidaDosTercios.rect.top=ALTO-100

    imgBarraDeVidaUnTercio = pygame.image.load("barraDeVidaUnTercio.jpg")
    barraDeVidaUnTercio = pygame.sprite.Sprite()
    barraDeVidaUnTercio.image = imgBarraDeVidaUnTercio
    barraDeVidaUnTercio.rect = imgBarraDeVidaUnTercio.get_rect()
    barraDeVidaUnTercio.rect.left = 20
    barraDeVidaUnTercio.rect.top = ALTO - 100

    imgBarraDeVidaVacia = pygame.image.load("barraDeVidaVacia.jpg")
    barraDeVidaVacia = pygame.sprite.Sprite()
    barraDeVidaVacia.image = imgBarraDeVidaVacia
    barraDeVidaVacia.rect = imgBarraDeVidaVacia.get_rect()
    barraDeVidaVacia.rect.left = 20
    barraDeVidaVacia.rect.top = ALTO - 100

    # Enemigos
    listaLeones=[]
    generarLeones(listaLeones,imgLeon)
    #Personaje
    imgGacela= pygame.image.load("gacela2.png")
    gacela=pygame.sprite.Sprite()
    gacela.image=imgGacela
    gacela.rect = imgGacela.get_rect()
    gacela.rect.left=0
    gacela.rect.top=150
    #Música de fondo
    mixer.init()
    pygame.mixer.music.load("elReyLeon.mp3")
    pygame.mixer.music.play(-1)
    #Efectos de sonido
    rugido = pygame.mixer.Sound("rugido.wav")
    magia = pygame.mixer.Sound("magia.wav")
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugando"
            elif estado == "jugando":
                if gacela.rect.colliderect(portal):
                    estado="juego2"
            elif estado=="jugando" or estado=="juego2":
                segundo=float(segundo)



        # Borrar pantalla
        ventana.fill(BLANCO)


        #Menu
        if estado == "menu":
            dibujarMenu(ventana, botonJugar, fondoDePantalla)
        #Nivel1
        elif estado == "jugando":

            dibujarJuego(ventana, listaLeones, portal,gacela, barraDeVida, fondoDePantalla, segundo, minuto)
            #Movimientos de la gacela, con sus condiciones para evitar que se salga de la pantalla.
            if evento.type==pygame. KEYDOWN:
                if evento.key==pygame.K_DOWN:
                    if gacela.rect.top>=ALTO-100:
                        gacela.rect.top-=0
                    if not gacela.rect.top>=ALTO-100:
                        gacela.rect.top+=15
                if evento.key==pygame.K_UP:
                    if gacela.rect.top==0:
                     gacela.rect.top+=0
                    if not gacela.rect.top==0:
                     gacela.rect.top-=15

                if evento.key==pygame.K_LEFT:
                    if gacela.rect.left==0:
                        gacela.rect.left -= 0
                    if not gacela.rect.left==0:
                        gacela.rect.left -= 15
                if evento.key==pygame.K_RIGHT:
                    if gacela.rect.right>=ANCHO:
                        gacela.rect.right+=0
                    if not gacela.rect.right>=ANCHO:
                        gacela.rect.right+=15
            #Genera los leones en el nivel, con sus movimientos.
            for l in range(0, len(listaLeones)):
                if gacela.rect.colliderect(listaLeones[l]):
                    contador +=1
                if contador==0:
                    barraDeVida=barradeVidaCompleta
                if contador==1:
                    barraDeVida=barraDeVidaDosTercios
                if contador==2:
                    barraDeVida=barraDeVidaUnTercio
                if contador==3:
                    barraDeVida=barraDeVidaVacia
                if contador>=4:
                    rugido.play()
                    estado="perdido"
                    formaDePerder=2
                if l == 0:
                    leon1 = listaLeones[0]
                    if abajo:

                        leon1.rect.top += 5
                    if not abajo:

                        leon1.rect.top -= 5

                    if leon1.rect.top == ALTO - 100:
                        abajo = False
                    if leon1.rect.top == 0:
                        abajo = True
                if l == 1:
                    leon2 = listaLeones[1]
                    if abajo2:

                        leon2.rect.top += 5
                    if not abajo2:

                        leon2.rect.top -= 5

                    if leon2.rect.top == ALTO - 100:
                        abajo2 = False
                    if leon2.rect.top == 0:
                        abajo2 = True
                if l == 2:
                    leon3 = listaLeones[2]
                    if abajo3:

                        leon3.rect.top += 5
                    if not abajo3:

                        leon3.rect.top -= 5

                    if leon3.rect.top == ALTO - 100:
                        abajo3 = False
                    if leon3.rect.top == 0:
                        abajo3 = True
            if gacela.rect.colliderect(portal):
                magia.play()
                estado="juego2"

        #Nivel2
        elif estado=="juego2":
                dibujarJuego2(ventana, listaLeones, lineaDeMeta, gacela, barraDeVida, fondoDePantalla, segundo, minuto)
                #Movimientos de la gacela, con sus condiciones para evitar que se salga de la pantalla
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        if gacela.rect.top >= ALTO - 100:
                            gacela.rect.top -= 0
                        if not gacela.rect.top >= ALTO - 100:
                            gacela.rect.top += 18
                    if evento.key == pygame.K_UP:
                        if gacela.rect.top <= 0:
                            gacela.rect.top += 0
                        if not gacela.rect.top <= 0:
                            gacela.rect.top -= 18

                    if evento.key == pygame.K_LEFT:
                        if gacela.rect.left <= 0:
                            gacela.rect.left -= 0
                        if not gacela.rect.left <= 0:
                            gacela.rect.left -= 18
                    if evento.key == pygame.K_RIGHT:
                        if gacela.rect.right >= ANCHO:
                            gacela.rect.right += 0
                        if not gacela.rect.right >= ANCHO:
                            gacela.rect.right += 18
                #Genera los leones, con sus respectivos movimientos
                for l in range(0, len(listaLeones)):
                    if gacela.rect.colliderect(listaLeones[l]):
                        contador += 1
                    if contador == 0:
                        barraDeVida = barradeVidaCompleta
                    if contador == 1:
                        barraDeVida = barraDeVidaDosTercios
                    if contador == 2:
                        barraDeVida = barraDeVidaUnTercio
                    if contador == 3:
                        barraDeVida = barraDeVidaVacia
                    if contador >= 4:
                        rugido.play()
                        estado = "perdido"
                        formaDePerder=2
                    if l == 0:
                        leon1 = listaLeones[0]
                        if abajo:  # rebotar(listaLeones)

                            leon1.rect.top += 25
                        if not abajo:  # rebotarIverso(listaLeones) #actualizarLeones(listaLeones)

                            leon1.rect.top -= 25

                        if leon1.rect.top >= ALTO - 150:
                            abajo = False
                        if leon1.rect.top <= 0:
                            abajo = True
                    if l == 1:
                        leon2 = listaLeones[1]
                        if abajo2:

                            leon2.rect.top += 10
                        if not abajo2:

                            leon2.rect.top -= 10

                        if leon2.rect.top >= ALTO - 150:
                            abajo2 = False
                        if leon2.rect.top <= 0:
                            abajo2 = True
                    if l == 2:
                        leon3 = listaLeones[2]
                        if abajo3:

                            leon3.rect.top += 10
                        if not abajo3:  # rebotarIverso(listaLeones) #actualizarLeones(listaLeones)

                            leon3.rect.top -= 10

                        if leon3.rect.top >= ALTO - 100:
                            abajo3 = False
                        if leon3.rect.top <= 0:
                            abajo3 = True
                if gacela.rect.colliderect(lineaDeMeta):
                    magia.play()
                    estado = "ganado"
        #Mensaje de juego ganado
        elif estado=="ganado":
            mejorTiempo = checarMejorTiempo(minuto,segundo)
            mostrarMensajeGanador(ventana, minuto, segundo, fondoDePantalla, mejorTiempo)

        #Mensaje de juego perdido
        elif estado=="perdido":

            dibujarMensajePerdido(ventana, minuto, segundo, fondoDePantalla, formaDePerder)
        #Cronómetro
        if estado=="jugando" or estado=="juego2":
            timer += 1 / 50
            timer2=timer//1

            if timer2!=timer:
                segundo=timer//1




        minuto=str(minuto)
        segundo=str(segundo)
        pygame.display.flip()  # Actualiza trazos
        reloj.tick(50)  # 50 fps

    pygame.quit()  # termina pygame


def main():#Programa Principal
    dibujar()


main()