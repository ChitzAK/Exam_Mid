from Human import *
from BOT import *

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


if __name__ == "__main__":

    print("Possible players HUMAN BOT")
    player1 = input("---Player 1 =")
    player2 = input("---Player 2 =")

    turn = 'X'
    count = 0
    currentPlayer = 1
    printBoard(theBoard)
    print("Player:",currentPlayer,"With:",turn,"Poz:")

    for i in range(9):
        if (currentPlayer == 1) and (player1 == "HUMAN"):
            human(theBoard)
        if (currentPlayer == 2) and (player2 == "HUMAN"):
            human(theBoard)

        if (currentPlayer == 1) and (player1 == "BOT"):
            robot(theBoard)
        if (currentPlayer == 2) and (player2 == "BOT"):
            robot(theBoard)

        count += 1

        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " +turn + " won. ****")
            break
        else:
            if count < 9:
                if turn == 'X':
                    turn = 'O'
                    currentPlayer = 2
                else:
                    turn = 'X'
                    currentPlayer = 1

                printBoard(theBoard)
                print("Player:", currentPlayer, "With:", turn, "Poz:")
            else:
                printBoard(theBoard)
                print("Drow")