import pygame
from pygame.locals import *
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)
def dibujarJuego(ventana, listaBalas,malo1,malo2,listaBalas2):
    ventana.blit(malo1.image, malo1.rect)
    ventana.blit(malo2.image, malo2.rect)
    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)
    for bala2 in listaBalas2:
        ventana.blit(bala2.image,bala2.rect)
def actualizarJuego(listaBalas,malo1,malo2,listaBalas2):
    nuevaLista=[]

    malo1.rect.top -= 5
    if malo1.rect.top <= 1:
        malo1.rect.top = ALTO // 2
    malo2.rect.top -= 5
    if malo2.rect.top <= 1:
        malo2.rect.top = ALTO // 2
    for bala in listaBalas:
        bala.rect.top+=40
    for bala2 in listaBalas2:
        bala2.rect.top+=40
    '''
    for bala in listaBalas:
        if bala.rect.top <= ALTO:
            listaBalas.remove(bala)
            borrarBala=True
            continue
        if borrarBala:
            listaBalas.remove(bala)
    '''
def dibujarFondo(ventana,imagenFondo):
    ventana.blit(imagenFondo,(0,0))

def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar.image,btnJugar.rect)


def generarMalo1():
    imgMalo1 = pygame.image.load("Malo.png")
    malo1 = pygame.sprite.Sprite()  # Sprite
    malo1.image = imgMalo1
    malo1.rect = imgMalo1.get_rect()
    malo1.rect.left = ANCHO - ANCHO//4 - malo1.rect.width // 2
    malo1.rect.top = ALTO // 2 - malo1.rect.height // 2
    return malo1

def generarMalo2():
    imgMalo1 = pygame.image.load("Malo.png")
    malo1 = pygame.sprite.Sprite()  # Sprite
    malo1.image = imgMalo1
    malo1.rect = imgMalo1.get_rect()
    malo1.rect.left = ANCHO // 4 - malo1.rect.width // 2
    malo1.rect.top = ALTO // 2 - malo1.rect.height // 2
    return malo1

def dibujar():
    #Fondo de pantalla al incio
    imagenFondo=pygame.image.load("Fondo.jpg")
    imagenFondoJuego=pygame.image.load("namek.jpg")
    estado = "menu"  # jugando,termina
    # Botones
    imgBotonJugar = pygame.image.load("button_jugar.png")
    btnJugar = pygame.sprite.Sprite()  # SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height // 2
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    imgGoku=pygame.image.load("Goku1.png")
    malo1= generarMalo1()
    malo2 = generarMalo2()
    xGoku=0
    timerTIEMPO=0
    listaBalas=[]
    listaBalas2=[]
    imgBala = pygame.image.load("Haaaaa.png")
    soltarBala=False
    pygame.mixer.init()
    pygame.mixer.music.load("cancion.mp3")
    pygame.mixer.music.play(-1)
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado=="menu":
                    xb,yb,anchoB,altoB=btnJugar.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado="jugando"
            elif evento.type==pygame.KEYDOWN:
                    if evento.key==pygame.K_SPACE:
                            bala1=pygame.sprite.Sprite()
                            bala1.image=imgBala
                            bala1.rect=imgBala.get_rect()
                            bala1.rect.left=malo1.rect.left
                            bala1.rect.top=malo1.rect.top
                            listaBalas.append(bala1)

                            bala2 = pygame.sprite.Sprite()
                            bala2.image = imgBala
                            bala2.rect = imgBala.get_rect()
                            bala2.rect.left = malo2.rect.left
                            bala2.rect.top = malo2.rect.top
                            listaBalas2.append(bala2)
                    if evento.key==pygame.K_ESCAPE:
                        if estado== "Fin" or "Acerca":
                            xb, yb, anchoB, altoB = btnJugar.rect
                            if xm > xb and xm <= xb + anchoB:
                                if ym >= yb and ym <= yb + altoB:
                                    # Cambiar de ventana/estado
                                    estado = "menu"


        # Borrar pantalla

        ventana.fill(VERDE_BANDERA)

        timerTIEMPO += 1/40

        # Dibujar, aquí haces todos los trazos que requieras
        if estado=="menu":
            dibujarFondo(ventana,imagenFondo)
            dibujarMenu(ventana,btnJugar)
        elif estado=="jugando":
            dibujarFondo(ventana,imagenFondoJuego)
            actualizarJuego(listaBalas,malo1,malo2,listaBalas2)
            dibujarJuego(ventana,listaBalas,malo1,malo2,listaBalas2)
            ventana.blit(imgGoku,(xGoku, ALTO - 90))
            xGoku,y= pygame.mouse.get_pos()
            fuente = pygame.font.SysFont("Arial Black", 20)
            tiempo = fuente.render("Tiempo: " + str(("%.2f") % timerTIEMPO), 1, NEGRO)
            ventana.blit(tiempo, (ANCHO - 140, 0))


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()