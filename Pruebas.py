import pygame

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (255, 255, 255)
ROJO = (0, 0, 0)

def rebotar():
    x = ANCHO//2
    y = ALTO//2
    radio = 20
    DX = 15 # derecha(suma)
    DY = 10
    #raqueta
    ALTO_RAQUETA = ALTO//4
    ANCHO_RAQUETA = ALTO_RAQUETA//5
    yRaqueta = y - ALTO_RAQUETA // 2
    xRaqueta = ANCHO_RAQUETA
    moverRaqueta = False
    DY_Raqueta = 20
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    yRaqueta -= 30
                elif evento.key == pygame.K_DOWN:
                    yRaqueta +=30

        # Cambiar color de pantalla en fps
        ventana.fill(VERDE_BANDERA)

        #dibujar raqueta
        pygame.draw.rect(ventana, ROJO,(xRaqueta,yRaqueta,ANCHO_RAQUETA, ALTO_RAQUETA))
        #dibujar pelota
        pygame.draw.circle(ventana, ROJO, (x,y),radio)
        x += DX    #x = x + 2
        if x>=ANCHO-radio:
            DX = -DX
        y += DY
        if y==ALTO-radio or y==radio:
            DY = -DY

        # Prueba colisión con raqueta
        if x<=ANCHO_RAQUETA+30 and y>=yRaqueta and y<=yRaqueta+ALTO_RAQUETA:
            DX = -DX
        # yRaqueta = y - ALTO_RAQUETA // 2

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    rebotar()