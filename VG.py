import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
imgDerecha = 2
imgIzquierda = 2
TIEMPO_ENTRE_FRAMES = 0.1
TIEMPO_TOTAL = imgDerecha * TIEMPO_ENTRE_FRAMES
TIEMPO_TOTAL1 = imgIzquierda * TIEMPO_ENTRE_FRAMES
x = 0


# Dibuja los botones de jugar e información
def dibujarMenu(ventana, botonJugar, botonInformacion):
    ventana.blit (botonJugar.image, botonJugar.rect)
    ventana.blit (botonInformacion.image, botonInformacion.rect)

    # Dibuja el botón de retroceso para volver al menú desde información


def dibujarRetroceso(ventana, Atras):
    ventana.blit (Atras.image, Atras.rect)


def dibujarPausa(ventana):
    pass


# Dibuja los chilaquiles
def dibujarJuego(ventana, listaObstaculos, lista69):
    for enemigo in listaObstaculos:
        ventana.blit (enemigo.image, enemigo.rect)

    for k in lista69:
        ventana.blit (k.image, k.rect)


# Dibuja el personaje jugable
def crearListaSprites():
    lista = []
    for i in range (imgDerecha):
        nombre = "M/Sprite-" + str (i) + ".png"
        imagen = pygame.image.load (nombre)
        spriteAnimacion = pygame.sprite.Sprite ()
        spriteAnimacion.image = imagen
        spriteAnimacion.rect = imagen.get_rect ()
        spriteAnimacion.rect.left = ANCHO - 780
        spriteAnimacion.rect.top = ALTO / 1.25
        lista.append (spriteAnimacion)
    return lista


def obtenerFrame(timerAnimacion, listaSprites):
    indice = int (timerAnimacion / TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]


# Genera enemigos en la pantalla jugando
def generarChilaquil(listaObstaculos, imgObstaculos):
    cx = randint (20, ANCHO - 128)
    cy = 0
    chilaquil = pygame.sprite.Sprite ()
    chilaquil.image = imgObstaculos
    chilaquil.rect = imgObstaculos.get_rect ()
    chilaquil.rect.left = cx
    chilaquil.rect.top = cy
    listaObstaculos.append (chilaquil)


# Hace que los objetos caigan
def caerChilaquil(lista69, listaSprites):

    for sesentaynueve in (lista69):
        sesentaynueve.rect.top += 10
        if sesentaynueve.rect.top < 0:
            lista69.remove (sesentaynueve)
            continue
        borrarsesentaynueve = False
        for i in range (len (listaSprites) - 1, -1, -1):
            enemigo = listaSprites[i]
            if sesentaynueve.rect.colliderect (enemigo):
                listaSprites.remove (enemigo)
        if borrarsesentaynueve:
            lista69.remove (sesentaynueve)



# Genera los 69's
def generarSesentaynueve(lista69, img69):
    cx = randint (20, ANCHO - 128)
    cy = 0
    sesentaynueve = pygame.sprite.Sprite ()
    sesentaynueve.image = img69
    sesentaynueve.rect = img69.get_rect ()
    sesentaynueve.rect.left = cx
    sesentaynueve.rect.top = cy
    lista69.append (sesentaynueve)


