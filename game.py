# -*- coding: utf-8 -*-

board = ["  1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


def checkWinner(winner, player):
	zeroString = " " + player
	winner = False	
	if board[0] == zeroString and board[1] == player and board[2] == player:
		winner = True
	elif board[3] == player and board[4] == player and board[5] == player:
		winner = True
	elif board[6] == player and board[7] == player and board[8] == player:
		winner = True
	elif board[0] == zeroString and board[3] == player and board[6] == player:
		winner = True
	elif board[1] == player and board[4] == player and board[7] == player:
		winner = True
	elif board[2] == player and board[5] == player and board[8] == player:
		winner = True
	elif board[0] == zeroString and board[4] == player and board[8] == player:
		winner = True
	elif board[2] == player and board[4] == player and board[6] == player:
		winner = True
	return winner


def askPlayerMove():
	playerMove = input("Enter the number of the square you would like to play in: ")
	return playerMove


def updateGameBoard(playerMove, player):
	# check first that the square does not already have a player move in it
	askAgain = False
	move = int(playerMove) - 1
	if board[move] == " X " or board[move] == " O " or board[move] == "  X ":
		print("Sorry that move has been taken you'll have to select another square.")
		askAgain = True
	
	# Then update the cell to be the player's token
	if askAgain == False:
		if move == 0:
			playerString = " " + player
			board[move] = playerString
		else:
			board[move] = player
	
	drawBoard()
	return askAgain


def drawBoard():
	print(board[0], "|", board[1], "|", board[2], "\n",
	   "-----------------\n",
	   board[3], "|", board[4], "|", board[5], "\n",
	   "-----------------\n",
	   board[6], "|", board[7], "|", board[8], "\n")
	

def runGame():
	player = " X "
	winner = False
	while winner == False:
		# ask for player move
		print("You are player", player)
		playerMove = askPlayerMove()
		# update game board
		askAgain = updateGameBoard(playerMove, player)
		if askAgain:
			continue
		# check for winner
		winner = checkWinner(winner, player)
		if winner == True:
			continue
		# change to other player
		if player == " X ":
			player = " O "
		else:
			player = " X "
	print("Well done!",player,"WINS!")

runGame()