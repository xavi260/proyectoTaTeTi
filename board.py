from os import system

def printBoard(board):
	system("clear")
	
	print(" ______")
	print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
	print(" ------")
	print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
	print( " ------")
	print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
	print( " ------")
	print()

def createBoard():
    return ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
