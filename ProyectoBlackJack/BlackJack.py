# encoding: UTF-8
# Autor: Jaime Orlando López Ramos, A01374696
# Proyecto final de Fundamentos de programación

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
bg = pygame.image.load("BlackFinal.png")
ace = pygame.image.load("ace.jpg")
two = pygame.image.load("two.jpg")
three = pygame.image.load("three.jpg")
four = pygame.image.load("four.jpg")
five = pygame.image.load("five.jpg")
six = pygame.image.load("six.jpg")
seven = pygame.image.load("Seven.jpg")
eigth = pygame.image.load("eight.jpg")
nine = pygame.image.load("nine.jpg")
ten = pygame.image.load("ten.jpg")
jack = pygame.image.load("jack.jpg")
queen = pygame.image.load("queen.jpg")
king = pygame.image.load("king.jpg")
manoEntrega=pygame.image.load("ManoEntrega.png")
imgMenu = pygame.image.load("menu.png")
imgBtn = pygame.image.load("button.png")
standBtn = pygame.image.load("stand_Button.png")
hitBtn = pygame.image.load("hit_Btn.png")
pierdesBtn = pygame.image.load("pierdes.png")
ganasBtn = pygame.image.load("ganas.png")
empateBtn = pygame.image.load("empate.png")
listaCartasJuego = [ace, two, three, four, five, six, seven, eigth, nine, ten, jack, queen, king]
diccionarioValores = {}
diccionarioValores["ace"] = 11
diccionarioValores["two"] = 2
diccionarioValores["three"] = 3
diccionarioValores["four"] = 4
diccionarioValores["five"] = 5
diccionarioValores["six"] = 6
diccionarioValores["seven"] = 7
diccionarioValores["eigth"] = 8
diccionarioValores["nine"] = 9
diccionarioValores["ten"] = 10
diccionarioValores["jack"] = 10
diccionarioValores["queen"] = 10
diccionarioValores["king"] = 10
xRes = ANCHO //2 - 100
yRes = 100



def darCartasJugador(ventana, xJugador, yJugador, listaCartasEntregadasJugador):
    x0Jugador = xJugador
    for i in range (len(listaCartasEntregadasJugador)):
        ventana.blit(listaCartasEntregadasJugador[i], [x0Jugador, yJugador])
        x0Jugador += 20


def darCartasDealer(ventana, xDealer, yDealer, listaCartasDealer):
    for index in range (len(listaCartasDealer)):
        ventana.blit(listaCartasDealer[index], [xDealer, yDealer])
        xDealer += 20

def generarCarta(listaCartasJuego):
    indiceCarta = randint(0, 12)
    carta = listaCartasJuego[indiceCarta]
    return carta

def animarManoJugador(ventana):
    posY0 = 250
    xMano = 700
    for posX in range(40):
        ventana.blit(bg, [0, 0])
        ventana.blit(manoEntrega, [xMano, posY0])
        xMano -= 10
        pygame.display.update()
        pygame.time.delay(50)

def animarManoDealer(ventana):
    posY0 = (150)
    xMano = 700
    for posX in range(40):
        ventana.blit(bg, [0, 0])
        ventana.blit(manoEntrega, [xMano, posY0])
        xMano -= 10
        pygame.display.update()
        pygame.time.delay(50)


def determinarGanador(puntajeJugador, puntajeDealer, cartasEntregadasDealer, cartasEntregadasJugador):
    if puntajeDealer > puntajeJugador:
        estado = "pierdes"
    elif puntajeJugador > puntajeDealer:
        estado = "ganas"
    elif (puntajeDealer == puntajeJugador) and (puntajeJugador != 21):
        estado = "empate"
    elif puntajeJugador == 21:
        if (len(cartasEntregadasJugador) == 2) and (len(cartasEntregadasDealer) != 2):
            estado = "ganas"
        elif (len(cartasEntregadasJugador) == 2) and (len(cartasEntregadasDealer) == 2) and puntajeDealer ==21:
            estado = "empate"
        elif (len(cartasEntregadasJugador) != 2) and (len(cartasEntregadasDealer) == 2) and puntajeDealer == 21:
            estado = "pierdes"
        elif (len(cartasEntregadasJugador) != 2) and (len(cartasEntregadasDealer) != 2) and puntajeDealer ==21:
            estado = "empate"
    return estado






