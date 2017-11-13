#encoding: UTF-8
#Sebastian Morales Martin
#Juego AimTrain, Espero que lo disfrute :-)




import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def dibujarJuego(ventana, btnJugar, lista):
    btnJugar.rect.left = ANCHO - btnJugar.rect.width
    btnJugar.rect.top = ALTO - btnJugar.rect.height
    ventana.blit(btnJugar.image, btnJugar.rect)
    #Dibujar todos los enemigos
    for enemigo in lista:
        ventana.blit(enemigo.image, enemigo.rect)


def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)


def generarEnemigos(listaEnemigos, imgBotonPlay):
    for x in range(3):
        for y in range(3):
            cx = 50+ x*260
            cy = 100 + y*100
            nuevo = pygame.sprite.Sprite()
            nuevo.image = imgBotonPlay
            nuevo.rect = imgBotonPlay.get_rect
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaEnemigos.append(nuevo)




def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    #Estados
    estado= "menu" #jugando, termina

    #botones
    imgBotonPlay = pygame.image.load("botonPlay.png")
    btnJugar =pygame.sprite.Sprite() #SPRITE
    btnJugar.image = imgBotonPlay
    btnJugar.rect = imgBotonPlay.get_rect(center = (ANCHO//2, ALTO//2))

    #enemigos
    listaEnemigos= []
    generarEnemigos(listaEnemigos, imgBotonPlay)

    #balas
    listaBalas = []


    timer = 0
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":

                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm>=xb and xm <=xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugando"
                elif estado == "jugando":
                    nuevo= pygame.sprite.Sprite()
                    nuevo.image= imgBotonPlay
                    nuevo.rect = imgBotonPlay.get_rect
                    nuevo.rect.left = xm
                    nuevo.rect.top= ym

                    listaEnemigos.append(nuevo)


        # Borrar pantalla
        ventana.fill(BLANCO)

        timer += 1/40
        if timer > 2:
            #acciones
            timer = 0

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, btnJugar)
        elif estado == "jugando":
            dibujarJuego(ventana, btnJugar, listaEnemigos)





        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()