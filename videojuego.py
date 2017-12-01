# encoding: utf-8
# autor: viviana osorio nieto
# juego
import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
puntos = []
marcador = []
vidas = ['1', '2', '3']


# mostrar enemigos y balas en la pantalla
def dibujarJuego(ventana, ListaEnemigos, listaBala):
    for enemigo in ListaEnemigos:
        actualizarEnemigos(ListaEnemigos)
        ventana.blit(enemigo.image, enemigo.rect)
    for bala in listaBala:
        actualizarBalas(listaBala, ListaEnemigos)
        ventana.blit(bala.image, bala.rect)

        # agregar enemigos a una lista para despues mostrarlos en pantalla


def generarEnemigos(ListaEnemigos):
    imagen_enemigo = pygame.image.load("enemigo.png")
    for x in range(5):
        for y in range(4):
            # generar enemigo en x,y
            cx = 50 + x * 150
            cy = 50 + y * 80
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imagen_enemigo
            enemigo.rect = imagen_enemigo.get_rect()
            enemigo.rect.left = cx
            enemigo.rect.top = cy
            ListaEnemigos.append(enemigo)


def actualizarEnemigos(ListaEnemigos):
    for enemigo in ListaEnemigos:
        enemigo.rect.top += 1 // 2
        if enemigo.rect.top <= 0:
            ListaEnemigos.remove(enemigo)
            continue  # regresa al inicio del ciclo


# elimina los enemigos y balas que chocaron
def actualizarBalas(listaBalas, ListaEnemigos):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue  # regresa al inicio del ciclo
        borrarBala = False
        for k in range(len(ListaEnemigos) - 1, -1, -1):
            enemigo = ListaEnemigos[k]
            if bala.rect.colliderect(enemigo):
                ListaEnemigos.remove(enemigo)
                puntos.append(1)
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)


