#!/usr/bin/env python3

from board import *
from playGame import *

board = createBoard()
humanMovements = []
computerMovements = []
turnCount = 0

while True:
	printBoard(board)
	
	humanPlay(board, humanMovements)
	if isVictory(humanMovements):
		printBoard(board)
		print("Ganaste")
		break
	
	computerPlay(board, computerMovements)
	if isVictory(computerMovements):
		printBoard(board)
		print("Ganaste")
		break
	
	turnCount += 1
	if turnCount == 9:
		printBoard(board)
		print("Empate")
		break
