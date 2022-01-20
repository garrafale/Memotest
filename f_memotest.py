from os import system
import platform

def borra():
    so = platform.system()
    if so == "Linux": system("clear")
    else: system("cls")

def continua():
    input("Presiona <ENTER> para continuar. ")
    borra()

def s(): # salto de linea
    print()


def instrucciones(memotest):
    print(memotest.center(105))
    s()
    print("Bienvenido al "+"\033[1;31m"+"MEMOTEST"+'\033[0;m'+". ¿Preparado para poner a prueba tu memoria?")
    s()
    print("\033[1;36m"+"Instrucciones:"+'\033[0;m')
    print("1. Primero, te aparecerá el tablero completo con sus 16 cartas (8 pares) visibles.\n" + 
            "   Deberás memorizar el orden de las cartas, rápidamente, ya que solo tenés 3 segundos\n" +
            "   para hacerlo.")
    print("2. Luego, escribí la primera coordenada, y te aparecerá el animal de esa carta.\n" +
            "   Inmediatamente, harás lo mismo con la segunda, mostrando los animales de ambas\n" +
            "   cartas, durante 3 segundos.")
    print("3. Cada vez que coincidan, te llevás esas cartas")
    print("4. El juego termina cuando te hayas llevado esos 8 pares de cartas con sus respectivos animales.")
    print("5. Hecho eso, te aparecerá en pantalla, tu cantidad de intentos totales y tu cantidad de\n" +
            "   intentos fallidos.")
    print("6. Según tu rendimiento, accederás a distintos niveles. Presioná enter para ver sus requisitos\n")
    
    continua()

def niveles(memotest):
    print(memotest.center(105))
    s()
    print("NIVEL ACCEDIDO SEGÚN CANTIDAD DE INTENTOS FALLIDOS: \n")
    print("\033[1;32m"+"0 intentos fallidos → NIVEL MEGA CRACK"+'\033[0;m')
    print("\033[1;36m"+"1-3 intentos fallidos → NIVEL MÁSTER"+'\033[0;m')
    print("\033[1;33m"+"4-7 intentos fallidos → NIVEL PROFESIONAL"+'\033[0;m')
    print("\033[1;35m"+"8-11 intentos fallidos → NIVEL AMATEUR"+'\033[0;m')
    print("\033[1;31m"+"12+ intentos fallidos → NIVEL PRINCIPIANTE"+'\033[0;m')
    print("\n¡¡Que comience el juego!! Mucha suerte.\n")
    input("Presioná <ENTER> para iniciar el "+"\033[1;31m"+"MEMOTEST"+'\033[0;m'+". ")
    borra()

def calcular_nivel(intentos_fallidos):
    print(input("Presiona enter para conocer tu nivel, según tu rendimiento. "))

    if intentos_fallidos==0:
        print("\033[1;32m"+"¡¡Pero qué buena memoria tenés!! No tuviste ningún intento fallido. NIVEL MEGA CRACK"+'\033[0;m')
    if 1<=intentos_fallidos<=3:
        print("\033[1;36m"+"Casi acertás todas sin fallar. ¡Seguí así!. NIVEL MÁSTER"+'\033[0;m')
    if 4<=intentos_fallidos<=7:
        print("\033[1;33m"+"Debés mejorar un poco, pero vas por buen camino. NIVEL PROFESIONAL"+'\033[0;m')
    if 8<=intentos_fallidos<=11:
        print("\033[1;35m"+"Parece que andamos olvidadizos. ¡¡¡A practicar!!!. NIVEL AMATEUR"+'\033[0;m')
    if intentos_fallidos>11:
        print("\033[1;31m"+"Pareciera que es la primera vez que jugás. NIVEL PRINCIPIANTE"+'\033[0;m')
