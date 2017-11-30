# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Lime = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple = (128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)

NUM_IMAGENES = 10
TIEMPO_ENTRE_FRAMES = 0.1           # Tiempo entre cada imagen de la animación
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES

#Enemigo
def crearListaSprites():
    lista = []

    for i in range(NUM_IMAGENES):
        nombre = "imagenes/Pacman-"+str(i+1)+".png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = ANCHO//2+40
        sprAnimacion.rect.bottom = ALTO-90
        lista.append(sprAnimacion)

    return lista

def crearListaSprites2():
    lista = []

    for i in range(NUM_IMAGENES):
        nombre = "imagenes/mario-"+str(i+1)+".png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = 40
        sprAnimacion.rect.bottom = ALTO-90
        lista.append(sprAnimacion)

    return lista

def obtenerFrame(timerAnimacion, listaSprites):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]

def obtenerFrame2(timerAnimacion, listaSprites):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]

def dibujarmenu(ventana,Jugar,logo,tutorial,records,salir):
    ventana.blit(Jugar.image,Jugar.rect)
    ventana.blit(logo.image,logo.rect)
    ventana.blit(tutorial.image,tutorial.rect)
    ventana.blit(records.image, records.rect)
    ventana.blit(salir.image, salir.rect)

def dibujartutorial(ventana, regresar,tutorial):
    ventana.fill(White)
    ventana.blit(tutorial.image,tutorial.rect)
    ventana.blit(regresar.image,regresar.rect)


def dibujarrecords(ventana, regresar,tiempos):
    ventana.fill(Teal)
    ventana.blit(regresar.image,regresar.rect)
    ventana.blit(tiempos.image,tiempos.rect)




