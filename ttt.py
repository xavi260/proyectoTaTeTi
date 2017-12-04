#!/usr/bin/env python3



import random #para generar numeros aleatoreos
import os # para borrar pantalla


# variables
movPc=random.randint(0,8)
winner=0

board=[" "," "," ",
	   " "," "," ",
	   " "," "," " ]

boardins=["7","8","9",
	   "4","5","6",
	   "1","2","3" ]

ins="Debes introducir los movimientos indicando un numero del 1 al 9 de este modo"

# funcion para imprimir tablero
def printBoard():
	print(" ______")
	print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
	print(" ------")
	print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
	print( " ------")
	print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
	print( " ------")
	print

# Funcion para comprobar ganador
def checkWinner():
	#human
	if board[0]=="x":
		if board[1]=="x" and board[2]=="x":
			return 1
		if board[3]=="x" and board[6]=="x":
			return 1
		if board[4]=="x" and board[8]=="x":
			return 1
	elif board[4]=="x":
		if board[3]=="x" and board[5]=="x":
			return 1
		if board[1]=="x" and board[7]=="x":
			return 1
		if board[2]=="x" and board[6]=="x":
			return 1
	elif board[8]=="x":
		if board[2]=="x" and board[5]=="x":
			return 1
		if board[7]=="x" and board[6]=="x":
			return 1
	#pc
	elif board[0]=="o":
		if board[1]=="o" and board[2]=="o":
			return 2
		if board[3]=="o" and board[6]=="o":
			return 2
		if board[4]=="o" and board[8]=="o":
			return 2
	elif board[4]=="o":
		if board[3]=="o" and board[5]=="o":
			return 2
		if board[1]=="o" and board[7]=="o":
			return 2
		if board[2]=="o" and board[6]=="o":
			return 2
	elif board[8]=="o":
		if board[2]=="o" and board[5]=="o":
			return 2
		if board[7]=="o" and board[6]=="o":
			return 2
	else:
	# Fin de comprobacion. Si no hay ganador mantiene en 0 la variable winner.
		return 0

def result(winner):
	if winner==1:
		print("Ganaste!!")
	elif winner==2:
		print("Perdiste!!")
	else:
		print("Empate!! Vuelve a intentar")


# Imprime instrucciones
print(ins)
print(" ______")
print("|" + boardins[0] + "|" + boardins[1] + "|" + boardins[2] + "|")
print(" ______")
print("|" + boardins[3] + "|" + boardins[4] + "|" + boardins[5] + "|")
print(" ______")
print("|" + boardins[6] + "|" + boardins[7] + "|" + boardins[8] + "|")
print(" ______")

# Bucle; movimientos (5) humano empieza, (4) pc
for turn in range(1,6):
	# movimiento humano y comprobacion
	movhuman=int(input("Inserta movimiento (1-9) "))
	movhuman-=1
	while movhuman>8 or movhuman<0 or board[movhuman]=="x" or board[movhuman]=="o":
		movhuman=int(input("Inserta movimiento valido (1-9)"))
		movhuman-=1
	board[movhuman]="x"

	# Impresion del turno humano
	os.system("clear")
	print("Humano:")
	printBoard()

#	# Comprueba si alguno de los dos ha ganado
	winner=checkWinner()
	if winner > 0 and winner < 3:
		break

	# pc 4 turnos (el ultimo no lo juega por falta de espacio en el tablero.
	if turn < 5:
		# movimiento pc genea el numero aleatorio con la resta aplicada, 
		# el while evita q la pc ponga ficha encima de las existentes
		movPc=random.randint(0,8)
		while board[movPc]=="x" or board[movPc]=="o":
			movPc=random.randint(0,8)
		board[movPc]="o"

		# Impresion turno maquina
		os.system("clear")
		print("Maquina:")
		printBoard()
		
#		# Comprueba si alguno de los dos ha ganado
		winner=checkWinner()
		if winner > 0 and winner < 3:
			break

resut(winner)

