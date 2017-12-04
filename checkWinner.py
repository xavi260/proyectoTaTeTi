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
