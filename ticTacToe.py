theBoard = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' ',
}
POS = '123456789'

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +board['3'])

turn = 'X'
turn_number = 9

while True:
    if turn_number < 0:
        break
    printBoard(theBoard)
    move = input('\nTurn for %s.\nMove on which space?\n\n' % (turn))
    if move not in POS or theBoard[move] != ' ':
        continue
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    turn_number -= 1

printBoard(theBoard)
