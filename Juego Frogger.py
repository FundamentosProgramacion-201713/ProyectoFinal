#encoding: UTF-8
#Javier Martínez Hernández
#juego de Frooger
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)




def dibujarMenu(ventana, btnJugar, btnRanking,fuente1,btnIns):
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnRanking.image, btnRanking.rect)
    ventana.blit(btnIns.image, btnIns.rect)
    texto=fuente1.render("Froggar",0,(VERDE_BANDERA))
    ventana.blit(texto,(ANCHO//2-90,ALTO-500))

def dibujarRanking(ventana, btnVolver,fuente1):
    ventana.blit(btnVolver.image,btnVolver.rect)
    datos=open("ranking.txt","r" ,encoding="UTF-8")
    linea=datos.readlines()
    contador=50
    for lineas in linea:
        texto=fuente1.render(lineas,0,NEGRO)
        ventana.blit(texto,(ANCHO//2-150,contador))
        contador+=50

def dibujarJuego(ventana,spriteRana,listaNinfas,listaTronco,listaCamiones,listaCarros):
    for ninfa in listaNinfas:
        ventana.blit(ninfa.image,ninfa.rect)
    for tronco in listaTronco:
        ventana.blit(tronco.image,tronco.rect)
    for camion in listaCamiones:
        ventana.blit(camion.image,camion.rect)
    for carro in listaCarros:
        ventana.blit(carro.image,carro.rect)
    ventana.blit(spriteRana.image,spriteRana.rect)

def vistaDeScore(ventana, fuente, nivel, vidas, timer):
    timer=str(int(timer))
    nivel=str(nivel)
    vidas=str(vidas)
    timerPantalla=fuente.render(timer,0,(NEGRO))
    nivelPantalla=fuente.render(nivel,0,(NEGRO))
    vidasPantalla=fuente.render(vidas,0,(NEGRO))
    ventana.blit(timerPantalla,(ANCHO-90,50))
    ventana.blit(nivelPantalla,(ANCHO-180,50))
    ventana.blit(vidasPantalla,(ANCHO-270,50))
    tiempoTexto = fuente.render("tiempo", 0, (NEGRO))
    nivelTexto = fuente.render("nivel", 0, (NEGRO))
    vidasTexto = fuente.render('vidas', 0, (NEGRO))
    ventana.blit(tiempoTexto, (ANCHO - 90, 25))
    ventana.blit(nivelTexto, (ANCHO - 180, 25))
    ventana.blit(vidasTexto, (ANCHO - 270, 25))

'''def modificarRanking(ventana, nivel, timer, vidas):
    datos=open("ranking.txt","a+",encoding="UTF-8")
    lineas=datos.readlines()
    for numeros in lineas[1]:
        scores=numeros.split()
        nivelR=int(scores[1])
        timerR=int(scores[2])
        vidasR=int(scores[3])
        #if nivel > nivelR:
            #if vidas > vidasR:'''

def pantallaFinal(estado,btnVolver,fuente,ventana):
    if estado=="ganaste":
        ventana.blit(btnVolver.image, btnVolver.rect)
        textoGanaste = fuente.render("Ganaste", 0, (ROJO))
        ventana.blit(textoGanaste, (ANCHO // 2 - 90, ALTO - 500))
    elif estado=="Game over":
        ventana.blit(btnVolver.image, btnVolver.rect)
        textoGameOver = fuente.render("Game over", 0, (NEGRO))
        ventana.blit(textoGameOver, (ANCHO // 2 - 90, ALTO - 500))
    vidas=3
    nivel=1
    tiempo=0
    return vidas,nivel,tiempo

def terminoDeJuego(nivel,vidas,estado):
    if nivel >= 11:
        estado="ganaste"
        #modificarRanking(ventana,nivel,timer,vidas)
    elif vidas == 0:
        estado="Game over"
        #modificarRanking(ventana,nivel,timer,vidas)
    return estado

def generarSuperficies(listaTroncos,imgTronco ,listaNinfas,imgNinfa,listaCamiones,imgCamion,listaCarros,imgCarro):
    for xTronco in range(5):
        for yTronco in range(2):
            cx=xTronco*140
            cy=20+yTronco*70
            nuevoTronco = pygame.sprite.Sprite()
            nuevoTronco.image = imgTronco
            nuevoTronco.rect = imgTronco.get_rect()
            nuevoTronco.rect.left = cx
            nuevoTronco.rect.top = cy
            listaTroncos.append(nuevoTronco)
    for xNinfa in range(6):
        for yNinfa in range(2):
            cxN=ANCHO-xNinfa*100
            cyN=57+yNinfa*65
            nuevoNinfa = pygame.sprite.Sprite()
            nuevoNinfa.image = imgNinfa
            nuevoNinfa.rect = imgTronco.get_rect()
            nuevoNinfa.rect.left = cxN
            nuevoNinfa.rect.top = cyN
            listaNinfas.append(nuevoNinfa)
    for xCamion in range(5):
        for yCamion in range(2):
            cxCa=xCamion*140
            cyCa=ALTO//2+yCamion*90
            nuevoCamion = pygame.sprite.Sprite()
            nuevoCamion.image = imgCamion
            nuevoCamion.rect = imgCamion.get_rect()
            nuevoCamion.rect.left = cxCa
            nuevoCamion.rect.top = cyCa
            listaCamiones.append(nuevoCamion)
    for xCarro in range(6):
        for yCarro in range(3):
            cxCrr=xCarro*140
            cyCrr=ALTO//2+yCarro*90-55
            nuevoCarro = pygame.sprite.Sprite()
            nuevoCarro.image = imgCarro
            nuevoCarro.rect = imgCarro.get_rect()
            nuevoCarro.rect.left = cxCrr
            nuevoCarro.rect.top = cyCrr
            listaCarros.append(nuevoCarro)

def MoverObjetos(listaNinfas, listaTroncos, listaCamiones, ListaCarros, nivel):
    pared=True
    paredN=True
    paredCm=True
    paredCrr=True
    for indiceTroncos in range(len(listaTroncos)):
        if listaTroncos[indiceTroncos].rect.left>=ANCHO-70:
            listaTroncos[indiceTroncos].rect.left=0
            pared=False
        if pared:
            listaTroncos[indiceTroncos].rect.left+=nivel
    for indiceNinfa in range(len(listaNinfas)):
        if listaNinfas[indiceNinfa].rect.left <= 0:
            listaNinfas[indiceNinfa].rect.left = ANCHO
        if paredN:
            listaNinfas[indiceNinfa].rect.left -= nivel * 2
    for indiceCamion in range(len(listaCamiones)):
        if listaCamiones[indiceCamion].rect.left >= ANCHO - 70:
            listaCamiones[indiceCamion].rect.left = 0
            paredCm = False
        if paredCm:
            listaCamiones[indiceCamion].rect.left += nivel
    for indiceCarro in range(len(ListaCarros)):
        if ListaCarros[indiceCarro].rect.left >= ANCHO - 50:
            ListaCarros[indiceCarro].rect.left = 0
            paredCrr = False
        if paredCrr:
            ListaCarros[indiceCarro].rect.left += nivel * 2

def actualizar(listaNinfas, listaTroncos, listaCamiones, listaCarros, spriteRana,vidas,choqueSonido,sobreElAgua):
    for choqueCamion in listaCamiones:
        if spriteRana.rect.colliderect(choqueCamion):
            choqueSonido.play()
            spriteRana.rect.left=ANCHO//2-spriteRana.rect.width//2
            spriteRana.rect.top=ALTO-spriteRana.rect.height
            return vidas-1
    for choqueCarro in listaCarros:
        if spriteRana.rect.colliderect(choqueCarro):
            choqueSonido.play()
            spriteRana.rect.left = ANCHO // 2 - spriteRana.rect.width // 2
            spriteRana.rect.top = ALTO - spriteRana.rect.height
            return vidas - 1
    for sobreTroncos in listaTroncos:
        if spriteRana.rect.colliderect(sobreTroncos):
            sobreElAgua.play()
            spriteRana.rect.left = ANCHO // 2 - spriteRana.rect.width // 2
            spriteRana.rect.top = ALTO - spriteRana.rect.height
            return vidas - 1
    for sobreNinfas in listaNinfas:
        if spriteRana.rect.colliderect(sobreNinfas):
            sobreElAgua.play()
            spriteRana.rect.left = ANCHO // 2 - spriteRana.rect.width // 2
            spriteRana.rect.top = ALTO - spriteRana.rect.height
            return vidas - 1
    return vidas

def dibujarInstrucciones(ventana, fuente1, btnVolver):
    ventana.blit(btnVolver.image,btnVolver.rect)
    texto=fuente1.render('El metodo de moviento del juego son las teclas wasd',0,(NEGRO))
    texto2=fuente1.render('y las flechas arriba,abajo,derecha,izquierda',0,(NEGRO))
    texto3=fuente1.render('objetivo del juego: conseguir llegar al otro lado sin que ningun objeto te golpee',0,NEGRO)
    texto4=fuente1.render('son 10 niveles exito',0,NEGRO)
    ventana.blit(texto,(0,0))
    ventana.blit(texto2, (0, 20))
    ventana.blit(texto3, (0, 40))
    ventana.blit(texto4, (0, 60))

def dibujar():#nombreDeUsuario):
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    # fuentes de texto
    fuente1 = pygame.font.Font(None, 60)
    fuente2 = pygame.font.Font(None, 30)

    #estados:
    estado="menu"  #jugando, ranking, game over
    #fondo
    imgFondoFrogger=pygame.image.load("Fondo Frogger.png")
    #nivel
    nivel=1
    # vidas
    vidas = 3
    #rana
    imgRana=pygame.image.load("rana.png")
    spriteRana=pygame.sprite.Sprite()
    spriteRana.image=imgRana
    spriteRana.rect=imgRana.get_rect()
    spriteRana.rect.left=ANCHO//2-spriteRana.rect.width//2
    spriteRana.rect.top=ALTO-spriteRana.rect.height

    #ninfa
    imgNinfa=pygame.image.load("ninfa.png")

    #tronco
    imgTronco=pygame.image.load("tronco.png")

    #Camion
    imgCamion=pygame.image.load("Camion.png")

    #Carro
    imgCarro = pygame.image.load("Carro.png")

    #canciones de fondo
    pygame.mixer.music.load("[Deemo] M2U - Magnolia .mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.queue('Deemo Sairai Full.mp3')
    pygame.mixer.music.queue('Deemo - Metal Hypnotized .mp3')
    pygame.mixer.music.queue('Deemo - Knight Iris - Forbidden Codex.mp3')

    #sonidos
    choqueSonido=pygame.mixer.Sound("choque.wav")
    sobreElAgua=pygame.mixer.Sound("burbujas.wav")

    #botones
    imgBotonJugar = pygame.image.load("button_jugar.png")
    btnJugar = pygame.sprite.Sprite()  # sprite
    btnJugar.image = imgBotonJugar
    btnJugar.rect = imgBotonJugar.get_rect()
    btnJugar.rect.left = ANCHO // 2 - btnJugar.rect.width // 2
    btnJugar.rect.top = ALTO // 2 - btnJugar.rect.height // 2

    imgBotonRanking = pygame.image.load("button_ranking.png")
    btnRanking = pygame.sprite.Sprite()  # sprite
    btnRanking.image = imgBotonRanking
    btnRanking.rect = imgBotonRanking.get_rect()
    btnRanking.rect.left = ANCHO // 2 - btnRanking.rect.width // 2
    btnRanking.rect.top = ALTO // 2 - btnRanking.rect.height // 2 + 75

    imgBotonInstrucciones=pygame.image.load("button_instrucciones.png")
    btnIns=pygame.sprite.Sprite()
    btnIns.image=imgBotonInstrucciones
    btnIns.rect=imgBotonInstrucciones.get_rect()
    btnIns.rect.left=ANCHO//2-btnIns.rect.width//2
    btnIns.rect.top=ALTO//2-btnIns.rect.height//2+150

    imgBotonVolver = pygame.image.load("button_volver.png")
    btnVolver = pygame.sprite.Sprite()  # sprite
    btnVolver.image = imgBotonVolver
    btnVolver.rect = imgBotonVolver.get_rect()
    btnVolver.rect.left = ANCHO-btnVolver.rect.width
    btnVolver.rect.top = ALTO-btnVolver.rect.height

    #listas
    listaTroncos=[]
    listaNinfas=[]
    listaCamiones=[]
    listaCarros=[]
    generarSuperficies(listaTroncos,imgTronco,listaNinfas,imgNinfa,listaCamiones,imgCamion,listaCarros,imgCarro)

    timer=0
    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb, yb, anchoB, altoB = btnJugar.rect
                xbR, ybR, anchoBR, altoBR = btnRanking.rect
                xbI,ybI,anchoBI,altoBI=btnIns.rect
                xbV, ybV, anchoBV, altoBV = btnVolver.rect
                if estado=="menu":
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb+altoB:
                            estado="jugando"
                    if xm >= xbR and xm <= xbR + anchoBR:
                        if ym >= ybR and ym <= ybR + altoBR:
                            estado = "ranking"
                        if xm >= xbI and xm <= xbI + anchoBI:
                            if ym >= ybI and ym <= ybI + altoBI:
                                estado = "instrucciones"
                #boton volver
                if xm>=xbV and xm<=xbV+anchoBV:
                    if ym>=ybV and ym<=ybV+altoBV:
                         estado="menu"
                #elif estado=="jugando":
            elif evento.type == pygame.KEYDOWN:
                if nivel <=10 and vidas>0:
                    if evento.key==pygame.K_LEFT or evento.key==pygame.K_a:
                        spriteRana.image=pygame.image.load("ranaIzquierda.png")
                        spriteRana.rect.left-=30
                    elif evento.key==pygame.K_RIGHT or evento.key==pygame.K_d:
                        spriteRana.image=pygame.image.load("ranaDerecha.png")
                        spriteRana.rect.left+=30
                    elif evento.key==pygame.K_DOWN or evento.key==pygame.K_s:
                        spriteRana.image = pygame.image.load("ranaAbajo.png")
                        spriteRana.rect.top+=30
                    elif evento.key==pygame.K_UP or evento.key==pygame.K_w:
                        spriteRana.image= pygame.image.load("rana.png")
                        spriteRana.rect.top-=30

        # Borrar pantalla
        ventana.fill(NEGRO)
        ventana.blit(imgFondoFrogger,(0,0))
        # Dibujar, aquí haces todos los trazos que requieras
        if estado =="menu":
            dibujarMenu(ventana,btnJugar,btnRanking,fuente1,btnIns)
        elif estado=="ranking":
            dibujarRanking(ventana,btnVolver,fuente1)
        elif estado=="jugando":
            MoverObjetos(listaNinfas, listaTroncos, listaCamiones, listaCarros, nivel)
            vidas=actualizar(listaNinfas,listaTroncos,listaCamiones,listaCarros,spriteRana,vidas,choqueSonido,sobreElAgua)
            dibujarJuego(ventana,spriteRana,listaNinfas,listaTroncos,listaCamiones,listaCarros)
            vistaDeScore(ventana, fuente2, nivel, vidas, timer)
            timer += 1 / 40
            if spriteRana.rect.top == 0:
                nivel += 1
                spriteRana.rect.left= ANCHO // 2 - spriteRana.rect.width // 2
                spriteRana.rect.top = ALTO - spriteRana.rect.height
            if spriteRana.rect.left<=0:
                spriteRana.rect.left=0
            if spriteRana.rect.left>=ANCHO:
                spriteRana.rect.left=ANCHO-spriteRana.rect.width
            if spriteRana.rect.top>=ALTO:
                spriteRana.rect.top=ALTO-spriteRana.rect.height
        elif estado=="instrucciones":
            dibujarInstrucciones(ventana,fuente2,btnVolver)
        #terminar juego:
        estado=terminoDeJuego(nivel,vidas,estado)
        if estado=="Game over" or estado=="ganaste":
            vidas,nivel,timer=pantallaFinal(estado,btnVolver, fuente1, ventana)
        #vista de score


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps


    pygame.quit()   # termina pygame


def main():
    #nombreDeUsuario = input("Tu nombre de Usuario: ")
    dibujar()#nombreDeUsuario)


main()