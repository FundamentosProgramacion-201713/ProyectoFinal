#Encoding: utf-8
#Diego González y amistades
#VideojuegoProyectoFinal
#Mucho copy right, no subir a la red, demanda segura.
#(cuphead, mario, sonidos wav carpeta inter, something jst like this, imagenes de google, etc)
#Cabe mencionar que no tiene menu y eso por ser e 1 dia(hoy)
#Solo es para su entretenimiento y para darles las gracias por el apoyo
#Seguire programando, aprendiendo y lo que le conte, pero lamentablemente no podre quesarme en ISC
#Fue un gusto tomar su clase y hablar con usted, de seguro en el futuro lo volvere a ver

import math
import random
import pygame
from pygame.locals import *


pygame.init()
pygame.mixer.init()
ancho, alto = 640, 480
pantalla = pygame.display.set_mode((ancho, alto))
llaves = [False, False, False, False]
playerPos = [100, 100]
acc = [0, 0]
balas = []
tiempoRespawn = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194


cupPlayer1 = pygame.image.load("imagenesFinal2/cupPlayer.png")
sky1 = pygame.image.load("imagenesFinal2/sky.png")
itemBox1 = pygame.image.load("imagenesFinal2/itemBox.png")
laser1 = pygame.image.load("imagenesFinal2/laser.png")
badguyimg1 = pygame.image.load("imagenesFinal2/enemy1.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("imagenesFinal2/healthbar.png")
health = pygame.image.load("imagenesFinal2/health.png")
gameover = pygame.image.load("imagenesFinal2/gameover.png")
youwin = pygame.image.load("imagenesFinal2/youwin.png")

hit = pygame.mixer.Sound("audio/explode.wav")
enemy = pygame.mixer.Sound("audio/enemy.wav")
shoot = pygame.mixer.Sound("audio/shoot.wav")
hit.set_volume(0.03)
enemy.set_volume(0.03)
shoot.set_volume(0.03)
pygame.mixer.music.load('audio/game2.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

run = 1
exitcode = 0

while run:

    pantalla.fill(0)

    for x in range(ancho // sky1.get_width()+1):
        for y in range(alto // sky1.get_height()+1):
            pantalla.blit(sky1, (x * 100, y * 100))
    pantalla.blit(itemBox1, (0, 30))
    pantalla.blit(itemBox1, (0, 135))
    pantalla.blit(itemBox1, (0, 240))
    pantalla.blit(itemBox1, (0, 345))

    posicion = pygame.mouse.get_pos()
    ang = math.atan2(posicion[1] - (playerPos[1] + 32), posicion[0] - (playerPos[0] + 26))
    playerrot = pygame.transform.rotate(cupPlayer1, 360 - ang * 57.29)
    posPlayer1 = (playerPos[0] - playerrot.get_rect().width / 2, playerPos[1] - playerrot.get_rect().height / 2)
    pantalla.blit(playerrot, posPlayer1)

    for bala in balas:
        index = 0
        velx = math.cos(bala[0]) * 10
        vely = math.sin(bala[0]) * 10
        bala[1] += velx
        bala[2] += vely
        if bala[1] <-64 or bala[1] > 640 or bala[2] <-64 or bala[2] > 480:
            balas.pop(index)
        index += 1
        for projectile in balas:
            arrow1 = pygame.transform.rotate(laser1, 360 - projectile[0] * 57.29)
            pantalla.blit(arrow1, (projectile[1], projectile[2]))

    if tiempoRespawn == 0:
        badguys.append([640, random.randint(50, 430)])
        tiempoRespawn = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] <-64:
            badguys.pop(index)
        badguy[0] -= 7

        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)

        index1 = 0
        for bala in balas:
            balarect = pygame.Rect(laser1.get_rect())
            balarect.left = bala[1]
            balarect.top = bala[2]
            if badrect.colliderect(balarect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                balas.pop(index1)
            index1 += 1

        index += 1
    for badguy in badguys:
        pantalla.blit(badguyimg, badguy)

    font = pygame.font.Font(None, 24)
    txtSurvive = font.render(str((90000 - pygame.time.get_ticks()) // 60000) + ":" + str((90000 - pygame.time.get_ticks()) // 1000 % 60).zfill(2), True, (0, 0, 0))
    textRect = txtSurvive.get_rect()
    textRect.topright = [635, 5]
    pantalla.blit(txtSurvive, textRect)

    pantalla.blit(healthbar, (5, 5))
    for health1 in range(healthvalue):
        pantalla.blit(health, (health1 + 8, 8))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_w:
                llaves[0] = True
            elif event.key == K_a:
                llaves[1] = True
            elif event.key == K_s:
                llaves[2] = True
            elif event.key == K_d:
                llaves[3] = True
        if event.type == KEYUP:
            if event.key == K_w:
                llaves[0] = False
            elif event.key == K_a:
                llaves[1] = False
            elif event.key == K_s:
                llaves[2] = False
            elif event.key == K_d:
                llaves[3] = False
        if event.type == QUIT:

            pygame.quit()
            exit(0)
        if event.type == MOUSEBUTTONDOWN:
            shoot.play()
            posicion = pygame.mouse.get_pos()
            acc[1] += 1
            balas.append([math.atan2(posicion[1] - (posPlayer1[1] + 32), posicion[0] - (posPlayer1[0] + 26)), posPlayer1[0] + 32, posPlayer1[1] + 32])

    if llaves[0]:
        playerPos[1] -= 5
    elif llaves[2]:
        playerPos[1] += 5
    if llaves[1]:
        playerPos[0] -= 5
    elif llaves[3]:
        playerPos[0] += 5
    tiempoRespawn -= 1

    if pygame.time.get_ticks() >= 90000:
        run = 0
        exitcode = 1
    if healthvalue <= 0:
        run = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy) + "%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = pantalla.get_rect().centerx
    textRect.centery = pantalla.get_rect().centery + 24
    pantalla.blit(gameover, (0, 0))
    pantalla.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = pantalla.get_rect().centerx
    textRect.centery = pantalla.get_rect().centery + 24
    pantalla.blit(youwin, (0, 0))
    pantalla.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
