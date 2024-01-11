######################### ANOTACIONES DE UN JUGADOR ###################################################
#Se pide crear un programa que facilite las estadísticas de anotaciones de un jugador. Para ello,     #
# el programa solicitará los datos siguientes:                                                        # 
#- Ingresar las puntuaciones de cada canasta: 3, 2 ó 1 (VALOR 0 PARA SALIR)                           #
#- Si el usuario ingresa un número que no sea 3, 2 ó 1, el programa mostrará un mensaje de error.     #
#- El programa deberá mostrar: nombre del jugador, los puntos totales obtenidos en el partido,        #
# las canastas encestadas y los tiros de 3, de 2 y de 1 punto respectivamente                         #
#######################################################################################################

##################################### PRESENTACIÓN INICIAL   ##########################################
print("********************************************")
print("         ESTADÍSTICAS DEL JUGADOR   ")
print("********************************************")
nombre_jugador=input("Introduzca el nombre del jugador: ")  # Opción para salto linea \n

########################    LISTA DE CANASTAS Y SELECCIÓN DE VALORES  #################################

anotaciones=[]  #lista "anotaciones"
puntos=int(input("Introduza las anotaciones del jugador (0 para terminar): "))

while puntos>=1:   #Bucle creación de lista. Valores válidos (1,2,3). Si puntos=0 salimos del bucle 

        if puntos>3:      # Si valor puntos>3 es un error del valor de entrada
            print("La puntuación no es correcta")
        else:
            anotaciones.append(puntos)  # elemento correcto de la lista "anotaciones"
        puntos=int(input("Introduza las anotaciones del jugador (0 para terminar): "))     

########################   CÓMPUTO DE VALORES DE LA LISTA   ###########################################

i,libres,canastas,triples,total=0,0,0,0,0  #Inicializamos las variables a utilizar en una sola linea
for i in range (len(anotaciones)):
    if anotaciones[i]==1:
        libres+=1
    if anotaciones[i]==2:
        canastas+=1
    if anotaciones[i]==3:
        triples+=1

total=libres+(canastas*2)+(triples*3)

########################## PRESENTACIÓN DE ESTADÍSTICAS DEL JUGADOR   #################################
print()  #salto de linea
print("ESTADÍSTICA DEL JUGADOR: ", nombre_jugador)
print()
print("El jugador", nombre_jugador, "ha anotado ",len(anotaciones), "canastas")
print("Las anotaciones han sido: ", anotaciones)
print("LIBRES (1 punto):-------- ", libres)
print("CANASTAS (2 puntos):----- ", canastas)
print("TRIPLES (3 puntos):------ ", triples)
print("TOTAL:------------------- ",total)