def actualizarPuntaje(carta, diccionarioValores, puntaje):
    if carta == ace and puntaje <= 10:
        puntaje = puntaje + 11
    elif carta == ace and puntaje > 10:
        puntaje = puntaje + 1
    elif carta == two:
        puntaje = puntaje + diccionarioValores["two"]
    elif carta == three:
        puntaje = puntaje + diccionarioValores["three"]
    elif carta == four:
        puntaje = puntaje + diccionarioValores["four"]
    elif carta == three:
        puntaje = puntaje + diccionarioValores["three"]
    elif carta == four:
        puntaje = puntaje + diccionarioValores["four"]
    elif carta == five:
        puntaje = puntaje + diccionarioValores["five"]
    elif carta == six:
        puntaje = puntaje + diccionarioValores["six"]
    elif carta == seven:
        puntaje = puntaje + diccionarioValores["seven"]
    elif carta == eigth:
        puntaje = puntaje + diccionarioValores["eigth"]
    elif carta == nine:
        puntaje = puntaje + diccionarioValores["nine"]
    elif carta == ten:
        puntaje = puntaje + diccionarioValores["ten"]
    elif carta == jack:
        puntaje = puntaje + diccionarioValores["jack"]
    elif carta == queen:
        puntaje = puntaje + diccionarioValores["queen"]
    elif carta == king:
        puntaje = puntaje + diccionarioValores["king"]
    return puntaje



