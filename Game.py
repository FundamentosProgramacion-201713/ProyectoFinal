#Encoding: UTF-8
#Autor: Alberto López Reyes
#Descripción: Proyecto Final
#Comentario: Estoy decepcionado de mí mismo

import pygame
from random import randint
import sys

# Dimensiones de la pantalla
intAncho = 600
intAlto = 800
# Colores
rgbBlanco = (255,255,255)  # R,G,B en el rango [0,255]
rgbNegro = (0, 0, 0)
keyRegistro = 0
intVelocidadObstaculo = 10
#1:SmallParticle
strNivelMapa = """
1111   1111
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1         1
1111   1111"""
Tyrant = "Tyrant Ship.png"


def writeDataBaseFile(file, estado):
    global keyRegistro
    if estado == "nueva partida":
        strNivel = "nivel1"
        file = open("PartidaTyrantDummy.txt", "w")
        lstLineas = ["PARTIDA TYRANT\n", "Registro,"+str(keyRegistro)+"\n", "Estado,jugando\n", "Nivel,"+strNivel+"\n", "Vidas,3\n", "Puntaje,0\n", "Municion,None\n"]
        file.writelines(lstLineas)

def definirEstadoPartida(linea, estado):
    estado[linea[0]] = linea[1]

def obtenerRawLineaFile(file):                                  #Enlista las lineas de un archivo por número de línea
    fileFile = open(file, "r", encoding = 'UTF-8')
    lstLineas = []
    for strLinea in fileFile:
        lstLineas.append(strLinea)
    fileFile.close()
    return lstLineas

def obtenerRawDataLinea(linea):                                 #Enlista los datos separados por comas de una linea
    strLinea = linea.split("\n")
    strDataToken = strLinea[0].split(",")
    return strDataToken

def dibujarPantallaMenu(ventana, botonesMenu, estadoFondo, estadoTitulo, estado):
    imgFondo = pygame.image.load(estadoFondo[estado])
    fondo = pygame.sprite.Sprite()  # Sprite
    fondo.image = imgFondo
    fondo.rect = imgFondo.get_rect()
    fondo.rect.left = intAncho // 2 - fondo.rect.width // 2
    fondo.rect.top = intAlto // 2 - fondo.rect.height // 2
    ventana.blit(fondo.image, fondo.rect)
    imgShip = pygame.image.load("Tyrant Ship.png")
    Ship = pygame.sprite.Sprite()  # Sprite
    Ship.image = imgShip
    Ship.rect = imgShip.get_rect()
    Ship.rect.left = intAncho // 2 - Ship.rect.width // 2
    Ship.rect.top = intAlto // 2 + 290 - Ship.rect.height // 2
    ventana.blit(Ship.image, Ship.rect)
    for indexBoton in range(0, len(botonesMenu)):
        imgBoton = pygame.image.load(botonesMenu[indexBoton])
        boton = pygame.sprite.Sprite()                      # Sprite
        boton.image = imgBoton
        boton.rect = imgBoton.get_rect()
        boton.rect.left = intAncho//2 - boton.rect.width//2
        boton.rect.top = intAlto//2 - boton.rect.height//2 + 200 - 60 * indexBoton
        ventana.blit(boton.image, boton.rect)
    imgTitulo = pygame.image.load(estadoTitulo[estado])
    Titulo = pygame.sprite.Sprite()  # Sprite
    Titulo.image = imgTitulo
    Titulo.rect = imgTitulo.get_rect()
    Titulo.rect.left = intAncho // 2 - Titulo.rect.width // 2
    Titulo.rect.top = intAlto // 2 - 200 - Titulo.rect.height // 2
    ventana.blit(Titulo.image, Titulo.rect)

