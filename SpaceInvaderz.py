# encoding: UTF-8
# Autor Aaron Villanueva
from random import randint
import pygame

#Dimensiones de la pantalla
anchoVentana = 800
altoVentana = 600
alturaMarco=600//10

#Variables globales para las condiciones de derrota
balasParaPerder=20
balasParaPerderEfecto=125
#Colores
principal=(255,255,255)
fondo=(0,0,0)

#Imagenes por segundo variable global.
fps=40

#Esta función crea el mensaje del final del juego
def conclusionPartida(ventana, listaEnemigos, timerFinal,numeroBalas):
    if numeroBalas<balasParaPerder:
        fuentePuntaje = pygame.font.SysFont("monospace", 80)
        fuentePuntajeFinal = pygame.font.SysFont("monospace", 50)
        textoPuntajeA = fuentePuntaje.render("FELICIDADES", 0,((randint(0, 255)), (randint(0, 255)), (randint(0, 255))))
        textoPuntajeB = fuentePuntaje.render("DERROTASTE A ", 0, ((randint(0, 255)), (randint(0, 255)), (randint(0, 255))))
        textoPuntajeC = fuentePuntaje.render("TODOS LOS", 0, ((randint(0, 255)), (randint(0, 255)), (randint(0, 255))))
        textoPuntajeD = fuentePuntaje.render("ALIENS", 0,((randint(0, 255)), (randint(0, 255)), (randint(0, 255))))
        textoPuntajeFinal= fuentePuntajeFinal.render(str(timerFinal)+" puntos",0,((randint(0, 255)), (randint(0, 255)), (randint(0, 255))))
        posicionPuntajeA = textoPuntajeA.get_rect(center=(anchoVentana // 2, 100))
        ventana.blit(textoPuntajeA, posicionPuntajeA)
        posicionPuntajeB = textoPuntajeB.get_rect(center=(anchoVentana // 2, 200))
        ventana.blit(textoPuntajeB, posicionPuntajeB)
        posicionPuntajeC = textoPuntajeC.get_rect(center=(anchoVentana // 2, 300))
        ventana.blit(textoPuntajeC, posicionPuntajeC)
        posicionPuntajeD = textoPuntajeD.get_rect(center=(anchoVentana // 2, 400))
        ventana.blit(textoPuntajeD, posicionPuntajeD)
        posicionPuntajeFinal = textoPuntajeFinal.get_rect(center=(anchoVentana // 2, 500))
        ventana.blit(textoPuntajeFinal, posicionPuntajeFinal)
    else:
        fuentePuntaje = pygame.font.SysFont("monospace", 80)
        fuentePuntajeFinal = pygame.font.SysFont("monospace", 50)
        textoPuntajeA = fuentePuntaje.render("FRACASASTE EN", 0, principal)
        textoPuntajeB = fuentePuntaje.render("DERROTAR A ", 0,principal)
        textoPuntajeC = fuentePuntaje.render("TODOS LOS", 0,principal)
        textoPuntajeD = fuentePuntaje.render("ALIENS", 0,principal)
        textoPuntajeFinal = fuentePuntajeFinal.render(str(timerFinal)+" puntos", 0,principal)
        posicionPuntajeA = textoPuntajeA.get_rect(center=(anchoVentana // 2, 100))
        ventana.blit(textoPuntajeA, posicionPuntajeA)
        posicionPuntajeB = textoPuntajeB.get_rect(center=(anchoVentana // 2, 200))
        ventana.blit(textoPuntajeB, posicionPuntajeB)
        posicionPuntajeC = textoPuntajeC.get_rect(center=(anchoVentana // 2, 300))
        ventana.blit(textoPuntajeC, posicionPuntajeC)
        posicionPuntajeD = textoPuntajeD.get_rect(center=(anchoVentana // 2, 400))
        ventana.blit(textoPuntajeD, posicionPuntajeD)
        posicionPuntajeFinal = textoPuntajeFinal.get_rect(center=(anchoVentana // 2, 500))
        ventana.blit(textoPuntajeFinal, posicionPuntajeFinal)

#Esta función dibuja el menu principal y la linea de apoyo para seleccionar una opción con teclado.
def dibujarMenu(ventana, botonJugar, botonMarcadores, botonSalir,seleccion):
    fuente=pygame.font.SysFont("monospace",20)
    textoInstrucciones=fuente.render("Utiliza las flechas para moverte",1,principal)
    textoInstrucciones2=fuente.render("Utiliza la barra espaciadora para seleccionar y disparar",1,principal)
    posicionI=textoInstrucciones.get_rect(center=(400,500))
    posicionI2=textoInstrucciones2.get_rect(center=(400,550))
    ventana.blit(textoInstrucciones,posicionI)
    ventana.blit(textoInstrucciones2,posicionI2)
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonMarcadores.image, botonMarcadores.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)
    if seleccion<=1:
        pygame.draw.line(ventana, principal, (200,  225), (600,  225), 3)
    elif seleccion==2:
        pygame.draw.line(ventana, principal, (200, 325), (600, 325), 3)
    elif seleccion>=3:
        pygame.draw.line(ventana, principal, (200, 425), (600, 425), 3)

#Esta función dibuja la interfaz del usuario con información relevante al juego y el espacio del mismo.
def dibujarInterfazUsuario(ventana, timer,puntaje,numeroBalas):
    fuente=pygame.font.SysFont("monospace", 40)
    pygame.draw.line(ventana, principal, (0,alturaMarco),(anchoVentana,alturaMarco),2)
    if timer<10 and numeroBalas<balasParaPerder:
        texto=fuente.render("Tiempo:"+"00"+str(int(timer)), 1, principal)
    elif timer<100 and numeroBalas<balasParaPerder:
        texto=fuente.render("Tiempo:" +"0" +str(int(timer)), 1, principal)
    elif timer>=100 and numeroBalas<balasParaPerder:
        texto=fuente.render("Tiempo:"  + str(int(timer)), 1, principal)
    if numeroBalas>=balasParaPerder:
        texto=fuente.render("TIEMPO:" + "999",2,principal)
    textoPuntaje = fuente.render("Puntuación: " + str(int(puntaje)),1,principal)
    ventana.blit(textoPuntaje, (50, 10))
    ventana.blit(texto, (520, 10))


#Esta función lee el archivo de marcadores y crea una lista por linea
def leerMarcadores():
    entrada=open("marcadoresMasAltos.txt","r", encoding="UTF-8")
    lineasFinales=entrada.readlines()[1:]
    entrada.close()
    return(lineasFinales)

#Esta función procesa la informacón del archivo de marcadores para poder utilizar los puntajes
def procesarMarcadores(lineasArchivo):
    listaPos=[]
    listaPuntajes=[]
    for linea in lineasArchivo:
        lineaSeparada=linea.split(",")
        nombre=lineaSeparada[0]
        puntaje=int(lineaSeparada[1])
        listaPos.append(nombre)
        listaPuntajes.append(puntaje)
    return(listaPos, listaPuntajes)

#Esta función dibuja la pantalla de marcadores accesible desde el menu principal
def dibujarMarcadores(ventana):
    fuente = pygame.font.SysFont("monospace", 20)
    fuenteMarcadores=pygame.font.SysFont("monospace",50)
    datos=leerMarcadores()
    pos, puntajes=procesarMarcadores(datos)
    textoMarcadores=fuenteMarcadores.render("Puntajes Más Altos",0,((randint(0,255)),(randint(0,255)),(randint(0,255))))
    posicionMarcadores=textoMarcadores.get_rect(center=(anchoVentana//2, 50))
    ventana.blit(textoMarcadores, posicionMarcadores)
    for k in range(0,10):
        textoInicio = fuente.render(str(k+1)+pos[k]+" - "+ str(puntajes[k]), 0, principal)
        if k <5:
            posicionInicio = textoInicio.get_rect(center=(250, 120+(100*k)))
        else:
            posicionInicio = textoInicio.get_rect(center=(550, 120+(100*(k-5))))
        ventana.blit(textoInicio, posicionInicio)

#Esta función recibe el puntaje del jugador, lee los puntajes anteriores y crea un archivo de texto con los 10 puntajes más altos
def añadirNuevoMarcador(puntajeNuevo):
    datos=leerMarcadores()
    pos, puntajes=procesarMarcadores(datos)
    puntajes.append(int(puntajeNuevo))
    puntajes.sort(reverse=True)
    puntajes.pop()
    salida = open("marcadoresMasAltos.txt", "w", encoding="UTF-8")
    for k in range (0,11):
        if k==0:
            salida.write("sufijo,puntaje"+"\n")
        else:
            salida.write(pos[k-1]+","+str(puntajes[k-1])+"\n")
    salida.close()

#Esta función dibuja las balas y los enemigos en la pantalla.
#Además, procesar el movimiento y dibuja al jugador
def dibujarJuego(ventana, listaEnemigos, listaBalas,posJugador, spriteJugador):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

    spriteJugador.rect.center = posJugador, 580
    ventana.blit(spriteJugador.image,spriteJugador.rect)

#Esta función permite que las balas se muevan a través de la pantalla de forma vertical
#Además, si hay una colisión con el área de juego o con un enemigo, borra la bala.
def actualizarBalas(listaBalas, listaEnemigos,puntaje):
    estado="jugando"
    for bala in listaBalas:
        bala.rect.top -= 5
        if bala.rect.top <= alturaMarco:
            listaBalas.remove(bala)
            continue
        borrarBala = False
        for k in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                puntaje+=100
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)
    if len(listaEnemigos)==0 or len(listaEnemigos)>=balasParaPerderEfecto:
        estado="terminado"
    return(puntaje, estado)

#Esta función genera los enemigos iniciales del nivel
def generarEnemigos(listaEnemigos, imgEnemigo):
    for x in range(6):
        for y in range(3):
            cx = 100 + x*100
            cy = 70 + y*100
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)

#Esta función permite ver los efectos del final del juego en caso de perder
def efectosDerrotaAlien(listaEnemigos, imgEnemigo):
    posX = randint(20,anchoVentana-128)
    posY = randint(50,altoVentana)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imgEnemigo
    enemigo.rect = imgEnemigo.get_rect()
    enemigo.rect.center=posX,posY
    listaEnemigos.append(enemigo)

def main():
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    reloj = pygame.time.Clock()
    termina = False

    #Texto
    fuente = pygame.font.SysFont("monospace", 48)

    estado = "menu"    # jugando, fin

    #Cargar imagenes para los botones y los elementos del juego
    imagenBotonJugar = pygame.image.load("BotonJugar.png")
    imagenBotonMarcadores=pygame.image.load("BotonMarcadores.png")
    imagenBotonSalir=pygame.image.load("BotonSalir.png")
    imagenJugador = pygame.image.load("nave.jpg")

    #Procesar el boton Jugar
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imagenBotonJugar
    botonJugar.rect = imagenBotonJugar.get_rect()
    botonJugar.rect.center= anchoVentana//2, 200

    #Procesar el boton Marcadores
    botonMarcadores=pygame.sprite.Sprite()
    botonMarcadores.image=imagenBotonMarcadores
    botonMarcadores.rect=imagenBotonMarcadores.get_rect()
    botonMarcadores.rect.center= anchoVentana//2, altoVentana//2

    #Procesar el boton Salir
    botonSalir = pygame.sprite.Sprite()
    botonSalir.image = imagenBotonSalir
    botonSalir.rect = imagenBotonSalir.get_rect()
    botonSalir.rect.center = anchoVentana // 2, 400

    #Procesar al jugador
    spriteJugador = pygame.sprite.Sprite()
    spriteJugador.image = imagenJugador
    spriteJugador.rect = imagenJugador.get_rect()

    #Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Enemigo.jpg")
    generarEnemigos(listaEnemigos, imgEnemigo)

    #Balas
    listaBalas = []
    imgBala = pygame.image.load("bala.jpg")

    #Variables de conveniencia. Alteradas.
    timer = 0
    seleccion = 1
    posicionX=400
    puntaje=0
    numeroBalas=0
    
    #Iniciar la música y repetirla
    pygame.mixer.init()
    pygame.mixer.music.load("Fondo.ogg")
    pygame.mixer.music.play(-1)

    #Cargar efectos de disparo
    efecto = pygame.mixer.Sound("disparo.wav")

    while not termina:
        #Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            #Controles con click del mouse
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xJugar, yJugar, anchoJugar, altoJugar = botonJugar.rect
                    if xm>=xJugar and xm<=xJugar+anchoJugar:
                        if ym>=yJugar and ym<=yJugar+altoJugar:
                            #Cambiar de estado y comenzar el juego
                            timer = 0
                            estado = "jugando"
                    xMarcadores, yMarcadores, anchoMarcadores, altoMarcadores=botonMarcadores.rect
                    if xm>=xMarcadores and xm<=xMarcadores+anchoMarcadores:
                        if ym>=yMarcadores and ym<=yMarcadores+altoMarcadores:
                            #Cambiar de estado y mostrar marcadores
                            estado="marcadores"
                    xSalir, ySalir, anchoSalir, altoSalir=botonSalir.rect
                    if xm>=xSalir and xm<=xSalir+anchoSalir:
                        if ym>=ySalir and ym<=ySalir+altoSalir:
                            #Salir del juego
                            termina=True
            #Controles con el teclado
            elif evento.type == pygame.KEYDOWN:
                if estado=="menu":
                    #Esta sección inicializa la selección del menu con teclas
                    if seleccion<=1:
                        seleccion=1
                    if seleccion>=3:
                        seleccion=3
                    #Solamente permite usar flechas arriba y abajo del teclado
                    if evento.key==pygame.K_UP:
                        seleccion-=1
                    if evento.key==pygame.K_DOWN:
                        seleccion+=1
                    #Para seleccionar una opción del menu se usa la barra espaciadora
                    if evento.key==pygame.K_SPACE:
                        if seleccion==1:
                            estado="jugando"
                        elif seleccion==2:
                            estado="marcadores"
                        elif seleccion==3:
                            termina=True
                elif estado=="marcadores":
                    #Permite que cualquier tecla que presione el usuario regrese al menu principal
                    estado="menu"
                #Controles cuando se esta jugando
                elif estado=="jugando":
                    if evento.key == pygame.K_SPACE:
                        efecto.play()
                        bala = pygame.sprite.Sprite()
                        bala.image = imgBala
                        bala.rect = imgBala.get_rect()
                        bala.rect.center=posicionX,580
                        listaBalas.append(bala)
                        numeroBalas+=1
                    if evento.key==pygame.K_LEFT:
                        #Esta sección evita que el jugador se salga de la pantalla
                        if posicionX>=80:
                            posicionX-=50
                        #Movimiento regular
                        else:
                            posicionX=30
                    if evento.key==pygame.K_RIGHT:
                        #Esta sección evita que el jugador se salga de la pantalla
                        if posicionX<=720:
                            posicionX+=50
                        #Movimiento regular
                        else:
                            posicionX=770
                elif estado=="terminado":
                    #Permite que cualquier tecla que presione el usuario regrese al menu principal
                    estado="menu"


        #Fondo
        ventana.fill(fondo)

        timer += 1 / fps

        #Condiciones para empezar la invasión y perder el juego
        if numeroBalas>=balasParaPerder:
            efectosDerrotaAlien(listaEnemigos,imgEnemigo)

        #Estados del juego y sus respectivas funciones para desempeñar su trabajo.
        if estado == "menu":
            dibujarMenu(ventana, botonJugar, botonMarcadores, botonSalir,seleccion)
        elif estado=="marcadores":
            dibujarMarcadores(ventana)
        elif estado == "jugando":
            puntaje, estado = actualizarBalas(listaBalas, listaEnemigos, puntaje)
            dibujarInterfazUsuario(ventana, timer,puntaje,numeroBalas)
            dibujarJuego(ventana, listaEnemigos, listaBalas,posicionX, spriteJugador)
        elif estado=="terminado":
            conclusionPartida(ventana, listaEnemigos, puntaje,numeroBalas)
            #Añade la puntuación del jugador a una lista de la cual solo se toman los 10 valores mas altos para el top.
            añadirNuevoMarcador(puntaje)
        pygame.display.flip()
        reloj.tick(fps)

    pygame.quit()

main()