def jugar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.wav")
    pygame.mixer.music.play(-1)
    xJugador = 300
    yJugador = 400
    xDealer = xJugador
    yDealer = 300
    estado =  "Menu"
    puntajeJugador = 0
    puntajeDealer = 0
    blackJacksPartida = 0



    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.blit(bg, [0, 0])
        # Dibujar, aquí haces todos los trazos que requieras

        if estado == "Menu":
            ventana.blit(imgMenu, [0, 0])
            ventana.blit(imgBtn, [ANCHO // 2 - 200, ALTO // 2])
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xb, yb, anchoB, ALTOB = imgBtn.get_rect()
                xm, ym = pygame.mouse.get_pos()
                if (ANCHO // 2 - 200 <= xm <= ANCHO // 2) and (ALTO // 2 <= ym <= ALTO // 2 + 100):
                    estado = "activarMano"
        elif estado ==  "activarMano":
            cartasEntregadasJug = []
            cartasEntregadasDeal = []
            animarManoJugador(ventana)
            estado = "darCartasIniciales"

        elif estado == "darCartasIniciales":
            contadorAceJug = 0
            contadorAceDeal = 0
            carta1Jug = generarCarta(listaCartasJuego)
            cartasEntregadasJug.append(carta1Jug)
            if carta1Jug == ace:
                contadorAceJug += 1
            puntajeJugador = actualizarPuntaje(carta1Jug, diccionarioValores, puntajeJugador)
            carta1Deal = generarCarta(listaCartasJuego)
            cartasEntregadasDeal.append(carta1Deal)
            if carta1Deal == ace:
                contadorAceDeal += 1
            puntajeDealer = actualizarPuntaje(carta1Deal, diccionarioValores, puntajeDealer)
            darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
            darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            carta2Jug = generarCarta(listaCartasJuego)
            cartasEntregadasJug.append(carta2Jug)
            if carta2Jug == ace and puntajeJugador < 11:
                contadorAceJug += 1
            puntajeJugador = actualizarPuntaje(carta2Jug, diccionarioValores, puntajeJugador)
            estado = "cartasInicialesListas"

        elif estado == "cartasInicialesListas":
            darCartas = False
            darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
            if puntajeJugador < 21:
                ventana.blit(hitBtn, [ANCHO- 150, 100])
                ventana.blit(standBtn, [ANCHO-150, 200])
                if darCartas == False:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        xm, ym = pygame.mouse.get_pos()
                        if (ANCHO-150 <= xm <= (ANCHO-50)) and (200 <= ym <= 200 + 50):
                            estado = "dealerJuega"
                        elif (ANCHO-150 <= xm <= (ANCHO-50)) and (100 <= ym <= 100 + 50):
                            estado = "hitJugador"
                            darCartas = True
            elif puntajeJugador > 21:
                estado = "verificarAceJugador"
            elif puntajeJugador == 21:
                if len(cartasEntregadasJug) == 2  and len(cartasEntregadasDeal) == 1:
                    blackJacksPartida += 1
                    if puntajeDealer == 10 or puntajeDealer==11:
                        estado = "dealerJuega"
                    else:
                        estado = "ganas"
                elif len(cartasEntregadasJug) == 2  and len(cartasEntregadasDeal) == 2 and puntajeDealer != 21:
                    estado ="ganas"
                    blackJacksPartida += 1
                else:
                    estado = "dealerJuega"


        elif estado == "hitJugador":
            if darCartas == True:
                carta = generarCarta(listaCartasJuego)
                if carta == ace and puntajeJugador < 11:
                    contadorAceJug += 1
                puntajeJugador = actualizarPuntaje(carta, diccionarioValores, puntajeJugador)
                cartasEntregadasJug.append(carta)
                estado = "cartasInicialesListas"

        elif estado == "verificarAceJugador":
            if puntajeJugador > 21 and contadorAceJug != 0:
                puntajeJugador -= 10
                contadorAceJug -= 1
                estado = "cartasInicialesListas"
            else:
                estado = "pierdes"

        elif estado == "dealerJuega":
            if puntajeDealer < 17:
                cartaDeal = generarCarta(listaCartasJuego)
                if cartaDeal == ace and puntajeDealer < 11:
                    contadorAceDeal += 1
                puntajeDealer = actualizarPuntaje(cartaDeal, diccionarioValores, puntajeDealer)
                cartasEntregadasDeal.append(cartaDeal)
                darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
                darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            elif 17<=puntajeDealer<= 21:
                estado = "compararPuntajes"
            elif puntajeDealer > 21:
                estado = "verificarAceDealer"

        elif estado == "verificarAceDealer":
            if puntajeDealer > 21 and contadorAceDeal != 0:
                puntajeDealer -= 10
                contadorAceDeal -= 1
                estado = "dealerJuega"
            else:
                estado = "ganas"

        elif estado == "compararPuntajes":
            estado = determinarGanador(puntajeJugador, puntajeDealer, cartasEntregadasDeal, cartasEntregadasJug)

        elif estado == "ganas":
            darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
            darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            ventana.blit(ganasBtn, [xRes, yRes])
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if (ANCHO//2-100 <= xm <= ANCHO//2+100) and 100 <= ym <= 200:
                    estado = "reset"


        elif estado == "pierdes":
            darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
            darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            ventana.blit(pierdesBtn, [xRes, yRes])
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if (ANCHO//2-100 <= xm <= ANCHO//2+100) and 100 <= ym <= 200:
                    estado = "reset"

        elif estado == "empate":
            darCartasJugador(ventana, xJugador, yJugador, cartasEntregadasJug)
            darCartasDealer(ventana, xDealer, yDealer, cartasEntregadasDeal)
            ventana.blit(empateBtn, [xRes, yRes])
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if (ANCHO//2-100 <= xm <= ANCHO//2+100) and 100 <= ym <= 200:
                    estado = "reset"

        elif estado == "reset":
            cartasEntregadasJug = []
            cartasEntregadasDeal = []
            xJugador = 300
            yJugador = 400
            xDealer = xJugador
            yDealer = 300
            puntajeJugador = 0
            puntajeDealer = 0
            estado = "activarMano"





        pygame.display.flip()   # Actualiza trazos
        reloj.tick(20)          # 20 fps


    pygame.quit()   # termina pygame
    archivo = open("blackjacks.txt", "a", encoding="UTF-8",) #Escribir blackjacks de la sesión en archivo
    archivo.write("BlackJacks registrados: ")
    blackJacksPartida = str(blackJacksPartida)
    archivo.write(blackJacksPartida)
    archivo.write("\n")
    archivo.close()


def main():                                     #Función principal
    jugar()



main()