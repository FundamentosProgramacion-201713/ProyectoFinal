#encoding:UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa del proyecto final: Videojuego que trata de defender tesoros de enemigos que llegen a atacar.

import pygame
from pygame.locals import *
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
FONDO = pygame.image.load("fondo.png")
FONDO2 = pygame.image.load("fondojuego.png")
FONDO3 = pygame.image.load("fondoPerder.png")
AZULOBS = (5, 23, 42)

# Puntaje
puntaje = "00"
tablaPuntuaciones = {1:"00",2:"00",3:"00",4:"00",5:"00",6:"00",7:"00",8:"00",9:"00",10:"00"}
contadorpuntaje = 0

#Funcion en la que dibujamos el menu y los botones
def dibujarMenu(ventana, btnJugar, btnpuntajes):
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnpuntajes.image, btnpuntajes.rect)

#Funcion que dibuja n la pantalla del juego el boton de ayuda para el jugador
def dibujarbotonAyuda(ventana, btnAyuda):
    ventana.blit(btnAyuda.image,btnAyuda.rect)

#Funcion que dibuja el boton de volver para las panallas que lo necesiten
def dibujarbotonVolver(ventana, btnVolver):
    ventana.blit(btnVolver.image,btnVolver.rect)

#Funcion que dibuja al personaje en la pantalla
def dibujarpersonaje(imgPersonaje, posxpersonaje, ventana):
    ventana.blit(imgPersonaje,(posxpersonaje,470))

#Funcion que actualiza la posicion dle personaje en el eje x
def actualizarposicion(posxpersonaje):
    presionada = pygame.key.get_pressed()
    if presionada[K_a]:
        if posxpersonaje >= 50:
            posxpersonaje -= 5
    elif presionada[K_d]:
        if posxpersonaje <= 750:
            posxpersonaje += 5
    return posxpersonaje

#Funcion que crea la lista de los tesoros que proteje el jugador y los dibuja
def creartesoros(imgTesoro, listaTesoros):
    for x in range(4):
        cx = 85 + x * 170
        tesoro = pygame.sprite.Sprite()  # SPRITE
        tesoro.image = imgTesoro
        tesoro.rect = imgTesoro.get_rect()
        tesoro.rect.left = cx
        tesoro.rect.top = 520
        if len(listaTesoros)<5:
            listaTesoros.append(tesoro)

#Funcion que creal al set de enemigos que el jugador debera combatir
def crearenemigos(imgEnemigo, listaEnemigos):
    for y in range(50):
        for x in range(4):
            if x == randint(0,3):
                cx = 115 + x * 170
                cy = -5030 + y * 100
                enemigo = pygame.sprite.Sprite()  # SPRITE
                enemigo.image = imgEnemigo
                enemigo.rect = imgEnemigo.get_rect()
                enemigo.rect.left = cx
                enemigo.rect.top = cy
                listaEnemigos.append(enemigo)

#Funcion que dibuja en pantalla los elementos en pantalla para poder jugar
def dibujarjuego(ventana, listaEnemigos, listaBalas, listaTesoros, listaVidas, imgCorazon):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
    for balas in listaBalas:
        ventana.blit(balas.image, balas.rect)
    for tesoro in listaTesoros:
        ventana.blit(tesoro.image, tesoro.rect)
    for vida in listaVidas:
        ventana.blit(imgCorazon,(10 + 50*vida,10))

#Funcion que actualiza las colisiones y las listas de juego
def actualizarlistas(listaEnemigos, listaBalas, listaTesoro,listaVidas,sonidogolpe, sonidorobo):
    for enemigo in listaEnemigos:
        enemigo.rect.top -= -2
    for bala in listaBalas:
        bala.rect.top -= 20
    #Eliminar balas fuera de la pantalla
    for i in range (-1, -len(listaBalas), -1):
        if listaBalas[i].rect.top <= -listaBalas[i].rect.height:
            listaBalas.remove(listaBalas[i])
    #Verificar colisiones bala/enemigo
    for bala in listaBalas:
        borrarBala = False
        for l in range(-1,-len(listaEnemigos)-1,-1):
            if bala.rect.colliderect(listaEnemigos[l]):
                sonidogolpe.play()
                global puntaje
                puntaje = str(int(puntaje)+50)
                listaEnemigos.remove(listaEnemigos[l])
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)
    #Verificar colisiones enemigo/tesoro
    for tesoro in listaTesoro:
        for j in range(-1,-len(listaEnemigos)-1,-1):
            if tesoro.rect.colliderect(listaEnemigos[j]):
                sonidorobo.play()
                if len(listaVidas)>0:
                    listaVidas.pop()
                listaEnemigos.remove(listaEnemigos[j])
                break

