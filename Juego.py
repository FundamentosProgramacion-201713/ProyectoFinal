#Encoding: UTF-8
#Autor: Joaquin Rios Corvera A01375441
#Juego: Pokemon Safari

####Todos los sprites, sonidos, musica y nombres pertenecen a Nintendo y Gamefreak####

import pygame, random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0,0,0)

#Pide nombre al usuario para guardar high score
def preguntarNombre():
    nombre = input("Bienvenido a Pokemon Safari. Antes de comenzar, por favor teclea tu nombre. Se utilizará para guardar tu puntuación: ")
    return nombre

#Genera un sprite aleatorio cada que se llama
def generarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts, Geodude, Pidgey, Koffing, Machop, Squirtle, Charmander, Bulbasaur, Pikachu, Jolteon, Flareon, Vaporeon, Mew, Mewtwo):
    #No importa de que sprite tomemos el rect porque todas tienen las mismas dimensiones
    enemigo = pygame.sprite.Sprite()
    enemigo.rect = Geodude.get_rect()
    enemigo.rect.top = random.randint(50, 350)
    enemigo.rect.left = -40

    rand = random.randint(1,100)

    if rand <= 60:
        pokemon = random.randint(1,4)
        if pokemon == 1:
            enemigo.image = Geodude
        elif pokemon == 2:
            enemigo.image = Pidgey
        elif pokemon == 3:
            enemigo.image = Koffing
        elif pokemon == 4:
            enemigo.image = Machop
        lista100pts.append(enemigo)
    elif rand <= 90:
        pokemon = random.randint(1,4)
        if pokemon == 1:
            enemigo.image = Squirtle
        elif pokemon == 2:
            enemigo.image = Charmander
        elif pokemon == 3:
            enemigo.image = Bulbasaur
        elif pokemon == 4:
            enemigo.image = Pikachu
        lista200pts.append(enemigo)
    elif rand <= 99:
        pokemon = random.randint(1,3)
        if pokemon == 1:
            enemigo.image = Vaporeon
        elif pokemon == 2:
            enemigo.image = Flareon
        elif pokemon == 3:
            enemigo.image = Jolteon
        lista500pts.append(enemigo)
    elif rand == 100:
        pokemon = random.randint(1,2)
        if pokemon == 1:
            enemigo.image = Mew
        elif pokemon == 2:
            enemigo.image = Mewtwo
        lista1000pts.append(enemigo)

#Dibuja todos los elementos del menu
def dibujarMenu(ventana, btnJugar, btnHighScore, btnHowToPlay, backgroundMenu):
    ventana.blit(backgroundMenu.image, backgroundMenu.rect)
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnHighScore.image, btnHighScore.rect)
    ventana.blit(btnHowToPlay.image, btnHowToPlay.rect)

#Dibuja todos los elementos mientras corra el juego
def dibujarJuego(ventana, lista100pts, lista200pts, lista500pts, lista1000pts, listaAtrapados, atrapados, puntuacion, pokebolasRestantes, fuenteTexto):
    #Este if evita que haya un error en caso de capturar a 2 enemigos con un mismo click
    if atrapados <= 12:
        ventana.blit(listaAtrapados[atrapados].image, listaAtrapados[atrapados].rect)
    else:
        ventana.blit(listaAtrapados[12].image, listaAtrapados[12].rect)
    for pokemon in lista100pts:
        ventana.blit(pokemon.image, pokemon.rect)
    for pokemon in lista200pts:
        ventana.blit(pokemon.image, pokemon.rect)
    for pokemon in lista500pts:
        ventana.blit(pokemon.image, pokemon.rect)
    for pokemon in lista1000pts:
        ventana.blit(pokemon.image, pokemon.rect)

    puntuacion = str(puntuacion)
    pokebolasRestantes = str(pokebolasRestantes)

    score = fuenteTexto.render(puntuacion, 1, BLANCO)
    balls = fuenteTexto.render(pokebolasRestantes, 1, BLANCO)

    ventana.blit(score, (630, 540))
    ventana.blit(balls, (120, 540))

