# encoding: UTF-8
# Autor: Luis Alfonso Alcántara López Ortega

import pygame

ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)

# Las dimensiones de la nave
xNave = 150
yNave = 120

puntuacion = 0
disparos = []

# Variables declaradas de las imágenes que se usarán
imagenFondo = pygame.image.load("fondo.png")
naveImagen = pygame.image.load("nave.PNG")
alien = pygame.image.load("alien2.png")


# Mensaje en Pantalla
def mensajeEnPantalla(m, ventana, x, y, tamano):
    font = pygame.font.SysFont("Arial", tamano)
    texto = font.render(m ,True, (255,255,255))
    ventana.blit(texto, [x,  y])
    return texto

# Valida los controles de la nave
def validarControlesNave(dx, dy, disparos):
    # Teclas presionadas
    teclasPresionadas = pygame.key.get_pressed()

    # Verificar si alguna tecla del control fue presionada
    if teclasPresionadas[pygame.K_LEFT] and dx > 0:
        dx -= 10
    if teclasPresionadas[pygame.K_RIGHT] and dx < ANCHO - xNave:
        dx += 10
    if teclasPresionadas[pygame.K_UP] and dy > 0:
        dy -= 10
    if teclasPresionadas[pygame.K_DOWN] and dy < ALTO - yNave:
        dy += 10
    if teclasPresionadas[pygame.K_a]:
        disparos.append({"x1": dx + 30, "x2": dx + 115, "y": dy})
    lista = [dx, dy, disparos]
    return lista

# Esta función permite ir recorriendo los disparos que realiza la nave y los muestra en la pantalla
def disparar(disparos, ventana):
    global puntuacion
    if len(disparos) >= 1:
        for x in range(len(disparos)):
            pygame.draw.rect(ventana, BLANCO, (disparos[x]["x1"], disparos[x]["y"] - 10, 1, 10))
            pygame.draw.rect(ventana, BLANCO, (disparos[x]["x2"], disparos[x]["y"] - 10, 1, 10))
        for x in range(len(disparos)):
            if disparos[x]["x1"] <= 300 and disparos[x]["x1"] >= 250:
                puntuacion += 10
            disparos[x]["y"] -= 15

#Inicia el pygame con la pantalla y el menú
def eliminarDisparosFueraDeRango(longitud, contador, resta, disparos):
    disparosNuevos = []
    while contador < longitud:
        if disparos[contador]["y"] > 0:
            disparosNuevos.append(disparos[contador])
        contador += 1
    return disparosNuevos

def iniciar():
    global disparos
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Galaluich")
    reloj = pygame.time.Clock()
    termina = False

    # Las dimensiones del enemigo
    yAlien = 37

    # Posición de la nave inicial
    dx = 400
    dy = 400

    # Posición del enemigo inicial
    dAlien = 15
    menu = True

    # Aquí va el menú inicial
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(0)
    while menu:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                menu = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
                pygame.quit()
                quit()

        ventana.blit(imagenFondo, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((ANCHO // 2), (ALTO // 2))
        ventana.blit(TextSurf, TextRect)
        '''
        mensajeEnPantalla("Space Invaders", ventana, 150, 100, 100)
        mensajeEnPantalla("Hecho por Luis Alcántara", ventana, 150, 200, 50)
        mensajeEnPantalla("Presiona SPACE para Comenzar", ventana, 150, 400, 50)
        mensajeEnPantalla("Presiona Q para Salir", ventana, 150, 450, 50)
        '''

        pygame.display.flip()
        reloj.tick(40)

    # Sprites
    nave = pygame.sprite.Sprite()
    nave.image = naveImagen
    nave.rect = naveImagen.get_rect()
    nave.rect.left = ANCHO // 2 - nave.rect.width // 2
    nave.rect.top = ALTO // 2 - nave.rect.height // 2


    listaDeSprites = pygame.sprite.Group()
    vidas = 3
    while not termina:
        # Registra cada evento que ocurre en Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Verificar controles de la nave y borrar disparos fuera del rango
        valoresNave = validarControlesNave(dx, dy, disparos)
        dx = valoresNave[0]
        dy = valoresNave[1]
        disparos = valoresNave[2]
        longitud = len(disparos)
        contador = 0
        resta = 0

        disparos = eliminarDisparosFueraDeRango(longitud, contador, resta, disparos)

        # Actualización de la nave y el enemigo
        ventana.blit(imagenFondo, (0, 0))
        ventana.blit(nave, (dx, dy))
        mensajeEnPantalla("Vidas: %d" % vidas, ventana, 10, 10, 40)
        mensajeEnPantalla("Puntuación: %d" % puntuacion, ventana, 550, 10, 40)

        # Valida que haya disparos, en caso de que haya los muestra en la pantalla y actualiza el puntaje
        disparar(disparos, ventana)

        pygame.display.flip()
        reloj.tick(40)
    print(disparos)
    pygame.time.delay(100)
    pygame.quit()

def main():
    iniciar()
main()