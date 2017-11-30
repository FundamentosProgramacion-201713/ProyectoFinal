#Encoding: UTF-8
# Autor: Luis Daniel Rivera Salinas
#Descripcion: Juego clasico de buscaminas con pequeñas modificaciones en scripts

import pygame
from random import randint

pygame.init()
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)


def Facil():
    pygame.init()



    def mine(n, bombs):  # Matrix para usar en el futuro
        table = make_table(n)
        table = add_bombs(table, bombs)
        table = change_table(table)
        return (table)

    def make_table(n):
        return [[0] * n for i in range(n)]  # matriz base

    def add_bombs(table, bombs):
        for i in range(bombs):
            is_bomb = False
            while not is_bomb:
                x = randint(0, len(table) - 1)
                y = randint(0, len(table) - 1)
                if table[x][y] != 9:  # Con 9 se dice que hay una bomba
                    table[x][y] = 9
                    is_bomb = True
        return (table)

    def change_table(table):  # Cambia el numero que indica que tan cerca esta de la bomba
        for x in range(len(table)):
            for y in range(len(table[x])):  # Posible error, cambiar x por i
                if table[x][y] == 9:
                    table = check_down_left(table, x, y)
                    table = check_down_right(table, x, y)
                    table = check_down(table, x, y)
                    table = check_up_left(table, x, y)
                    table = check_up_right(table, x, y)
                    table = check_up(table, x, y)
                    table = check_left(table, x, y)
                    table = check_right(table, x, y)
        return (table)

    def check_down_left(table, x, y):
        if x + 1 < len(table[x]) and y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x + 1][y - 1] != 9:  # No cambiar si es bomba
                table[x + 1][y - 1] += 1
        return (table)

    def check_down_right(table, x, y):
        if x + 1 < len(table[0]) and y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x + 1][y + 1] != 9:  # No cambiar si es bomba
                table[x + 1][y + 1] += 1
        return (table)

    def check_down(table, x, y):
        if x + 1 < len(table[0]):  # Checa si esta en izquierda abajo
            if table[x + 1][y] != 9:  # No cambiar si es bomba
                table[x + 1][y] += 1
        return (table)

    def check_up_left(table, x, y):
        if x - 1 >= 0 and y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x - 1][y - 1] != 9:  # No cambiar si es bomba
                table[x - 1][y - 1] += 1
        return (table)

    def check_up_right(table, x, y):
        if x - 1 >= 0 and y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x - 1][y + 1] != 9:  # No cambiar si es bomba
                table[x - 1][y + 1] += 1
        return (table)

    def check_up(table, x, y):
        if x - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x - 1][y] != 9:  # No cambiar si es bomba
                table[x - 1][y] += 1
        return (table)

    def check_left(table, x, y):
        if y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x][y - 1] != 9:  # No cambiar si es bomba
                table[x][y - 1] += 1
        return (table)

    def check_right(table, x, y):
        if y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x][y + 1] != 9:  # No cambiar si es bomba
                table[x][y + 1] += 1
        return (table)

    def pr(table):  # Crea un print para la matriz
        for i in table:
            print(i)

    """table = mine(10,4) poner esto en la parte de hasta abajo, luego meter una funcion que reciba los parametros de tablero chico, mediano y laro #Definir los tamaños de los tableros
    pr(table)"""

    class Board:  # Para el tablero entero
        def __init__(self, board):
            self.board = board

        def __repr__(self):
            pr(self.board)
            return ("is your table")

    class Square:  # Para cada pieza en el tablero
        def __init__(self, x, y, w, h, board, ij):
            self.rect = pygame.rect.Rect(x, y, w, h)
            i, j = ij
            self.val = board[i][j]
            self.x = x
            self.y = y
            self.visible = False
            self.flag = False

    def restart(size, bombs):
        game(size, bombs)

    def open_game(lst, square):  # Zero box tiene que tener las cajas abiertas
        square.visible = True
        i, j = square.x // 40, square.y // 40
        if i + 1 < len(lst):
            # Checa un cubo a la redonda del seleccionado, si esta y no es visible y si no esta con bandera,
            # Abrir la casilla , si es zero (en blanco) abrir todos los que estan en blanco
            if lst[i + 1][j].visible == False and lst[i + 1][j].flag == False:
                lst[i + 1][j].visible = True
                if lst[i + 1][j].val == 0:
                    open_game(lst, lst[i + 1][j])

            # Si no, se ejecuta el resto
            if j + 1 < len(lst):
                if lst[i + 1][j + 1].visible == False and lst[i + 1][j + 1].flag == False:
                    lst[i + 1][j + 1].visible = True
                    if lst[i + 1][j + 1].val == 0:
                        open_game(lst, lst[i + 1][j + 1])

            if j - 1 > 0:
                if lst[i + 1][j - 1].visible == False and lst[i + 1][j - 1].flag == False:
                    lst[i + 1][j - 1].visible = True
                    if lst[i + 1][j - 1].val == 0:
                        open_game(lst, lst[i + 1][j - 1])

        if i - 1 >= 0:
            if lst[i - 1][j].visible == False and lst[i - 1][j].flag == False:
                lst[i - 1][j].visible = True
                if lst[i - 1][j].val == 0:
                    open_game(lst, lst[i - 1][j])

            if j + 1 < len(lst):
                if lst[i - 1][j + 1].visible == False and lst[i - 1][j + 1].flag == False:
                    lst[i - 1][j + 1].visible = True
                    if lst[i - 1][j + 1].val == 0:
                        open_game(lst, lst[i - 1][j + 1])

            if j - 1 > 0:
                if lst[i - 1][j - 1].visible == False and lst[i - 1][j - 1].flag == False:
                    lst[i - 1][j - 1].visible = True
                    if lst[i - 1][j - 1].val == 0:
                        open_game(lst, lst[i - 1][j - 1])

        if j - 1 >= 0:
            if lst[i][j - 1].visible == False and lst[i][j - 1].flag == False:
                lst[i][j - 1].visible = True
                if lst[i][j - 1].val == 0:
                    open_game(lst, lst[i][j - 1])

        if j + 1 < len(lst):
            if lst[i][j + 1].visible == False and lst[i][j + 1].flag == False:
                lst[i][j + 1].visible = True
                if lst[i][j + 1].val == 0:
                    open_game(lst, lst[i][j + 1])

    def game(size, bombs):  # Crear menu con game , funcion que hace que corra el juego
        # Aqui se añaden las imagenes

        # 40 X 40 Pixeles
        grey = pygame.image.load("grey.jpg")
        white = pygame.image.load("white.jpg")

        # 20 X 20 Pixeles
        zero = pygame.image.load("0.jpg")  # Cuadro blanco de 20 x 20
        one = pygame.image.load("1.jpg")  # num 1
        two = pygame.image.load("2.jpg")  # num 2
        three = pygame.image.load("3.jpg")  # num 3
        four = pygame.image.load("4.jpg")  # num 4
        five = pygame.image.load("5.jpg")  # num 5
        six = pygame.image.load("6.jpg")  # num 6
        seven = pygame.image.load("7.jpg")  # num 7
        eight = pygame.image.load("8.jpg")  # num 8
        nine = pygame.image.load("9.jpg")  # bomba // Recordando: La bomba tiene el valor de 9
        flag = pygame.image.load("flag.jpg")  # Bandera

        wins = 0

        pygame.mixer.init()
        efectoGanar = pygame.mixer.Sound("Victory.wav")
        efectoBomba = pygame.mixer.Sound("bomb.wav")
        efectoPerder = pygame.mixer.Sound("game over voice.wav")

        numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

        c = Board(mine(size, bombs))  # Crea tablero
        W = h = len(c.board) * 75  # Tamaño de la ventana del juego, modificar, posbile error, en vez de W = w, en linea de abajo
        screen = pygame.display.set_mode((W, h))

        # Crea una lista de todos los cuadrados como en la v.01
        lst = [[] for i in range(size)]
        for i in range(0, size * 40, 40):
            for j in range(0, size * 40, 40):
                lst[i // 40] += [Square(i, j, 40, 40, c.board, (i // 40, j // 40))]

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    efectoPerder.play()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Checar cuando se haga click izquiero , en que cuadro se preciono
                    for i in lst:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                            if j.rect.colliderect(r):  # Si preciono en el cuadrado actual , donde esta el mouse
                                if j.flag == False:  # Si tiene bandera, no se puede precionar
                                    if j.val == 9:  # Si es una bomba
                                        efectoBomba.play()  # Desplegar sonido game over
                                        efectoPerder.play()
                                        run = False
                                    j.visible = True
                                    if j.val == 0:
                                        j.visible = (open_game(lst, j))  # Llama a open game funcion
                                        j.visible = True

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # Si se hace click derecho, pone o quita banderas
                    for i in lst:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                            if j.rect.colliderect(r):
                                if j.visible == False:
                                    if j.flag == False:
                                        j.flag = True
                                    elif j.flag == True:
                                        j.flag = False

            # Abrir todos los recuadros para ver el ganador

            for i in lst:
                for j in i:
                    if j.visible == True:
                        screen.blit(white, (j.x, j.y))
                        screen.blit(numbers[j.val], (j.x + 10, j.y + 10))
                        # Mostrar numeros en la derecha
                    if j.flag == True:
                        screen.blit(flag, (j.x + 10, j.y + 10))
                    if j.flag == False and j.visible == False:
                        screen.blit(grey, (j.x, j.y))
            cnt = 0
            for i in lst:
                for j in i:
                    if j.visible == True and j.val != 9:
                        cnt += 1
                        # Cuenta los espacios abiertos, si no abrimos ninguna bomba, ganamos
                if cnt == (size * size) - bombs:
                    run = False
                    efectoGanar.play()
                    wins += 1
                    return (wins)
            pygame.display.update()

        # Si gana o no, abrir mapa para ver donde todas las bombas
        for i in lst:
            for j in i:
                if j.val == 9:
                    screen.blit(nine, (j.x + 10, j.y + 10))
        pygame.display.update()

        # esperar hasta terminar o reiniciar
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    dibujar()
                    pygame.quit()
                    break


    size = 8
    bombs = (size * size) // 7
    game(size, bombs)

def Medio():
    pygame.init()

    def mine(n, bombs):  # Matrix para usar en el futuro
        table = make_table(n)
        table = add_bombs(table, bombs)
        table = change_table(table)
        return (table)

    def make_table(n):
        return [[0] * n for i in range(n)]  # matriz base

    def add_bombs(table, bombs):
        for i in range(bombs):
            is_bomb = False
            while not is_bomb:
                x = randint(0, len(table) - 1)
                y = randint(0, len(table) - 1)
                if table[x][y] != 9:  # Con 9 se dice que hay una bomba
                    table[x][y] = 9
                    is_bomb = True
        return (table)

    def change_table(table):  # Cambia el numero que indica que tan cerca esta de la bomba
        for x in range(len(table)):
            for y in range(len(table[x])):  # Posible error, cambiar x por i
                if table[x][y] == 9:
                    table = check_down_left(table, x, y)
                    table = check_down_right(table, x, y)
                    table = check_down(table, x, y)
                    table = check_up_left(table, x, y)
                    table = check_up_right(table, x, y)
                    table = check_up(table, x, y)
                    table = check_left(table, x, y)
                    table = check_right(table, x, y)
        return (table)

    def check_down_left(table, x, y):
        if x + 1 < len(table[x]) and y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x + 1][y - 1] != 9:  # No cambiar si es bomba
                table[x + 1][y - 1] += 1
        return (table)

    def check_down_right(table, x, y):
        if x + 1 < len(table[0]) and y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x + 1][y + 1] != 9:  # No cambiar si es bomba
                table[x + 1][y + 1] += 1
        return (table)

    def check_down(table, x, y):
        if x + 1 < len(table[0]):  # Checa si esta en izquierda abajo
            if table[x + 1][y] != 9:  # No cambiar si es bomba
                table[x + 1][y] += 1
        return (table)

    def check_up_left(table, x, y):
        if x - 1 >= 0 and y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x - 1][y - 1] != 9:  # No cambiar si es bomba
                table[x - 1][y - 1] += 1
        return (table)

    def check_up_right(table, x, y):
        if x - 1 >= 0 and y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x - 1][y + 1] != 9:  # No cambiar si es bomba
                table[x - 1][y + 1] += 1
        return (table)

    def check_up(table, x, y):
        if x - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x - 1][y] != 9:  # No cambiar si es bomba
                table[x - 1][y] += 1
        return (table)

    def check_left(table, x, y):
        if y - 1 >= 0:  # Checa si esta en izquierda abajo
            if table[x][y - 1] != 9:  # No cambiar si es bomba
                table[x][y - 1] += 1
        return (table)

    def check_right(table, x, y):
        if y + 1 < len(table):  # Checa si esta en izquierda abajo
            if table[x][y + 1] != 9:  # No cambiar si es bomba
                table[x][y + 1] += 1
        return (table)

    def pr(table):  # Crea un print para la matriz
        for i in table:
            print(i)

    """table = mine(10,4) poner esto en la parte de hasta abajo, luego meter una funcion que reciba los parametros de tablero chico, mediano y laro #Definir los tamaños de los tableros
    pr(table)"""

    class Board:  # Para el tablero entero
        def __init__(self, board):
            self.board = board

        def __repr__(self):
            pr(self.board)
            return ("is your table")

    class Square:  # Para cada pieza en el tablero
        def __init__(self, x, y, w, h, board, ij):
            self.rect = pygame.rect.Rect(x, y, w, h)
            i, j = ij
            self.val = board[i][j]
            self.x = x
            self.y = y
            self.visible = False
            self.flag = False

    def restart(size, bombs):
        game(size, bombs)

    def open_game(lst, square):  # Zero box tiene que tener las cajas abiertas
        square.visible = True
        i, j = square.x // 40, square.y // 40
        if i + 1 < len(lst):
            # Checa un cubo a la redonda del seleccionado, si esta y no es visible y si no esta con bandera,
            # Abrir la casilla , si es zero (en blanco) abrir todos los que estan en blanco
            if lst[i + 1][j].visible == False and lst[i + 1][j].flag == False:
                lst[i + 1][j].visible = True
                if lst[i + 1][j].val == 0:
                    open_game(lst, lst[i + 1][j])

            # Si no, se ejecuta el resto
            if j + 1 < len(lst):
                if lst[i + 1][j + 1].visible == False and lst[i + 1][j + 1].flag == False:
                    lst[i + 1][j + 1].visible = True
                    if lst[i + 1][j + 1].val == 0:
                        open_game(lst, lst[i + 1][j + 1])

            if j - 1 > 0:
                if lst[i + 1][j - 1].visible == False and lst[i + 1][j - 1].flag == False:
                    lst[i + 1][j - 1].visible = True
                    if lst[i + 1][j - 1].val == 0:
                        open_game(lst, lst[i + 1][j - 1])

        if i - 1 >= 0:
            if lst[i - 1][j].visible == False and lst[i - 1][j].flag == False:
                lst[i - 1][j].visible = True
                if lst[i - 1][j].val == 0:
                    open_game(lst, lst[i - 1][j])

            if j + 1 < len(lst):
                if lst[i - 1][j + 1].visible == False and lst[i - 1][j + 1].flag == False:
                    lst[i - 1][j + 1].visible = True
                    if lst[i - 1][j + 1].val == 0:
                        open_game(lst, lst[i - 1][j + 1])

            if j - 1 > 0:
                if lst[i - 1][j - 1].visible == False and lst[i - 1][j - 1].flag == False:
                    lst[i - 1][j - 1].visible = True
                    if lst[i - 1][j - 1].val == 0:
                        open_game(lst, lst[i - 1][j - 1])

        if j - 1 >= 0:
            if lst[i][j - 1].visible == False and lst[i][j - 1].flag == False:
                lst[i][j - 1].visible = True
                if lst[i][j - 1].val == 0:
                    open_game(lst, lst[i][j - 1])

        if j + 1 < len(lst):
            if lst[i][j + 1].visible == False and lst[i][j + 1].flag == False:
                lst[i][j + 1].visible = True
                if lst[i][j + 1].val == 0:
                    open_game(lst, lst[i][j + 1])

    def game(size, bombs):  # Crear menu con game , funcion que hace que corra el juego
        # Aqui se añaden las imagenes

        # 40 X 40 Pixeles
        grey = pygame.image.load("grey.jpg")
        white = pygame.image.load("white.jpg")

        # 20 X 20 Pixeles
        zero = pygame.image.load("0.jpg")  # Cuadro blanco de 20 x 20
        one = pygame.image.load("1.jpg")  # num 1
        two = pygame.image.load("2.jpg")  # num 2
        three = pygame.image.load("3.jpg")  # num 3
        four = pygame.image.load("4.jpg")  # num 4
        five = pygame.image.load("5.jpg")  # num 5
        six = pygame.image.load("6.jpg")  # num 6
        seven = pygame.image.load("7.jpg")  # num 7
        eight = pygame.image.load("8.jpg")  # num 8
        nine = pygame.image.load("9.jpg")  # bomba // Recordando: La bomba tiene el valor de 9
        flag = pygame.image.load("flag.jpg")  # Bandera

        wins = 0

        numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

        pygame.mixer.init()
        efectoGanar = pygame.mixer.Sound("Victory.wav")
        efectoBomba = pygame.mixer.Sound("bomb.wav")
        efectoPerder = pygame.mixer.Sound("game over voice.wav")

        c = Board(mine(size, bombs))  # Crea tablero
        W = h = len(c.board) * 60  # Tamaño de la ventana del juego, modificar, posbile error, en vez de W = w, en linea de abajo
        screen = pygame.display.set_mode((W, h))

        # Crea una lista de todos los cuadrados como en la v.01
        lst = [[] for i in range(size)]
        for i in range(0, size * 40, 40):
            for j in range(0, size * 40, 40):
                lst[i // 40] += [Square(i, j, 40, 40, c.board, (i // 40, j // 40))]

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    efectoPerder.play()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Checar cuando se haga click izquiero , en que cuadro se preciono
                    for i in lst:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                            if j.rect.colliderect(r):  # Si preciono en el cuadrado actual , donde esta el mouse
                                if j.flag == False:  # Si tiene bandera, no se puede precionar
                                    if j.val == 9:  # Si es una bomba
                                        efectoBomba.play()  # Desplegar sonido game over
                                        efectoPerder.play()
                                        run = False
                                    j.visible = True
                                    if j.val == 0:
                                        j.visible = (open_game(lst, j))  # Llama a open game funcion
                                        j.visible = True

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # Si se hace click derecho, pone o quita banderas
                    for i in lst:
                        for j in i:
                            r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                            if j.rect.colliderect(r):
                                if j.visible == False:
                                    if j.flag == False:
                                        j.flag = True
                                    elif j.flag == True:
                                        j.flag = False

            # Abrir todos los recuadros para ver el ganador

            for i in lst:
                for j in i:
                    if j.visible == True:
                        screen.blit(white, (j.x, j.y))
                        screen.blit(numbers[j.val], (j.x + 10, j.y + 10))
                        # Mostrar numeros en la derecha
                    if j.flag == True:
                        screen.blit(flag, (j.x + 10, j.y + 10))
                    if j.flag == False and j.visible == False:
                        screen.blit(grey, (j.x, j.y))
            cnt = 0
            for i in lst:
                for j in i:
                    if j.visible == True and j.val != 9:
                        cnt += 1
                        # Cuenta los espacios abiertos, si no abrimos ninguna bomba, ganamos
                if cnt == (size * size) - bombs:
                    run = False
                    efectoGanar.play()  #Aparecer sonido
                    wins += 1
                    return (wins)


            pygame.display.update()

        # Si gana o no, abrir mapa para ver donde todas las bombas
        for i in lst:
            for j in i:
                if j.val == 9:
                    screen.blit(nine, (j.x + 10, j.y + 10))
        pygame.display.update()

        # esperar hasta terminar o reiniciar
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    dibujar()
                    pygame.quit()
                    break


    size = 10
    bombs = (size * size) // 6
    game(size, bombs)


def dibujarMenu(ventana,btnJugar,btnScore, titulo): #ventana de menu
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnScore.image, btnScore.rect)
    ventana.blit(titulo.image, titulo.rect)