#Imprime las 3 puntuaciones mas altas
def dibujarHighScore(ventana, fuenteTexto, btnRegreso, backgroundHighScore):
    ventana.blit(backgroundHighScore.image, backgroundHighScore.rect)
    ventana.blit(btnRegreso.image, btnRegreso.rect)

    entrada = open("HighScores.txt")
    listaDupla = []
    scores = entrada.readlines()
    for score in scores:
        score = score.rstrip()
        score = score.split("-")
        listaDupla.append((score[0], int(score[1])))

    #Ordena por puntuacion, pero cada puntuacion mantiene su nombre
    listaDupla.sort(key=lambda tup: tup[1], reverse=True)

    if len(listaDupla) > 0:
        nombre1, score1 = listaDupla[0]
        nombre1 = fuenteTexto.render(nombre1, 1, NEGRO)
        score1 = fuenteTexto.render(str(score1), 1, NEGRO)
        ventana.blit(nombre1, (220, 150))
        ventana.blit(score1, (450, 150))

    if len(listaDupla) > 1:
        nombre2, score2 = listaDupla[1]
        nombre2 = fuenteTexto.render(nombre2, 1, NEGRO)
        score2 = fuenteTexto.render(str(score2), 1, NEGRO)
        ventana.blit(nombre2, (220, 250))
        ventana.blit(score2, (450, 250))

    if len(listaDupla) > 2:
        nombre3, score3 = listaDupla[2]
        nombre3 = fuenteTexto.render(nombre3, 1, NEGRO)
        score3 = fuenteTexto.render(str(score3), 1, NEGRO)
        ventana.blit(nombre3, (220, 350))
        ventana.blit(score3, (450, 350))



#Dibuja instructivo
def dibujarHowToPlay(ventana, backgroundHowToPlay,btnRegreso):
    ventana.blit(backgroundHowToPlay.image, backgroundHowToPlay.rect)
    ventana.blit(btnRegreso.image, btnRegreso.rect)

#Genera movimiento aleatorio en y para enemigos y en x depende de su puntaje
def moverEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts):
    for pokemon in lista100pts:
        y = random.randint(-10,10)
        pokemon.rect.top += y
        pokemon.rect.left += 5
    for pokemon in lista200pts:
        y = random.randint(-10,10)
        pokemon.rect.top += y
        pokemon.rect.left += 15
    for pokemon in lista500pts:
        y = random.randint(-10,10)
        pokemon.rect.top += y
        pokemon.rect.left += 25
    for pokemon in lista1000pts:
        y = random.randint(-10,10)
        pokemon.rect.top += y
        pokemon.rect.left += 35

#Borra enemigos cuando salen de pantalla
def actualizarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts):
    #Crea una nueva lista con los elementos de la original que cumplen con la condición
    lista100pts[:] = [pokemon for pokemon in lista100pts if not (pokemon.rect.left > 850)]
    lista200pts[:] = [pokemon for pokemon in lista200pts if not (pokemon.rect.left > 850)]
    lista500pts[:] = [pokemon for pokemon in lista500pts if not (pokemon.rect.left > 850)]
    lista1000pts[:] = [pokemon for pokemon in lista1000pts if not (pokemon.rect.left > 850)]

#Suma tus puntos y guarda el total
def actualizarPuntuacion(lista100pts, lista200pts, lista500pts, lista1000pts, xm, ym, puntuacion, atrapados, atrapar):
    mouse = xm,ym
    for pokemon in lista100pts:
        if pokemon.rect.collidepoint(mouse):
            puntuacion += 100
            atrapados += 1
            atrapar.play()
    for pokemon in lista200pts:
        if pokemon.rect.collidepoint(mouse):
            puntuacion += 200
            atrapados += 1
            atrapar.play()
    for pokemon in lista500pts:
        if pokemon.rect.collidepoint(mouse):
            puntuacion += 500
            atrapados += 1
            atrapar.play()
    for pokemon in lista1000pts:
        if pokemon.rect.collidepoint(mouse):
            puntuacion += 1000
            atrapados += 1
            atrapar.play()

    return puntuacion,atrapados

#Elimina enemigos al hacerles click
def eliminarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts, xm, ym):
    mouse = xm,ym
    lista100pts[:] = [pokemon for pokemon in lista100pts if not (pokemon.rect.collidepoint(mouse))]
    lista200pts[:] = [pokemon for pokemon in lista200pts if not (pokemon.rect.collidepoint(mouse))]
    lista500pts[:] = [pokemon for pokemon in lista500pts if not (pokemon.rect.collidepoint(mouse))]
    lista1000pts[:] = [pokemon for pokemon in lista1000pts if not (pokemon.rect.collidepoint(mouse))]