def dibujarjungando(ventana,laberinto1,laberinto2,frameActual,frameActual2,texto1,texto2,texto4,texto5,texto6):
    ventana.fill(Olive)
    ventana.blit(laberinto1.image,laberinto1.rect)
    ventana.blit(laberinto2.image,laberinto2.rect)
    ventana.blit(frameActual.image, frameActual.rect)
    ventana.blit(frameActual2.image,frameActual2.rect)
    ventana.blit(texto1,(10,15))
    ventana.blit(texto2,((ANCHO//4),15))
    ventana.blit(texto4,((ANCHO*1.5//3),15))
    ventana.blit(texto5,((ANCHO//4),40))
    ventana.blit(texto6,((10,40)))



def dibujarperdiste(ventana, texto3,salir):
    ventana.fill(Red)
    ventana.blit(texto3,(ANCHO//2-100,ALTO//2))
    ventana.blit(salir.image,salir.rect)


def dibujarganaste(ventana, texto7,texto4):
    ventana.blit(texto7,(ANCHO//2-300,ALTO//2))
    ventana.blit(texto4,(ANCHO//2-100,ALTO*2//3))


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    # estados
    estado = 'menu'  # Jugando,  Termina, Tutorial, Records,Perdiste

    listaSprites = crearListaSprites()
    listaSprites2=crearListaSprites2()
    timerAnimacion = 0

    # botones
    imglogo = pygame.image.load('imagenes/Logo.png')
    logo= pygame.sprite.Sprite()
    logo.image = imglogo
    logo.rect = imglogo.get_rect()
    logo.rect.left = ANCHO // 2 - logo.rect.width // 2
    logo.rect.top = ALTO // 6 - logo.rect.height // 2

    imgtutorial = pygame.image.load('imagenes/Tutorial.png')
    tutorial = pygame.sprite.Sprite()
    tutorial.image = imgtutorial
    tutorial.rect = imgtutorial.get_rect()
    tutorial.rect.left = 0
    tutorial.rect.top = 0

    imgtiempos= pygame.image.load('imagenes/Tiempos.png')
    tiempos = pygame.sprite.Sprite()
    tiempos.image = imgtiempos
    tiempos.rect = imgtiempos.get_rect()
    tiempos.rect.left = 0
    tiempos.rect.top = 0

    imgBotonJugar1 = pygame.image.load('botones/button_jugar1.png')
    imgBotonJugar2 = pygame.image.load('botones/button_jugar2.png')
    btnJugar = pygame.sprite.Sprite()
    btnJugar.image = imgBotonJugar1
    btnJugar.rect = imgBotonJugar1.get_rect()
    btnJugar.rect.left = ANCHO // 4 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO*2 // 5 - btnJugar.rect.height // 2

    imgBotontutorial1 = pygame.image.load('botones/button_tutorial1.png')
    imgBotontutorial2 = pygame.image.load('botones/button_tutorial2.png')
    btntutorial = pygame.sprite.Sprite()
    btntutorial.image = imgBotontutorial1
    btntutorial.rect = imgBotontutorial1.get_rect()
    btntutorial.rect.left = ANCHO*3 // 4 - btntutorial.rect.width // 2
    btntutorial.rect.top = ALTO*2 // 5 - btntutorial.rect.height // 2

    imgBotonregresar1 = pygame.image.load('botones/button_return1.png')
    imgBotonregresar2 = pygame.image.load('botones/button_return2.png')
    btnregresar = pygame.sprite.Sprite()
    btnregresar.image = imgBotonregresar1
    btnregresar.rect = imgBotonregresar1.get_rect()
    btnregresar.rect.right = btnregresar.rect.width
    btnregresar.rect.top = ALTO-btnregresar.rect.height

    imgBotonrecords1 = pygame.image.load('botones/button_records1.png')
    imgBotonrecords2 = pygame.image.load('botones/button_records2.png')
    btnrecords = pygame.sprite.Sprite()
    btnrecords.image = imgBotonrecords1
    btnrecords.rect = imgBotonrecords1.get_rect()
    btnrecords.rect.left = ANCHO // 4 - btnrecords.rect.width // 2
    btnrecords.rect.top = ALTO*3 // 5 - btnrecords.rect.height // 2

    imgBotonsalir1 = pygame.image.load('botones/button_salir1.png')
    imgBotonsalir2 = pygame.image.load('botones/button_salir2.png')
    btnsalir = pygame.sprite.Sprite()
    btnsalir.image = imgBotonsalir1
    btnsalir.rect = imgBotonsalir1.get_rect()
    btnsalir.rect.left = ANCHO*3 // 4 - btnsalir.rect.width // 2
    btnsalir.rect.top = ALTO*3 // 5 - btnsalir.rect.height // 2

    #Musica
    pygame.mixer.init()
    pygame.mixer.music.load("Rize_up.mp3")
    pygame.mixer.music.play(-1)

    #efecto = pygame.mixer.Sound("shoot.wav")
    #jugador

    #Laberinto
    imglaberinto1 = pygame.image.load('imagenes/laberinto-02.png')
    laberinto1 = pygame.sprite.Sprite()
    laberinto1.image = imglaberinto1
    laberinto1.rect = imglaberinto1.get_rect()
    laberinto1.rect.left = 10
    laberinto1.rect.bottom = ALTO-10

    imglaberinto2 = pygame.image.load('imagenes/laberinto-02.png')
    laberinto2 = pygame.sprite.Sprite()
    laberinto2.image = imglaberinto2
    laberinto2.rect = imglaberinto2.get_rect()
    laberinto2.rect.left = ANCHO//2+10
    laberinto2.rect.bottom = ALTO - 10

    #Tiempos
    timer=5
    tiempo=0
    #Racha
    racha=10


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEMOTION:
                xm, ym = pygame.mouse.get_pos()
                if estado=='menu':
                    xb1, yb1, anchob1, altob1 = btnJugar.rect
                    xb2, yb2, anchob2, altob2 = btntutorial.rect
                    xb4, yb4, anchob4, altob4 = btnrecords.rect
                    xb5, yb5, anchob5, altob5 = btnsalir.rect
                    if xm >= xb1 and xm <= xb1 + anchob1:
                        if ym >= yb1 and ym <= yb1 + altob1:
                            btnJugar.image=imgBotonJugar2
                        else:
                            btnJugar.image = imgBotonJugar1
                    if xm >= xb2 and xm <= xb2 + anchob2:
                        if ym >= yb2 and ym <= yb2 + altob2:
                            btntutorial.image=imgBotontutorial2
                        else:
                            btntutorial.image = imgBotontutorial1
                    if xm >= xb4 and xm <= xb4 + anchob4:
                        if ym >= yb4 and ym <= yb4 + altob4:
                            btnrecords.image = imgBotonrecords2
                        else:
                            btnrecords.image = imgBotonrecords1
                    elif xm >= xb5 and xm <= xb5 + anchob5:
                        if ym >= yb5 and ym <= yb5 + altob5:
                            btnsalir.image = imgBotonsalir2
                        else:
                            btnsalir.image = imgBotonsalir1
                    else:
                        btnJugar.image=imgBotonJugar1
                        btntutorial.image = imgBotontutorial1
                        btnrecords.image = imgBotonrecords1
                        btnsalir.image = imgBotonsalir1
                elif estado=='tutorial' or estado=='records':
                    xb3, yb3, anchob3, altob3 = btnregresar.rect
                    if xm >= xb3 and xm <= xb3 + anchob3:
                        if ym >= yb3 and ym <= yb3 + altob3:
                            btnregresar.image=imgBotonregresar2
                        else:
                            btnregresar.image = imgBotonregresar1
                elif estado=='Perdiste':
                    xb5, yb5, anchob5, altob5 = btnsalir.rect
                    if xm >= xb5 and xm <= xb5 + anchob5:
                        if ym >= yb5 and ym <= yb5 + altob5:
                            btnsalir.image = imgBotonsalir2
                        else:
                            btnsalir.image = imgBotonsalir1
                    else:
                        btnsalir.image = imgBotonsalir1

            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado=='menu':
                    xb1,yb1, anchob1,altob1= btnJugar.rect
                    xb2, yb2, anchob2, altob2 = btntutorial.rect
                    xb4, yb4, anchob4, altob4 = btnrecords.rect
                    xb5, yb5, anchob5, altob5 = btnsalir.rect
                    if xm >=xb1 and xm<=xb1+anchob1:
                        if ym>=yb1 and ym<=yb1+altob1:
                            estado ='jugando'
                            timer=5
                    if xm >= xb2 and xm <= xb2 + anchob2:
                        if ym >= yb2 and ym <= yb2 + altob2:
                            estado = 'tutorial'
                    if xm >= xb4 and xm <= xb4 + anchob4:
                        if ym >= yb4 and ym <= yb4 + altob4:
                            estado = 'records'
                    if xm >= xb5 and xm <= xb5 + anchob5:
                        if ym >= yb5 and ym <= yb5 + altob5:
                            estado = 'termina'
                elif estado=='tutorial' or estado=='records':
                    xb3, yb3, anchob3, altob3 = btnregresar.rect
                    if xm >= xb3 and xm <= xb3 + anchob3:
                        if ym >= yb3 and ym <= yb3 + altob3:
                            estado = 'menu'
                elif estado=='Perdiste':
                    xb5, yb5, anchob5, altob5 = btnsalir.rect
                    if xm >= xb5 and xm <= xb5 + anchob5:
                        if ym >= yb5 and ym <= yb5 + altob5:
                            estado = 'termina'
            elif evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_SPACE:
                    for i in listaSprites2:
                        if i.rect.top >= 260:
                            i.rect.top -= 10
                        elif i.rect.top <= 260 and i.rect.right <= 160:
                            i.rect.right += 10
                        elif i.rect.right <= 161 and i.rect.top >= 160:
                            i.rect.top -= 10
                        elif i.rect.top <= 159 and i.rect.right <= 230:
                            i.rect.right += 10
                        elif i.rect.right <= 240 and i.rect.top >=105:
                            i.rect.top -= 10
                        elif i.rect.top <= 105 and i.rect.left <= 400:
                            i.rect.left += 10
                        elif i.rect.top <= 105 and i.rect.right >= 401:
                            estado = 'Ganaste'
        if estado!='Ganaste':
            tiempo+=1/40
        else:
            tiempo+=0
        timer -= 1 / 40
        if timer <= 0:
            timer = 5
            racha=0
        fuente = pygame.font.SysFont("monospace", 30)
        texto1 = fuente.render("Tiempo: " + str('%.2f'%timer), 1, Blue)
        texto2=fuente.render("Racha: "+str(racha),1,Lime)
        fuente2 = pygame.font.SysFont("monospace", 68)
        texto3 = fuente2.render("Perdiste!",1,Black)
        texto4= fuente.render("Tiempo Total: " +str('%.2f'%tiempo),1,Cyan)
        texto5= fuente.render("Enemigo: PACMON",1,Red)
        texto6= fuente.render("Jugador:Pancho",1,Maroon)
        texto7=fuente2.render("Ganaste con un tiempo de: ",1,Maroon)

        # Borrar pantalla
        ventana.fill(Navy)
        frameActual = obtenerFrame(timerAnimacion, listaSprites)
        frameActual2=obtenerFrame2(timerAnimacion,listaSprites2)
        if estado=='menu':
            dibujarmenu(ventana,btnJugar,logo,btntutorial,btnrecords,btnsalir)
        elif estado=='tutorial':
            dibujartutorial(ventana,btnregresar,tutorial)
        elif estado=='jugando':
            for i in listaSprites:
                if i.rect.top >= 264:
                    i.rect.top -= 1
                elif i.rect.top <= 263 and i.rect.right <= 560:
                    i.rect.right += 1
                elif i.rect.right <= 561 and i.rect.top >= 160:
                    i.rect.top -= 1
                elif i.rect.top <= 159 and i.rect.right <= 630:
                    i.rect.right += 1
                elif i.rect.right <= 631 and i.rect.top > 105:
                    i.rect.top -= 1
                elif i.rect.top <= 105 and i.rect.left <= 800:
                    i.rect.left += 1
                elif i.rect.top <= 105 and i.rect.left <= 801:
                    estado = 'Perdiste'
            dibujarjungando(ventana,laberinto1,laberinto2,frameActual,frameActual2,texto1,texto2,texto4,texto5,texto6)
        elif estado=='records':
            dibujarrecords(ventana,btnregresar,tiempos)
        elif estado=='termina':
            termina=True
        elif estado=='Perdiste':
            dibujarperdiste(ventana,texto3,btnsalir)
        elif estado=='Ganaste':
            dibujarganaste(ventana,texto7,texto4)

        # Dibujar, aquí haces todos los trazos que requieras


        pygame.display.flip()  # Actualiza trazos
        timerAnimacion += reloj.tick(40) / 1000  # Tiempo exacto entre frames

        if timerAnimacion >= TIEMPO_TOTAL:
            timerAnimacion = 0

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()