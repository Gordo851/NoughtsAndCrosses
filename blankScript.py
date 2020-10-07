# -*- coding: utf-8 -*-

board = [1,2,3,4,5,6,7,8,9]

"""
def board_xo (rows):
    for number in range(0, rows):
        print("- | - | - \n")
    print()
    

board_xo(3)
"""


def board_xo (rows):
    for number in range(0, rows):
        print(str(board[number*rows]) + 
			  "|" + str(board[number*rows+1]) +  
			  "|" + str(board[number*rows+2]) + "\n")
    print()
    

board_xo(3)

def askUser():
	move = input("where would you like to play? ")
	return move

thisMove = askUser()

"""
move = int(thisMove) - 1
board[move] = "X"
board_xo(3)
"""

for point in board:
	if point == int(thisMove):
		board[point-1] = "X"





board_xo(3)