#encoding:UTF-8
#José Antonio Gómez Mora
#Proyecto final. Flappy Bird

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NUM_IMAGENES = 5                     # Para las monedas cambien a 10
TIEMPO_ENTRE_FRAMES = 0.1           # Tiempo entre cada imagen de la animación
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES
ESPACIOOBSTACULOS=117


def dibujarBotonJugar():
    imgBotonJugar = pygame.image.load("botones/botonJugar.png")
    btnJugar = pygame.sprite.Sprite()  # Sprite
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height // 2
    return btnJugar


def dibujarPersonaje(timerAnimacion,listaSprites):
    indice = int(timerAnimacion / TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]


def dibujarJuego(ventana, listaObstaculos,listaObstaculos2,personaje):
    #Dibuja personaje
    ventana.blit(personaje.image, personaje.rect)
    #Dibuja obstaculo de abajo
    for obstaculo in listaObstaculos:
        ventana.blit(obstaculo.image,obstaculo.rect)
    #Dibuja obstaculo de arriba
    for obstaculo2 in listaObstaculos2:
        ventana.blit(obstaculo2.image,obstaculo2.rect)


def dibujarMenu(ventana,botonJugar,botonInstrucciones,botonRecord,titulo):
    ventana.blit(botonJugar.image,botonJugar.rect)
    ventana.blit(botonInstrucciones.image,botonInstrucciones.rect)
    ventana.blit(botonRecord.image,botonRecord.rect)
    ventana.blit(titulo.image,titulo.rect)


def crearListaSprites():
    lista=[]
    for i in range(NUM_IMAGENES):
        nombre="imagenes/"+"pajaro"+str(i)+".png"
        imagen = pygame.image.load(nombre)
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = ANCHO-ANCHO//4 - sprAnimacion.rect.width // 2
        sprAnimacion.rect.top = ALTO // 2 - sprAnimacion.rect.height // 2
        lista.append(sprAnimacion)

    return lista


def generarObstaculo1():
    imgObstaculo=pygame.image.load("imagenes/pipe-red.png")
    sprObstaculo=pygame.sprite.Sprite()
    sprObstaculo.image=imgObstaculo
    sprObstaculo.rect=imgObstaculo.get_rect()
    sprObstaculo.rect.left=0-sprObstaculo.rect.width
    sprObstaculo.rect.top=randint(290,ALTO-117)
    return sprObstaculo


def actualizarJuego(listaObstaculos,listaObstaculos2,personaje,listaSprites,moverPersonaje,sonidoPerder):
    if moverPersonaje:
        personaje.rect.top-=30
    if not moverPersonaje:
        personaje.rect.top+=3
    y=personaje.rect.top

    #actualiza sprites con la nueva posicion
    for sprite in listaSprites:
        sprite.rect.top=y

    for obstaculo in listaObstaculos:
        obstaculo.rect.left+=2
        choqueObstaculo1=personaje.rect.colliderect(obstaculo)
        if choqueObstaculo1:
            sonidoPerder.play()
            termina=True

            return termina

    for obstaculo2 in listaObstaculos2:
        obstaculo2.rect.left+=2
        choqueObstaculo2=personaje.rect.colliderect(obstaculo2)
        if choqueObstaculo2:
            sonidoPerder.play()
            termina=True
            return termina

    for k in range(-1,-len(listaObstaculos)+1,-1):
         if listaObstaculos[k].rect.left>=ANCHO:
             listaObstaculos.remove(listaObstaculos[k])

    for k in range(-1,-len(listaObstaculos2)+1,-1):
         if listaObstaculos2[k].rect.left>=ANCHO:
             listaObstaculos2.remove(listaObstaculos2[k])


def generarObstaculo2(obstaculo):
    imgObstaculo = pygame.image.load("imagenes/pipe-red1.png")
    sprObstaculo = pygame.sprite.Sprite()
    sprObstaculo.image = imgObstaculo
    sprObstaculo.rect = imgObstaculo.get_rect()
    sprObstaculo.rect.left =0-sprObstaculo.rect.width
    sprObstaculo.rect.top = obstaculo.rect.top-ESPACIOOBSTACULOS-540
    return sprObstaculo


def actualizarPuntuacion(listaObstaculos,personaje,sonidoPunto):
    xPersonaje = personaje.rect.left
    for obstaculo in listaObstaculos:
        xObstaculo = obstaculo.rect.left
        if xPersonaje<xObstaculo:
            sonidoPunto.play()
            return 1
    return 0


def generarBotonRecord():
    img = pygame.image.load("botones/botonRecord.png")
    btnRecord = pygame.sprite.Sprite()
    btnRecord.image = img
    btnRecord.rect = img.get_rect()
    btnRecord.rect.left = 100
    btnRecord.rect.top = ALTO//2
    return btnRecord


