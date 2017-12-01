#Anaid Fernanda Labat González A01746289
import pygame



# Dimensiones de la pantalla

ANCHO = 800
ALTO = 600

# Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


def dibujarMenu(ventana, botonJugar, botonV,botonCred,botonSalir):
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonV.image, botonV.rect)
    ventana.blit(botonCred.image, botonCred.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)
def jugando(ventana,ahorcado,abecedario,botonReturn,botonSalir,botonCreditos):
    ventana.blit(ahorcado.image,ahorcado.rect)
    ventana.blit(abecedario.image, abecedario.rect)
    ventana.blit(botonReturn.image, botonReturn.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)
    ventana.blit(botonCreditos.image, botonCreditos.rect)
def puntos(ventana,trofeo,botonReturn,botonSalir,botonCreditos):
    ventana.blit(trofeo.image,trofeo.rect)
    ventana.blit(botonReturn.image, botonReturn.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)
    ventana.blit(botonCreditos.image, botonCreditos.rect)
def creditos(ventana,botonReturn,botonSalir,tec):
    ventana.blit(botonReturn.image, botonReturn.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)
    ventana.blit(tec.image,tec.rect)
def dibujar():
    pygame.mixer.init()
    pygame.mixer.music.load("piratas.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.20)
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    pygame.display.set_caption("Juego de ahorcado: Animales")

    reloj = pygame.time.Clock() # Para limitar los fpsestado = "menu"  # jugando, fin
    termina=False


    estado = "menu"  # jugando, fin


    # Cargar botones
    imgBtnJugar = pygame.image.load("botonJugar.png")
    imgBtnPMayor=pygame.image.load("botonPuntajes.png")
    imgAhorcado = pygame.image.load("ahorcado.png")
    imgAbecedario=pygame.image.load("abecedario.jpg")
    imgTrofeo=pygame.image.load("trofeo.png")
    imgTec = pygame.image.load("tec.jpg")
    imgBtnReturn=pygame.image.load("return.png")
    imgBtnSalir=pygame.image.load("salir.jpg")
    imgBtnCreditos=pygame.image.load("creditos.jpg")
    imgBtnCred = pygame.image.load("cred.jpg")
    # Sprite
    ahorcado = pygame.sprite.Sprite()
    ahorcado.image = imgAhorcado
    ahorcado.rect = imgAhorcado.get_rect()
    ahorcado.rect.left = ANCHO // 2 - ahorcado.rect.width // 2-250
    ahorcado.rect.top = ALTO // 2 - ahorcado.rect.height // 2 -50

    abecedario = pygame.sprite.Sprite()
    abecedario.image = imgAbecedario
    abecedario.rect = imgAbecedario.get_rect()
    abecedario.rect.left = ANCHO // 2 - abecedario.rect.width // 2 + 200
    abecedario.rect.top = ALTO // 2 - abecedario.rect.height // 2 + 200

    trofeo = pygame.sprite.Sprite()
    trofeo.image = imgTrofeo
    trofeo.rect = imgTrofeo.get_rect()
    trofeo.rect.left = ANCHO // 2 - trofeo.rect.width // 2 -200
    trofeo.rect.top = ALTO // 2 - trofeo.rect.height // 2 +50

    tec= pygame.sprite.Sprite()
    tec.image = imgTec
    tec.rect = imgTec.get_rect()
    tec.rect.left = ANCHO // 2 - tec.rect.width // 2 +100
    tec.rect.top = ALTO // 2 - tec.rect.height // 2

    botonReturn = pygame.sprite.Sprite()
    botonReturn.image = imgBtnReturn
    botonReturn.rect = imgBtnReturn.get_rect()
    botonReturn.rect.left = ANCHO // 2 - botonReturn.rect.width // 2 +325
    botonReturn.rect.top = ALTO // 2 - botonReturn.rect.height // 2 -275

    botonCreditos = pygame.sprite.Sprite()
    botonCreditos.image = imgBtnCreditos
    botonCreditos.rect = imgBtnCreditos.get_rect()
    botonCreditos.rect.left = ANCHO // 2 - botonCreditos.rect.width // 2 + 225
    botonCreditos.rect.top = ALTO // 2 - botonCreditos.rect.height // 2 - 275

    botonCred = pygame.sprite.Sprite()
    botonCred.image = imgBtnCred
    botonCred.rect = imgBtnCred.get_rect()
    botonCred.rect.left = ANCHO // 2 - botonCred.rect.width // 2 + 300
    botonCred.rect.top = ALTO // 2 - botonCred.rect.height // 2 - 275

    botonSalir = pygame.sprite.Sprite()
    botonSalir.image = imgBtnSalir
    botonSalir.rect = imgBtnSalir.get_rect()
    botonSalir.rect.left = ANCHO // 2 - botonSalir.rect.width // 2 +375
    botonSalir.rect.top = ALTO // 2 - botonSalir.rect.height // 2 -275

    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2 -25

    botonPuntajes=pygame.sprite.Sprite()
    botonPuntajes.image = imgBtnPMayor
    botonPuntajes.rect = imgBtnPMayor.get_rect()
    botonPuntajes.rect.left=ANCHO // 2 - botonPuntajes.rect.width //2
    botonPuntajes.rect.top= ALTO // 2 - botonPuntajes.rect.height // 2 +100
    while not termina:

        # Procesa los eventos que recibe

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana
                            estado = "jugando"

                if estado=="menu":
                    xb,yb,anchoB,altoB=botonPuntajes.rect
                    if xm>=xb and xm<=xb + anchoB:
                        if ym>= yb and ym<=yb + altoB:
                            estado="puntos"
                if estado=="menu":
                    xb,yb,anchoB,altoB=botonCred.rect
                    if xm>=xb and xm<=xb + anchoB:
                        if ym>= yb and ym<=yb + altoB:
                            estado="creditos"
                if estado == "menu":
                    xb, yb, anchoB, altoB = botonSalir.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            termina=True

                if estado == "jugando":
                    xb, yb, anchoB, altoB = botonReturn.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "menu"
                if estado == "jugando":
                    xb, yb, anchoB, altoB = botonSalir.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            termina = True
                if estado == "jugando":
                    xb, yb, anchoB, altoB = botonCreditos.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "creditos"

                if estado == "puntos":
                    xb, yb, anchoB, altoB = botonReturn.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "menu"

                if estado == "puntos":
                    xb, yb, anchoB, altoB = botonSalir.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            termina=True

                if estado == "puntos":
                    xb, yb, anchoB, altoB = botonCreditos.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado="creditos"

                if estado == "creditos":
                    xb, yb, anchoB, altoB = botonSalir.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            termina=True
                if estado == "creditos":
                    xb, yb, anchoB, altoB = botonReturn.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "menu"

        ventana.fill(NEGRO)


        if estado=="menu":
            dibujarMenu(ventana,botonJugar, botonPuntajes,botonCred,botonSalir)
            fuente = pygame.font.SysFont("Broadway", 45)
            texto = fuente.render('Ahorcado : Animales', True, ROJO)
            ventana.blit(texto, [150, 100])
        elif estado=="jugando":
            jugando(ventana,ahorcado,abecedario,botonReturn,botonSalir,botonCreditos)
            fuente = pygame.font.SysFont("Broadway", 40)
            texto = fuente.render('Presiona una letra', True, AZUL)
            ventana.blit(texto, [50, 450])
            fuente = pygame.font.SysFont("Broadway", 40)
            texto = fuente.render(' en tu teclado', True, AZUL)
            ventana.blit(texto, [85, 500])
        elif estado=="puntos":
            puntos(ventana,trofeo,botonReturn,botonSalir,botonCreditos)
            fuente = pygame.font.SysFont("Broadway", 70)
            texto = fuente.render('Mejores puntajes:', True, VIOLETA)
            ventana.blit(texto, [55, 100])
        elif estado=="creditos":
            creditos(ventana,botonSalir,botonReturn,tec)
            fuente = pygame.font.SysFont("Broadway", 40)
            texto = fuente.render('Anaid Fernanda Labat González', True, VERDE)
            ventana.blit(texto, [55, 100])
            fuente = pygame.font.SysFont("Broadway", 40)
            texto = fuente.render('A01746289', True, VERDE)
            ventana.blit(texto, [55, 200])
            fuente = pygame.font.SysFont("Broadway", 20)
            texto = fuente.render('ISDR', True, VERDE)
            ventana.blit(texto, [55, 300])
            fuente = pygame.font.SysFont("Broadway", 20)
            texto = fuente.render('Fundamentos de programación', True, VERDE)
            ventana.blit(texto, [55, 400])

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps


    pygame.quit()   # termina pygame





def main():
    dibujar()
main()

