#!/usr/bin/env python3

from board import *
from playGame import *

board = createBoard()
humanMovements = []
computerMovements = []
turnCount = 0

while True:
	message = "Ingrese Posicion:"
	printBoard(board, message)
	
	humanPlay(board, humanMovements)
	if isVictory(humanMovements):
		print("Ganaste")
		break
	
	computerPlay(board, computerMovements)
	if isVictory(humanMovements):
		print("Ganaste")
		break
	
	turnCount += 1
	if turncount == 9:
		print("Empate")
		break
