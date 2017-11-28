# encoding: UTF-8
# Autor: Luis Miguel Baqueiro Vallejo
# Proyecto final

import pygame, math

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS = (87, 87, 87)
FONDO = (45, 10, 64)
SUELO = (16, 82, 13)

ANCHO = 800
ALTO = 600
camina = 0
cie = True
instancia = 1
jugadorx = 0
jugadory = 0
primer = [0]
sal = [0]
JUGAR = 0
SALIR = 0
PERSONAJE = 0
REGRESAR = 0
AUMENTO = 0
GUARDAR = 0
nivel = 0
pestana = 0
camina = 800
cierras = []
cier = []
cierrasinicial = []
numcierrs = 0
bouserderecha = False
draw = 1
imagennombre = "NES_Caminar_1.png"
imsaltar = "NES_Saltar.png"
DERECHA = True
IZQUIERDA = True
CREAR = 0
ABAJO = True
ARRIBA = True
saltar = 0
saltando = False
salto = 0
variable = 0
bajando = False
vida = 3
a = True
b = True
c = True
suelo = False
v = False
w = True
tamanoxjugador = 12
tamanoyjugador = 16
numcierras = 0
ciera = 0
mover = 0
move = 0
muve = 0
colocando = False
juegoguardado = 0
crearcierras = []
seleccionardireccion = False
cierrax, cierray, cierraxf, cierrayf = (0, 0, 0, 0)
preguntar = 0
velocidad = 1
CONFIRMAR = False
CANCELAR = False
rotar = 0
colocarmeta = False
meta = False
colocarcierra = False
crearmeta = []
inici = []
iniciar = False
colocarmario = False
eliminando = False
eliminar = False
crearpiso = []
crearpinchos = []
SUELO = False
colocarsuelo = False
suelox = -1
sueloy = -1
sueloxf = 0
sueloyf = 0
colocarpincho = False
PINCHO = False
parpadea = 0
vidap = True
elimina = 0
error = 0
pausa = False
paso = 0
camino1 = "NES_Caminar_2.png"
camino2 = "NES_Caminar_3.png"
animacion = 0
caminar = False


def instancias(JUGAR, SALIR, PERSONAJE, REGRESAR, AUMENTO, pestana, draw):
    if instancia == 1:
        play(JUGAR, SALIR, PERSONAJE)
    if instancia == 2:
        jugar(REGRESAR, AUMENTO)
    if instancia == 3:
        personajes(REGRESAR, pestana, draw)
    if instancia == 4:
        mundos()
    if instancia == 5:
        crearmundo()
    if instancia == 6:
        jugarmundocreado()
    if pausa and (instancia == 4 or instancia == 6):
        pause()


def pause():
    pygame.draw.rect(ventana, NEGRO, (100, 100, 600, 400))
    pygame.draw.rect(ventana, ROJO, (650, 100, 50, 50))
    fuente = pygame.font.Font(None, 70)
    texto = fuente.render("X", 1, BLANCO)
    ventana.blit(texto, (655, 105))
    pygame.draw.rect(ventana, BLANCO, (120, 210, 560, 180), 1)
    fuente = pygame.font.Font(None, 270)
    texto = fuente.render("SALIR", 1, BLANCO)
    ventana.blit(texto, (125, 215))


