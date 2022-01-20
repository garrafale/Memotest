from funciones import borra, s, instrucciones, continua, niveles, calcular_nivel
import time
import random

borra()

continua()

borra()

"""
Se inicializa esta variable para que el "título del juego" (memotest) 
tenga la posibilidad de centrarse, ya que siempre se mostrará en pantalla 
(excepto en la pantalla donde se muestra el nombre de los autores)
"""
memotest=("\033[1;37;41m"+"MEMOTEST"+'\033[0;m') 

# Imprime las instrucciones del juego
instrucciones(memotest)

niveles(memotest)
print(memotest.center(105))
print()
#lista con las coordenadas
coord_orig=["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"] 
coord_acert=[]
cartas=["Perro".ljust(15), "Gato".ljust(15), "Delfín".ljust(15), "Cocodrilo".ljust(15), "Jirafa".ljust(15), "Elefante".ljust(15), "Pez".ljust(15), "Hormiga".ljust(15), "Perro".ljust(15), "Gato".ljust(15), "Delfín".ljust(15), "Cocodrilo".ljust(15), "Jirafa".ljust(15), "Elefante".ljust(15), "Pez".ljust(15), "Hormiga".ljust(15)] #lista con el nombre de cada carta (cada animal se repite para buscar el par).

# ramdon.seed para hacer testing. 
# random.seed(1)

random.shuffle(cartas)
# se inicializa esta lista para poder agregar en ella el animal contenido en 
# cada par de cartas (y luego, mostrarlas en pantalla)
animal_acert=[] 

