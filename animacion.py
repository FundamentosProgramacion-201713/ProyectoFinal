#encoding UTF-8
#Autor: Javier León Alcántara
#Proyecto final Videojuego

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)

NUM_IMAGENES = 2                    # Numero de disfraces
TIEMPO_ENTRE_FRAMES = 0.1           # Tiempo entre cada imagen de la animación
TIEMPO_TOTAL = NUM_IMAGENES * TIEMPO_ENTRE_FRAMES

x = 100
y = 200

def crearListaSprites():
    lista = []

    for i in range(NUM_IMAGENES):
        nombre = "disfraces/imagen-"+str(i)+".png"
        imagen = pygame.image.load(nombre)
        imagen = pygame.transform.scale(imagen,(100,79))
        sprAnimacion = pygame.sprite.Sprite()
        sprAnimacion.image = imagen
        sprAnimacion.rect = imagen.get_rect()
        sprAnimacion.rect.left = x
        sprAnimacion.rect.top = y
        lista.append(sprAnimacion)

    return lista


def obtenerFrame(timerAnimacion, listaSprites):
    indice = int(timerAnimacion/TIEMPO_ENTRE_FRAMES)
    return listaSprites[indice]



def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    pygame.display.set_caption("Juego Javier León")
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Animación del murcielago (sprites)
    listaSprites = crearListaSprites()
    timerAnimacion = 0



    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True


        # Borrar pantalla
        ventana.fill(BLANCO)



        # Dibujar, aquí haces todos los trazos que requieras

        frameActual = obtenerFrame(timerAnimacion, listaSprites)
        img = frameActual.image
        ventana.blit(img, frameActual.rect)


        pygame.display.flip()   # Actualiza trazos
        timerAnimacion += reloj.tick(40) / 1200  # Tiempo exacto entre frames
        if timerAnimacion >= TIEMPO_TOTAL:
            timerAnimacion = 0

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()