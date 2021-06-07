#BOT

def robot(theBoard):

        count1 = 0
        count2 = 0
        check = 0

        for key in theBoard:
            if theBoard[key] == 'X':
                count1 += 1

            if theBoard[key] == 'O':
                count2 += 1

        count_tot = count1 + count2

        if count1 == count2:
            turn = 'X'
        else:
            turn = 'O'

        win = 0
        defend = 0

        for i in range(1,9):
            if i == 1:
                a = '1'
                b = '2'
                c = '3'
            if i == 2:
                a = '4'
                b = '5'
                c = '6'
            if i == 3:
                a = '7'
                b = '8'
                c = '9'
            if i == 4:
                a = '1'
                b = '4'
                c = '7'
            if i == 5:
                a = '2'
                b = '5'
                c = '8'
            if i == 6:
                a = '3'
                b = '6'
                c = '9'
            if i == 7:
                a = '1'
                b = '5'
                c = '9'
            if i == 8:
                a = '3'
                b = '5'
                c = '7'

            if theBoard[a] == theBoard[b] == turn == 'X':
                if theBoard[c] == ' ':
                    theBoard[c] = 'X'
                    win = 1
                    break
            if theBoard[a] == theBoard[c] == turn == 'X':
                if theBoard[b] == ' ':
                    theBoard[b] = 'X'
                    win = 1
                    break
            if theBoard[b] == theBoard[c] == turn == 'X':
                if theBoard[a] == ' ':
                    theBoard[a] = 'X'
                    win = 1
                    break
            if theBoard[a] == theBoard[b] == turn == 'O':
                if theBoard[c] == ' ':
                    theBoard[c] = 'O'
                    win = 1
                    break
            if theBoard[a] == theBoard[c] == turn == 'O':
                if theBoard[b] == ' ':
                    theBoard[b] = 'O'
                    win = 1
                    break
            if theBoard[b] == theBoard[c] == turn == 'O':
                if theBoard[a] == ' ':
                    theBoard[a] = 'O'
                    win = 1
                    break

        if win == 0:
            for i in range(1,9):
                if i == 1:
                    a = '1'
                    b = '2'
                    c = '3'
                if i == 2:
                    a = '4'
                    b = '5'
                    c = '6'
                if i == 3:
                    a = '7'
                    b = '8'
                    c = '9'
                if i == 4:
                    a = '1'
                    b = '4'
                    c = '7'
                if i == 5:
                    a = '2'
                    b = '5'
                    c = '8'
                if i == 6:
                    a = '3'
                    b = '6'
                    c = '9'
                if i == 7:
                    a = '1'
                    b = '5'
                    c = '9'
                if i == 8:
                    a = '3'
                    b = '5'
                    c = '7'

                if theBoard[a] == theBoard[b] == 'O' and (turn == 'X'):
                    if theBoard[c] == ' ':
                        theBoard[c] = turn
                        defend = 1
                        break
                if theBoard[a] == theBoard[c] == 'O' and (turn == 'X'):
                    if theBoard[b] == ' ':
                        theBoard[b] = turn
                        defend = 1
                        break
                if theBoard[b] == theBoard[c] == 'O' and (turn == 'X'):
                    if theBoard[a] == ' ':
                        theBoard[a] = turn
                        defend = 1
                        break
                if theBoard[a] == theBoard[b] == 'X' and (turn == 'O'):
                    if theBoard[c] == ' ':
                        theBoard[c] = turn
                        defend = 1
                        break
                if theBoard[a] == theBoard[c] == 'X' and (turn == 'O'):
                    if theBoard[b] == ' ':
                        theBoard[b] = turn
                        defend = 1
                        break
                if theBoard[b] == theBoard[c] == 'X' and (turn == 'O'):
                    if theBoard[a] == ' ':
                        theBoard[a] = turn
                        defend = 1
                        break

        if win == 0 and defend == 0:
            if count_tot == 0:
                theBoard['5'] = turn

            if count_tot == 1:
                if theBoard['5'] != ' ':
                    check = 1

                if check == 1:
                    theBoard['1'] = turn
                else:
                    theBoard['5'] = turn

            if count_tot == 2:
                for key in theBoard:
                    if theBoard[key] == 'O':
                        if key == '1':
                            theBoard['9'] = turn
                        if key == '3':
                            theBoard['7'] = turn
                        if key == '7':
                            theBoard['3'] = turn
                        if key == '9':
                            theBoard['1'] = turn
                        if key == '2' or key == '4' or key == '6' or key == '8':
                            theBoard['1'] = turn

            if count_tot == 3:
                if theBoard['5'] == 'X':
                    check = 1
                else:
                    check = 2

                if check == 1:
                    for key in theBoard:
                        if theBoard[key] == 'X':
                            if key != '9':
                                    if key == '1':
                                        theBoard['9'] = turn
                                    if key == '3':
                                        theBoard['7'] = turn
                                    if key == '7':
                                        theBoard['3'] = turn
                                    if key == '2':
                                        theBoard['8'] = turn
                                    if key == '4':
                                        theBoard['6'] = turn
                                    if key == '6':
                                        theBoard['4'] = turn
                                    if key == '8':
                                        theBoard['2'] = turn
                            else:
                                theBoard['3'] = turn
                if check == 2:
                    if theBoard['1'] == 'X' and theBoard['8'] == 'X':
                        theBoard['7'] = turn
                    if theBoard['1'] == 'X' and theBoard['6'] == 'X':
                        theBoard['3'] = turn
                    if theBoard['1'] == 'X' and theBoard['9'] == 'X':
                        theBoard['2'] = turn
                    if theBoard['2'] == 'X':
                        theBoard['1'] = turn
                    if theBoard['3'] == 'X' and theBoard['4'] == 'X':
                        theBoard['1'] = turn
                    if theBoard['3'] == 'X' and theBoard['7'] == 'X':
                        theBoard['2'] = turn
                    if theBoard['3'] == 'X' and theBoard['8'] == 'X':
                        theBoard['9'] = turn
                    if theBoard['4'] == 'X' and (theBoard['6'] == 'X' or theBoard['8'] == 'X' or theBoard['9'] == 'X') :
                        theBoard['1'] = turn
                    if theBoard['6'] == 'X' and (theBoard['7'] == 'X' or theBoard['8'] == 'X'):
                        theBoard['9'] = turn

            if count_tot == 4:
                checkfew = 0

                if theBoard['5'] == 'X' and theBoard['7'] == 'X' and theBoard['3'] == 'O' and theBoard['4'] == 'O':
                    theBoard['8'] = turn
                    checkfew = 1
                if theBoard['5'] == 'X' and theBoard['9'] == 'X' and theBoard['1'] == 'O' and theBoard['6'] == 'O':
                    theBoard['8'] = turn
                    checkfew = 1
                if theBoard['5'] == 'X' and theBoard['9'] == 'X' and theBoard['1'] == 'O' and theBoard['8'] == 'O':
                    theBoard['6'] = turn
                    checkfew = 1
                if theBoard['5'] == 'X' and theBoard['3'] == 'X' and theBoard['6'] == 'O' and theBoard['7'] == 'O':
                    theBoard['2'] = turn
                    checkfew = 1
                if theBoard['5'] == 'X' and theBoard['1'] == 'X' and theBoard['2'] == 'O' and theBoard['9'] == 'O':
                    theBoard['4'] = turn
                    checkfew = 1

                if checkfew == 0:
                    for key in theBoard:
                        if theBoard[key] == ' ':
                            theBoard[key] = turn
                            break

            if count_tot >= 5:
                for key in theBoard:
                    if theBoard[key] == ' ':
                        theBoard[key] = turn
                        break
