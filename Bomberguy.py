# encoding: utf-8
# autor: Iván Alejandro Dumas Martínez
# descripción: este juego para el Proyecto Final de la materia es un


from collections import OrderedDict
import pygame,time
from pygame.locals import *
from random import randint

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600
# Colores
WHITE = (255, 255, 255)  # R,G,B en el rango [0,255]
GREEN = (0, 122, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

DOWN = 'down'
UP = 'up'
RIGHT = 'right'
LEFT = 'left'


title = "Bomberguy"

BOMB_TIME = 3


def menu(window, play_button,score_button,logo):
    window.blit(score_button.image,score_button.rect)
    window.blit(play_button.image, play_button.rect)
    window.blit(logo.image, logo.rect)

def openHighscores():
    dictHighscores={}
    file = open("highscores.txt","r",encoding="UTF-8")
    content = file.readlines()
    file.close()
    content.remove(content[0])
    for line in content:
        newLine = line.split(",")
        dictHighscores[newLine[1]]=float(newLine[2])
    return dictHighscores


def draw(window,breakableList,blockList,bombList,tacoList):
    for breakable in breakableList:
        window.blit(breakable.image,breakable.rect)
    for taco in tacoList:
        window.blit(taco.image,taco.rect)
    #for enemy in enemyList:
        #window.blit(enemy.image, enemy.rect)
    for block in blockList:
        window.blit(block.image, block.rect)
    for bomb in bombList:
        window.blit(bomb.image, bomb.rect)


"""
def createLevels():
    for i in range(10):
        level = "resources/levels/level_"
        level += str(i)+".txt"
        file = open(level,"w")
        line1 = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 n\n"
        line2 = "1 0 0 1 2 2 2 0 0 2 0 2 0 2 1 n\n"
        line3 = "1 0 2 0 2 0 2 0 1 0 1 2 1 1 1 n\n"
        file.write(line1+line2+line3)
        for k in range(8):
            lineK = "1"
            for j in range(13):
                randominteger = randint(2,5)
                lineK += " "+str(randominteger)
            lineK += " 1 n\n"
            file.write(lineK)
        file.write(line1)
        file.close()
"""


def checkFireCollision(fireList, breakableList,bomberguy):
    lifeLost = False
    for breakable in breakableList:
        for fire in fireList:
            if fire.rect.colliderect(breakable):
                breakableList.remove(breakable)
                break
    for fire in fireList:
        if bomberguy.rect.colliderect(fire):
            lifeLost = True
    return lifeLost

def checkBomberguyCollisions(bomberguy,tacoList,tacoSound):
    lifeWon = False
    for taco in tacoList:
        if bomberguy.rect.colliderect(taco):
            lifeWon = True
            tacoList.remove(taco)
            tacoSound.play()
    return lifeWon


def erase(window,bombList,bombTimer,breakableList,imgFire,bomberguy,explotion):
    fireList = []
    fire = pygame.sprite.Sprite()
    fire.image = imgFire
    fire.rect = imgFire.get_rect()
    for bomb in bombList:
        print("2:", bombTimer)
        if bombTimer>=BOMB_TIME-0.2:
            xBomb = bomb.rect.left
            yBomb = bomb.rect.top
            fire.rect.left = xBomb - fire.rect.width//4
            fire.rect.top = yBomb - fire.rect.height//4
            bombList.remove(bomb)
            fireList.append(fire)
            explotion.play()
    for fire in fireList:
        window.blit(fire.image,fire.rect)
    lifeLost = checkFireCollision(fireList, breakableList,bomberguy)
    return lifeLost



def generateMap(level,imgBlock,blockList,imgBreakable, breakableList,imgTaco,tacoList):
    mapFile = open(level,"r")
    content = mapFile.readlines()
    #specialObjectsList = [taco, salsa, speed, ""]
    mapFile.close()
    count = 0
    for line in content:
        column = line.split(" ")
        yD = count * 50 + 50
        for index in range(len(column)):
            xD = index * 50 + 25
            #print(xD,yD)
            if column[index]== "0":
                taco = pygame.sprite.Sprite()
                taco.image = imgTaco
                taco.rect = imgTaco.get_rect()
                taco.rect.left = xD
                taco.rect.top = yD
                luck = randint(1,20)
                if luck == 2:
                    tacoList.append(taco)
            if column[index]=="1":
                block = pygame.sprite.Sprite()
                block.image = imgBlock
                block.rect = imgBlock.get_rect()
                block.rect.left = xD
                block.rect.top = yD
                blockList.append(block)
            elif column[index]=="2":
                breakable = pygame.sprite.Sprite()
                breakable.image = imgBreakable
                breakable.rect = imgBreakable.get_rect()
                breakable.rect.left = xD
                breakable.rect.top = yD
                #rc = random.choice(len(specialObjectsList))
                #object = specialObjectsList[rc]
                #object
                breakableList.append(breakable)
        count += 1

    return tacoList,breakableList,blockList


def playing(window,bomberguy,blockList,breakableList,tacoList,bombList,bombTimer,imgFire,explotion):
    level = "l1"

    if level == "l1":
        win = False
        draw(window, breakableList, blockList, bombList,tacoList)
        lifeLost = erase(window, bombList, bombTimer, breakableList, imgFire,bomberguy,explotion)
        if win == True:
            level = "END"
    if level == "END":
        #generateMap("resources/levels/level_two.txt",block,blockList,breakable, breakableList)
        #END = True
        pass

    return lifeLost


def drawHighscores(window, returnButton):
    window.blit(returnButton.image,returnButton.rect)


def drawGameover(window, imgGO, playAgain_button):
    window.blit(imgGO,(0,0))


def processHighscores(dictHighscore,usuario, score):
    newFile = open("highscores.txt","w",encoding='UTF-8')
    dictHighscore[usuario]=score
    orderedDict = dict(OrderedDict(sorted(dictHighscore.items(), key=lambda t: t[1], reverse=False)))
    keys = []
    values = []
    for key in dictHighscore:
        keys.append(key)
        values.append(dictHighscore[key])
    print(keys,values)
    newFile.write("0,Username,Play Time,n\n")
    for index in range(len(orderedDict)):
        newFile.write(str(index+1) + ","+ keys[index] +","+ str(values[index]) +",n\n")
    newFile.close()

def mainDraw():
    xBG = 80
    yBG = 110

    lives = 3

    timeScore = 0
    delay = 0

    usuario = input("Teclea el nombre de usuario: ")

    dictHighscores = openHighscores()

    pygame.init()   # Inicializa pygame
    pygame.display.set_caption(title)
    window = pygame.display.set_mode((WIDTH, HEIGHT))    # Crea la ventana de dibujo
    clock = pygame.time.Clock() # Para limitar los fps
    ends = False # Bandera para saber si termina la ejecución

    bombTimer = 0
    bombBool = False
    #Imágenes

    imgPlayButton = pygame.image.load("resources/images/play_button.png")
    playButton = pygame.sprite.Sprite()
    playButton.image = imgPlayButton
    playButton.rect = imgPlayButton.get_rect()
    playButton.rect.left = WIDTH // 2 - playButton.rect.width // 2
    playButton.rect.top = HEIGHT // 2 - playButton.rect.height // 2

    imgLogo = pygame.image.load("resources/images/logo.png")
    logo = pygame.sprite.Sprite()
    logo.image = imgLogo
    logo.rect = imgLogo.get_rect()
    logo.rect.left = WIDTH//2 - logo.rect.width//2
    logo.rect.top = HEIGHT//6

    imgScoreButton = pygame.image.load("resources/images/score_button.png")
    scoreButton = pygame.sprite.Sprite()
    scoreButton.image = imgScoreButton
    scoreButton.rect = imgScoreButton.get_rect()
    scoreButton.rect.left = WIDTH // 2 - scoreButton.rect.width // 2
    scoreButton.rect.top = HEIGHT // 2 + scoreButton.rect.height

    imgReturnButton = pygame.image.load("resources/images/return_button.png")
    returnButton = pygame.sprite.Sprite()
    returnButton.image = imgReturnButton
    returnButton.rect = imgReturnButton.get_rect()
    returnButton.rect.left = returnButton.rect.width//2
    returnButton.rect.top = HEIGHT - 1.5*(returnButton.rect.height)

    imgPlayAButton = pygame.image.load("resources/images/playagain_button.png")
    playAButton = pygame.sprite.Sprite()
    playAButton.image = imgPlayAButton
    playAButton.rect = imgPlayAButton.get_rect()
    playAButton.rect.left = playAButton.rect.width//2
    playAButton.rect.top = HEIGHT - 1.5*(playAButton.rect.height)

    imgBomberguy = pygame.image.load("resources/images/bomberguy_down.png")

    imgBlock = pygame.image.load("resources/images/block.png")
    blockList = []

    imgBreakable = pygame.image.load("resources/images/breakable.png")
    breakableList = []

    imgTaco = pygame.image.load("resources/images/taco.png")
    tacoList = []

    tacoList,breakableList,blockList = generateMap("resources/levels/level_one.txt", imgBlock, blockList, imgBreakable, breakableList,imgTaco,tacoList)

    imgBomb = pygame.image.load("resources/images/bomb.png")
    bombList = []

    imgFire = pygame.image.load("resources/images/fire.png")

    bgImage = pygame.image.load("resources/images/grass_background.png")
    imgGO = pygame.image.load("resources/images/gameover.jpg")

    #audio
    explotion = pygame.mixer.Sound("resources/sounds/explode.wav")
    tacoSound = pygame.mixer.Sound("resources/sounds/taco.wav")
    song = pygame.mixer.Sound("resources/sounds/moonlight.wav")

    state = "menu"

    while not ends:
        # Procesa los eventos que recibe
        for event in pygame.event.get():
            xM, yM = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                ends = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if state == "menu":
                    xPB, yPB, widthB, heightB = playButton.rect
                    if (xM >= xPB and xM <= xPB + widthB) and (yM >= yPB and yM <= yPB + heightB):
                        state = "playing"
                    xScoreB,yScoreB,widthSB,heightSB=scoreButton.rect
                    if (xM >= xScoreB and xM <= xScoreB + widthSB) and (yM >= yScoreB and yM <= yScoreB + heightSB):
                        state = "highscores"

                if state == "playing":
                    pass
                if state == "highscores":
                    xRtrn, yRtrn,heightRtrn, widthRtrn = returnButton.rect
                    if (xM >= xRtrn and xM <= xRtrn + widthRtrn) and (yM >= yRtrn and yM <= yRtrn + heightRtrn):
                        state = "menu"
            elif event.type == pygame.KEYDOWN:
                if state == "playing":
                    if (event.key == pygame.K_SPACE):
                        bombBool = True
                        if bombTimer < BOMB_TIME:
                            bomb= pygame.sprite.Sprite()
                            bomb.image = imgBomb
                            bomb.rect = imgBomb.get_rect()
                            bomb.rect.left = xBG
                            bomb.rect.top = yBG
                            bombList.append(bomb)



        # Borrar pantalla
        window.fill(WHITE)

        # Dibujar, aquí haces todos los trazos que requieras
        if state == "menu":
            song.play()
            menu(window,playButton,scoreButton,logo)
        if state == "highscores":
            drawHighscores(window, returnButton)
        if state == "playing":
            song.stop()
            window.blit(bgImage,(0,0))
            bomberguy = pygame.sprite.Sprite()
            bomberguy.image = imgBomberguy
            bomberguy.rect = imgBomberguy.get_rect()
            bomberguy.rect.left = xBG
            bomberguy.rect.top = yBG
            window.blit(bomberguy.image, bomberguy.rect)

            lifeLost = playing(window,bomberguy,blockList,breakableList,tacoList,bombList,bombTimer,imgFire,explotion)
            #bomberguyDraw(window, imgBomberguy, xBG, yBG,blockList,breakableList)
            lifeWon = checkBomberguyCollisions(bomberguy,tacoList,tacoSound)

            pressed_key = pygame.key.get_pressed()

            bomberguy = pygame.sprite.Sprite()
            bomberguy.image = imgBomberguy
            bomberguy.rect = imgBomberguy.get_rect()
            bomberguy.rect.left = xBG
            bomberguy.rect.top = yBG
            window.blit(bomberguy.image, bomberguy.rect)

            """if pressed_key[K_DOWN]:
                yBG += 5

            if pressed_key[K_UP]:
                yBG -= 5

            if pressed_key[K_RIGHT]:
                xBG += 5

            if pressed_key[K_LEFT]:
                xBG -= 5"""
            if lives == 0:
                state="GAMEOVER"


            if pressed_key[K_DOWN] and bomberguy.rect.y<(HEIGHT-bomberguy.rect.height-50):
                yBG += 10
                imgBomberguy = pygame.image.load("resources/images/bomberguy_down.png")
                if pygame.sprite.spritecollide(bomberguy, breakableList, False):
                    yBG -= 20

            if pressed_key[K_UP] and bomberguy.rect.y>100:
                yBG -= 10
                imgBomberguy = pygame.image.load("resources/images/bomberguy_up.png")
                if pygame.sprite.spritecollide(bomberguy, breakableList, False):
                    yBG += 20

            if pressed_key[K_RIGHT] and bomberguy.rect.x<(WIDTH-bomberguy.rect.width-75):
                xBG += 10
                imgBomberguy = pygame.image.load("resources/images/bomberguy_right.png")
                if pygame.sprite.spritecollide(bomberguy, breakableList, False):
                    xBG -= 20

            if pressed_key[K_LEFT] and bomberguy.rect.x>75:
                xBG -= 10
                imgBomberguy = pygame.image.load("resources/images/bomberguy_left.png")
                if pygame.sprite.spritecollide(bomberguy, breakableList, False):
                    xBG += 20

            """for block in blockList:
                if block.rect.colliderect(bomberguy):
                    collides = True

            for breakable in breakableList:
                if breakable.rect.colliderect(bomberguy):
                    collides = True"""



            """if pressed_key[K_UP] and not collides:
                yBG -= 10
            if pressed_key[K_RIGHT] and not collides:
                xBG += 10
            if pressed_key[K_LEFT] and not collides:
                xBG -= 10
            if pressed_key[K_SPACE] and not collides:
                xB = xBG
                yB = yBG"""

            if lifeLost == True:
                lives -= 1
            elif lifeWon == True:
                lives += 1

            font = pygame.font.SysFont("monospace", 25)
            text = font.render("Vidas:" + str(lives), 1, WHITE)
            window.blit(text, (10, 10))


        if state == "GAMEOVER":
            score = overallTime
            drawGameover(window,imgGO,playAButton)
            delay += overallTime/1000
            if delay == 5:
                ends = True


        pygame.display.flip()   # Actualiza trazos
        overallTime = clock.tick(40)
        print("Score",timeScore)
        print("time:",overallTime)
        if bombBool == True:
            bombTimer += overallTime / 1000
            if bombTimer >= BOMB_TIME:
                bombTimer = 0           #  40 fps


    pygame.quit()
    processHighscores(dictHighscores, usuario, score)# termina pygame


def main():
    mainDraw()
    #createLevels()
    #openHighscores()


main()