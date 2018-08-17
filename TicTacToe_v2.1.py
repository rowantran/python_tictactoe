# -*- coding: utf-8 -*-
"""
Spyder Editor
@author Scott

CURRENT VERSION (2.1):
    Player vs player
    Player vs AI making random moves
    
TODO:
    Check invalid input when entering row/column
    Randomly choose which player goes first
    Smart AI
    Spectate AI vs AI?
"""

import random

gameOver = 0
turn = 1
p1 = 1
p2 = 2
resp = ""
markers = [[" "," "," "],[" "," "," "],[" "," "," "]]

# Prints current board
def printBoard():
    print("    1   2   3")
    print("   -----------")
    for x in range(0, 3):
        print(str(x + 1) + " |", end=" ")
        for y in range(0, 3):
            print(str(markers[x][y]) + " | ", end="")
        print()
        print("   -----------")
    return

# Asks for player's move and changes marker
def move(player):
    row = -1
    col = -1
    
    print()
    print()
    while((row < 1) or (row > 3) or (col < 1) or (col > 3) or (markers[row-1][col-1] != " ")):
        print("Enter move for player \"" + str(player) + "\":")
        print()
        print("Enter row.", end=" ")
        row = int(input())
        print("Enter column.", end=" ")
        col = int(input())
        print()
        print()
    markers[row-1][col-1] = str(player)
    return

# Chooses a random legal move
def randomAIMove():
    open = [0,1,2,3,4,5,6,7,8]
    for x in range(0,3):
        for y in range(0,3):
            if markers[x][y] != " ":
                loc = 3 * x + y
                open.remove(loc)
    item =  random.randint(0,len(open))
    markers[int(open[item] / 3)][int(open[item] % 3)] = "O"
    return

# Checks if a player has won or if there is a tie
def checkEnd():
    printBoard()
    global gameOver
    gameOver = 2
    for x in range(0, 3):
        if markers[x][0] == markers[x][1] == markers[x][2] and markers[x][0] != " ":
            print(str(markers[x][0]) + " has won!")
            gameOver = 1
        elif markers[0][x] == markers[1][x] == markers[2][x] and markers[0][x] != " ":
            print(str(markers[0][x] + " has won!"))
            gameOver = 1
    if markers[0][0] == markers[1][1] == markers[2][2] and markers[0][0] != " ":
        print(str(markers[0][0]) + " has won!")
        gameOver = 1
    elif markers[0][2] == markers[1][1] == markers[2][0] and markers[0][2] != " ":
        print(str(markers[0][2]) + " has won!")
        gameOver = 1
    if gameOver != 1:
        for x in range(0, 3):
            for y in range(0, 3):
                if str(markers[x][y]) == " ":
                    gameOver = 0
    if gameOver == 2:
        print("Tie game.")
    elif gameOver == -1:
        return
    return
    
# Cycles between turns
def nextTurn():
    global turn
    global p1
    global p2
    if turn == 1:
        move("X")
        checkEnd()
        turn = p2
    elif turn == 2:
        move("O")
        checkEnd()
        turn = p1
    elif turn == 0:
        randomAIMove()
        checkEnd()
        turn = p1
    return


printBoard()

while resp != "ai" and resp != "pvp":
    print("Would you like to play against \"ai\" or play \"pvp\"?")
    resp = input()

if resp == "ai":
    p1 = 1
    p2 = 0
    
elif resp == "pvp":
    p1 = 1
    p2 = 2

while gameOver == 0:
    nextTurn()