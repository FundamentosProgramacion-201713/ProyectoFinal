import pygame, sys, time
from pygame.locals import *
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 500
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDEPANTALLA = (55, 126, 3)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
GRIS = (89, 89, 89)
vida = 3
nivel = 1
comida = 0


def dibujarSnake(snake, ventana):
    for i in range(len(snake)):
        pygame.draw.rect(ventana, NEGRO, (snake[i][1] * 20, snake[i][0] * 20, 20, 20), 4)


def dibujarVentanita(ventana):
    pygame.draw.rect(ventana, NEGRO, (20, 40, ANCHO - 40, ALTO - 60), 1)


def avanzar(snake, nuevaPos):
    for i in reversed(range(1, len(snake))):
        snake[i] = snake[i - 1]
    snake[0] = nuevaPos
    return snake


def iniciarVentana():
    global vida, nivel, comida
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    snake, limites = [[5, 7], [5, 6], [5, 5]], [5, 7, 5, 5]
    comidavenenosa = []
    derecha, izquierda, arriba, abajo, rand1, rand2 = True, False, False, False, 10, 10
    muerto = False

    while True:
        ventana.fill(VERDEPANTALLA)
        dibujarVentanita(ventana)
        pygame.draw.rect(ventana, GRIS, (rand1 * 20, rand2 * 20, 20, 20))
        fuente = pygame.font.Font(None, 45)
        texto1 = fuente.render("Snake: " + str(comida + (10 * (nivel - 1))), 1, NEGRO)
        texto2 = fuente.render("Vidas: " + str(vida), 1, NEGRO)
        texto3 = fuente.render("Nivel: " + str(nivel), 1, NEGRO)
        ventana.blit(texto1, (10, 10))
        ventana.blit(texto2, (650, 10))
        ventana.blit(texto3, (350, 10))

        if not muerto:
            dibujarSnake(snake, ventana)

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()
            if not muerto:
                if events.type == KEYDOWN:
                    if events.key == K_DOWN and not arriba:
                        abajo, arriba, derecha, izquierda = True, False, False, False
                    elif events.key == K_UP and not abajo:
                        arriba, abajo, derecha, izquierda = True, False, False, False
                    elif events.key == K_RIGHT and not izquierda:
                        derecha, arriba, abajo, izquierda = True, False, False, False
                    elif events.key == K_LEFT and not derecha:
                        izquierda, arriba, derecha, abajo = True, False, False, False

        if snake[0][0] == rand2 and snake[0][1] == rand1:
            snake.append([0, 0])
            rand1, rand2 = randint(2, 37), randint(3, 21)
            comida += 1

        for i in range(0, len(comidavenenosa)):
            if rand1 == comidavenenosa[i][0] and rand2 == comidavenenosa[i][0]:
                rand1, rand2 = randint(2, 37), randint(3, 21)
                break

        for i in range(1, len(snake)):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                pygame.quit()
                sys.exit()

        if comida == 10:
            nivel += 1
            comida = 0
            com1, com2 = randint(1, 38), randint(2, 22)
            comidavenenosa.append([com1, com2])

        for i in range(0, len(comidavenenosa)):
            pygame.draw.rect(ventana, ROJO, (comidavenenosa[i][0] * 20, comidavenenosa[i][1] * 20, 20, 20))
            if snake[0][0] == comidavenenosa[i][1] and snake[0][1] == comidavenenosa[i][0]:
                derecha = True
                izquierda = False
                arriba = False
                abajo = False
                vida -= 1
                comida = 0
                snake = [[5, 7], [5, 6], [5, 5]]

        if vida == 0:
            fuente = pygame.font.Font(None, 150)
            texto4 = fuente.render("GAME OVER", 1, NEGRO)
            ventana.blit(texto4, (100, 200))
            muerto = True

        if vida == -1:
            vida = 3
            muerto = False

        if snake[0][0] <= 1 or snake[0][0] >= 24 or snake[0][1] <= 0 or snake[0][1] >= 39:
            derecha = True
            izquierda = False
            arriba = False
            abajo = False
            vida -= 1
            snake = [[5, 7], [5, 6], [5, 5]]

        if derecha:
            snake = avanzar(snake, [snake[0][0], snake[0][1] + 1])
        elif izquierda:
            snake = avanzar(snake, [snake[0][0], snake[0][1] - 1])
        elif arriba:
            snake = avanzar(snake, [snake[0][0] - 1, snake[0][1]])
        elif abajo:
            snake = avanzar(snake, [snake[0][0] + 1, snake[0][1]])
        time.sleep(.1)
        pygame.display.update()


def main():
    iniciarVentana()


main()