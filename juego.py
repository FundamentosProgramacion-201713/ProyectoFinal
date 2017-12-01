import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_LIMON = (0, 255, 0)
ROJO = (255, 0, 0)

movx = 0
movy = 0
derecha = True

# La funcion dibuja la estructura del menu
def estructurar_Menu(ventana, botonJugar,titulo):
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(titulo.image, titulo.rect)

# Se estructura el fondo
def estructurar_Fondo_Menu(ventana, imagenFondo1):
    ventana.blit(imagenFondo1, (0, 0))

#La funcion da la estructura al juego
def estructurar_Juego(ventana, lista_Enemigos, lista_Proyectil):
    global movx, movy, derecha
    for enemigo in lista_Enemigos:
        x, y , alto, ancho = enemigo.rect
        if derecha:
            enemigo.rect = (x + 1, y + movy, alto, ancho)
        else:
            enemigo.rect = (x - 1, y + movy, alto, ancho)
        ventana.blit(enemigo.image, enemigo.rect)
    for lazer in lista_Proyectil:
        ventana.blit(lazer.image, lazer.rect)
    if movx == -200:
        derecha = True
        movy = 15
    else:
        movy = 0
    if movx >= 200:
        derecha = False
        movy = 15
    if derecha:
        movx += 5
    else:
        movx -=5



#La funcion actualiza el lazer
def actualizar_Proyectil(lista_Proyectil, lista_Enemigos):
    for lazer in lista_Proyectil:
        lazer.rect.top -= 20
        if lazer.rect.top <=8:
            lista_Proyectil.remove(lazer)
            continue  #REINICIAR  UN CICLO, REGRESA AL INICIO DEL CICLO
        borrarLazer = False
        for k in range(len(lista_Enemigos)-1,-1,-1):
            alien = lista_Enemigos[k]
            if lazer.rect.colliderect(alien):
                lista_Enemigos.remove(alien)
                borrarLazer = True
                break   #TERMINA EL CICLO
        if borrarLazer:
            lista_Proyectil.remove(lazer)