def generarBotonInstrucciones():
    img = pygame.image.load("botones/botonInstrucciones.png")
    btnInstrucciones = pygame.sprite.Sprite()  # Sprite
    btnInstrucciones.image = img
    btnInstrucciones.rect = img.get_rect()
    btnInstrucciones.rect.left = 700 - btnInstrucciones.rect.width
    btnInstrucciones.rect.top = ALTO//2
    return btnInstrucciones


def crearSpriteTitulo():
    img = pygame.image.load("imagenes/titulo.png")
    titulo = pygame.sprite.Sprite()  # Sprite
    titulo.image = img
    titulo.rect = img.get_rect()
    titulo.rect.left = ANCHO //2 - titulo.rect.width//2
    titulo.rect.top = ALTO//6
    return titulo


def generarBotonMenu():
    img = pygame.image.load("botones/botonMenu.png")
    btnMenu = pygame.sprite.Sprite()  # Sprite
    btnMenu.image = img
    btnMenu.rect = img.get_rect()
    btnMenu.rect.left = ANCHO-btnMenu.rect.width
    btnMenu.rect.top = ALTO-btnMenu.rect.height
    return btnMenu


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))   # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado="menu"
    listaObstaculos=[]
    listaObstaculos2=[]


    btnJugar = dibujarBotonJugar()
    btnRecord = generarBotonRecord()
    btnInstrucciones = generarBotonInstrucciones()
    btnMenu = generarBotonMenu()

    titulo= crearSpriteTitulo()

    listaSprites=crearListaSprites()
    timerAnimacion=0

    imagenFondo=pygame.image.load("imagenes/fondoCiudad.jpg")
    x=0

    timer=0
    moverPersonaje=False

    puntos=0

    pygame.mixer.init()
    sonidoElevar= pygame.mixer.Sound("sonidos/wing.wav")
    sonidoPerder = pygame.mixer.Sound("sonidos/hit.wav")
    sonidoPunto = pygame.mixer.Sound("sonidos/point.wav")
    sonidoBorde = pygame.mixer.Sound("sonidos/die.wav")

    fuente = pygame.font.SysFont("American Typewriter", 40)
    nuevoRecord=False

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse,yMouse=pygame.mouse.get_pos()

                if estado=="menu":
                    xBoton,yBoton,largoBoton,altoBoton=btnJugar.rect
                    if xMouse>=xBoton and xMouse<=xBoton+largoBoton:
                        if yMouse>=yBoton and yMouse<=yBoton+altoBoton:
                            estado="jugando"

                    xRecord, yRecord, largoRecord, altoRecord = btnRecord.rect
                    if xMouse>=xRecord and xMouse<=xRecord+largoRecord:
                        if yMouse>=yRecord and yMouse<=yRecord+altoRecord:
                            estado="record"

                    xInstrucciones, yInstrucciones, largoInstrucciones, altoInstrucciones = btnInstrucciones.rect
                    if xMouse>=xInstrucciones and xMouse<=xInstrucciones+largoInstrucciones:
                        if yMouse>=yInstrucciones and yMouse<=yInstrucciones+altoInstrucciones:
                            estado="instrucciones"

                if estado == "instrucciones":
                    xMenu, yMenu, largoMenu, altoMenu = btnMenu.rect
                    if xMouse >= xMenu and xMouse <= xMenu + largoMenu:
                        if yMouse >= yMenu and yMouse <= yMenu + altoMenu:
                            estado = "menu"

                if estado == "record":
                    xMenu, yMenu, largoMenu, altoMenu = btnMenu.rect
                    if xMouse >= xMenu and xMouse <= xMenu + largoMenu:
                        if yMouse >= yMenu and yMouse <= yMenu + altoMenu:
                            estado = "menu"

                if estado=="gameOver":
                    archivo = open("puntuacionMasAlta.txt", "r")
                    lineas = archivo.readlines()
                    for linea in lineas:
                        if int(linea) < puntos:
                            archivo = open("puntuacionMasAlta.txt", "w")
                            archivo.write(str(puntos))
                            archivo.close()
                        else:
                            archivo.close()
                        return True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    sonidoElevar.play()
                    moverPersonaje=True

            if evento.type == pygame.K_UP:
                moverPersonaje=False
        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado=="menu":
            ventana.blit(imagenFondo,(0,0))
            dibujarMenu(ventana,btnJugar,btnInstrucciones,btnRecord,titulo)

        if estado == "record":
            record = open("puntuacionMasAlta.txt")
            record = record.readlines()
            imprimirRecord = False
            ventana.blit(imagenFondo, (x, 0))
            ventana.blit(btnMenu.image,btnMenu.rect)
            for puntuacion in record:
                if int(puntuacion)>0:
                    imprimirRecord = True
                    if imprimirRecord:
                        record = fuente.render("RÉCORD: %d "%int(puntuacion),1,BLANCO)
                        ventana.blit(record,(ANCHO//2-80,ALTO//2))

            if imprimirRecord == False:
                noHayRecord = fuente.render("Aún no hay récord",1,BLANCO)
                ventana.blit(noHayRecord,(ANCHO//2,ALTO//2))

        if estado == "instrucciones":
            obstaculosIntrucciones = []
            ventana.blit(imagenFondo,(0, 0))
            ventana.blit(btnMenu.image, btnMenu.rect)
            pajaroInstrucc = listaSprites[0]

            if len(obstaculosIntrucciones)<2:
                obsInstrucc1=generarObstaculo1()
                obsInstrucc1.rect.left=ANCHO//4
                obsInstrucc1.rect.top = ALTO//2
                obstaculosIntrucciones.append(obsInstrucc1)
                obsInstrucc2=generarObstaculo2(obsInstrucc1)
                obsInstrucc2.rect.left = ANCHO // 4
                obsInstrucc1.rect.top=ALTO-ALTO//2
                obstaculosIntrucciones.append(obsInstrucc2)
            ventana.blit(pajaroInstrucc.image,pajaroInstrucc.rect)
            ventana.blit(obstaculosIntrucciones[0].image,obstaculosIntrucciones[0].rect)
            ventana.blit(obstaculosIntrucciones[1].image,obstaculosIntrucciones[1].rect)
            instrucciones1 = fuente.render("¡Presiona la tecla espacio para volar!",1,BLANCO)
            instrucciones2=fuente.render("¡El juego consiste en pasar en medio de las pipas!",1,BLANCO)
            instrucciones3=fuente.render("¡Mucha Suerte!",1,BLANCO)
            ventana.blit(instrucciones1,(ANCHO//8,ALTO//4))
            ventana.blit(instrucciones2,(ANCHO//8,ALTO//2))
            ventana.blit(instrucciones3,(ANCHO//8,ALTO-ALTO//4))

        if estado=="jugando":
            ventana.blit(imagenFondo,(x,0))
            ventana.blit(imagenFondo,(-ANCHO+x,0))
            personaje = dibujarPersonaje(timerAnimacion, listaSprites)
            x+=1

            if x>=ANCHO:
                x=0
            fuente=pygame.font.SysFont("American Typewriter",40)
            colision=actualizarJuego(listaObstaculos,listaObstaculos2,personaje,listaSprites,moverPersonaje,sonidoPerder)
            dibujarJuego(ventana,listaObstaculos,listaObstaculos2,personaje)
            moverPersonaje = False

            if colision:
                estado="gameOver"
                timer=0

            #genera los obstaculos cada cuatro segundos
            if timer>4:
                obstaculo=generarObstaculo1()
                listaObstaculos.append(obstaculo)
                obstaculo2=generarObstaculo2(obstaculo)
                listaObstaculos2.append(obstaculo2)
                timer=0
                if not colision:
                    punto  = actualizarPuntuacion(listaObstaculos, personaje, sonidoPunto)
                    puntos+=punto
            #puntuacion en pantalla
            score = fuente.render(str(puntos), 1, BLANCO)
            ventana.blit(score, (ANCHO // 2 , ALTO - 500))
            #Prueba colision con bordes de pantalla
            if personaje.rect.top>ALTO:
                sonidoBorde.play()
                estado="gameOver"
                timer=0
                timerAnimacion=0

            if personaje.rect.top<0:
                sonidoBorde.play()
                estado="gameOver"
                timer=0
                timerAnimacion=0
            timer += 1 / 40

        if estado=="gameOver":
            puntuacionMasAlta=open("puntuacionMasAlta.txt")
            leerArchivo=puntuacionMasAlta.readlines()
            for linea in leerArchivo:
                if int(linea)<=puntos:

                    nuevoRecord=True
            mensajeRecord = fuente.render("NUEVO RÉCORD!", 1, BLANCO)

            ventana.blit(imagenFondo,(0,0))
            if nuevoRecord:
                ventana.blit(mensajeRecord,(ANCHO//2-100,ALTO//2-100))

            score = fuente.render("SCORE %d " % puntos, 1, BLANCO)
            gameOver=fuente.render("GAMEOVER",1,BLANCO)
            mensaje=fuente.render("Da click para continuar",1,BLANCO)
            ventana.blit(score, (ANCHO // 2 - 50, ALTO - 500))
            ventana.blit(gameOver,(ANCHO // 2-65, ALTO//2))
            ventana.blit(mensaje,(ANCHO//2-130,ALTO-ALTO//4))

        pygame.display.flip()# Actualiza trazos
        timerAnimacion += reloj.tick(40) / 1000  # Tiempo exacto entre frames
        if timerAnimacion >= TIEMPO_TOTAL:
            timerAnimacion = 0

    pygame.quit()  # termina pygame


def main():
    jugar=dibujar()
    while jugar:
        jugar=dibujar()


main()