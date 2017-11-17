# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)


def dibujarJuego(ventana, btnJugar, lista, listaBalas):
    btnJugar.rect.left = ANCHO-btnJugar.rect.width
    btnJugar.rect.top = ALTO-btnJugar.rect.height
    ventana.blit(btnJugar.image,btnJugar.rect)
    #DIBUJAMOS TODOS LOS ENEMIGOS
    for enemigo in lista:
        ventana.blit(enemigo.image,enemigo.rect)
    for bala in lista:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas,listaEnemigos):
    for bala in listaBalas:
        bala.rect.top -= 5
        #ELIMINAR BALAS
    for k in range(-1,-len(listaBalas)-1,-1):
        if listaBalas[k].rect.top >= -16:
            listaBalas.remove(k)
    #VERIFICAR COLISIONES
    for bala in listaEnemigos:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo):
                #LE PEGÓ!!!!!!!!!!
                #INCORRECTO
                listaEnemigos.remove(enemigo)



def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    #Estados
    estado = "menu" #jugando, termina

    #Botones
    imgBotonJugar = pygame.image.load("Botonjugar.png")
    btnJugar = pygame.sprite.Sprite() #SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect() #rect(x,y,width,lenght)
    btnJugar.rect.left = ANCHO//2  - btnJugar.rect.width//2 #LEFT ES EL EJE X
    btnJugar.rect.top = ALTO//2  - btnJugar.rect.height//2#LEFT ES EL EJE Y

    #ENEMIGOS
    listaEnemigos = []

    #BALAS
    listaBalas = []
    imgBala = pygame.image.load("Bala.png")


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()  # Obtener coordenadas mouse
                if estado == "menu":

                    xb, yb, anchoB, altoB = btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado = "jugando"
                elif estado == "jugando":
                    nuevo = pygame.sprite.Sprite()
                    nuevo.image = imgBotonJugar
                    nuevo.rect = imgBotonJugar.get_rect()
                    nuevo.rect.left = xm
                    nuevo.rect.top = ym
                    listaEnemigos.append(nuevo)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    #Crear bala
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = ANCHO//2
                    bala.rect.top = ALTO - bala.rect.height
                    listaBalas.append(bala)


        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana,btnJugar)
        elif estado == "jugando":
            actualizarBalas(listaBalas)
            dibujarJuego(ventana, btnJugar, listaEnemigos,listaBalas)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()