# La funcion genera a los enemigos
def generar_Enemigos(lista_Enemigos, imagen_Enemigo):
    # Coordeanada horizontal
    for x in range(8):
        # Coordenada vertical
        for y in range(5): #Generar el enemigo en x,y
            coordenadax = 150 + x*70
            coordenaday = 50 + y*80
            alien = pygame.sprite.Sprite()
            alien.image = imagen_Enemigo
            alien.rect = imagen_Enemigo.get_rect()
            alien.rect.left = (coordenadax - alien.rect.width // 2)
            alien.rect.top = coordenaday - 50
            lista_Enemigos.append(alien)



# La funcion analiza el puntaje si se le acierta al enemigo
def analizarPuntaje(lista_Proyectil, lista_Enemigos, Puntaje):
    for lazer in lista_Proyectil:
        lazer.rect.top -= 20
        #Toma de decision, si no le atina al alien pierde un punto
        if lazer.rect.top <= 10:
            Puntaje=Puntaje-1

        for k in range(len(lista_Enemigos) - 1, -1,-1):
            enemigo = lista_Enemigos[k]
            #Si le atina al enemigo entonces gana 25 puntos
            if lazer.rect.colliderect(enemigo):
                Puntaje = Puntaje + 25

    return Puntaje



def dibujar():
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado = "menu"

    #FONDOS
    y = 0
    imagen_Fondo_inicio = pygame.image.load("fondo1.jpg")
    imagen_Fondo_juego = pygame.image.load("fondojuego.jpg")


    #Cargar imagen del boton jugar
    imagen_BotonJugar = pygame.image.load("boton_jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imagen_BotonJugar
    botonJugar.rect = imagen_BotonJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2 + 100


    #Cargar imagen del titulo
    imagen_Titulo = pygame.image.load("titulo.png")
    titulo = pygame.sprite.Sprite()
    titulo.image = imagen_Titulo
    titulo.rect = imagen_Titulo.get_rect()
    titulo.rect.left = ANCHO // 2 - titulo.rect.width // 2
    titulo.rect.top = ALTO // 2 - titulo.rect.height // 2 - 100


    # Cargar imagen del boton puntuaciones
    imgagen_BotonPuntajes = pygame.image.load("boton_puntuaciones.png")
    botonPuntajes = pygame.sprite.Sprite()
    botonPuntajes.image = imgagen_BotonPuntajes
    botonPuntajes.rect = imgagen_BotonPuntajes.get_rect()
    botonPuntajes.rect.left = ANCHO // 2 - botonPuntajes.rect.width // 2 - 250
    botonPuntajes.rect.top = ALTO // 2 - botonPuntajes.rect.height // 2 + 150

    # AQUI VAN LOS ENEMIGOS
    lista_Enemigos = []
    imagen_Enemigo1 = pygame.image.load("alien_1.png")
    generar_Enemigos(lista_Enemigos, imagen_Enemigo1)

    # AQUI VA LA NAVE PRINCIPAL
    imagen_Defensor = pygame.image.load("defensor.png")
    defensor = imagen_Defensor.get_rect()
    defensor.left = ANCHO / 2
    defensor.top = ALTO - 50
    coordenadax_Defensor = 0

    # AQUI VA EL PROYECTIL
    lista_Proyectil = []
    imagen_Proyectil = pygame.image.load("laserdefender.png")

    # PUNTAJE Y CONTADORES
    timer = 0
    Puntaje = 0

    # AQUI VAN LOS SONIDOS Y LA CANCION
    pygame.mixer.init()
    pygame.mixer.music.load("arcadesong.mp3")
    pygame.mixer.music.play(-1)

    efecto_Lazer = pygame.mixer.Sound("laser.wav")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # El usuario hizo click
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()

                # TOMA DE DECISION DEL ESTADO
                if estado == "menu":
                    coordenadaX_Boton, coordenadaY_Boton, anchoBoton, altoBoton = botonJugar.rect


                    if xm >= coordenadaX_Boton and xm <=  coordenadaX_Boton + anchoBoton:
                        if ym >= coordenadaY_Boton and ym <= coordenadaY_Boton + altoBoton:
                            # Cambiar de ventana
                            estado = "jugando"

                # Si se esta jugando se dibuja al enemigo
                elif estado == "jugando":
                    alien1 = pygame.sprite.Sprite()
                    alien1.image = imagen_Enemigo1
                    alien1.rect = imagen_Enemigo1.get_rect()
                    alien1.rect.left = xm - ANCHO // 2
                    alien1.rect.top = ym - ALTO // 2


            # Posicion y disparo del lazer
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    efecto_Lazer.play()
                    lazer = pygame.sprite.Sprite()
                    lazer.image = imagen_Proyectil
                    lazer.rect = imagen_Proyectil.get_rect()
                    lazer.rect.left = coordenadax_Defensor - 8
                    lazer.rect.top = ALTO - lazer.rect.height - 48
                    lista_Proyectil.append(lazer)



        # Borrar pantalla
        ventana.fill(BLANCO)
        timer += 1 / 40


        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            estructurar_Fondo_Menu(ventana,imagen_Fondo_inicio)
            estructurar_Menu(ventana,botonJugar,titulo)

        elif estado == "jugando":
            ventana.blit(imagen_Fondo_juego, (0, y))
            ventana.blit(imagen_Fondo_juego, (0, ALTO + y))
            y -= 1
            if y <= -ALTO:
                y = 0
            (estructurar_Juego(ventana, lista_Enemigos, lista_Proyectil))
            actualizar_Proyectil(lista_Proyectil, lista_Enemigos)
            Puntaje = analizarPuntaje(lista_Proyectil, lista_Enemigos, Puntaje)

            # Dibujar al DEFENSOR
            ventana.blit(imagen_Defensor, (coordenadax_Defensor - 39, ALTO - 86))
            coordenadax_Defensor, yDefensor = pygame.mouse.get_pos()
            #Informacion acerca de puntos y tiempo
            fuente = pygame.font.SysFont("Helvetica", 20, "negrita cursiva")
            tiempo = fuente.render("Tiempo: " + str(("%.2f") % timer), 1, VERDE_LIMON)
            ventana.blit(tiempo, (40, 5))
            puntos = fuente.render("Puntuación: " + str(Puntaje), 1, VERDE_LIMON)
            ventana.blit(puntos, (ANCHO - 250, 5))



        # Actualiza trazos
        pygame.display.flip()
        reloj.tick(40)

    # termina pygame
    pygame.quit()


def main():
    dibujar()


main()