signo=["?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15),"?".ljust(15)] #se inicializa esta lista con símbolos "?" para poder representarlos en el tablero

# cuenta las cantidad de cartas (NO de pares de cartas) acertadas
cant_cartas=0
# cuenta la cantidad de intentos totales realizados 
intentos=0 
# cuenta la cantidad de intentos fallidos
intentos_fallidos=0 

# nombre de cada columna del tablero (A,B,C,D)
fila0="\t"+"\t"+"\033[1;33m"+"A".ljust(15)+'\033[0;m'+"\t"+"\t"+"\033[1;33m"+"B".ljust(15)+'\033[0;m'+"\t"+"\t"+"\033[1;33m"+"C".ljust(15)+'\033[0;m'+"\t"+"\t"+"\033[1;33m"+"D".ljust(15)+'\033[0;m'+"\n" 
# filas 1 al 4, del tablero con las cartas visibles
fila1="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+cartas[0]+"\t"+"\t"+cartas[4]+"\t"+"\t"+cartas[8]+"\t"+"\t"+cartas[12]+"\n" 
fila2="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+cartas[1]+"\t"+"\t"+cartas[5]+"\t"+"\t"+cartas[9]+"\t"+"\t"+cartas[13]+"\n" 
fila3="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+cartas[2]+"\t"+"\t"+cartas[6]+"\t"+"\t"+cartas[10]+"\t"+"\t"+cartas[14]+"\n" 
fila4="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+cartas[3]+"\t"+"\t"+cartas[7]+"\t"+"\t"+cartas[11]+"\t"+"\t"+cartas[15]+"\n" 
# junta los nombres de las columnas del tablero con sus 4 filas (cartas visibles)
tablero=(fila0+fila1+fila2+fila3+fila4) 
print(tablero)

# se toma un tiempo de espera para después borrar la pantalla. La idea es haber 
# memorizado, en esos segundos, las cartas en su posición
time.sleep(5) 
borra()

print(memotest.center(105))
print()

fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n" #fila 1 del tablero con las cartas ocultas
fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n" #fila 2 del tablero con las cartas ocultas
fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"#fila 3 del tablero con las cartas ocultas
fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"#fila 4 del tablero con las cartas ocultas

# junta los nombres de las columnas del tablero (la variable es "fila0") con sus 4 filas (cartas ocultas)
tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto) 
print(tablero_oculto)
# mientras no se hayan acertado las 16 cartas, el while se seguirá ejecutando
while cant_cartas < 16: 
    # se inicializa esta variable de esta manera, para que pudiera entrar al próximo while
	coord_1="coord_1" 
	coord_2="coord_2" 

	print()
    # si la coordenada colocada nunca existió, o ya fue acertada, no se saldrá 
    # de este while hasta haberla colocado bien
	while (coord_1.upper() not in coord_orig) or (coord_1.upper() in coord_acert): 
		coord_1=input("\033[1;33m"+"Elegí la primera carta (A1-D4): "+'\033[0;m')
		if coord_1.upper() not in coord_orig:
            # se mostrará este mensaje si la coordenada nunca existió.
			print("\033[1;31m"+"Coordenada no válida. Volvé a escribir la coordenada de la carta.\n"+'\033[0;m') 
		if coord_1.upper() in coord_acert:
            # se mostrará este mensaje si la coordenada de la carta ya fue acertada
			print("\033[1;31m"+"Coordenada de una carta ya acertada. Volvé a escribir la coordenada de la carta.\n"+'\033[0;m') 
	print()
    # en esta variable se alojará la posición de la primera coordenada elegida, 
    # dentro de la lista de coordenadas originales (coord_orig)
	pos_coord_1=coord_orig.index(coord_1.upper()) 
    # reemplaza el signo oculto de esa coordenada, por el nombre de los dos animales 
    # de las dos cartas (coincidan o no), para ver en qué parte del tablero se encuentran		
	signo[pos_coord_1]=signo[pos_coord_1].replace(signo[pos_coord_1],cartas[pos_coord_1]) 
	fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
	fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
	fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
	fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"
    # tablero con las cartas ocultas (solamente muestra el nombre de los 2 animales sacados recientemente)
	tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto) 
	borra()
	print(memotest.center(105))
	print()
	print(tablero_oculto)
    # a partir del segundo intento, muestra el historial parcial
	if intentos>0: 
        # si no se acertaron cartas aún
		if cant_cartas==0: 
            #no se recolectó ningún par de cartas hasta el momento
			print("\033[1;31m"+"\nSin cartas agarradas hasta el momento"+'\033[0;m') 
			print("\033[1;31m"+"\nPares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)	
		if cant_cartas>=2 and cant_cartas<=14:
			print("\033[1;31m"+"Pares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
            # si cant_cartas = 0, no habrá cartas recolectadas (no hace falta poner 
            # esta leyenda), y si es = 16, habrá terminado el juego (por ende, no tiene 
            # sentido mostrar este renglón)		
			print("\n¡¡¡Los animales que ves en pantalla son los que ya acertaste!!!") 
	print()
	while (coord_2.upper() not in coord_orig) or (coord_1.upper() == coord_2.upper()) or (coord_2.upper() in coord_acert): #si la coordenada colocada nunca existió, ya fue acertada, o bien, es igual a la que fue escrita primera, no se podrá salir de este while
		coord_2=input("\033[1;35m"+"Elegí la segunda carta (A1-D4): "+'\033[0;m')
		if coord_2.upper() not in coord_orig:
            # se mostrará este mensaje si la coordenada nunca existió
			print("\033[1;31m"+"Coordenada no válida. Volvé a escribir la coordenada de la carta.\n\n"+'\033[0;m') 
		if coord_1.upper()==coord_2.upper():
            # se mostrará este mensaje si la segunda coordenada escrita, coincide con la primera
			print("\033[1;31m"+"Ambas coordenadas no pueden ser iguales. Volvé a escribir la coordenada de la carta.\n\n"+'\033[0;m') 
		if coord_2.upper() in coord_acert:
            # se mostrará este mensaje si la coordenada de la carta ya fue acertada
			print("\033[1;31m"+"Coordenada de una carta ya acertada. Volvé a escribir la coordenada de la carta.\n\n"+'\033[0;m') 
	s()
	pos_coord_2=coord_orig.index(coord_2.upper()) #en esta variable se alojará la posición de la segunda coordenada elegida, dentro de la lista de coordenadas originales (coord_orig)
	signo[pos_coord_2]=signo[pos_coord_2].replace(signo[pos_coord_2],cartas[pos_coord_2]) #reemplaza el signo oculto de esa coordenada, por el nombre de los dos animales de las dos cartas (coincidan o no), para ver en qué parte del tablero se encuentran		
	fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
	fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
	fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
	fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"

    # tablero con las cartas ocultas (solamente muestra el nombre de 
    # los 2 animales sacados recientemente)
	tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto) 
	print(tablero_oculto)
	s()
    # se borra la pantalla para proceder a mostrar las 2 cartas elegidas, 
    # para observar si coinciden o no
	borra() 
	print(memotest.center(105))
	s()
	print("\033[1;32m"+"Coordenadas elegidas:",coord_1.upper(),"y",coord_2.upper()+'\033[0;m') #muestra las coordenadas elegidas
    # suma 1 intento para luego mostrarlo
	intentos+=1 

	s()	
    # si ambas cartas contienen al mismo animal
	if cartas[pos_coord_1]==cartas[pos_coord_2]: 
		fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
		fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
		fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
		fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"
        # tablero con las cartas ocultas (solamente muestra el nombre de los 2 animales sacados recientemente)
		tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto) 
        # se agrega el nombre del animal de las cartas acertadas para dejarlos fijos en pantalla 
        # (NOTA: cada vez que se acierta la coincidencia, se agrega una sola vez porque es el mismo animal)
		animal_acert.append(cartas[pos_coord_1]) 
        #se agregan las coordenadas ya acertadas a esta lista (vacía en un primer momento), para que 
        # cuando escribamos una coordena ya acertada nos salga la leyenda "coordena ya acertada"
		coord_acert.append(coord_orig[pos_coord_1]) 
        # se agregan las coordenadas ya acertadas a esta lista (vacía en un primer momento), para que 
        # cuando escribamos una coordena ya acertada nos salga la leyenda "coordena ya acertada"
		coord_acert.append(coord_orig[pos_coord_2]) 

		print(tablero_oculto)
		print()
		print("\033[1;32m"+"¡Acertaste! Los animales coinciden"+'\033[0;m')
		print()
        # refleja la cantidad de pares de cartas acertados hasta ese momento
		print("\033[1;32m"+"Pares acertados:"+'\033[0;m',len(animal_acert)) 
        # suma la cantidad de cartas acertadas
		cant_cartas +=2 
        # indica los PARES de cartas que faltan recolectar
		pares_restantes=int(((16-cant_cartas)/2)) 

		time.sleep(3)
        #se borra la pantalla, después de unos segundos, para escribir las nuevas coordenadas. 
        # La idea es haber memorizado, en esos segundos, la posición de las dos cartas recientemente 
        # elegidas (hayan coincidido o no)
		borra() 
		print(memotest.center(105))
		print()
        # si no se acertaron cartas aún
		if cant_cartas==0: 
			fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
			fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
			fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
			fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"
			tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto)
			print(tablero_oculto)
			print()
            # no se recolectó ningún par de cartas hasta el momento
			print("\033[1;31m"+"Sin cartas agarradas hasta el momento"+'\033[0;m') 
			print()
			print("\033[1;31m"+"Pares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
		if cant_cartas>=2 and cant_cartas<=14:
			fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
			fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
			fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
			fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"
			tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto)
			print(tablero_oculto)
			print()			
			print("\033[1;31m"+"Pares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
			print()
            # si cant_cartas = 0, no habrá cartas recolectadas (no hace falta poner esta leyenda), 
            # y si es = 16, habrá terminado el juego (por ende, no tiene sentido mostrar este renglón)		
			print("¡¡¡Los animales que ves en pantalla son los que ya acertaste!!!") 
		if cant_cartas==16:
            # si ya se acertaron todas, muestra el tablero original		
			print(tablero) 
			print("\033[1;32m"+"Felicidades. Agarraste todos los pares de cartas. Lo hiciste en"+'\033[0;m',intentos,"\033[1;32m"+"intentos totales"+'\033[0;m')
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
    # si ambas cartas NO contienen al mismo animal
	if cartas[pos_coord_1]!=cartas[pos_coord_2]: 
		intentos_fallidos+=1
		fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
		fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
		fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
		fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"
        # tablero con las cartas ocultas (solamente muestra el nombre de 
        # los 2 animales sacados recientemente)
		tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto) 
		print(tablero_oculto)
		print()
		print("\033[1;31m"+"Fallaste. Los animales no coinciden"+'\033[0;m')
		print()
		print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
			
		time.sleep(5)
        # se borra la pantalla, después de unos segundos, para escribir las nuevas coordenadas. 
        # La idea es haber memorizado, en esos segundos, la posición de las dos cartas 
        # recientemente elegidas (hayan coincidido o no)
		borra() 
		print(memotest.center(105))
		print()
        # se revierte el reemplazo hecho anteriormente (originalmente tenía el símbolo 
        # de pregunta, y pasó a tener el nombre del animal, y ahora nuevamente tendrá 
        # el signo de interrogación). Se hace para poder volver a mostrar la carta oculta 
        # ("?"), a partir de la próxima elección de cartas.
		signo[pos_coord_1]=signo[pos_coord_1].replace(cartas[pos_coord_1],"?".ljust(15)) 
		signo[pos_coord_2]=signo[pos_coord_2].replace(cartas[pos_coord_2],"?".ljust(15)) 

		fila1_oculto="\033[1;33m"+"1"+'\033[0;m'+"\t"+"\t"+signo[0]+"\t"+"\t"+signo[4]+"\t"+"\t"+signo[8]+"\t"+"\t"+signo[12]+"\n"
		fila2_oculto="\033[1;33m"+"2"+'\033[0;m'+"\t"+"\t"+signo[1]+"\t"+"\t"+signo[5]+"\t"+"\t"+signo[9]+"\t"+"\t"+signo[13]+"\n"
		fila3_oculto="\033[1;33m"+"3"+'\033[0;m'+"\t"+"\t"+signo[2]+"\t"+"\t"+signo[6]+"\t"+"\t"+signo[10]+"\t"+"\t"+signo[14]+"\n"
		fila4_oculto="\033[1;33m"+"4"+'\033[0;m'+"\t"+"\t"+signo[3]+"\t"+"\t"+signo[7]+"\t"+"\t"+signo[11]+"\t"+"\t"+signo[15]+"\n"

		tablero_oculto=(fila0+fila1_oculto+fila2_oculto+fila3_oculto+fila4_oculto)
		print(tablero_oculto)
		print()
        # indica los PARES de cartas que faltan recolectar
		pares_restantes=int(((16-cant_cartas)/2))
        # si no se acertaron cartas aún
		if cant_cartas==0: 
            # no se recolectó ningún par de cartas hasta el momento
			print("\033[1;31m"+"Sin cartas agarradas hasta el momento"+'\033[0;m')
			print()
			print("\033[1;31m"+"Pares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)	
		if cant_cartas>=2 and cant_cartas<=14:
			print("\033[1;31m"+"Pares de cartas sin agarrar:"+'\033[0;m',pares_restantes)
			print("\033[1;31m"+"Intentos fallidos:"+'\033[0;m',intentos_fallidos)
			print()
            # si cant_cartas = 0, no habrá cartas recolectadas (no hace falta poner esta leyenda), 
            # y si es = 16, habrá terminado el juego (por ende, no tiene sentido mostrar este renglón)
			print("¡¡¡Los animales que ves en pantalla son los que ya acertaste!!!") 
print()

calcular_nivel(intentos_fallidos)

s()
s()