def generarEnemigosAzar(ListaEnemigos):
    imagen_enemigo = pygame.image.load("enemigo.png")
    cx = randint(20, ANCHO - 130)
    cy = randint(10, ALTO // 2)
    enemigo = pygame.sprite.Sprite()
    enemigo.image = imagen_enemigo
    enemigo.rect = imagen_enemigo.get_rect()
    enemigo.rect.left = cx
    enemigo.rect.top = cy
    ListaEnemigos.append(enemigo)


# si choca la nave con un enemigo
def colision(ListaEnemigos, font1, ventana, nave):
    a_colision = False
    for k in range(len(ListaEnemigos) - 1):
        enemigo = ListaEnemigos[k]
        if nave.rect.colliderect(enemigo):
            a_colision = True

    return a_colision


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()
    termina = False  #
    estado = "menu"  # jugando, fin

    nivel = '1'
    # spreites
    imagen_boton_jugar = pygame.image.load("boton_jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imagen_boton_jugar
    botonJugar.rect = imagen_boton_jugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2 + 150

    imagen_nave = pygame.image.load("nave.png")
    nave = pygame.sprite.Sprite()
    nave.image = imagen_nave
    nave.rect = imagen_nave.get_rect()
    nave.rect.left = ANCHO // 2
    nave.rect.top = ALTO - 80

    fondo = pygame.image.load("fondo.png")
    imagen_bala = pygame.image.load("bala.jpg")

    # listas,sonido,  musica inicio
    ListaEnemigos = []
    generarEnemigos(ListaEnemigos)
    listaBala = []
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(3)
    soni_ex = pygame.mixer.Sound('explocion.wav')
    level_up = pygame.mixer.Sound('level_up.wav')

    # configuracion de texto
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 40)

    x1 = 0  # mover pantalla
    timer = 0

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchob, altob = botonJugar.rect
                    if xm >= xb and xm <= xb + anchob:
                        if ym >= yb and ym <= yb + altob:  # cambiar de ventana
                            estado = "jugando"
                elif estado == "jugando":
                    generarEnemigos(ListaEnemigos)
            if evento.type == pygame.KEYDOWN:
                (X, Y) = pygame.mouse.get_pos()  # poner balas
                if evento.key == pygame.K_SPACE:
                    Sound = pygame.mixer.Sound('Laser.wav')
                    Sound.play()
                    bala = pygame.sprite.Sprite()
                    bala.image = imagen_bala
                    bala.rect = imagen_bala.get_rect()
                    bala.rect.left = X - bala.rect.width // 2
                    bala.rect.top = Y - bala.rect.height // 2
                    listaBala.append(bala)
                nave.update()
        # Borrar pantalla
        ventana.fill(NEGRO)
        x1 += 7  # mover fondo
        if x1 >= ALTO:
            x1 = 0
        ventana.blit(fondo, (0, 0))
        ventana.blit(fondo, (0, x1 + x1))

        # Dibujar
        if estado == "menu":
            ventana.blit(botonJugar.image, botonJugar.rect)
            nombre = font1.render(('Hero'), 1, BLANCO)
            nombre2 = font2.render(('koalaGames'), 1, BLANCO)
            ventana.blit(nombre, (330, 150))  # muestra el nombre del videojugo
            ventana.blit((nombre2), (326, 250))

            data = open('HighScores.txt', 'r')  # ARCHIVo
            movimiento_y = 0
            lista_data = data.readlines()
            for i in lista_data:
                list(i)
                movimiento_y += 50
                mayor_p = font2.render((str(i)), 1, BLANCO)  # highscores
                ventana.blit(mayor_p, (330, 250 + movimiento_y))
            data.close()


        elif estado == "jugando":

            dibujarJuego(ventana, ListaEnemigos, listaBala)
            a_colision = colision(ListaEnemigos, font1, ventana, nave)
            puntos_actuales = 0
            (x, y) = pygame.mouse.get_pos()  # pos para la nave
            nave.rect.left = x - nave.rect.width // 2
            nave.rect.top = y - nave.rect.height // 2

            explocion_imagen = pygame.image.load('explo.png')
            ex = pygame.sprite.Sprite()
            ex.image = explocion_imagen
            ex.rect = explocion_imagen.get_rect()
            ex.rect.left = x - (ex.rect.width)  # mismo lugar que la nave
            ex.rect.top = y - ex.rect.height

            if a_colision == True:
                vidas.remove(vidas[0])
                soni_ex.play()
                ventana.blit(ex.image, ex.rect)  # si no esta explotando, se enseña la nave
            else:
                ventana.blit(nave.image, nave.rect)

            for i in puntos:
                puntos_actuales = puntos_actuales + i
                marcador.append(puntos_actuales)
            puntaje = font2.render((str(puntos_actuales)), 1, BLANCO)  # muestra el puntaje
            ventana.blit(puntaje, (50, 50))
            if len(vidas) == 0:
                estado = 'gameOver'  # si se acaban las vidas, acaba el juego

            if nivel == '1':
                nivel1 = font2.render('nivel 1 ', 1, BLANCO)  # muestra en que nivel esta
                ventana.blit(nivel1, (50, 550))
                timer += 1 / 50
                if timer >= 2:
                    timer = 0
                    generarEnemigosAzar(ListaEnemigos)
                    if puntos_actuales >= 15:
                        level_up.play(0)
                        nivel = '2'
            elif nivel == '2':
                nivel2 = font2.render('nivel 2 ', 1, BLANCO)  # muestra en que nivel esta
                ventana.blit(nivel2, (50, 550))
                timer += 1 / 10  # pone enemigos mas rapido
                if timer >= 2:
                    timer = 0
                    generarEnemigosAzar(ListaEnemigos)

                    if puntos_actuales >= 30:
                        nivel = '3'
            elif nivel == '3':
                estado = 'gano'
        elif estado == 'gameOver':  # perdio
            text = font1.render(('Game Over'), 1, BLANCO)  # mensaje
            ventana.blit(text, (250, 180))
            maximo = [max(marcador)]  # sacamos el maximo puntaje
            for i in maximo:
                if i not in lista_data:  # que no se repita
                    lista_data.append(i)
            tuple(lista_data)

            archivo = open('HighScores.txt', 'w')  # abrimos el archivo

            for i in lista_data:
                archivo.write(str(i) + '\n')  # adjuntamos el puntaje al archivo
            archivo.close()
            s_op = font2.render(('there aren´t second chances in life'), 1, BLANCO)
            ventana.blit(s_op, (200, 280))
        elif estado == 'gano':
            gano = font2.render(('The B team is here'), 1, BLANCO)
            gano2 = font2.render((' Go rest yourself.'), 1, BLANCO)
            gano3 = font2.render((' You did great...'), 1, BLANCO)
            ventana.blit(gano, (120, 180))
            ventana.blit(gano2, (120, 220))
            ventana.blit(gano3, (120, 250))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    dibujar()


main()