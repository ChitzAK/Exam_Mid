# human
def human(theBoard):

        move = input()
        count1 = 0
        count2 = 0

        for key in theBoard:
            if theBoard[key] == 'X':
                count1 += 1

            if theBoard[key] == 'O':
                count2 += 1

        if count1 == count2:
            turn = 'X'
        else:
            turn = 'O'

        theBoard[move] = turn



