# encoding: UTF-8
# Javier Pascal Flores

import pygame
from random import randint
from collections import OrderedDict

# Dimensiones de la pantalla
ancho = 800
alto = 600
screen = pygame.display.set_mode((ancho,alto))
# Colores
blanco = (255, 255, 255)  # R,G,B en el rango [0,255]
verde_bandera = (0, 122, 0)
rojo = (255, 0, 0)
negro = (0, 0, 0)
print("Moverse = Mouse" + "\n" + "Disparar = Espacio")
username=input("Dame tu username: ")


def drawMenu(ventana, playButton, Logo, high):
    ventana.blit(playButton.image, playButton.rect)
    ventana.blit(Logo.image, Logo.rect)
    ventana.blit(high.image, high.rect)
def drawGAmeover(ventana):
    imgGO=pygame.image.load("Images/Gameover.png")
    ventana.blit(imgGO,(200,200))


def drawGame(ventana, enemiesList, bulletList):
    for enemy in enemiesList:
        ventana.blit(enemy.image, enemy.rect)
    for bullet in bulletList:
        ventana.blit(bullet.image, bullet.rect)

def refreshBullets(bulletlist, enemiesList,puntos):

    for bullet in bulletlist:  # DO NOT MODIFY CONNECTION
        bullet.rect.top -= 15
        if bullet.rect.top < -15:
            bulletlist.remove(bullet)
            continue
        delBullet = False
        for k in range(len(enemiesList) - 1, -1, -1):
            enemy = enemiesList[k]
            if bullet.rect.colliderect(enemy):
                enemiesList.remove(enemy)
                delBullet = True
                puntos+=50
                break
        if delBullet == True:
            bulletlist.remove(bullet)
    return puntos
def refreshEnemies(enemiesList):
    for enemy in enemiesList:  # DO NOT MODIFY CONNECTION
        enemy.rect.top += 2




"""def spawnEnemies(enemiesList, imgEnemy):
    for x in range(5):
        for y in range(2):
            # X,Y coordenates
            cx = 50 + x * 150
            cy = 50 + y * 150
            enemy = pygame.sprite.Sprite()
            enemy.image = imgEnemy
            enemy.rect = imgEnemy.get_rect()
            enemy.rect.left = cx - enemy.rect.width // 2
            enemy.rect.top = cy - enemy.rect.height // 2
            enemiesList.append(enemy)"""


def DibujarBogo(ventana):
    xm, ym = pygame.mouse.get_pos()
    imgBogo = pygame.image.load("Images/Spaceship.png")
    bogo = pygame.sprite.Sprite()
    bogo.image = imgBogo
    bogo.rect = imgBogo.get_rect()
    bogo.rect.left = xm - 55
    bogo.rect.top = alto - bogo.rect.height

    ventana.blit(bogo.image,bogo.rect)
    return bogo





def randomEnemies(enemiesList, imgEnemy, imgEnemy_69,img_Comet):
    enemy = pygame.sprite.Sprite()
    enemy.image = imgEnemy
    enemy.rect = imgEnemy.get_rect()
    cx = randint(10, ancho - enemy.rect.width)
    cy = -enemy.rect.height
    enemy.rect.left = cx
    enemy.rect.top =cy
    fail = pygame.sprite.Sprite()
    fail.image = imgEnemy_69
    fail.rect = imgEnemy_69.get_rect()
    fail.rect.left = randint(10, ancho - fail.rect.width)
    fail.rect.top = -fail.rect.height
    comet = pygame.sprite.Sprite()
    comet.image = img_Comet
    comet.rect = img_Comet.get_rect()
    comet.rect.left = randint(10, ancho - comet.rect.width)
    comet.rect.top = -comet.rect.height


    enemiesList.append(enemy)
    enemiesList.append((fail))
    enemiesList.append((comet))


def drawHighscores(ventana, Logo, screen,state):
    entrada = open("highscores.txt", "r", encoding='UTF-8')
    contenido = entrada.readlines()

    entrada.close()

    imgSpace = pygame.image.load("images/Back/Space.png")
    ventana.blit(imgSpace,(0,0))
    ventana.blit(Logo.image, Logo.rect)
    displacement=0
    for linea in contenido:

        displacement+=30
        font = pygame.font.SysFont("monospace", 25)
        text = font.render(str(linea), 5, rojo)
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery+displacement
        ventana.blit(text, textrect)
    xm, ym = pygame.mouse.get_pos()
    imgButPlay = pygame.image.load("Images/button_jugar.png")
    # Sprite
    playButton = pygame.sprite.Sprite()
    playButton.image = imgButPlay
    playButton.rect = imgButPlay.get_rect()
    playButton.rect.left = 0
    playButton.rect.top = 0
    xb, yb, anchoB, altoB = playButton.rect
    if xm >= xb and xm <= xb + anchoB:
        if ym >= yb and ym <= yb + altoB:
            state= "jugando"
    ventana.blit(playButton.image, playButton.rect)
    return state