def dibujarNiveles(ventana,facil,medio ): #ventana de Niveles
    ventana.blit(facil.image, facil.rect)
    ventana.blit(medio.image, medio.rect)



def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    #estados
    estado="menu" #jugando,termina

    #botones
    #Jugar
    imgBotonJugar=pygame.image.load("jugar.png")
    btnJugar=pygame.sprite.Sprite()  #sprite
    btnJugar.image=imgBotonJugar
    btnJugar.rect=imgBotonJugar.get_rect()
    btnJugar.rect.left=ANCHO//2-btnJugar.rect.width//2
    btnJugar.rect.top=((ALTO//2)+150)-btnJugar.rect.height//2

    #High Score
    imgBotonScore = pygame.image.load("highscore.png")
    btnScore = pygame.sprite.Sprite()  #sprite
    btnScore.image = imgBotonScore
    btnScore.rect = imgBotonScore.get_rect()
    btnScore.rect.left = ANCHO//2-btnScore.rect.width//2
    btnScore.rect.top =((ALTO//2)+250)-btnScore.rect.height//2

    #Titulo
    imgTitulo = pygame.image.load("titulo.png")
    titulo = pygame.sprite.Sprite()  #sprite
    titulo.image = imgTitulo
    titulo.rect = imgTitulo.get_rect()
    titulo.rect.left = ANCHO//2-titulo.rect.width//2
    titulo.rect.top =((ALTO//2)-150)-titulo.rect.height//2

    #High Score
    imgBotonScore = pygame.image.load("highscore.png")
    btnScore = pygame.sprite.Sprite()  #sprite
    btnScore.image = imgBotonScore
    btnScore.rect = imgBotonScore.get_rect()
    btnScore.rect.left = ANCHO//2-btnScore.rect.width//2
    btnScore.rect.top =((ALTO//2)+250)-btnScore.rect.height//2

    #Facil
    imgBotonFacil = pygame.image.load("facil.png")
    facil = pygame.sprite.Sprite()  #sprite
    facil.image = imgBotonFacil
    facil.rect = imgBotonFacil.get_rect()
    facil.rect.left = ANCHO//2-facil.rect.width//2
    facil.rect.top =((ALTO//2)-150)-facil.rect.height//2

    #Medio
    imgBotonMedio = pygame.image.load("medio.png")
    medio = pygame.sprite.Sprite()  #sprite
    medio.image = imgBotonMedio
    medio.rect = imgBotonMedio.get_rect()
    medio.rect.left = ANCHO//2-medio.rect.width//2
    medio.rect.top =(ALTO//2)-medio.rect.height//2



    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    xb, yb, anchoB, altoB = btnJugar.rect
                    xb2, yb2, anchoB2, altoB2 = btnScore.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = "jugando"
                    if xm >= xb2 and xm <= xb2 + anchoB2:
                        if ym >= yb2 and ym <= yb2 + altoB2:
                            wins = 0
                            estado = "Scores"

                if estado == "jugando":
                    xbf, ybf, anchoBf, altoBf = facil.rect  # Coordenadas boton facil
                    xbm, ybm, anchoBm, altoBm = medio.rect  # Coordenadas boton medio

                    if xm >= xbf and xm <= xbf + anchoBf:
                        if ym >= ybf and ym <= ybf + altoBf:
                            estado = "facil"
                    if xm >= xbm and xm <= xbm + anchoBm:
                        if ym >= ybm and ym <= ybm + altoBm:
                            estado = "medio"


# Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado =="menu":
            dibujarMenu(ventana,btnJugar,btnScore, titulo)
        elif estado == "jugando":
            dibujarNiveles(ventana,facil, medio )
        elif estado == "facil":
            Facil()
            break
        elif estado == "medio":
            Medio()
            break
        elif estado == "Scores":
            if wins == 0:
                Nombre = "Player1 -"
                scores = open("HighScores.txt", "w", encoding="UTF-8")
                scores.write("Nombre\tJuegos Terminados\n")
                scores.write(str(Nombre))
                scores.write(str(wins))
                scores.close

            else:
                Nombre = "Player1 -"
                scores = open("HighScores.txt", "w", encoding="UTF-8")
                scores.write("Nombre\tJuegos Terminados\n")
                scores.write(str(Nombre))
                scores.write(str(wins))
                scores.close


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():

    dibujar()

main()