#Funcion que actualiza los textos del juego como el puntaje
def actualizartextos(ventana, puntaje):
    fuente = pygame.font.Font(None, 30)
    texto1 = fuente.render(("Puntaje: %s" % puntaje),1, (255, 255, 255))
    ventana.blit(texto1,(650,20))

#Funcion que cambia el estado del juego si el jugador pierde o gana
def actalizarestado(listaVidas, listaEnemigos,sonidoganar,sonidoperder):
    if len(listaVidas)== 0:
        sonidoperder.play()
        estado = "perder"
        return estado
    elif len(listaEnemigos) == 0:
        sonidoganar.play()
        estado = "ganar"
        return estado
    else:
        return "jugando"

#Funcion que pide las intrucciones de un txt y las pone en pantalla
def imprimirinstrucciones(ventana):
    instrucciones = open("instrucciones.txt","r",encoding="UTF-8")
    lineas = instrucciones.readlines()
    fuente = pygame.font.Font(None, 40)
    contador = 0
    for linea in lineas:
        contador+=1
        texto = fuente.render(linea, 1, (255, 255, 255))
        ventana.blit(texto, (200, 50+contador * 50))

#Funcion que compara la spuntuaciones con el dicionario de tabla de puntuacion
def revisartablapuntuaciones(tablaPuntuaciones, puntaje):
    puntaje2 = "00"
    global contadorpuntaje
    for llave in tablaPuntuaciones:
        if contadorpuntaje < 11:
            if int(puntaje) >= int(tablaPuntuaciones[llave]):
                puntaje2 = str(int(tablaPuntuaciones[llave]))
                tablaPuntuaciones[llave] = puntaje
                puntaje = puntaje2
            contadorpuntaje += 1
        else:
            pass

#Funcion que escribe las punttuaciones en la tabla de puntuaciones
def escribirpuntuaciones(tablaPuntuaciones, ventana):
    fuente = pygame.font.Font(None, 40)
    textoencabezado = fuente.render("Lugar        Puntaje", 1, (255, 255, 255))
    ventana.blit(textoencabezado, (280, 80))
    fuente = pygame.font.Font(None, 35)
    for renglon in range(1,11,1):
        textoencabezado = fuente.render("  %d..................%s" % (renglon,tablaPuntuaciones[renglon]), 1, (255, 255, 255))
        ventana.blit(textoencabezado, (300, 100 + renglon*35))

