# encoding: UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Proyecto final: videojuego.

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

# Dibujar botones en la ventena menu
def dibujarMenu(ventana, btnJugar, btnSalir):
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnSalir.image, btnSalir.rect)


# Dibujar botones en la ventena de juego perdido
def dibujarPerdido(ventana, btnVolverAlMenu):
    ventana.blit(btnVolverAlMenu.image, btnVolverAlMenu.rect)


# Dibujar botones en la ventena de juego ganado
def dibujarGanado(ventana, btnVolverAlMenu):
    ventana.blit(btnVolverAlMenu.image, btnVolverAlMenu.rect)


# Dibujar elementos mientras se juega
def dibujarJuego(ventana, btnVolverAlMenu, listaGotas, mariposa):
    btnVolverAlMenu.rect.left = ANCHO - btnVolverAlMenu.rect.width - 50
    btnVolverAlMenu.rect.top = ALTO - btnVolverAlMenu.rect.height - 50
    ventana.blit(btnVolverAlMenu.image, btnVolverAlMenu.rect)

    dxMariposa = 20
    dyMariposa = 20
    moverMariposa = False

    # Dibujando la mariposa:
    ventana.blit(mariposa.image, mariposa.rect)

    '''
    if mariposa.rect.left < 0 or mariposa.rect.left > ANCHO:    # Si la mariposa toca los bordes en x
        moverMariposa = False                                   # La mariposa no se puede mover
    if mariposa.rect.top < 0 or mariposa.rect.top > ALTO:       # Si la mariposa toca los bordes en y
        moverMariposa = False                                   # La mariposa no se puede mover
    '''

    for nuevaGota in listaGotas:
        ventana.blit(nuevaGota.image, nuevaGota.rect)


# Eliminar gotas innecesarias y verificar colisiones
def actualizarGotas(listaGotas, mariposa, contador, efecto):

    # Eliminar gotas fuera de la pantalla:
    for k in range(1, len(listaGotas)-1, 1):
        if listaGotas[k].rect.top >= ALTO+16:
            listaGotas.remove(listaGotas[k])

    # Verificar colisiones:
    for nuevaGota in listaGotas:
        borrarGota = False
        # Si la gota toca a la mariposa:
        if nuevaGota.rect.colliderect(mariposa):
            listaGotas.remove(nuevaGota)
            borrarGota = True
            contador = contarVidas(contador)
            efecto.play()
            break   # Detener el ciclo for.

        if borrarGota:
            listaGotas.remove(nuevaGota)

    return contador


# Actualizar número de vidas
def contarVidas(contador):
    contadorNuevo = contador - 1
    return contadorNuevo


# Generar gotas como sprites y añadirlas a una lista
def generarGotas(listaGotas, imagenGota):
    for x in range(2):
            for y in range(1):

                # Coordenadas de las gotas:
                xGota = randint(0, ANCHO)
                yGota = 0

                nuevaGota= pygame.sprite.Sprite()
                nuevaGota.image = imagenGota
                nuevaGota.rect = imagenGota.get_rect()
                nuevaGota.rect.left = xGota
                nuevaGota.rect.top = yGota
                listaGotas.append(nuevaGota)


# Modificar las coordenadas de las gotas para crear movimiento
def moverGotas(listaGotas):
    for nuevaGota in listaGotas:
        nuevaGota.rect.top += 3