def highscoresinterpreter(highscoresDicc,usuario, score):
    newFile = open("highscores.txt","w",encoding='UTF-8')
    highscoresDicc[usuario]=score
    orderedDict = dict(OrderedDict(sorted(highscoresDicc.items(), key=lambda t: t[1], reverse=False)))
    keys = []
    values = []
    for key in highscoresDicc:
        keys.append(key)
        values.append(highscoresDicc[key])
    print(keys,values)
    newFile.write("0,Username,Play Time,n\n")
    for index in range(len(orderedDict)):
        newFile.write(str(index+1) + ","+ keys[index] +","+ str(values[index]) +",n\n")
    newFile.close()

def makeHighscores():
    highscoresDicc = {}
    file = open("highscores.txt", "r", encoding="UTF-8")
    content = file.readlines()
    file.close()

    content.remove(content[0])

    for line in content:
        newLine = line.split(",")
        highscoresDicc[newLine[1]] = float(newLine[2])
    return highscoresDicc


def Livesubstract(ventana, bogo, enemiesList, lives):
    for enemy in enemiesList:
        if pygame.sprite.collide_rect(bogo, enemy):
            lives -= 1
    font = pygame.font.SysFont("monospace", 18)
    text = font.render("Vidas:" + str(lives), 1, blanco)
    ventana.blit(text, (10, 10))
    return lives

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ancho, alto))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    state = "menu"  # playing, end
    lives=1

    # Load images
    imgButPlay = pygame.image.load("Images/button_jugar.png")
    # Sprite
    playButton = pygame.sprite.Sprite()
    playButton.image = imgButPlay
    playButton.rect = imgButPlay.get_rect()
    playButton.rect.left = ancho // 2 - playButton.rect.width // 2
    playButton.rect.top = alto // 2 - playButton.rect.height // 2
    # Load images
    imgLogo = pygame.image.load("Images/Logo.png")
    # Sprite
    Logo = pygame.sprite.Sprite()
    Logo.image = imgLogo
    Logo.rect = imgLogo.get_rect()
    Logo.rect.left = ancho // 2 - Logo.rect.width // 2
    Logo.rect.top = playButton.rect.top - 200
    #Loadd Images
    imgButHigh = pygame.image.load("Images/button_highscores.png")
    # Sprite
    highButton = pygame.sprite.Sprite()
    highButton.image = imgButHigh
    highButton.rect = imgButHigh.get_rect()
    highButton.rect.left = (ancho // 2 - highButton.rect.width // 2)
    highButton.rect.top = (alto // 2 - highButton.rect.height // 2)+150
    #Sprite





    #Fondo de Menu
    imgSpace = pygame.image.load("images/Back/Space.png")
    #Game Over



    #Imagen Fondo
    image_back = pygame.image.load("images/Back/FondoSpace.png")
    y = 0
    #
    enemiesList = []
    imgEnemy = pygame.image.load("Images/DA.png")
    imgEnemy_69=pygame.image.load("Images/69.png")
    img_Comet = pygame.image.load("Images/Comet.png")

    #spawnEnemies(enemiesList, imgEnemy)

    # Balas
    bulletList = []
    imgBullet = pygame.image.load("Images/rayito.png")

    timer = 0


    # Music
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/zizibum.mp3")
    pygame.mixer.music.play(-1)


    highscoreDicc=makeHighscores()
    score=0

    while not termina:
        # Procesa los eventos que recibe

        xm, ym = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Mouse Clicked

                if state == "menu":
                    xb, yb, anchoB, altoB = playButton.rect
                    xh, yh, anchoH, altoH = highButton.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            state = "jugando"
                            # Switch Window
                    if xm >= xh and xm <= xh + anchoH:
                        if ym >= yh and ym <= yh + altoH:
                            state = "highscore"
                elif state == "jugando":
                    enemy = pygame.sprite.Sprite()
                    enemy.image = imgEnemy
                    enemy.rect = imgEnemy.get_rect()
                    enemy.rect.left = xm - enemy.rect.width // 2
                    enemy.rect.top = ym - enemy.rect.height // 2
                    enemiesList.append(enemy)


            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:

                    bullet = pygame.sprite.Sprite()
                    bullet.image = imgBullet
                    bullet.rect = imgBullet.get_rect()
                    bullet.rect.left = xm
                    bullet.rect.top = alto
                    bulletList.append(bullet)


        # Borrar pantalla

        ventana.fill(negro)


        # Enemies every 2 sec

        timer += 1 / 40
        if timer >= 1:
            timer = 0
            randomEnemies(enemiesList, imgEnemy, imgEnemy_69, img_Comet)

        # Dibujar, aquí haces todos los trazos que requieras
        if state == "menu":
            ventana.blit(imgSpace, (0, 0))
            drawMenu(ventana, playButton,Logo,highButton)
        elif state == "highscore":

            estado=drawHighscores(ventana, Logo, screen, state)
            if estado =="jugando":
                state="jugando"





        elif state == "jugando":
            ventana.blit(image_back, (0, y))

            ventana.blit(image_back, (0, y))
            y -= 9

            if y <= -10000:
                y = 0

            refreshBullets(bulletList, enemiesList,0)
            refreshEnemies(enemiesList)
            drawGame(ventana, enemiesList, bulletList)
            bogo=DibujarBogo(ventana)
            lives=Livesubstract(ventana, bogo, enemiesList, lives)
            if lives ==0:
                state ="gameover"
        elif state == "gameover":
            drawGAmeover(ventana)

        score+=1
        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame
    highscoresinterpreter(highscoreDicc, username, score)


def main():
    dibujar()

main()
