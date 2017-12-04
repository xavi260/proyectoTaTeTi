#!/usr/bin/env python3

import random #para generar numeros aleatoreos
import os # para borrar pantalla
from board import *
from checkWinner import *

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

checkWinner(text) 


def result(winner):
	if winner==1:
		print("Ganaste!!")
	elif winner==2:
		print("Perdiste!!")
	else:
		print("Empate!! Vuelve a intentar")


printBoard(boardins, ins)

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
	printBoard(board)

#	# Comprueba si alguno de los dos ha ganado
#	winner=checkWinner()
#	if winner > 0 and winner < 3:
#		break

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
		printBoard(board)
		
#		# Comprueba si alguno de los dos ha ganado
#	winner=checkWinner()
#	if winner > 0 and winner < 3:
#		break

resut(winner)