# Mostrar en la pantalla el puntaje al terminar el juego
def dibujarPuntaje(ventana, contadorFinal):
    fuente = pygame.font.SysFont("didot", 48)
    texto = fuente.render("Tu puntaje fue: " + str(contadorFinal), 1, BLANCO)
    ventana.blit(texto, (ANCHO // 3 - 160, 2*ALTO // 3 + 10))


# Mostrar en la pantalla del menu un mensaje de texto
def dibujarPuntajeMasAlto(ventana):
    fuente = pygame.font.SysFont("didot", 30)
    texto = fuente.render("El puntaje más alto posible es 600", 1, ROJO)
    ventana.blit(texto, (40, 2 * ALTO // 3 - 50))


def dibujar():
    # Imagen Menu
    imagenMenu = pygame.image.load("imagenMenu.png")

    # Imagen Fondo Nivel 1
    imagenFondo1 = pygame.image.load("imagenFondoNivel1.png")

    # Imagen Fondo Nivel 2
    imagenFondo2 = pygame.image.load("imagenFondoNivel2.png")

    # Imagen Juego Ganado
    imagenGanado = pygame.image.load("imagenGanado.png")

    # Imagen Juego Perdido
    imagenPerdido = pygame.image.load("imagenPerdido.png")

    # Imagen Mariposa
    imagenMariposa = pygame.image.load("mariposa.png")

    # Imagen Gota
    imagenGota = pygame.image.load("gota.png")

    # Coordenadas de la mariposa:
    xMariposa = ANCHO//2 - 50
    yMariposa = ALTO//2 - 25

    dxMariposa = 20
    dyMariposa = 20
    moverMariposa = False

    mariposa = pygame.sprite.Sprite()
    mariposa.image = imagenMariposa
    mariposa.rect = imagenMariposa.get_rect()
    mariposa.rect.left = xMariposa
    mariposa.rect.top = yMariposa

    # Coordenadas de las gotas:
    xGota = randint(0, ANCHO)
    yGota = 0

    dyGota = 3
    moverGota = True

    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Estados:
    estado = "menu"  # Jugando, termina

    # Botones:
    imgBotonJugar = pygame.image.load("botonJugar.png")
    btnJugar = pygame.sprite.Sprite()  # Sprite
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 + 150

    imgBotonSalir = pygame.image.load("botonSalir.png")
    btnSalir = pygame.sprite.Sprite()  # Sprite
    btnSalir.image = imgBotonSalir
    btnSalir.rect = imgBotonSalir.get_rect()
    btnSalir.rect.left = ANCHO // 2 - btnSalir.rect.width // 2 + 200
    btnSalir.rect.top = ALTO // 2 + 150

    imgBotonVolverAlMenu = pygame.image.load("botonVolverAlMenu.png")
    btnVolverAlMenu = pygame.sprite.Sprite()  # Sprite
    btnVolverAlMenu.image = imgBotonVolverAlMenu
    btnVolverAlMenu.rect = imgBotonVolverAlMenu.get_rect()
    btnVolverAlMenu.rect.left = ANCHO // 2 - btnVolverAlMenu.rect.width // 2 - 500
    btnVolverAlMenu.rect.top = ALTO // 2 + 150

    # Gotas:
    listaGotas = []
    timerGotas = 0
    timerNivel = 0

    generarGotas(listaGotas, imagenGota)

    # Vidas:
    contadorVidas = 3
    listaPuntajes = []

    contadorNivel1 = 0
    contadorNivel2 = 0

    masAlto = 0

    # Crear archivo con los estados del juego
    estados = open("estados.txt", "a", encoding='UTF-8')
    estados.write("Registro de Estados" + "\n")
    estados.write("")

    pygame.mixer.init()
    pygame.mixer.music.load("musicaDeFondo.mp3")
    pygame.mixer.music.play(-1)

    efecto = pygame.mixer.Sound("plop.wav")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugandoNivel1"

                    xs, ys, anchoS, altoS = btnSalir.rect
                    if xm >= xs and xm <= xs + anchoS:
                        if ym >= ys and ym <= ys + altoS:
                            termina = True

                elif estado == "jugandoNivel1":
                    xv, yv, anchoV, altoV = btnVolverAlMenu.rect
                    if xm >= xv and xm <= xv + anchoV:
                        if ym >= yv and ym <= yv + altoV:
                            estado = "menu"

                elif estado == "jugandoNivel2":
                    xv, yv, anchoV, altoV = btnVolverAlMenu.rect
                    if xm >= xv and xm <= xv + anchoV:
                        if ym >= yv and ym <= yv + altoV:
                            estado = "menu"

                elif estado == "ganado" or estado == "perdido":
                    xv, yv, anchoV, altoV = btnVolverAlMenu.rect
                    if xm >= xv and xm <= xv + anchoV:
                        if ym >= yv and ym <= yv + altoV:
                            estado = "menu"
                            contadorVidas = 3

            # Si se oprime alguna tecla:
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:        # Flecha hacia arriba
                    dyMariposa = -10
                    dxMariposa = 0
                    moverMariposa = True
                if evento.key == pygame.K_DOWN:      # Flecha hacia abajo
                    dyMariposa = 10
                    dxMariposa = 0
                    moverMariposa = True
                if evento.key == pygame.K_RIGHT:     # Flecha hacia la derecha
                    dxMariposa = 10
                    dyMariposa = 0
                    moverMariposa = True
                if evento.key == pygame.K_LEFT:      # Flecha hacia la derecha
                    dxMariposa = -10
                    dyMariposa = 0
                    moverMariposa = True
            if evento.type == pygame.KEYUP:
                moverMariposa = False

        # Borrar pantalla
        if estado == "menu":
            ventana.blit(imagenMenu, (0,0))
        elif estado == "jugandoNivel1":
            ventana.blit(imagenFondo1, (0,0))
        elif estado == "jugandoNivel2":
            ventana.blit(imagenFondo2, (0,0))
        elif estado == "ganado":
            ventana.blit(imagenGanado, (0,0))
        elif estado == "perdido":
            ventana.blit(imagenPerdido, (0,0))

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, btnJugar, btnSalir)
            dibujarPuntajeMasAlto(ventana)
        elif estado == "jugandoNivel1" or estado == "jugandoNivel2":
            contadorVidas = actualizarGotas(listaGotas, mariposa, contadorVidas, efecto)
            dibujarJuego(ventana, btnVolverAlMenu, listaGotas, mariposa)
            if contadorVidas == 0:
                estado = "perdido"

            # Actualizar posición de la mariposa
            if moverMariposa:
                mariposa.rect.left += dxMariposa
                mariposa.rect.top += dyMariposa

            # Actualizar posición de las gotas de agua
            moverGotas(listaGotas)

        elif estado == "perdido":
            dibujarPerdido(ventana, btnVolverAlMenu)
            dibujarPuntaje(ventana, contadorFinal)

        elif estado == "ganado":
            dibujarGanado(ventana, btnVolverAlMenu)
            dibujarPuntaje(ventana, contadorFinal)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

        # Creación de timers
        timerGotas += reloj.tick(40) / 1000  # Timer para la generación de gotas
        timerNivel += reloj.tick(40) / 1000  # Timer para la generación de gotas

        # Generar gotas regenerando el timer cuando llega a 1.7
        if timerGotas >= 1.7:
            generarGotas(listaGotas, imagenGota)
            timerGotas = 0

        # Cambiar de nivel regenerando el timer cuando llega a 15
        if timerNivel >= 15 and estado == "jugandoNivel1":
            estado = "jugandoNivel2"
            contadorNivel1 = 100 * contadorVidas
            timerNivel = 0

        # Ganar el juego cuando timer cuando llega a 15 por segunda vez
        if timerNivel >= 15 and estado == "jugandoNivel2":
            estado = "ganado"
            contadorNivel2 = 100 * contadorVidas
            timerNivel = 0

        contadorFinal = contadorNivel1 + contadorNivel2

        # Añadir el estado actual al registro
        if estado == "perdido" or estado == "ganado":
            estados.write("Estado: " + estado + "\t" + "Puntaje: " + str(contadorFinal) + "\n")

    pygame.quit()   # termina pygame

# Función principal
def main():
    dibujar()


main()