def ordenarCoordenadasCentralesImagen(imagen, xadicional, yadicional, xconstnate, yconstante):
    imgImagen = pygame.image.load(imagen)
    Imagen = pygame.sprite.Sprite()
    Imagen.image = imgImagen
    Imagen.rect = imgImagen.get_rect()
    Imagen.rect.left = intAncho // 2 - Imagen.rect.width // 2 * xconstnate + xadicional
    Imagen.rect.top = (intAlto // 2) - (Imagen.rect.height // 2) * yconstante + yadicional
    return Imagen.image, Imagen.rect

def ordenarCoordenadasArbitrariasImagen(imagen, xadicional, yadicional, xconstnate, yconstante, x, y):
    imgImagen = pygame.image.load(imagen)
    Imagen = pygame.sprite.Sprite()
    Imagen.image = imgImagen
    Imagen.rect = imgImagen.get_rect()
    Imagen.rect.left = x * xconstnate + xadicional - Imagen.rect.width // 2
    Imagen.rect.top = y * yconstante + yadicional - (Imagen.rect.height // 2)
    return Imagen.image, Imagen.rect


def dibujarPantallaJuego(jugador, ventana, estadoJugando, nivelFondo, nivelBarra, nombreTitulo, nombreObstaculo, nombreNaveEnemiga, nombreNave, tiempofuera):
    while estadoJugando == "nivel1" or estadoJugando == "nivel2":
        TyrantPropiedades = ordenarCoordenadasCentralesImagen("Tyrant Ship.png", 0, 1, 0, 1) #TyPr -> Nombre Nave
        print(TyrantPropiedades)
        ventana.blit(TyrantPropiedades)
        Jugador, intVelocidadJugador = ventana.blit(TyrantPropiedades[0], TyrantPropiedades[1]), 5

        while estadoJugando == "nivel1":
            intEscalaMapa = 1/50
            mapaObstaculos = strNivelMapa.split()[1:]
            xobstaculo, yobstaculo = 0, 0
            obstaculos = []

            imgFondo = pygame.image.load(nivelFondo[estadoJugando])
            fondo = pygame.sprite.Sprite()  # Sprite
            fondo.image = imgFondo
            fondo.rect = imgFondo.get_rect()
            fondo.rect.left = intAncho // 2 - fondo.rect.width // 2
            fondo.rect.top = intAlto // 2 - fondo.rect.height // 2
            ventana.blit(fondo.image, fondo.rect)

            imgBarra = pygame.image.load(nivelFondo[estadoJugando])
            barra = pygame.sprite.Sprite()  # Sprite
            barra.image = imgBarra
            barra.rect = imgBarra.get_rect()
            barra.rect.left = intAncho // 2 - barra.rect.width // 2
            barra.rect.top = intAlto // 2 - barra.rect.height // 2
            ventana.blit(barra.image, barra.rect)

            for linea in mapaObstaculos:
                for char in mapaObstaculos:
                    if char == "1":
                        TinyCrate = ordenarCoordenadasCentralesImagen(nombreObstaculo["Tiny"], 0, intEscalaMapa, 0, intEscalaMapa)
                        obstaculos.append(ventana.blit(TinyCrate[0], TinyCrate[1]))
                    if char == "2":
                        ""
                    yobstaculo = yobstaculo + 1
                xobstaculo, yobstaculo = xobstaculo + 1, 0


    '''
    imgShip = pygame.image.load("Tyrant Ship.png")
    Ship = pygame.sprite.Sprite()  # Sprite
    Ship.image = imgShip
    Ship.rect = imgShip.get_rect()
    Ship.rect.left = intAncho // 2 - Ship.rect.width // 2
    Ship.rect.top = intAlto // 2 + 290 - Ship.rect.height // 2
    ventana.blit(Ship.image, Ship.rect)

    for indexBoton in range(0, len(botonesMenu)):
        imgBoton = pygame.image.load(botonesMenu[indexBoton])
        boton = pygame.sprite.Sprite()                      # Sprite
        boton.image = imgBoton
        boton.rect = imgBoton.get_rect()
        boton.rect.left = intAncho//2 - boton.rect.width//2
        boton.rect.top = intAlto//2 - boton.rect.height//2 + 200 - 60 * indexBoton
        ventana.blit(boton.image, boton.rect)
    imgTitulo = pygame.image.load(estadoTitulo[estado])
    Titulo = pygame.sprite.Sprite()  # Sprite
    Titulo.image = imgTitulo
    Titulo.rect = imgTitulo.get_rect()
    Titulo.rect.left = intAncho // 2 - Titulo.rect.width // 2
    Titulo.rect.top = intAlto // 2 - 200 - Titulo.rect.height // 2
    ventana.blit(Titulo.image, Titulo.rect)
    '''

def dibujarPantallaPuntaje():
    """"""

def escogerBotonMenu(botonesMenu, botonesMenuEstado, xm, ym):
    for indexBoton in range(0, len(botonesMenu)):
        imagen = obtenerCoordenadasImagen(botonesMenu[indexBoton], botonesMenu, indexBoton)
        xb, yb, anchoB, altoB = imagen
        print(xb, yb, anchoB, altoB)
        if xm >= xb and xm <= xb + anchoB:
            if ym >= yb and ym <= yb + altoB:
                estado = botonesMenuEstado[botonesMenu[indexBoton]]
                print(estado)
                return estado
        else:
            return "None"

def obtenerCoordenadasImagen(imagen, imagenes, index):
    imgImagenBack = pygame.image.load(imagen)
    imgImagen = pygame.sprite.Sprite()
    imgImagen.image = imgImagenBack
    imgImagen.rect = imgImagenBack.get_rect()
    imgImagen.rect.left = intAncho // 2 - imgImagen.rect.width // 2
    imgImagen.rect.top = intAlto // 2 - imgImagen.rect.height // 2 + 200 - 60 * index
    return imgImagen.rect

def salir():
    sys.exit()

def dibujar():
    pygame.init()                                               # Inicializa pygame
    ventana = pygame.display.set_mode((intAncho, intAlto))      # Crea la ventana de dibujo
    reloj = pygame.time.Clock()                                 # Para limitar los fps
    termina = False                                             # Bandera para saber si termina la ejecución
                                                                # Estados:
    estado = "menu"                                             # Jugando, termina.
                                                                # Botones Menú
    tiempofuera = 0
    intEscalaMapa = 50

    estadoPartida = {}
    definirEstadoPartida(obtenerRawDataLinea(
        obtenerRawLineaFile("PartidaTyrant.txt")[2]), estadoPartida)
    print(estadoPartida)
    lstBotonesMenu = ["button_salir.png", "button_sobre-el-juego.png", "button_puntaje.png",
                      "button_nueva-partida.png", "button_continuar.png"]
    lstEstadosMenuBotonContinuar = ["continuar", "continuar inactive"]
    if estadoPartida["Estado"] == "None":
        lstBotonesMenu[4] = "button_continuar_inactive.png"
        lstEstadosMenuBotonContinuar.reverse()
    dicBotonesMenuEstado = {lstBotonesMenu[0]:"salir", lstBotonesMenu[1]:"sobre el juego", lstBotonesMenu[2]:"puntaje",
                        lstBotonesMenu[3]:"nueva partida", lstBotonesMenu[4]:lstEstadosMenuBotonContinuar[0]}
    timer = 0
    lstFondosPantalla = ["Tyrant Arena Floor.jpg", "Tyrant Arena Floor 2.jpg"]
    dicEstadoFondo = {"menu":"Tyrant Arena Floor.jpg"}
    lstTitulos = ["title_tyrant.png"]
    dicEstadoTitulo = {"menu":"title_tyrant.png"}
    lstObstaculos = ["Tyrant Crate Tiny.jpg", "Tyrant Crate Small.jpg", "Tyrant Crate Medium Particle.jpg"
                     , "Tyrant Crate Medium Barrier Vertical.png", "Tyrant Crate Medium Barrier Horizontal.png",
                     "Tyrant Crate Big Particle.jpg", "Tyrant Crate Big Barrier Vertical.png", "Tyrant Crate Big Barrier Horizontal.png"]
    dicNombreObstaculo = {"Tiny":"Tyrant Crate Tiny.jpg", "Small":"Tyrant Crate Small.jpg", "MediumParticle":"Tyrant Crate Medium Particle.jpg"
                     ,"MediumBarrierVertical":"Tyrant Crate Medium Barrier Vertical.png", "MediumBarrierHorizontal":"Tyrant Crate Medium Barrier Horizontal.png",
                     "BigParticle":"Tyrant Crate Big Particle.jpg", "BigBarrierVertical":"Tyrant Crate Big Barrier Vertical.png", "BigBarrierHorizontal":"Tyrant Crate Big Barrier Horizontal.png"}
    dicNivelBarra = {"nivel1":"Barra Nivel 1.png", "nivel2":"Barra Nivel 2.png"}
    dicNombreNaveEnemiga = {}
    dicNombreImgTitulosJuego = {}
    dicNivelFondo = {"nivel1":"Tyrant Arena Floor.jpg", "nivel2":"Tyrant Arena Floor 2.jpg"}

    mapaObstaculos = strNivelMapa.split()[1:]
    xobstaculo, yobstaculo = 0, 0
    lstObstaculos = []
    TyrantPropiedades = ordenarCoordenadasCentralesImagen("Tyrant Ship.png", 0, 1, 0, 1)
    Jugador, intVelocidadJugador = ventana.blit(TyrantPropiedades[0], TyrantPropiedades[1]), 10
    for linea in mapaObstaculos:
        for char in linea:
            if char == "1":
                TinyCrate = ordenarCoordenadasArbitrariasImagen(dicNombreObstaculo["Tiny"], 0,
                                                                intEscalaMapa, 0, intEscalaMapa, xobstaculo,
                                                                yobstaculo)
                lstObstaculos.append(TinyCrate)
            if char == "2":
                ""
            yobstaculo = yobstaculo - 1
        xobstaculo, yobstaculo = xobstaculo - 1, 0

    while not termina:                                          # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:                      # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                print(xm)
                print(ym)
                if estado == "menu":
                    print(estado)
                    print(pygame.mouse.get_pressed())
                    estado = escogerBotonMenu(lstBotonesMenu, dicBotonesMenuEstado, xm, ym)
                if estado == "nueva partida":
                    estado = "jugando"
                    estadoJugando = "nivel1"
                    print(estado)
                    if estado == "jugando":
                        TyrantPropiedades = ordenarCoordenadasCentralesImagen("Tyrant Ship.png", 0, 1, 0,
                                                                              1)
                        print("TyrantPropiedades", TyrantPropiedades)
                        if estadoJugando == "nivel1":
                            """"""

        if estado == "menu":
            print(estado)
            dibujarPantallaMenu(ventana, lstBotonesMenu, dicEstadoFondo, dicEstadoTitulo, estado)
        elif estado == "salir":
            print(estado)
            salir()
        elif estado == "sobre el juego":
            print(estado)
            ventana.fill(rgbNegro)
            """"""
        elif estado == "puntaje":
            print(estado)
            ventana.fill(rgbNegro)
            """"""
        elif estado == "jugando":
            print(estado)
            if estadoJugando == "nivel1":

                imgFondo = pygame.image.load(dicNivelFondo[estadoJugando])              #Optimizar
                fondo = pygame.sprite.Sprite()  # Sprite
                fondo.image = imgFondo
                fondo.rect = imgFondo.get_rect()
                fondo.rect.left = intAncho // 2 - fondo.rect.width // 2
                fondo.rect.top = intAlto // 2 - fondo.rect.height // 2
                ventana.blit(fondo.image, fondo.rect)

                imgBarra = pygame.image.load(dicNivelFondo[estadoJugando])
                barra = pygame.sprite.Sprite()  # Sprite
                barra.image = imgBarra
                barra.rect = imgBarra.get_rect()
                barra.rect.left = intAncho // 2 - barra.rect.width // 2
                barra.rect.top = intAlto // 2 - barra.rect.height // 2
                ventana.blit(barra.image, barra.rect)

                if tiempofuera:
                    print(tiempofuera)
                    tiempofuera = tiempofuera - 1
                else:
                    teclaPresionada = pygame.key.get_pressed()
                    print(teclaPresionada)
                    if teclaPresionada[pygame.K_UP]: Jugador.move_ip(-intVelocidadJugador, 0)
                    if teclaPresionada[pygame.K_DOWN]: Jugador.move_ip(intVelocidadJugador, 0)
                    if teclaPresionada[pygame.K_LEFT]: Jugador.move_ip(0, -intVelocidadJugador)
                    if teclaPresionada[pygame.K_RIGHT]: Jugador.move_ip(0, intVelocidadJugador)

                for obstaculo in lstObstaculos:
                    obstaculo[1].move_ip(0, intVelocidadObstaculo)
                    if obstaculo[1].colliderect(Jugador) and not tiempofuera:
                        tiempofuera = 100
                    """
                    if obstaculo[1].top > 50:
                        lstObstaculos.remove(obstaculo)
                        """

                for obstaculo in lstObstaculos:
                    print("Obstaculo:", obstaculo)
                    ventana.blit(obstaculo[0], obstaculo[1])


                if tiempofuera == False:
                    print(Jugador)
                    ventana.blit(TyrantPropiedades[0], TyrantPropiedades[1])

            """
            keyRegistro = keyRegistro + 1
            """

        elif estado == "continuar":
            ventana.fill(rgbNegro)
            """"""
        elif estado == "continuar inactive":
            dibujar()
            """
        elif estado == "jugando":
            actualizarBalas(listaBalas, listaEnemigos )
            dibujarJuego(ventana, btnJugar, listaEnemigos, listaBalas)
            """


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()

main()

"""
writeDataBaseFile("file")
print(obtenerRawLineaFile("PartidaTyrant.txt"))
"""