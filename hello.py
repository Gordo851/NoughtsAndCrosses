# -*- coding: utf-8 -*-

board = ["  1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]

# print board
def drawBoard(board):
	print(board[0], "|", board[1], "|", board[2], "\n",
	   "-----------------\n",
	   board[3], "|", board[4], "|", board[5], "\n",
	   "-----------------\n",
	   board[6], "|", board[7], "|", board[8], "\n")

drawBoard(board)

# user input

def askPlayerMove():
	playerMove = input("Enter the number of the square you would like to play in: ")
	return playerMove


def updateGameBoard(playerMove, player):
	move = int(playerMove) - 1
	# Then update the cell to be the player's token
	if move == 0:
		playerString = " " + player
		board[move] = playerString
	else:
		board[move] = player
	
	drawBoard(board)

move = askPlayerMove()
player = "X"
updateGameBoard(move,player)
# update board





# check win



# while loop 


