#encoding: UTF-8
#Sebastian Morales Martin
#Juego AimTrain, Espero que lo disfrute :-)





import pygame
import random





# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)
pygame.font.init()
font = pygame.font.SysFont('Consolas', 48)

def dibujarJuego(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
    #btnEnemigo = btnEnemigo.image
    #btnEnemigo.rect.left = ANCHO//2 - btnEnemigo.rect.width
    #btnEnemigo.rect.top = ALTO//2 - btnEnemigo.rect.height

    #Dibujar todos los enemigos




def dibujarMenu(ventana, btnJugar, fondo):
    ventana.blit(fondo.image, fondo.rect)
    ventana.blit(btnJugar.image, btnJugar.rect)

def generarEnemigos(listaEnemigos, imgEnemigo):
    for x in range(5):
        for y in range(4):

            cx = 50 + x * 150
            cy = 50 + y * 100
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            listaEnemigos.append(enemigo)




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
    btnJugar.rect = imgBotonPlay.get_rect(center=(ANCHO//2, ALTO//2))

    #enemigo



    #fondo
    imgFondo = pygame.image.load("gun range.jpg")
    fondo = pygame.sprite.Sprite()
    fondo.image = imgFondo
    fondo.rect = imgFondo.get_rect(center=(ANCHO//2, ALTO//2))

    #enemigos
    listaEnemigos= []
    imgBlanco = pygame.image.load("blancoEnemigo.png")
    generarEnemigos(listaEnemigos, imgBlanco)

    #musica y efectos
    pygame.mixer.init()
    pygame.mixer.music.load("hotPursuit.mp3")
    pygame.mixer.music.play(-1)


    efecto = pygame.mixer.Sound("disparo.wav")






    timer = 0
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()

                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    if mouseX>=xb and mouseX <=xb + anchoB:
                        if mouseY >= yb and mouseY <= yb + altoB:
                            pygame.draw.rect(ventana, ROJO, ((ALTO // 2) + 55, (ALTO // 2) - 20, 90, 40), 1)
                            estado = "jugando"
                elif estado == "jugando":
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        efecto.play()
                        generarEnemigos(listaEnemigos, imgBlanco)







        # Borrar pantalla
        ventana.fill(NEGRO)

        timer += 1/40
        if timer >= 3:   #genera Enemigos cada 5 segundos y actualiza el timer a 0

            timer = 0
            generarEnemigos(listaEnemigos, imgBlanco)
            #generarEnemigos(listaEnemigos, imgBlanco)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":

            dibujarMenu(ventana, btnJugar, fondo)
            ventana.blit(font.render("AimTrain", True, (BLANCO)), (32, 48))

        elif estado == "jugando":
            dibujarJuego(imgBlanco, listaEnemigos)








        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()