# encoding: UTF-8
# Autor: David Ramírez Ríos, A01338802
# Descripción: Remake del clásico videojuego "Space Invaders"


import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
AZUL = (100, 149, 237)
dx = 2

# Comprueba que exista un archivo de marcadores; en caso de no exitir crea uno nuevo
archivo = open("Marcadores.txt", "a")
archivo.close()

# Dibuja el menú
def dibujarMenu(ventana, botonJugar, botonMarcador, botonSalir):
    ventana.blit(botonJugar.image, botonJugar.rect)
    ventana.blit(botonMarcador.image, botonMarcador.rect)
    ventana.blit(botonSalir.image, botonSalir.rect)

# Dibuja el marcador
def dibujarMarcador(ventana, botonRegresar, botonMarcador, botonJugar):
    ventana.blit(botonRegresar.image, botonRegresar.rect)
    botonMarcador.rect.top = 50 # Ajusta "marcador" para encajar con el menú actual
    ventana.blit(botonMarcador.image, botonMarcador.rect)
    botonMarcador.rect.top = 225 + botonJugar.rect.height
    archivo = open("Marcadores.txt")
    marcadores = archivo.readlines()
    archivo.close()
    fuente = pygame.font.SysFont("monospace", 40, 1)
    # Comprueba si hay marcadores previos
    if len(marcadores) == 0:
        texto = fuente.render("No hay marcadores previos", 1, AZUL)
        ventana.blit(texto, (ANCHO//2 - 300, ALTO//2))
    else:
        # Comprueba el número de marcadores previos (1, 2, 3) para escribrir las posiciones
        if len(marcadores) == 1:
            texto = fuente.render("1° " + str(int(marcadores[0])), 1, AZUL)
            ventana.blit(texto, (ANCHO // 2 - 80, ALTO//2))
        elif len(marcadores) == 2:
            texto1 = fuente.render("1° " + str(int(marcadores[0])), 1, AZUL)
            texto2 = fuente.render("2° " + str(int(marcadores[1])), 1, AZUL)
            ventana.blit(texto1, (ANCHO // 2 - 80, ALTO//2 - 20))
            ventana.blit(texto2, (ANCHO // 2 - 80, ALTO//2 + 20))
        else:
            texto1 = fuente.render("1° " + str(int(marcadores[0])), 1, AZUL)
            texto2 = fuente.render("2° " + str(int(marcadores[1])), 1, AZUL)
            texto3 = fuente.render("3° " + str(int(marcadores[2])), 1, AZUL)
            ventana.blit(texto1, (ANCHO // 2 - 50, ALTO//2 - 40))
            ventana.blit(texto2, (ANCHO // 2 - 50, ALTO//2))
            ventana.blit(texto3, (ANCHO // 2 - 50, ALTO//2 + 40))
    botonMarcador.rect.top = 225 + botonJugar.rect.height # Regresa "marcador" a su posición original

# Dibuja el juego
def dibujarJuego(ventana, jugador, listaBalas, listaEnemigos):
    ventana.blit(jugador.image, jugador.rect)
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

# Mueve al jugador de acuerdo a dx
def moverJugador(jugador, Dx):
    if jugador.rect.left+jugador.rect.width<=780 and jugador.rect.left>=20: # Comprueba que este dentro del margen
        if jugador.rect.left + jugador.rect.width + Dx <=780 and jugador.rect.left + Dx >=20: # Comprueba que el siguiente paso no se pasará del margen
            jugador.rect.left += Dx

# Elimina un enemigo y una bala en caso de colisión
def actualizarBalas(listaBalas, listaEnemigos, marcador, vidasE, aceleracion):
    for bala in listaBalas:  # NO DEBEN  modificar la conexion
        bala.rect.top -= 15
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue  # Continua al siguiente indice del ciclo for de arriba, como si hubiera terminado el resto de instrucciones del for
        borrarBala = False
        for k in range(len(listaEnemigos)-1, -1,-1):
            enemigo = listaEnemigos[k]

            if bala.rect.colliderect(enemigo): # Enemigo eliminado
                if aceleracion == 6:
                    vidasE[enemigo] -= 1
                    if vidasE[enemigo] == 0:
                        listaEnemigos.remove(enemigo)
                        marcador += 1 # Suma un punto al marcador
                else:
                    listaEnemigos.remove(enemigo)
                    marcador += 1  # Suma un punto al marcador
                borrarBala = True
                break  # Termina el Ciclo
        if borrarBala:
            listaBalas.remove(bala)
    return marcador

# Genera el grupo de enemigos (15)
def generarEnemigos(listaEnemigos, imgEnemigo):
    for x in range(5):
        for y in range(3):
            # Generar el enemigo
            cx = 22 + x * 160  # cada 160 px habrá un enemigo empezando de 20
            cy = 50 + y * 89
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = cx  # Pos en x
            enemigo.rect.top = cy  # Pos en y
            listaEnemigos.append(enemigo)

# Mueve los enemigos de izquierda a derecha y viceversa, y de arriba a abajo
def moverEnemigos(listaEnemigos, dx, c):
    for enemigo in listaEnemigos:
        enemigo.rect.left += dx
    if c == -1:
        for enemigo in listaEnemigos:
            enemigo.rect.top +=5

# Dibuja el menu de dificultad a elegir para jugar
def dibujarDificultades(ventana, botonDificultad, botonFacil, botonMedia, botonDificil, botonRegresar):
    ventana.blit(botonDificultad.image, botonDificultad.rect)
    ventana.blit(botonFacil.image, botonFacil.rect)
    ventana.blit(botonMedia.image, botonMedia.rect)
    ventana.blit(botonDificil.image, botonDificil.rect)
    ventana.blit(botonRegresar.image, botonRegresar.rect)

# Dibuja el menu de Game Over
def dibujarPerder(ventana, botonPerdido, botonPuntacion, botonRegresar, marcador):
    ventana.blit(botonPerdido.image, botonPerdido.rect)
    ventana.blit(botonPuntacion.image, botonPuntacion.rect)
    ventana.blit(botonRegresar.image, botonRegresar.rect)
    # Escribe la puntuación obtenida
    fuente = pygame.font.SysFont("monospace", 40, 1)
    texto = fuente.render(str(marcador), 1, AZUL)
    ventana.blit(texto, (ANCHO // 2-20, ALTO//2))

# Revisa y compara el marcador
def revisarMarcador(marcador):
    if marcador > 0: # El jugador obtuvo una puntuación mayor que 0
        #marcadores = []
        archivo = open("Marcadores.txt")
        marcadores = archivo.readlines()
        archivo.close()
        if len(marcadores) == 0: # Si no hay ningún marcador solo inserta el nuevo
            archivo = open("Marcadores.txt", "w")
            archivo.write(str(marcador) + "\n")
            archivo.close()
        else:
            marcadoresINT = []
            for k in marcadores: # Extrae los marcadores y los convierte a "int" para su análisis
                marcadoresINT.append(int(k))
            marcadoresINT.sort(reverse=True) # Ordena de mayor a menor
            if len(marcadores) <3: # El marcador no esta lleno
                # Reordena en caso de ser necesario
                if min(marcadoresINT)>marcador:
                    marcadoresINT.append(marcador)
                else:
                    marcadoresINT.append(marcador)
                    marcadoresINT.sort(reverse=True)
                marcadores = []
                for k in marcadoresINT: # Devuelve los nuevos marcadores en "str"
                    marcadores.append(str(k) + "\n")
                archivo = open("Marcadores.txt", "w")
                archivo.writelines(marcadores) # Escribe los nuevos marcadores
                archivo.close()
            elif len(marcadores) == 3: # El marcador está lleno
                if min(marcadoresINT) < marcador: # Si la puntacion es superior a la miníma del top 3 lo inserta y borra la mínima
                    marcadoresINT.remove(min(marcadoresINT))
                    marcadoresINT.append(marcador)
                    marcadoresINT.sort(reverse=True)
                archivo = open("Marcadores.txt", "w")
                marcadores = []
                for k in marcadoresINT: # Devuelve los nuevos marcadores en "str"
                    marcadores.append(str(k) + "\n")
                archivo.writelines(marcadores) # Escribe los nuevos marcadores
                archivo.close()

def dibujar(dx):
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    # Estado Menu: Jugar, Marcadores, Salir
    estado = "menu"
    marcador = 0

    # Boton Jugar
    imgBtnJugar = pygame.image.load("button_jugar.png")
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO//2 - botonJugar.rect.width//2
    botonJugar.rect.top = 175

    # Boton Marcador
    imgBtnMarcador = pygame.image.load("button_marcador.png")
    botonMarcador =  pygame.sprite.Sprite()
    botonMarcador.image = imgBtnMarcador
    botonMarcador.rect = imgBtnMarcador.get_rect()
    botonMarcador.rect.left = ANCHO//2 - botonMarcador.rect.width//2
    botonMarcador.rect.top = 225 + botonJugar.rect.height

    # Boton Salir
    imgBtnSalir = pygame.image.load("button_salir.png")
    botonSalir = pygame.sprite.Sprite()
    botonSalir.image = imgBtnSalir
    botonSalir.rect = imgBtnSalir.get_rect()
    botonSalir.rect.left = ANCHO//2 - botonSalir.rect.width//2
    botonSalir.rect.top = 375

    # Boton Regresar
    imgBtnRegresar = pygame.image.load("button_regresar.png")
    botonRegresar = pygame.sprite.Sprite()
    botonRegresar.image = imgBtnRegresar
    botonRegresar.rect = imgBtnRegresar.get_rect()
    botonRegresar.rect.left = ANCHO//2 - botonRegresar.rect.width//2
    botonRegresar.rect.top = 500

    # Boton Dificultad
    imgBtnDificultad = pygame.image.load("button_dificultad.png")
    botonDificultad = pygame.sprite.Sprite()
    botonDificultad.image = imgBtnDificultad
    botonDificultad.rect = imgBtnDificultad.get_rect()
    botonDificultad.rect.left = ANCHO//2 - botonDificultad.rect.width//2
    botonDificultad.rect.top = 50

    # boton Facil
    imgBtnFacil = pygame.image.load("button_facil.png")
    botonFacil = pygame.sprite.Sprite()
    botonFacil.image = imgBtnFacil
    botonFacil.rect = imgBtnFacil.get_rect()
    botonFacil.rect.left = ANCHO//2 - botonFacil.rect.width//2
    botonFacil.rect.top = 200

    # Boton Media
    imgBtnMedia = pygame.image.load("button_media.png")
    botonMedia = pygame.sprite.Sprite()
    botonMedia.image = imgBtnMedia
    botonMedia.rect = imgBtnMedia.get_rect()
    botonMedia.rect.left = ANCHO // 2 - botonMedia.rect.width // 2
    botonMedia.rect.top = 300

    # Boton Dificil
    imgBtnDificil = pygame.image.load("button_dificil.png")
    botonDificil = pygame.sprite.Sprite()
    botonDificil.image = imgBtnDificil
    botonDificil.rect = imgBtnDificil.get_rect()
    botonDificil.rect.left = ANCHO // 2 - botonDificil.rect.width // 2
    botonDificil.rect.top = 400

    # Boton Perdido
    imgBtnPerdido = pygame.image.load("button_perdido.png")
    botonPerdido = pygame.sprite.Sprite()
    botonPerdido.image = imgBtnPerdido
    botonPerdido.rect = imgBtnPerdido.get_rect()
    botonPerdido.rect.left = ANCHO // 2 - botonPerdido.rect.width // 2
    botonPerdido.rect.top = 50

    # Boton Punbtuacion
    imgBtnPuntacion = pygame.image.load("button_puntuacion.png")
    botonPuntacion = pygame.sprite.Sprite()
    botonPuntacion.image = imgBtnPuntacion
    botonPuntacion.rect = imgBtnPuntacion.get_rect()
    botonPuntacion.rect.left = ANCHO // 2 - botonPuntacion.rect.width // 2
    botonPuntacion.rect.top = 150

    # Fondo
    imgFondo = pygame.image.load("Cielo_Estrellado.jpeg")

    # Jugador
    imgJugador = pygame.image.load("Nave08.png")
    jugador = pygame.sprite.Sprite()
    jugador.image = imgJugador
    jugador.rect = imgJugador.get_rect()
    jugador.rect.left = ANCHO//2 - jugador.rect.width//2
    jugador.rect.top = 580 - jugador.rect.height//2*2
    mover = False

    # Enemigo
    listaEnemigos = []
    imgEnemigo = pygame.image.load("alien1.png")
    generarEnemigos(listaEnemigos, imgEnemigo)
    vidasE = {}
    for enemigo in listaEnemigos:
        vidasE[enemigo] = 2

    # Bala
    listaBalas = []
    imgBala = pygame.image.load("bullet1.png")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = (pygame.mouse.get_pos()) # Posición del mouse
                if estado == "menu":
                    xbJ, ybJ, anchobJ, altobJ = botonJugar.rect
                    xbM , ybM, anchobM, altobM = botonMarcador.rect
                    xbS, ybS, anchobS, altobS = botonSalir.rect
                    if xm>=xbJ and xm<=xbJ+anchobJ:
                        if ym>=ybJ and ym<=ybJ+altobJ:
                            estado = "dificultad"
                    if xm>=xbM and xm<=xbM+anchobJ: # Muestra marcadores
                        if ym>=ybM and ym<=ybM+altobM:
                            estado = "marcador"
                    if xm>=xbS and xm<=xbS+anchobS: # Sale del juego
                        if ym>=ybS and ym<=ybS+altobS:
                            termina = True
                elif estado == "marcador":
                    xbR, ybR, anchobR, altobR = botonRegresar.rect
                    if xm>=xbR and xm<=xbR+anchobR: # Regresa al menú
                        if ym>=ybR and ym<=ybR+altobR:
                            estado = "menu"
                elif estado == "dificultad":
                    xbD_F, ybD_F, anchobD_F, altobD_F = botonFacil.rect
                    xbD_M, ybD_M, anchobD_M, altobD_M = botonMedia.rect
                    xbD_D, ybD_D, anchobD_D, altobD_D = botonDificil.rect
                    xbR, ybR, anchobR, altobR = botonRegresar.rect
                    if xm>=xbR and xm<=xbR+anchobR: # Regresa al menú
                        if ym>=ybR and ym<=ybR+altobR:
                            estado = "menu"
                    if xm>=xbD_F and xm<=xbD_F+anchobD_F: # Fácil
                        if ym>=ybD_F and ym<=ybD_F+altobD_F:
                            estado = "jugando"
                            aceleracion = 2
                    if xm>=xbD_M and xm<=xbD_M+anchobD_M: # Media
                        if ym>=ybD_M and ym<=ybD_M+altobD_M:
                            estado = "jugando"
                            aceleracion = 4
                    if xm>=xbD_D and xm<=xbD_D+anchobD_D: # Dificil
                        if ym>=ybD_D and ym<=ybD_D+altobD_D:
                            estado = "jugando"
                            aceleracion = 6
                elif estado == "perder":
                    xbR, ybR, anchobR, altobR = botonRegresar.rect
                    if xm >= xbR and xm <= xbR + anchobR: # Regresa al menú
                        if ym >= ybR and ym <= ybR + altobR:
                            revisarMarcador(marcador)
                            estado = "menu"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT: # Mover jugador a la derecha
                    mover = True
                    Dx = 8
                elif evento.key == pygame.K_LEFT: # Mover jugador a la izquierda
                    mover = True
                    Dx = -8
                elif evento.key == pygame.K_SPACE: # Disparar
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.top = jugador.rect.top + jugador.rect.height//2 - bala.rect.height//2
                    bala.rect.left = jugador.rect.left + jugador.rect.width//2 - bala.rect.width//2
                    listaBalas.append(bala)
            elif evento.type == pygame.KEYUP: # Detener movimiento
                if evento.key == pygame.K_RIGHT: # Mover jugador a la derecha
                    mover = False
                elif evento.key == pygame.K_LEFT:
                    mover = False


        # Borrar pantalla
        ventana.fill(BLANCO)
        ventana.blit(imgFondo, (0,0)) # Fondo

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu": # Dibuja el menu
            dibujarMenu(ventana, botonJugar, botonMarcador, botonSalir)
            marcador = 0
        elif estado == "marcador": # Dibuja las tres puntuaciones más altas
            dibujarMarcador(ventana, botonRegresar, botonMarcador, botonJugar)
        elif estado == "dificultad":
            dibujarDificultades(ventana, botonDificultad, botonFacil, botonMedia, botonDificil, botonRegresar)
        elif estado == "jugando":
            dibujarJuego(ventana, jugador, listaBalas, listaEnemigos)
            if mover:
                moverJugador(jugador, Dx)
            xEnemigos = []
            yEnemigos = []
            if len(listaEnemigos)==0: # Genera nuevos enemigos en caso de no haber ninguno
                generarEnemigos(listaEnemigos, imgEnemigo)
                dx -= 2 # Reduce la aceleración para disminuir la dificultad de progresar
                vidasE = {}
                for enemigo in listaEnemigos:
                    vidasE[enemigo] = 2
            for enemigo in listaEnemigos: # Extrae las posisciones "x" de cada enemigo
                xEnemigos.append(enemigo.rect.left)
            for enemigo in listaEnemigos: # Extrae las posiciones "y" de cada enemigo
                yEnemigos.append(enemigo.rect.top + enemigo.rect.height)
            if max(yEnemigos) >= jugador.rect.top: # Comprueba si algún enemigo ha alcanzado al jugador
                estado = "perder"
            if min(xEnemigos) <= 20 or max(xEnemigos)+80 >= 780: # Comprueba que los enemigos no pasen del margen (20px)
                c = -1
            elif min(xEnemigos) + dx <= 20 or max(xEnemigos)+ 80 + dx >= 780: # Comprueba que el próximo movimiento no saque a los enemigos del margen
                c = -1
            else:
                c = 1
            # Comprueba que la aceleración se produsca en dirección al movimiento acutal
            if dx <= 0:
                dx -= aceleracion/40
            else:
                dx += aceleracion/40
            dx *= c # Cambia o no de dirección

            marcador = actualizarBalas(listaBalas, listaEnemigos, marcador, vidasE, aceleracion) # Actualiza balas y regresa marcador actual
            moverEnemigos(listaEnemigos, dx, c)

            # Escribe dificultad y puntuación adtual
            fuente = pygame.font.SysFont("monospace", 40, 1)
            if aceleracion == 2:
                texto = fuente.render("Fácil - " + str(marcador), 1, AZUL)
            elif aceleracion == 4:
                texto = fuente.render("Media - " + str(marcador), 1, AZUL)
            else:
                texto = fuente.render("Difícil - " + str(marcador), 1, AZUL)

            ventana.blit(texto, (20, 10))
        elif estado == "perder": # El jugador ha perdido
            dibujarPerder(ventana, botonPerdido, botonPuntacion, botonRegresar, marcador)
            jugador.rect.left = ANCHO//2
            listaEnemigos = []
            dx = 4
            listaBalas = []

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame



def main():
    dibujar(dx)

main()