def moverJugador(dx, listaSprites):
    for k in listaSprites:
        if k.rect.left > 10 and k.rect.left + k.rect.width < 790:
            if k.rect.left + dx > 10 and k.rect.left + dx + k.rect.width < 790:
                listaSprites[0].rect.left += dx
                listaSprites[1].rect.left += dx


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init ()  # Inicializa pygame
    ventana = pygame.display.set_mode ((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock ()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    # Animación
    listaSprites = crearListaSprites ()
    timerAnimacion = 0

    estado = "menu"
    # Imágenes
    img = pygame.image.load ("button_jugar.png")
    botonJugar = pygame.sprite.Sprite ()
    botonJugar.image = img
    botonJugar.rect = img.get_rect ()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2
    # Imagen 2
    img1 = pygame.image.load ("Fondo juego.png")
    img2 = pygame.image.load ("button_informacion.png")
    botonInformacion = pygame.sprite.Sprite ()
    botonInformacion.image = img2
    botonInformacion.rect = img2.get_rect ()
    botonInformacion.rect.left = ANCHO // 2 - botonJugar.rect.width / 2.5
    botonInformacion.rect.top = ALTO / (1.3) - botonJugar.rect.height // 3
    informacion = pygame.image.load ("informacion.jpg")
    # Imagen 3
    img3 = pygame.image.load ("button_atras.png")
    Atras = pygame.sprite.Sprite ()
    Atras.image = img3
    Atras.rect = img3.get_rect ()
    Atras.rect.left = ANCHO // (40)
    Atras.rect.top = 0
    img4 = pygame.image.load ("button_pausa.png")
    img5 = pygame.image.load ("Fondo.jpg")
    # Imagen 6
    img6 = pygame.image.load ("button_volver-a-jugar.png")
    Vaj = pygame.sprite.Sprite ()
    Vaj.image = img6
    Vaj.rect = img6.get_rect ()
    Vaj.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    Vaj.rect.top = ALTO // 2 - botonJugar.rect.height // 2

    # Obstáculos
    listaObstaculos = []
    imgObstaculos = pygame.image.load ("large.png")
    generarChilaquil (listaObstaculos, imgObstaculos)
    # 69's
    lista69 = []
    img69 = pygame.image.load ("Enemigo.png")
    generarSesentaynueve (lista69, img69)

    # Tiempo
    timer = 0
    x = 0
    mover = False
    vidas = 3

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos ()
                if estado == "menu":
                    xb, yb, anchoB, altoB = botonInformacion.rect
                if xm >= xb and xm <= xb + anchoB:
                    if ym >= yb and ym <= yb + altoB:
                        estado = "informacion"
                        if estado == "informacion":
                            xb, yb, anchoB, altoB = Atras.rect
                        if xm >= xb and xm <= xb + anchoB:
                            if ym >= yb and ym <= yb + altoB:
                                estado = "menu"
                if estado == "menu":
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugando"
                        elif estado == "jugando":
                            enemigo = pygame.sprite.Sprite ()
                            enemigo.image = img69
                            enemigo.rect = img69.get_rect ()
                            enemigo.rect.left = xm
                            enemigo.rect.top = ym
                            lista69.append (enemigo)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    dx = 10
                    mover = True
                if evento.key == pygame.K_LEFT:
                    dx = -10
                    mover = True
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    mover = False
                if evento.key == pygame.K_LEFT:
                    mover = False
                    if vidas == 0:
                            estado = "gameover"
                            xb, yb, anchoB, altoB = botonJugar.rect
                            if xm >= xb and xm <= xb + anchoB:
                                if ym >= yb and ym <= yb + altoB:
                                    pass

        # Borrar pantalla
        ventana.fill (BLANCO)

        fuente = pygame.font.SysFont ("monosspace", 48)
        texto = fuente.render ("Vidas:)" + str (timer), 1, VERDE_BANDERA)

        timer += 1 / reloj.tick (40)
        if timer >= 2:
            timer = 0
            generarChilaquil (listaObstaculos, imgObstaculos)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            ventana.blit (img1, (0, 0))
            dibujarMenu (ventana, botonJugar, botonInformacion)

        elif estado == "jugando":
            ventana.blit (img5, (0, 0))
            dibujarJuego (ventana, listaObstaculos, lista69)
            generarChilaquil (listaObstaculos, imgObstaculos)
            generarSesentaynueve (lista69, img69)

            frameActual = obtenerFrame (timerAnimacion, listaSprites)
            ventana.blit (frameActual.image, frameActual.rect)
            if mover:
                moverJugador (dx, listaSprites)
            frameActual = obtenerFrame (timerAnimacion, listaSprites)
            ventana.blit (frameActual.image, frameActual.rect)
            caerChilaquil (lista69, listaSprites)
            pygame.display.flip ()  # Actualiza trazos
            timerAnimacion += reloj.tick (40) / 1000
            if timerAnimacion >= TIEMPO_TOTAL:
                timerAnimacion = 0


            pygame.display.flip ()  # Actualiza trazos


        elif estado == "informacion":
            ventana.blit (informacion, (0, 0))
            dibujarRetroceso (ventana, Atras)

        pygame.display.flip ()  # Actualiza trazos
        reloj.tick (40)  # 40 fps

    pygame.quit ()  # termina pygame


def main():
    dibujar ()


main ()