def play(JUGAR, SALIR, PERSONAJE):
    ventana.fill(FONDO)
    pygame.draw.rect(ventana, BLANCO, (210, 190, 380, 110), 1)
    fuente = pygame.font.Font(None, 150 - JUGAR)
    texto = fuente.render("JUGAR", 1, BLANCO)
    ventana.blit(texto, (220 + JUGAR, 200 + (JUGAR // 2)))
    pygame.draw.rect(ventana, BLANCO, (240, 320, 320, 110), 1)
    fuente = pygame.font.Font(None, 150 - SALIR)
    texto = fuente.render("SALIR", 1, BLANCO)
    ventana.blit(texto, (250 + SALIR, 330 + (SALIR // 2)))
    pygame.draw.rect(ventana, BLANCO, (70, 460, 660, 110), 1)
    fuente = pygame.font.Font(None, 150 - PERSONAJE)
    texto = fuente.render("PERSONAJE", 1, BLANCO)
    ventana.blit(texto, (75 + (PERSONAJE * 2), 470 + (PERSONAJE // 2)))


def jugar(REGRESAR, AUMENTO):
    mundo.seek(0)
    ventana.fill(FONDO)
    fuente = pygame.font.Font(None, 150)
    texto = fuente.render("NIVELES", 1, BLANCO)
    ventana.blit(texto, (150, 10))
    pygame.draw.rect(ventana, BLANCO, (395, 495, 395, 70), 1)
    fuente = pygame.font.Font(None, 100 - REGRESAR)
    texto = fuente.render("REGRESAR", 1, BLANCO)
    ventana.blit(texto, (400 + REGRESAR, 500 + (REGRESAR // 2)))
    pygame.draw.rect(ventana, BLANCO, (10, 495, 255, 70), 1)
    fuente = pygame.font.Font(None, 100 - CREAR)
    texto = fuente.render("CREAR", 1, BLANCO)
    ventana.blit(texto, (15 + CREAR, 500 + (CREAR // 2)))
    for linea in mundo:
        imagen = pygame.image.load("fondo.png")
        cadena = linea.split()
        cuadrox = int(cadena[0])
        cuadroy = int(cadena[1])
        cuadroancho = 122
        numerocuadro = cadena[2]
        valor = int(cadena[3])
        pygame.draw.rect(ventana, BLANCO, (cuadrox, cuadroy, cuadroancho, cuadroancho), 1)
        if valor == 1:
            ventana.blit(imagen, (cuadrox + 1, cuadroy + 1))
            fuente = pygame.font.Font(None, 100 + AUMENTO)
            texto = fuente.render(numerocuadro, 1, BLANCO)
            ventana.blit(texto, (cuadrox + 10, cuadroy + 10))
        elif valor == 0:
            pygame.draw.rect(ventana, GRIS, (cuadrox + 1, cuadroy + 1, cuadroancho - 2, cuadroancho - 2))


def personajes(REGRESAR, pestana, draw):
    ventana.fill(FONDO)
    eleccion = draw - pestana
    if eleccion == 1:
        pygame.draw.rect(ventana, ROJO, (71, 151, 208, 298))
    elif eleccion == 2:
        pygame.draw.rect(ventana, ROJO, (291, 151, 208, 298))
    elif eleccion == 3:
        pygame.draw.rect(ventana, ROJO, (511, 151, 208, 298))
    pygame.draw.rect(ventana, BLANCO, (395, 495, 395, 70), 1)
    fuente = pygame.font.Font(None, 100 - REGRESAR)
    texto = fuente.render("REGRESAR", 1, BLANCO)
    ventana.blit(texto, (400 + REGRESAR, 500 + (REGRESAR // 2)))
    fuente = pygame.font.Font(None, 150)
    texto = fuente.render("PERSONAJES", 1, BLANCO)
    ventana.blit(texto, (50, 10))
    if 1 <= pestana <= 2:
        pygame.draw.rect(ventana, BLANCO, (10, 300, 50, 50), 1)
        pygame.draw.polygon(ventana, BLANCO, ((55, 305), (55, 345), (15, 325)))
    if 0 <= pestana <= 1:
        pygame.draw.rect(ventana, BLANCO, (740, 300, 50, 50), 1)
        pygame.draw.polygon(ventana, BLANCO, ((745, 305), (745, 345), (785, 325)))
    personaje.seek(0)
    for i in range(0, pestana):
        personaje.readline()
    for linea in personaje:
        cadena = linea.split()
        cuadrox = int(cadena[0]) - (pestana * 220)
        cuadroy = 150
        cuadroancho = 210
        cuadroalto = 300
        nombre = cadena[1]
        existencia = int(cadena[2])
        imagennombre = cadena[3]
        imagen = pygame.image.load(imagennombre)
        valor = int(cadena[4]) - pestana
        if valor <= 3:
            pygame.draw.rect(ventana, BLANCO, (cuadrox, cuadroy, cuadroancho, cuadroalto), 1)
            if existencia == 1:
                fuente = pygame.font.Font(None, 35)
                texto = fuente.render(nombre, 2, BLANCO)
                ventana.blit(texto, (cuadrox + 10, cuadroy + 10))
                ventana.blit(imagen, (cuadrox + 18, cuadroy + 50))
            else:
                pygame.draw.rect(ventana, GRIS, (cuadrox + 1, cuadroy + 1, cuadroancho - 2, cuadroalto - 2))


def mundos():
    global camina, bouserderecha, numcierrs, ciera, parpadea, vidap
    ventana.fill(NEGRO)
    fondo = pygame.image.load("lab.jpg")
    ventana.blit(fondo, (170, 150))
    if camina <= 0:
        bouserderecha = True
    if camina >= ANCHO - 200:
        bouserderecha = False
    if bouserderecha:
        camina += 2
        bouser = pygame.image.load("bouserd.png")
        ventana.blit(bouser, (camina, 250))
    else:
        camina -= 2
        bouser = pygame.image.load("bouser.png")
        ventana.blit(bouser, (camina, 250))
    fondo = pygame.image.load("fondo-mundo.png")
    ventana.blit(fondo, (0, 0))
    if parpadea <= 0:
        vidap = True
    if parpadea >= 20:
        vidap = False
    if vidap:
        parpadea += 2
        corazon = pygame.image.load("vida.png")
    else:
        parpadea -= 2
        corazon = pygame.image.load("vida2.png")
    for i in range(0, vida):
        x = 10 + (i * 22)
        ventana.blit(corazon, (x, 10))
    lvl.seek(0)
    caracteres = lvl.readline()
    h = caracteres.split()
    lvl.seek(0)
    for i in range(0, int(h[nivel - 1])):
        lvl.readline()
    for linea in lvl:
        cadena = linea.split()
        if cadena[0] != "stop":
            if cadena[0] == "p": #Pinchos
                x = int(cadena[1]) # De 0 a 800
                y = int(cadena[2]) # De 0 a 600
                ancho = int(cadena[3]) - x # De 0 a 800
                alto = int(cadena[4]) - y # De 0 a 600
                pygame.draw.rect(ventana, ROJO, (x, y, ancho, alto))
            if cadena[0] == "f": # Piso
                x = int(cadena[1]) # De 0 a 800
                y = int(cadena[2]) # De 0 a 600
                ancho = int(cadena[3]) - x # De 0 a 800
                alto = int(cadena[4]) - y # De 0 a 600
                pygame.draw.rect(ventana, VERDE_BANDERA, (x, y, ancho, alto))
            if cadena[0] == "c" and cie: #cierra
                numcierrs += 1
                x = int(cadena[1])  # De 0 a 800
                y = int(cadena[2])  # De 0 a 600
                xf = int(cadena[3]) # De 0 a 800
                yf = int(cadena[4]) # De 0 a 800
                velocidad = int(cadena[5]) # De 1 a 100
                if x - xf != 0 and y - yf != 0:
                    vx = int(math.fabs(x - xf) / (((((x - xf) ** 2) + ((y - yf) ** 2)) ** (1 / 2)) / velocidad))
                    vy = int(math.fabs(y - yf) / (((((x - xf) ** 2) + ((y - yf) ** 2)) ** (1 / 2)) / velocidad))
                else:
                    vx = 0
                    vy = 0
                    if x - xf == 0:
                        vy = velocidad
                    if y - yf == 0:
                        vx = velocidad
                cierras.append([x, y, xf, yf, vx, vy])
                cier.append(numcierrs)
            if cadena[0] == "e":
                print("enemigo")
            if cadena[0] == "i": #inicio
                posxjugador = int(cadena[1])
                posyjugador = int(cadena[2])
                mario(posxjugador, posyjugador)
            if cadena[0] == "m": #meta
                posxmeta = int(cadena[1])
                posymeta = int(cadena[2])
                meta = pygame.image.load("meta.png")
                ventana.blit(meta, (posxmeta, posymeta))
        else:
            break
    cierra(numcierrs)


def jugarmundocreado():
    global camina, bouserderecha, numcierrs, ciera, parpadea, vidap, instancia
    ventana.fill(NEGRO)
    fondo = pygame.image.load("lab.jpg")
    ventana.blit(fondo, (170, 150))
    if camina <= 0:
        bouserderecha = True
    if camina >= ANCHO - 200:
        bouserderecha = False
    if bouserderecha:
        camina += 2
        bouser = pygame.image.load("bouserd.png")
        ventana.blit(bouser, (camina, 250))
    else:
        camina -= 2
        bouser = pygame.image.load("bouser.png")
        ventana.blit(bouser, (camina, 250))
    fondo = pygame.image.load("fondo-mundo.png")
    ventana.blit(fondo, (0, 0))
    if parpadea <= 0:
        vidap = True
    if parpadea >= 20:
        vidap = False
    if vidap:
        parpadea += 2
        corazon = pygame.image.load("vida.png")
    else:
        parpadea -= 2
        corazon = pygame.image.load("vida2.png")
    for i in range(0, vida):
        x = 10 + (i * 22)
        ventana.blit(corazon, (x, 10))
    jugarmundo.seek(0)
    for linea in jugarmundo:
        cadena = linea.split()
        if cadena[0] == "p": #Pinchos
            x = int(cadena[1]) # De 0 a 800
            y = int(cadena[2]) # De 0 a 600
            ancho = int(cadena[3]) - x # De 0 a 800
            alto = int(cadena[4]) - y # De 0 a 600
            pygame.draw.rect(ventana, ROJO, (x, y, ancho, alto))
        if cadena[0] == "f": # Piso
            x = int(cadena[1]) # De 0 a 800
            y = int(cadena[2]) # De 0 a 600
            ancho = int(cadena[3]) - x # De 0 a 800
            alto = int(cadena[4]) - y # De 0 a 600
            pygame.draw.rect(ventana, VERDE_BANDERA, (x, y, ancho, alto))
        if cadena[0] == "c" and cie: #cierra
            numcierrs += 1
            x = int(cadena[1])  # De 0 a 800
            y = int(cadena[2])  # De 0 a 600
            xf = int(cadena[3]) # De 0 a 800
            yf = int(cadena[4]) # De 0 a 800
            velocidad = int(cadena[5]) # De 1 a 100
            if x - xf != 0 and y - yf != 0:
                vx = int(math.fabs(x - xf) / (((((x - xf) ** 2) + ((y - yf) ** 2)) ** (1 / 2)) / velocidad))
                vy = int(math.fabs(y - yf) / (((((x - xf) ** 2) + ((y - yf) ** 2)) ** (1 / 2)) / velocidad))
            else:
                vx = 0
                vy = 0
                if x - xf == 0:
                    vy = velocidad
                if y - yf == 0:
                    vx = velocidad
            cierras.append([x, y, xf, yf, vx, vy])
            cier.append(numcierrs)
        if cadena[0] == "e":
            print("enemigo")
        if cadena[0] == "i": #inicio
            posxjugador = int(cadena[1])
            posyjugador = int(cadena[2])
            mario(posxjugador, posyjugador)
        if cadena[0] == "m": #meta
            posxmeta = int(cadena[1])
            posymeta = int(cadena[2])
            meta = pygame.image.load("meta.png")
            ventana.blit(meta, (posxmeta, posymeta))
    cierra(numcierrs)


def cierra(numcierras):
    global cie, ciera
    cie = False
    for d in range(0, numcierras):
        datos = cierras[d]
        if len(cier) > 0 and d == ciera:
            x = datos[0]
            y = datos[1]
            xf = datos[2]
            yf = datos[3]
            if x > xf:
                sentidox = "izq"
            elif x < xf:
                sentidox = "der"
            else:
                sentidox = "non"
            if y > yf:
                sentidoy = "ar"
            elif y < yf:
                sentidoy = "ab"
            else:
                sentidoy = "non"
            cierrasinicial.append([x, y, sentidox, sentidoy])
            cier.remove(cier[0])
            ciera += 1
        inicio = cierrasinicial[d]
        cposx = inicio[0]
        cposy = inicio[1]
        x = datos[0]
        y = datos[1]
        xf = datos[2]
        yf = datos[3]
        vx = datos[4]
        vy = datos[5]
        if inicio[2] == "non":
            vx = 0
        if inicio[3] == "non":
            vy = 0
        if inicio[2] == "izq":
            if not pausa:
                cposx -= vx
            if xf < x:
                if cposx < xf:
                    inicio[2] = "der"
            elif xf > x:
                if cposx < x:
                    inicio[2] = "der"
        elif inicio[2] == "der":
            if not pausa:
                cposx += vx
            if xf < x:
                if cposx > x:
                    inicio[2] = "izq"
            elif xf > x:
                if cposx > xf:
                    inicio[2] = "izq"
        if inicio[3] == "ab":
            if not pausa:
                cposy += vy
            if yf < y:
                if cposy > y:
                    inicio[3] = "ar"
            if yf > y:
                if cposy > yf:
                    inicio[3] = "ar"
        elif inicio[3] == "ar":
            if not pausa:
                cposy -= vy
            if yf < y:
                if cposy < yf:
                    inicio[3] = "ab"
            if yf > y:
                if cposy < y:
                    inicio[3] = "ab"
        c = pygame.image.load("cierra.png")
        inicio[0] = cposx
        inicio[1] = cposy
        cierrasinicial[d] = inicio
        ventana.blit(c, (cposx, cposy))


def mario(iniciox, inicioy):
    global DERECHA, IZQUIERDA, ARRIBA, ABAJO, saltar, vida, instancia, suelo, imagennombre, imsaltar, camino0, camino1, camino2, animacion, caminar
    if len(primer) == 1:
        global jugadorx, jugadory
        jugadorx = iniciox
        jugadory = inicioy
        ABAJO = True
        primer.clear()
        if imagennombre == "NES_Caminar_1.png":
            imsaltar = "NES_Saltar.png"
            camino0 = "NES_Caminar_1.png"
            camino1 = "NES_Caminar_2.png"
            camino2 = "NES_Caminar_3.png"
        elif imagennombre == "MARIO3_Caminar_1.png":
            imsaltar = "MARIO3_Saltar.png"
            camino0 = "MARIO3_Caminar_1.png"
            camino1 = "MARIO3_Caminar_2.png"
            camino2 = "MARIO3_Caminar_3.png"
        elif imagennombre == "SUPER_Caminar_1.png":
            imsaltar = "SUPER_Caminar_1.png"
            camino0 = "SUPER_Caminar_1.png"
            camino1 = "SUPER_Caminar_1.png"
            camino2 = "SUPER_Caminar_1.png"
    if jugadorx <= 0:
        IZQUIERDA = False
        jugadorx = 0
    else:
        DERECHA = True
    if jugadorx >= 800 - tamanoxjugador:
        DERECHA = False
        jugadorx = 800 - tamanoxjugador
    else:
        DERECHA = True
    if jugadory >= 584:
        vida -= 1
        ABAJO = True
        jugadorx = iniciox
        jugadory = inicioy
    if jugadory <= 0:
        ARRIBA = False
        jugadory = 0
    else:
        ARRIBA = True
    if ABAJO and not pausa:
        jugadory += 5
        ARRIBA = False
    if saltar == 1:
        global saltando, salto, variable, bajando, v
        if len(sal) == 1:
            salto = 0
            saltando = True
            ABAJO = False
            variable = jugadory
            sal.clear()
            v = True
            bajando = False
        if not pausa:
            if not ARRIBA:
                saltando = False
                bajando = True
            if saltando:
                salto -= 5
            if salto <= -50:
                saltando = False
                bajando = True
            if bajando:
                ABAJO = True
                sal.append(0)
                saltar = 0
            jugadory = variable + salto
            if not bajando:
                m = pygame.image.load(imsaltar)
                ventana.blit(m, (jugadorx, jugadory))
    else:
        if not suelo:
            ABAJO = True
    if vida <= 0:
        instancia = 2
        vida = 3
    if animacion <= 0:
        imagennombre = camino0
        if caminar:
            animacion -= 2
    elif animacion <= 10:
        imagennombre = camino1
        if caminar:
            animacion -= 2
    elif animacion <= 15:
        imagennombre = camino2
        if caminar:
            animacion -= 2
    if animacion <= -5:
        if caminar:
            animacion = 15
    if not caminar:
        animacion = 0
    m = pygame.image.load(imagennombre)
    if saltar != 1:
        ventana.blit(m, (jugadorx, jugadory))
    if caminar:
        caminar = False


def crearmundo():
    global ventana, juegoguardado, error
    ventana.fill(NEGRO)
    fondo = pygame.image.load("lab.jpg")
    ventana.blit(fondo, (170, 150))
    fondo = pygame.image.load("fondo-mundo.png")
    ventana.blit(fondo, (0, 0))
    for i in range(0, len(crearpinchos)):
        lista = crearpinchos[i]
        pygame.draw.rect(ventana, ROJO, (lista[0], lista[1], lista[2] - lista[0], lista[3] - lista[1]))
    for i in range(0, len(crearpiso)):
        lista = crearpiso[i]
        pygame.draw.rect(ventana, VERDE_BANDERA, (lista[0], lista[1], lista[2] - lista[0], lista[3] - lista[1]))
    for i in range(0, len(crearcierras)):
        cierra = crearcierras[i]
        c = pygame.image.load("cierra.png")
        ventana.blit(c, (cierra[0], cierra[1]))
        pygame.draw.line(ventana, BLANCO, (cierra[0] + 25, cierra[1] + 25), (cierra[2] + 25, cierra[3] + 25))
    if meta:
        m = pygame.image.load("meta.png")
        w = crearmeta[0]
        ventana.blit(m, (w[0], w[1]))
    if iniciar:
        m = pygame.image.load("NES_Caminar_1.png")
        g = inici[0]
        ventana.blit(m, (g[0], g[1]))
    if not colocando:
        pygame.draw.rect(ventana, BLANCO, (375, 540 - mover, 50, 50))
        pygame.draw.polygon(ventana, NEGRO, ((380 + move, 585 + muve - move - (mover * 1.2)), (420 - move, 585 - move + muve - (mover * 1.2)), (400, 545 - (mover * 0.8) + move - muve)))
        pygame.draw.rect(ventana, VERDE_BANDERA, (0, 600 - mover, 800, 200))
        pygame.draw.rect(ventana, GRIS, (0, 600 - mover, 800, 200), 5)
        pygame.draw.rect(ventana, GRIS, (740, 615 - mover, 50, 50), 1)
        pygame.draw.rect(ventana, GRIS, (740, 675 - mover, 50, 50), 1)
        pygame.draw.rect(ventana, GRIS, (660, 735 - mover, 130, 50), 1)
        if JUGAR == 1:
            pygame.draw.rect(ventana, ROJO, (741, 616 - mover, 48, 48))
        if GUARDAR == 1:
            pygame.draw.rect(ventana, ROJO, (741, 676 - mover, 48, 48))
        if SALIR == 1:
            pygame.draw.rect(ventana, ROJO, (661, 736 - mover, 128, 48))
        if eliminar:
            pygame.draw.rect(ventana, BLANCO, (11, 701 - mover, 58, 88))
        if SUELO:
            pygame.draw.rect(ventana, ROJO, (101, 611 - mover, 178, 178))
        if PINCHO:
            pygame.draw.rect(ventana, GRIS, (291, 611 - mover, 218, 178))
        fuente = pygame.font.Font(None, 60)
        texto = fuente.render("SALIR", 1, BLANCO)
        ventana.blit(texto, (663, 740 - mover))
        pygame.draw.polygon(ventana, BLANCO, ((745, 620- mover), (745, 660 - mover), (785, 640 - mover)))
        pygame.draw.rect(ventana, BLANCO, (745, 680 - mover, 40, 40))
        pygame.draw.rect(ventana, VERDE_BANDERA, (765, 685 - mover, 15, 5))
        pygame.draw.rect(ventana, VERDE_BANDERA, (750, 695 - mover, 30, 20), 2)
        if juegoguardado > 0:
            fuente = pygame.font.Font(None, 70)
            texto = fuente.render("JUEGO GUARDADO", 1, ROJO)
            ventana.blit(texto, (10, 10))
            juegoguardado -= 1
        if error > 0:
            fuente = pygame.font.Font(None, 70)
            texto = fuente.render("Necesitas poner la meta y el inicio", 1, ROJO)
            ventana.blit(texto, (10, 10))
            error -= 1
        c = pygame.image.load("cierra.png")
        ventana.blit(c, (10, 610 - mover))
        pygame.draw.rect(ventana, NEGRO, (10, 700 - mover, 60, 90), 1)
        pygame.draw.polygon(ventana, ROJO, ((15, 705 - mover), (35, 705 - mover), (40, 722 - mover), (45, 705 - mover), (65, 705 - mover), (65, 740 - mover), (48, 745 - mover), (65, 750 - mover), (65, 785 - mover), (45, 785 - mover), (40, 768 - mover), (35, 785 - mover), (15, 785 - mover), (15, 750 - mover), (32, 745 - mover), (15, 740 - mover)))
        pygame.draw.rect(ventana, NEGRO, (100, 610 - mover, 180, 180), 3)
        fuente = pygame.font.Font(None, 70)
        texto = fuente.render("SUELO", 1, BLANCO)
        ventana.blit(texto, (110, 680 - mover))
        pygame.draw.rect(ventana, NEGRO, (290, 610 - mover, 220, 180), 3)
        fuente = pygame.font.Font(None, 70)
        texto = fuente.render("PINCHO", 1, BLANCO)
        ventana.blit(texto, (300, 680 - mover))
        if not iniciar:
            m = pygame.image.load("NES_Caminar_1.png")
            ventana.blit(m, (10, 670 - mover))
        if not meta:
            m = pygame.image.load("meta.png")
            ventana.blit(m, (40, 670 - mover))
    if colocando:
        if colocarcierra:
            c = pygame.image.load("cierra.png")
            ventana.blit(c, (mousex - 25, mousey - 25))
        elif seleccionardireccion:
            c = pygame.image.load("cierra.png")
            ventana.blit(c, (cierrax, cierray))
            pygame.draw.line(ventana, BLANCO, (cierrax + 25, cierray + 25), (mousex, mousey))
        elif preguntar == 1:
            c = pygame.image.load("cierra.png")
            ventana.blit(c, (cierrax, cierray))
            pygame.draw.line(ventana, BLANCO, (cierrax + 25, cierray + 25), (cierraxf + 25, cierrayf + 25))
            pygame.draw.rect(ventana, VERDE_BANDERA, (200, 100, 400, 400))
            pygame.draw.rect(ventana, BLANCO, (350, 200, 100, 70))
            fuente = pygame.font.Font(None,35)
            texto = fuente.render("MAXIMO DOS DIJITOS", 1, NEGRO)
            ventana.blit(texto, (210, 165))
            fuente = pygame.font.Font(None, 100)
            texto = fuente.render(str(velocidad), 1, NEGRO)
            ventana.blit(texto, (355, 205))
            fuente = pygame.font.Font(None, 60)
            texto = fuente.render("VELOCIDAD:", 1, BLANCO)
            ventana.blit(texto, (210, 110))
            if CONFIRMAR:
                pygame.draw.rect(ventana, ROJO, (406, 456, 183, 33))
            pygame.draw.rect(ventana, BLANCO, (405, 455, 185, 35), 1)
            fuente = pygame.font.Font(None, 40)
            texto = fuente.render("CONFIRMAR", 1, BLANCO)
            ventana.blit(texto, (410, 460))
            # cancelar
            if CANCELAR:
                pygame.draw.rect(ventana, ROJO, (211, 456, 183, 33))
            pygame.draw.rect(ventana, BLANCO, (210, 455, 185, 35), 1)
            fuente = pygame.font.Font(None, 40)
            texto = fuente.render("CANCELAR", 1, BLANCO)
            ventana.blit(texto, (215, 460))
        if colocarmeta:
            m = pygame.image.load("meta.png")
            ventana.blit(m, (mousex - 8, mousey - 7))
        if colocarmario:
            m = pygame.image.load("NES_Caminar_1.png")
            ventana.blit(m, (mousex - 6, mousey - 8))
        if colocarsuelo:
            if suelox != -1 and sueloy != -1:
                pygame.draw.rect(ventana, VERDE_BANDERA, (suelox, sueloy, mousex - suelox, mousey - sueloy))
        if colocarpincho:
            if suelox != -1 and sueloy != -1:
                pygame.draw.rect(ventana, ROJO, (suelox, sueloy, mousex - suelox, mousey - sueloy))


def modificar_mundos(nivel):
    contenido = list()
    filas = [nivel + 1]
    columna = 3
    nuevo_dato = "1"
    with open("mundos.txt", 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila-1].split(' ')
            columnas[columna] = nuevo_dato
            contenido[fila-1] = ' '.join(columnas)+ '\n'
    with open("mundos.txt", 'w') as archivo:
        archivo.writelines(contenido)


pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
termina = False
pygame.display.set_caption("LuismiBros")
pygame.key.set_repeat(True)


mundo = open("mundos.txt")
personaje = open("personajes.txt")
lvl = open("mundo.txt")
jugarmundo = open("MundoCreado.txt")

jugarmundo.seek(0)
for linea in jugarmundo:
    cadena = linea.split()
    if cadena[0] != "stop":
        if cadena[0] == "p":  # Pinchos
            x = int(cadena[1])  # De 0 a 800
            y = int(cadena[2])  # De 0 a 600
            xf = int(cadena[3]) # De 0 a 800
            yf = int(cadena[4]) # De 0 a 600
            crearpinchos.append([x, y, xf, yf])
        if cadena[0] == "f":  # Piso
            x = int(cadena[1])  # De 0 a 800
            y = int(cadena[2])  # De 0 a 600
            xf = int(cadena[3]) # De 0 a 800
            yf = int(cadena[4])  # De 0 a 600
            crearpiso.append([x, y, xf, yf])
        if cadena[0] == "c": # cierra
            x = int(cadena[1])  # De 0 a 800
            y = int(cadena[2])  # De 0 a 600
            xf = int(cadena[3])  # De 0 a 800
            yf = int(cadena[4])  # De 0 a 800
            velocidad = int(cadena[5])  # De 1 a 100
            crearcierras.append([x, y, xf, yf, velocidad])
        if cadena[0] == "i":  # inicio
            posxjugador = int(cadena[1])
            posyjugador = int(cadena[2])
            iniciar = True
            inici.append([posxjugador, posyjugador])
        if cadena[0] == "m":  # meta
            posxmeta = int(cadena[1])
            posymeta = int(cadena[2])
            meta = True
            crearmeta.append([posxmeta, posymeta])
    else:
        break


while not termina:

    mousex, mousey = pygame.mouse.get_pos()
    boton_mouse = [0]

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True

        if pygame.key.get_focused():
            press = pygame.key.get_pressed()
            for i in range(0, len(press)):
                if press[i] == 1:
                    suma = i
                    if suma == 32 and saltar != 1:
                        if not pausa:
                            saltar = 1
                    if suma == 276:
                        if IZQUIERDA:
                            if not pausa:
                                jugadorx -= 5
                                caminar = True
                    if suma == 275:
                        if DERECHA:
                            if not pausa:
                                jugadorx += 5
                                caminar = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                boton_mouse[0] = 1

    if instancia == 1:

        if 210 <= mousex <= 590 and 190 <= mousey <= 300:
            JUGAR = 5
            if boton_mouse[0] == 1:
                instancia = 2
        else:
            JUGAR = 0

        if 240 <= mousex <= 560 and 320 <= mousey <= 430:
            SALIR = 5
            if boton_mouse[0] == 1:
                termina = True
        else:
            SALIR = 0

        if 70 <= mousex <= 730 and 460 <= mousey <= 570:
            PERSONAJE = 5
            if boton_mouse[0] == 1:
                instancia = 3
        else:
            PERSONAJE = 0

    elif instancia == 2:

        if 395 <= mousex <= 790 and 495 <= mousey <= 565:
            REGRESAR = 5
            if boton_mouse[0] == 1:
                instancia = 1
        else:
            REGRESAR = 0

        if 10 <= mousex <= 265 and 495 <= mousey <= 565:
            CREAR = 5
            if boton_mouse[0] == 1:
                instancia = 5
        else:
            CREAR = 0

        mundo.seek(0)
        for linea in mundo:
            cadena = linea.split()
            cuadrox = int(cadena[0])
            cuadroy = int(cadena[1])
            cuadroancho = 122 + cuadrox
            cuadroalto = 122 + cuadroy
            valor = int(cadena[3])
            if cuadrox <= mousex <= cuadroancho and cuadroy <= mousey <= cuadroalto and boton_mouse[0] == 1 and valor == 1:
                instancia = valor + 3
                nivel = int(cadena[2])
                cier.clear()
                cierras.clear()
                cierrasinicial.clear()
                cie = True
                numcierras = 0
                numcierrs = 0
                ciera = 0

    elif instancia == 3:
        personaje.seek(0)
        for i in range(0, pestana):
            personaje.readline()

        for linea in personaje:
            cadena = linea.split()
            cuadrox = int(cadena[0]) - (pestana * 220)
            cuadroy = 150
            cuadroancho = 210
            cuadroalto = 300
            existencia = int(cadena[2])
            valor = int(cadena[4]) - pestana
            if valor <= 3:
                if existencia == 1 and cuadrox <= mousex <= cuadrox + cuadroancho and cuadroy <= mousey <= cuadroy + cuadroalto and boton_mouse[0] == 1:
                    draw = int(cadena[4])
                    tamanoxjugador = int(cadena[6])
                    tamanoyjugador = int(cadena[7])
                    imagennombre = cadena[5]

        if 10 <= mousex <= 60 and 300 <= mousey <= 350 and boton_mouse[0] == 1 and 1 <= pestana <= 2:
            pestana -= 1

        if 740 <= mousex <= 790 and 300 <= mousey <= 350 and boton_mouse[0] == 1 and 0 <= pestana <= 1:
            pestana += 1

        if 395 <= mousex <= 790 and 495 <= mousey <= 565:
            REGRESAR = 5
            if boton_mouse[0] == 1:
                instancia = 1
        else:
            REGRESAR = 0

    elif instancia == 4:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if not pausa:
                    pausa = True
                else:
                    pausa = False
        lvl.seek(0)
        caracteres = lvl.readline()
        h = caracteres.split()
        lvl.seek(0)
        for i in range(0, int(h[nivel - 1])):
            lvl.readline()
        for linea in lvl:
            cadena = linea.split()
            if cadena[0] != "stop":
                if cadena[0] == "f":  # Piso
                    x = int(cadena[1])  # De 0 a 800
                    y = int(cadena[2])  # De 0 a 600
                    ancho = int(cadena[3]) - x  # De 0 a 800
                    alto = int(cadena[4]) - y  # De 0 a 600
                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + 10 >= jugadory + tamanoyjugador >= y:
                        jugadory = y - tamanoyjugador
                        suelo = True
                        ABAJO = False
                    else:
                        suelo = False

                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + alto >= jugadory >= y + alto - 10:
                        ARRIBA = False
                        ABAJO = True
                    else:
                        ARRIBA = True

                    if x + 10 >= jugadorx + tamanoxjugador >= x and y + alto >= jugadory >= y:
                        DERECHA = False
                        jugadorx = x - 12
                    else:
                        DERECHA = True

                    if x + ancho - 10 <= jugadorx <= x + ancho and y + alto >= jugadory >= y:
                        IZQUIERDA = False
                        jugadorx = x + ancho
                    else:
                        IZQUIERDA = True

                if cadena[0] == "p":  # Pinchos
                    x = int(cadena[1])  # De 0 a 800
                    y = int(cadena[2])  # De 0 a 600
                    ancho = int(cadena[3]) - x  # De 0 a 800
                    alto = int(cadena[4]) - y  # De 0 a 600
                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + alto >= jugadory >= y - tamanoyjugador:
                        jugadory = 700

                if cadena[0] == "m":  # meta
                    posxmeta = int(cadena[1])
                    posymeta = int(cadena[2])
                    if 16 + posxmeta >= jugadorx >= posxmeta - 12 and 15 + posymeta >= jugadory >= posymeta - 16:
                        instancia = 2
                        primer.append(0)
                        ABAJO = True
                        cie = True
                        modificar_mundos(nivel)

            else:
                break

        for i in range(0, len(cierrasinicial)):
            inicio = cierrasinicial[i]
            cx = inicio[0]  # De 0 a 800
            cy = inicio[1]  # De 0 a 600
            if cx + 50 >= jugadorx >= cx - tamanoxjugador and cy + 50 >= jugadory >= cy - tamanoyjugador:
                jugadory = 700

    elif instancia == 5:
        if not colocando:
            if mover != 200:
                if 375 <= mousex <= 425 and 540 <= mousey <= 590 and mover == 0:
                    move = 2
                    if boton_mouse[0] == 1:
                        mover = 200
                else:
                    move = 0
                    muve = 0
            elif mover == 200:
                if 375 <= mousex <= 425 and 340 <= mousey <= 390:
                    move = 2
                    muve = 4
                    if boton_mouse[0] == 1:
                        mover = 0
                else:
                    move = 0
                    muve = 0
                if 740 <= mousex <= 790 and 415 <= mousey <= 465:
                    JUGAR = 1
                    if boton_mouse[0] == 1:
                        if meta and iniciar:
                            instancia = 6
                            mover = 0
                        else:
                            error = 10
                else:
                    JUGAR = 0

                if 740 <= mousex <= 790 and 475 <= mousey <= 525:
                    GUARDAR = 1
                    if boton_mouse[0] == 1 and juegoguardado == 0:
                        if boton_mouse[0] == 1:
                            mundocreado = open("MundoCreado.txt", "w")
                            for i in range(0, len(crearcierras)):
                                w = crearcierras[i]
                                x = str(w[0])
                                y = str(w[1])
                                xf = str(w[2])
                                yf = str(w[3])
                                velocidad = str(w[4])
                                mundocreado.write("c" + " " + x + " " + y + " " + xf + " " + yf + " " + velocidad + "\n")
                            for i in range(0, len(crearpiso)):
                                w = crearpiso[i]
                                x = str(w[0])
                                y = str(w[1])
                                xf = str(w[2])
                                yf = str(w[3])
                                mundocreado.write("f" + " " + x + " " + y + " " + xf + " " + yf + "\n")
                            for i in range(0, len(crearpinchos)):
                                w = crearpinchos[i]
                                x = str(w[0])
                                y = str(w[1])
                                xf = str(w[2])
                                yf = str(w[3])
                                mundocreado.write("p" + " " + x + " " + y + " " + xf + " " + yf + "\n")
                            if meta:
                                w = crearmeta[0]
                                x = str(w[0])
                                y = str(w[1])
                                mundocreado.write("m" + " " + x + " " + y + "\n")
                            if iniciar:
                                w = inici[0]
                                x = str(w[0])
                                y = str(w[1])
                                mundocreado.write("i" + " " + x + " " + y)
                            mundocreado.close()
                        juegoguardado = 10
                else:
                    GUARDAR = 0
                if 660 <= mousex <= 790 and 535 <= mousey <= 585:
                    SALIR = 1
                    if boton_mouse[0] == 1:
                        instancia = 2
                        SALIR = 0
                else:
                    SALIR = 0
                if 10 <= mousex <= 60 and 410 <= mousey <= 460 and boton_mouse[0] == 1:
                    colocando = True
                    colocarcierra = True
                if not meta:
                    if 40 <= mousex <= 56 and 470 <= mousey <= 485 and boton_mouse[0] == 1:
                        colocando = True
                        colocarmeta = True
                if not iniciar:
                    if 10 <= mousex <= 22 and 470 <= mousey <= 486 and boton_mouse[0] == 1:
                        colocando = True
                        colocarmario = True
                if 10 <= mousex <= 70 and 500 <= mousey <= 590:
                    eliminar = True
                    if boton_mouse[0] == 1:
                        colocando = True
                        eliminando = True
                else:
                    eliminar = False
                if 100 <= mousex <= 280 and 410 <= mousey <= 590:
                    SUELO = True
                    if boton_mouse[0] == 1:
                        colocando = True
                        colocarsuelo = True
                else:
                    SUELO = False
                if 290 <= mousex <= 510 and 410 <= mousey <= 590:
                    PINCHO = True
                    if boton_mouse[0] == 1:
                        colocando = True
                        colocarpincho = True
                else:
                    PINCHO = False
        elif colocando:
            if colocarcierra:
                if boton_mouse[0]:
                    colocarcierra = False
                    seleccionardireccion = True
                    cierrax, cierray = (mousex - 25, mousey - 25)
            elif seleccionardireccion:
                if boton_mouse[0]:
                    cierraxf = mousex - 25
                    cierrayf = mousey - 25
                    preguntar = 1
                    seleccionardireccion = False
            elif preguntar == 1:
                if evento.type == pygame.KEYDOWN and rotar == 0:
                    if velocidad <= 9:
                        if evento.key == pygame.K_0:
                            if velocidad == 0:
                                velocidad = 0
                            else:
                                velocidad = velocidad * 10
                            rotar = 5
                        elif evento.key == pygame.K_1:
                            velocidad = velocidad * 10 + 1
                            rotar = 5
                        elif evento.key == pygame.K_2:
                            velocidad = velocidad * 10 + 2
                            rotar = 5
                        elif evento.key == pygame.K_3:
                            velocidad = velocidad * 10 + 3
                            rotar = 5
                        elif evento.key == pygame.K_4:
                            velocidad = velocidad * 10 + 4
                            rotar = 5
                        elif evento.key == pygame.K_5:
                            velocidad = velocidad * 10 + 5
                            rotar = 5
                        elif evento.key == pygame.K_6:
                            velocidad = velocidad * 10 + 6
                            rotar = 5
                        elif evento.key == pygame.K_7:
                            velocidad = velocidad * 10 + 7
                            rotar = 5
                        elif evento.key == pygame.K_8:
                            velocidad = velocidad * 10 + 8
                            rotar = 5
                        elif evento.key == pygame.K_9:
                            velocidad = velocidad * 10 + 9
                            rotar = 5
                        elif evento.key == pygame.K_BACKSPACE:
                            velocidad = 0
                            rotar = 5
                    else:
                        if evento.key == pygame.K_BACKSPACE:
                            velocidad = int(velocidad / 10)
                            rotar = 5
                if evento.type == pygame.KEYUP:
                    rotar = 0
                if rotar != 0:
                    rotar -= 1
                if 405 <= mousex <= 590 and 455 <= mousey <= 490:
                    CONFIRMAR = True
                    if boton_mouse[0] == 1:
                        crearcierras.append([cierrax, cierray, cierraxf, cierrayf, velocidad])
                        preguntar = 0
                        colocando = False
                        mover = 0
                else:
                    CONFIRMAR = False
                if 210 <= mousex <= 395 and 455 <= mousey <= 490:
                    CANCELAR = True
                    if boton_mouse[0] == 1:
                        preguntar = 0
                        colocando = False
                        mover = 0
                else:
                    CANCELAR = False
            if colocarmeta:
                if boton_mouse[0]:
                    colocarmeta = False
                    meta = True
                    crearmeta.append([mousex - 8, mousey - 7])
                    colocando = False
                    mover = 0
            if colocarmario:
                if boton_mouse[0]:
                    colocarmario = False
                    iniciar = True
                    inici.append([mousex - 6, mousey - 8])
                    colocando = False
                    mover = 0
            if eliminando and boton_mouse[0] == 1:
                elimina = 0
                if elimina == 0:
                    for i in range(0, len(crearcierras)):
                        lista = crearcierras[i]
                        if lista[0] + 50 >= mousex >= lista[0] and lista[1] + 50 >= mousey >= lista[1]:
                            crearcierras.remove(crearcierras[i])
                            eliminando = False
                            colocando = False
                            mover = 0
                            elimina = 1
                            break
                if elimina == 0:
                    for i in range(0, len(crearpiso)):
                        lista = crearpiso[i]
                        if lista[0] <= mousex <= lista[2] and lista[1] <= mousey <= lista[3]:
                            crearpiso.remove(crearpiso[i])
                            eliminando = False
                            colocando = False
                            mover = 0
                            elimina = 1
                            break
                if elimina == 0:
                    for i in range(0, len(crearpinchos)):
                        lista = crearpinchos[i]
                        if lista[0] <= mousex <= lista[2] and lista[1] <= mousey <= lista[3]:
                            crearpinchos.remove(crearpinchos[i])
                            eliminando = False
                            colocando = False
                            mover = 0
                            elimina = 1
                            break
                if meta:
                    if crearmeta[0][0] + 16 >= mousex >= crearmeta[0][0] and crearmeta[0][1] + 15 >= mousey >= crearmeta[0][1]:
                        crearmeta.remove(crearmeta[0])
                        eliminando = False
                        colocando = False
                        meta = False
                        mover = 0
                        elimina = 1
                elif iniciar:
                    if inici[0][0] + 12 >= mousex >= inici[0][0] and inici[0][1] + 16 >= mousey >= inici[0][1]:
                        inici.remove(inici[0])
                        eliminando = False
                        colocando = False
                        iniciar = False
                        mover = 0
                        elimina = 1
            if colocarsuelo:
                if boton_mouse[0] == 1 and suelox == -1 and sueloy == -1:
                    suelox = mousex
                    sueloy = mousey
                elif boton_mouse[0] == 1:
                    if suelox > mousex:
                        sueloxf = suelox
                        suelox = mousex
                    else:
                        sueloxf = mousex
                    if sueloy > mousey:
                        sueloyf = sueloy
                        sueloy = mousey
                    else:
                        sueloyf = mousey
                    crearpiso.append([suelox, sueloy, sueloxf, sueloyf])
                    mover = 0
                    colocarsuelo = False
                    colocando = False
                    suelox = -1
                    sueloy = -1
            if colocarpincho:
                if boton_mouse[0] == 1 and suelox == -1 and sueloy == -1:
                    suelox = mousex
                    sueloy = mousey
                elif boton_mouse[0] == 1:
                    if suelox > mousex:
                        sueloxf = suelox
                        suelox = mousex
                    else:
                        sueloxf = mousex
                    if sueloy > mousey:
                        sueloyf = sueloy
                        sueloy = mousey
                    else:
                        sueloyf = mousey
                    crearpinchos.append([suelox, sueloy, sueloxf, sueloyf])
                    mover = 0
                    colocarpincho = False
                    colocando = False
                    suelox = -1
                    sueloy = -1

    elif instancia == 6:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if not pausa:
                    pausa = True
                elif pausa:
                    pausa = False
        jugarmundo.seek(0)
        for linea in jugarmundo:
            cadena = linea.split()
            if cadena[0] != "stop":
                if cadena[0] == "f":  # Piso
                    x = int(cadena[1])  # De 0 a 800
                    y = int(cadena[2])  # De 0 a 600
                    ancho = int(cadena[3]) - x  # De 0 a 800
                    alto = int(cadena[4]) - y  # De 0 a 600
                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + 10 >= jugadory + tamanoyjugador >= y:
                        jugadory = y - tamanoyjugador
                        suelo = True
                        ABAJO = False
                    else:
                        suelo = False

                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + alto >= jugadory >= y + alto - 10:
                        ARRIBA = False
                        ABAJO = True
                    else:
                        ARRIBA = True

                    if x + 10 >= jugadorx + tamanoxjugador >= x and y + alto >= jugadory >= y:
                        DERECHA = False
                        jugadorx = x - 12
                    else:
                        DERECHA = True

                    if x + ancho - 10 <= jugadorx <= x + ancho and y + alto >= jugadory >= y:
                        IZQUIERDA = False
                        jugadorx = x + ancho
                    else:
                        IZQUIERDA = True

                if cadena[0] == "p":  # Pinchos
                    x = int(cadena[1])  # De 0 a 800
                    y = int(cadena[2])  # De 0 a 600
                    ancho = int(cadena[3]) - x  # De 0 a 800
                    alto = int(cadena[4]) - y  # De 0 a 600
                    if x + ancho >= jugadorx >= x - tamanoxjugador and y + alto >= jugadory >= y - tamanoyjugador:
                        jugadory = 700

                if cadena[0] == "m":  # meta
                    posxmeta = int(cadena[1])
                    posymeta = int(cadena[2])
                    if 16 + posxmeta >= jugadorx >= posxmeta - 12 and 15 + posymeta >= jugadory >= posymeta - 16:
                        instancia = 5
                        primer.append(0)
                        ABAJO = True
                        cie = True
                        cierras.clear()
                        cier.clear()
                        numcierrs = 0
            else:
                break

        for i in range(0, len(cierrasinicial)):
            inicio = cierrasinicial[i]
            cx = inicio[0]  # De 0 a 800
            cy = inicio[1]  # De 0 a 600
            if cx + 50 >= jugadorx >= cx - tamanoxjugador and cy + 50 >= jugadory >= cy - tamanoyjugador:
                jugadory = 700

    if pausa:
        if 120 <= mousex <= 680 and 210 <= mousey <= 390 and boton_mouse[0] == 1:
            pausa = False
            instancia = 2
        if 650 <= mousex <= 700 and 100 <= mousey <= 150 and boton_mouse[0] == 1:
            pausa = False

    instancias(JUGAR, SALIR, PERSONAJE, REGRESAR, AUMENTO, pestana, draw)

    pygame.display.flip()
    reloj.tick(40)

pygame.quit()