#Muestra cuando acaba el juego y enseña tu puntuacion
def dibujarGameOver(ventana, backgroundGameOver, btnRegreso, puntuacion, fuenteTexto):
    ventana.blit(backgroundGameOver.image, backgroundGameOver.rect)
    ventana.blit(btnRegreso.image, btnRegreso.rect)

    puntuacion = str(puntuacion)

    score = fuenteTexto.render(puntuacion, 1, BLANCO)
    ventana.blit(score, (360, 540))

#Guarda tu puntuacion en una lista de puntuaciones
def anotarPuntuacion(puntuacion, listaPuntuaciones):
    listaPuntuaciones.append(puntuacion)


def dibujar():

    nombre = preguntarNombre()
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    #Estados
    estado = "menu"  #jugando, termina, comoJugar, highScore, GameOver
    listaPuntuaciones = []  #Aqui se guardaran las puntuaciones del jugador

    #Backgrounds
    imgBackgroundMenu = pygame.image.load("MainMenuBG.png")
    backgroundMenu = pygame.sprite.Sprite()
    backgroundMenu.image = imgBackgroundMenu
    backgroundMenu.rect = imgBackgroundMenu.get_rect()
    backgroundMenu.rect.left = 0
    backgroundMenu.rect.top = 0

    imgBackgroundHowToPlay = pygame.image.load("HowToPlay.png")
    backgroundHowToPlay = pygame.sprite.Sprite()
    backgroundHowToPlay.image = imgBackgroundHowToPlay
    backgroundHowToPlay.rect = imgBackgroundHowToPlay.get_rect()
    backgroundHowToPlay.rect.left = 0
    backgroundHowToPlay.rect.top = 0

    imgBackgroundGameOver = pygame.image.load("GameOver.png")
    backgroundGameOver = pygame.sprite.Sprite()
    backgroundGameOver.image = imgBackgroundGameOver
    backgroundGameOver.rect = imgBackgroundGameOver.get_rect()
    backgroundGameOver.rect.left = 0
    backgroundGameOver.rect.top = 0

    imgBackgroundHighScore = pygame.image.load("HallOfFame.png")
    backgroundHighScore = pygame.sprite.Sprite()
    backgroundHighScore.image = imgBackgroundHighScore
    backgroundHighScore.rect = imgBackgroundHighScore.get_rect()
    backgroundHighScore.rect.left = 0
    backgroundHighScore.rect.top = 0

    imgCaught0 = pygame.image.load("Caught0.png")
    Caught0 = pygame.sprite.Sprite()
    Caught0.image = imgCaught0
    Caught0.rect = imgCaught0.get_rect()
    Caught0.rect.left = 0
    Caught0.rect.top = 0

    imgCaught1 = pygame.image.load("Caught1.png")
    Caught1 = pygame.sprite.Sprite()
    Caught1.image = imgCaught1
    Caught1.rect = imgCaught1.get_rect()
    Caught1.rect.left = 0
    Caught1.rect.top = 0

    imgCaught2 = pygame.image.load("Caught2.png")
    Caught2 = pygame.sprite.Sprite()
    Caught2.image = imgCaught2
    Caught2.rect = imgCaught2.get_rect()
    Caught2.rect.left = 0
    Caught2.rect.top = 0

    imgCaught3 = pygame.image.load("Caught3.png")
    Caught3 = pygame.sprite.Sprite()
    Caught3.image = imgCaught3
    Caught3.rect = imgCaught3.get_rect()
    Caught3.rect.left = 0
    Caught3.rect.top = 0

    imgCaught4 = pygame.image.load("Caught4.png")
    Caught4 = pygame.sprite.Sprite()
    Caught4.image = imgCaught4
    Caught4.rect = imgCaught4.get_rect()
    Caught4.rect.left = 0
    Caught4.rect.top = 0

    imgCaught5 = pygame.image.load("Caught5.png")
    Caught5 = pygame.sprite.Sprite()
    Caught5.image = imgCaught5
    Caught5.rect = imgCaught5.get_rect()
    Caught5.rect.left = 0
    Caught5.rect.top = 0

    imgCaught6 = pygame.image.load("Caught6.png")
    Caught6 = pygame.sprite.Sprite()
    Caught6.image = imgCaught6
    Caught6.rect = imgCaught6.get_rect()
    Caught6.rect.left = 0
    Caught6.rect.top = 0

    imgCaught7 = pygame.image.load("Caught7.png")
    Caught7 = pygame.sprite.Sprite()
    Caught7.image = imgCaught7
    Caught7.rect = imgCaught7.get_rect()
    Caught7.rect.left = 0
    Caught7.rect.top = 0

    imgCaught8 = pygame.image.load("Caught8.png")
    Caught8 = pygame.sprite.Sprite()
    Caught8.image = imgCaught8
    Caught8.rect = imgCaught8.get_rect()
    Caught8.rect.left = 0
    Caught8.rect.top = 0

    imgCaught9 = pygame.image.load("Caught9.png")
    Caught9 = pygame.sprite.Sprite()
    Caught9.image = imgCaught9
    Caught9.rect = imgCaught9.get_rect()
    Caught9.rect.left = 0
    Caught9.rect.top = 0

    imgCaught10 = pygame.image.load("Caught10.png")
    Caught10 = pygame.sprite.Sprite()
    Caught10.image = imgCaught10
    Caught10.rect = imgCaught10.get_rect()
    Caught10.rect.left = 0
    Caught10.rect.top = 0

    imgCaught11 = pygame.image.load("Caught11.png")
    Caught11 = pygame.sprite.Sprite()
    Caught11.image = imgCaught11
    Caught11.rect = imgCaught11.get_rect()
    Caught11.rect.left = 0
    Caught11.rect.top = 0

    imgCaught12 = pygame.image.load("Caught12.png")
    Caught12 = pygame.sprite.Sprite()
    Caught12.image = imgCaught12
    Caught12.rect = imgCaught12.get_rect()
    Caught12.rect.left = 0
    Caught12.rect.top = 0

    listaAtrapados = [Caught0, Caught1, Caught2, Caught3, Caught4, Caught5, Caught6, Caught7, Caught8, Caught9, Caught10, Caught11, Caught12]

    #Botones
    imgBotonJugar = pygame.image.load("StartBtn.png")
    btnJugar = pygame.sprite.Sprite()  #SPRITE
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO//2 - btnJugar.rect.width//2 - 200 #coordenada x
    btnJugar.rect.top = ALTO//2 - btnJugar.rect.height//2  #coordenada y

    imgBotonHighScore = pygame.image.load("HighScoresBtn.png")
    btnHighScore = pygame.sprite.Sprite()
    btnHighScore.image = imgBotonHighScore
    btnHighScore.rect = imgBotonHighScore.get_rect()
    btnHighScore.rect.left = ANCHO//2 - btnHighScore.rect.width//2 - 200
    btnHighScore.rect.top = ALTO//2 + btnHighScore.rect.height//2 + 5

    imgBotonHowToPlay = pygame.image.load("HowToPlayBtn.png")
    btnHowToPlay = pygame.sprite.Sprite()
    btnHowToPlay.image = imgBotonHowToPlay
    btnHowToPlay.rect = imgBotonHowToPlay.get_rect()
    btnHowToPlay.rect.left = ANCHO//2 - btnHowToPlay.rect.width//2 - 200
    btnHowToPlay.rect.top = ALTO//2 + btnHighScore.rect.height//2 + btnHighScore.rect.height + 10

    imgBotonRegreso = pygame.image.load("BackBtn.png")
    btnRegreso = pygame.sprite.Sprite()
    btnRegreso.image = imgBotonRegreso
    btnRegreso.rect = imgBotonRegreso.get_rect()
    btnRegreso.rect.left = 50
    btnRegreso.rect.top = 500

    #Fuentes
    pygame.font.init()
    fuenteTexto = pygame.font.SysFont("Titles.ttf", 50)

    #Sprites

    Geodude = pygame.image.load("Geodude.png")
    Pidgey = pygame.image.load("Pidgey.png")
    Machop = pygame.image.load("Machop.png")
    Koffing = pygame.image.load("Koffing.png")
    Squirtle = pygame.image.load("Squirtle.png")
    Bulbasaur = pygame.image.load("Bulbasaur.png")
    Charmander = pygame.image.load("Charmander.png")
    Pikachu = pygame.image.load("Pikachu.png")
    Vaporeon = pygame.image.load("Vaporeon.png")
    Flareon = pygame.image.load("Flareon.png")
    Jolteon = pygame.image.load("Jolteon.png")
    Mew = pygame.image.load("Mew.png")
    Mewtwo = pygame.image.load("Mewtwo.png")

    #Listas Enemigos
    lista100pts = []
    lista200pts = []
    lista500pts = []
    lista1000pts = []

    #Sonidos
    pygame.mixer.init()
    pygame.mixer.music.load("Undella Town.mp3")
    pygame.mixer.music.play(-1)

    click = pygame.mixer.Sound("Click.wav")
    click.set_volume(.5)
    disparar = pygame.mixer.Sound("PokeballThrow.wav")
    disparar.set_volume(.4)
    atrapar = pygame.mixer.Sound("PokeballCatch.wav")
    atrapar.set_volume(.3)

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    click.play()
                    xJugar, yJugar, anchoJugar, altoJugar = btnJugar.rect
                    xHighScore, yHighScore, anchoHighScore, altoHighScore = btnHighScore.rect
                    xHowTo, yHowTo, anchoHowTo, altoHowTo = btnHowToPlay.rect
                    if xm>=xJugar and xm<=xJugar+anchoJugar and ym>=yJugar and ym<=yJugar+altoJugar:
                        estado = "jugando"
                    elif xm>=xHighScore and xm<=xHighScore+anchoHighScore and ym>=yHighScore and ym<=yHighScore+altoHighScore:
                        estado = "HighScore"
                    elif xm>=xHowTo and xm<=xHowTo+anchoHowTo and ym>=yHowTo and ym<=yHowTo+altoHowTo:
                        estado = "HowToPlay"

                elif estado == "jugando":
                    disparar.play()
                    pokebolasRestantes -= 1
                    puntuacion,atrapados = actualizarPuntuacion(lista100pts, lista200pts, lista500pts, lista1000pts, xm, ym, puntuacion, atrapados, atrapar)
                    eliminarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts, xm, ym)

                elif estado == "HowToPlay" or estado == "GameOver" or estado == "HighScore":
                    click.play()
                    xBack, yBack, anchoBack, altoBack = btnRegreso.rect
                    if xm>=xBack and xm<=xBack+anchoBack and ym>=yBack and ym<=yBack+altoBack:
                        estado = "menu"



        # Borrar pantalla
        ventana.fill(BLANCO)

        #Acciones

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, btnJugar, btnHighScore, btnHowToPlay, backgroundMenu)

            # Aqui declaro todos los counters que voy a necesitar, para que se reinicien cada vez que se vuelva al menu
            timerEnemigos = 0
            atrapados = 0
            pokebolasRestantes = 12
            puntuacion = 0
        elif estado == "jugando":
            dibujarJuego(ventana, lista100pts, lista200pts, lista500pts, lista1000pts, listaAtrapados, atrapados, puntuacion, pokebolasRestantes, fuenteTexto)
            moverEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts)
            actualizarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts)
            if pokebolasRestantes == 0:
                estado = "GameOver"

            timerEnemigos += 1/40
            if timerEnemigos > 1:
                generarEnemigos(lista100pts, lista200pts, lista500pts, lista1000pts, Geodude, Pidgey, Koffing, Machop,
                                Squirtle, Charmander, Bulbasaur, Pikachu, Jolteon, Flareon, Vaporeon, Mew, Mewtwo)
                timerEnemigos = 0

        elif estado == "HighScore":
            dibujarHighScore(ventana, fuenteTexto, btnRegreso, backgroundHighScore)
        elif estado == "HowToPlay":
            dibujarHowToPlay(ventana, backgroundHowToPlay, btnRegreso)
        elif estado == "GameOver":
            dibujarGameOver(ventana, backgroundGameOver, btnRegreso, puntuacion, fuenteTexto)
            anotarPuntuacion(puntuacion, listaPuntuaciones)
        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame

    #Cuando cierras el juego, guarda tu puntuacion mas alta con tu nombre
    if len(listaPuntuaciones)>0:
        listaPuntuaciones.sort(reverse=True)
        salida = open("HighScores.txt", "a")
        salida.write(nombre + "-" + str(listaPuntuaciones[0])+"\n")
        salida.close()

def main():
    dibujar()

main()