#Funcion que dibuja el juego y regula sus estados
def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Estado
    estado = "menu"

    # Botones
    imgBotonJugar = pygame.image.load("botonjugar.png")
    btnJugar = pygame.sprite.Sprite()  # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height

    imgBotonPuntaje = pygame.image.load("botonpuntajes.png")
    btnPuntajes = pygame.sprite.Sprite()  # SPRITE
    btnPuntajes.image = imgBotonPuntaje
    btnPuntajes.rect = imgBotonPuntaje.get_rect()
    btnPuntajes.rect.left = ANCHO // 2 - btnPuntajes.rect.width // 2
    btnPuntajes.rect.top = ALTO // 2 + btnPuntajes.rect.height // 2

    imgBotonAyuda = pygame.image.load("btnAyuda.png")
    btnAyuda = pygame.sprite.Sprite()  # SPRITE
    btnAyuda.image = imgBotonAyuda
    btnAyuda.rect = imgBotonAyuda.get_rect()
    btnAyuda.rect.left = 740
    btnAyuda.rect.top = 540

    imgBotonVolver= pygame.image.load("btnVolver.png")
    btnVolver = pygame.sprite.Sprite()  # SPRITE
    btnVolver.image = imgBotonVolver
    btnVolver.rect = imgBotonVolver.get_rect()
    btnVolver.rect.left = 10
    btnVolver.rect.top = 10


    # Objetos
    imgPersonaje = pygame.image.load("defensor.png")
    imgEnemigo = pygame.image.load("enemigo.png")
    imgTesoro = pygame.image.load("tesoro.png")
    imgBala = pygame.image.load("balafuego.png")
    imgCorazon = pygame.image.load("corazon.png")

    # Enemigos
    listaEnemigos = []
    crearenemigos(imgEnemigo, listaEnemigos)

    # Balas
    listaBalas = []

    #Tesoros
    listaTesoros = []

    #Vidas
    listaVidas = [1,2,3]

    #Condiciones del personaje
    posxpersonaje = 380

    #Sonidos
    pygame.mixer.music.load("Reverse - Parallel Universe.mp3")
    pygame.mixer.music.play(-1)
    sonidobala = pygame.mixer.Sound("hechizo.wav")
    sonidogolpe = pygame.mixer.Sound("golpe.wav")
    sonidorobo = pygame.mixer.Sound("tesoro.wav")
    sonidoboton = pygame.mixer.Sound("boton.wav")
    sonidoganar = pygame.mixer.Sound("ganar.wav")
    sonidoperder = pygame.mixer.Sound("perder.wav")




    while not termina:
        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    xb2, yb2, anchoB2, altoB2 = btnPuntajes.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            sonidoboton.play()
                            estado = "jugando"
                    if xm >= xb2 and xm <= xb2 + anchoB2:
                        if ym >= yb2 and ym <= yb2 + altoB2:
                            sonidoboton.play()
                            estado = "tablapuntuaciones"

                if estado == "jugando":
                    xb, yb, anchoB, altoB = btnAyuda.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            sonidoboton.play()
                            estado = "ayuda"

                if estado == "ayuda":
                    xb, yb, anchoB, altoB = btnVolver.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            sonidoboton.play()
                            estado = "jugando"

                if estado == "perder" or estado == "ganar":
                    xb, yb, anchoB, altoB = btnVolver.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            sonidoboton.play()
                            global puntaje
                            puntaje = "00"
                            global contadorpuntaje
                            contadorpuntaje = 0
                            main()

                if estado == "tablapuntuaciones":
                    xb, yb, anchoB, altoB = btnVolver.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            sonidoboton.play()
                            estado = "menu"

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    sonidobala.play()
                    # crear bala
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = posxpersonaje
                    bala.rect.top = 470
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(AZULOBS)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            ventana.blit(FONDO, (0, 0))
            dibujarMenu(ventana, btnJugar, btnPuntajes)

        elif estado == "jugando":
            ventana.blit(FONDO2,(0,0))
            posxpersonaje = actualizarposicion(posxpersonaje)
            dibujarpersonaje(imgPersonaje, posxpersonaje, ventana)
            creartesoros(imgTesoro, listaTesoros)
            dibujarjuego(ventana, listaEnemigos, listaBalas,listaTesoros, listaVidas, imgCorazon)
            actualizarlistas(listaEnemigos, listaBalas,listaTesoros,listaVidas, sonidogolpe, sonidorobo)
            actualizartextos(ventana, puntaje)
            dibujarbotonAyuda(ventana, btnAyuda)
            estado = actalizarestado(listaVidas,listaEnemigos,sonidoganar,sonidoperder)

        elif estado == "perder":
            ventana.blit(FONDO3, (0,0))
            fuente2 = pygame.font.Font(None, 100)
            textoPerder = fuente2.render(("¡Has perdido!"), 1, (36,3,3))
            ventana.blit(textoPerder, (180, 200))
            fuente = pygame.font.Font(None, 30)
            texto1 = fuente.render(("Tu puntaje ha sido: %s" % puntaje), 1, (36,20,20))
            ventana.blit(texto1, (280,300))
            revisartablapuntuaciones(tablaPuntuaciones, puntaje)
            dibujarbotonVolver(ventana, btnVolver)

        elif estado == "ganar":
            ventana.blit(FONDO2, (0, 0))
            fuente2 = pygame.font.Font(None, 100)
            textoPerder = fuente2.render(("¡Has Ganado!"), 1, (32, 14 ,139))
            ventana.blit(textoPerder, (175, 200))
            fuente = pygame.font.Font(None, 30)
            texto1 = fuente.render(("Tu puntaje ha sido: %s" % puntaje), 1, (32, 14 ,139))
            ventana.blit(texto1, (280, 300))
            revisartablapuntuaciones(tablaPuntuaciones, puntaje)
            dibujarbotonVolver(ventana, btnVolver)

        elif estado == "ayuda":
            dibujarbotonVolver(ventana, btnVolver)
            ventana.blit(FONDO2, (0, 0))
            dibujarbotonVolver(ventana,btnVolver)
            imprimirinstrucciones(ventana)

        elif estado == "tablapuntuaciones":
            ventana.blit(FONDO2, (0, 0))
            escribirpuntuaciones(tablaPuntuaciones,ventana)
            dibujarbotonVolver(ventana, btnVolver)


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame

#Funcion que llama al juego 
def main():
    dibujar()


main()