#Anaid Fernanda Labat González 01746289
mport random

IMÁGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |
 ---------''', ''' 
   +---+
   |   |
   O   |
       |
       |
       |
 ---------''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 ---------''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 ---------''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 ---------''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 ---------''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 ---------''']
archivo = open("palabras.txt", "r", encoding='UTF-8')
for linea in archivo.readlines():
    palabras = linea.split(' ')

def obtenerPalabraAlAzar(listaDePalabras):
    índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[índiceDePalabras]


def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()


def obtenerIntento(letrasProbadas):
    while True:
        print('Ingresa una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:\
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':\
            print('Por favor ingresa una LETRA.')
        else:
            return intento


def jugarDeNuevo():
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while juegoTerminado==False:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
                print('¡Felicidades! ¡La palabra secreta es ', palabraSecreta)
                juegoTerminado = True

    else:
            print("Esta letra no se encuentra en la palabra.")
            letrasIncorrectas +=intento
            if len(letrasIncorrectas)==7:
                print("Te has quedado sin intentos, la palabra corrrecta era:", palabraSecreta)
                juegoTerminado=True
