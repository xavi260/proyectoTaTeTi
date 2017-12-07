from random import randomint 

def humanPlay(board, humanMovements):
	while True:
		position = int(input("Ingrese Posicion: ")
	
		print(board[position])
		if board[position] == "-":
			board[position] = "X"
			humanMovements.append(position)
			break


def computerPlay(board, computerMovements):
	while True:
		position = randint(0, 8)
		
		if board[position] == "-":
			board[position] = "O"
			computerMovements.append(position)
			break

def isVictory(board, movements):
	victoryCondition = []
	victoryCondition.append([0, 1, 2])
	victoryCondition.append([3, 4, 5])
	victoryCondition.append([6, 7, 8])
	victoryCondition.append([0, 3, 6])
	victoryCondition.append([1, 4, 7])
	victoryCondition.append([2, 5, 8])
	victoryCondition.append([6, 4, 2])
	victoryCondition.append([8, 4, 0])
	
	for condition in victoryCondition:
		if all(i in movements for i in condition):
			return true
