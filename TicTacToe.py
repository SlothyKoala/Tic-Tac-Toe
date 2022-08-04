import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def playerInput():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:   
        return 'computer'   
    else:   
        return 'player'

def playAgain():
    print('Do you want to play again?(y/n)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def boardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    
    return dupeBoard

def spaceFree(board, move):
    return board[move] == ' '

def playerTurn(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if spaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computerTurn(board, computerLetter):
    print("Computer's turn!")
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = boardCopy(board)
        if spaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if winner(copy, computerLetter):
                return i

        for i in range(1, 10):
            copy = boardCopy(board)
            if spaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if winner(copy, playerLetter):
                    return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if spaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def fullBoard(board):
    for i in range(1, 10):
        if spaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = playerInput()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gamePlaying = True

    while gamePlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = playerTurn(theBoard)
            makeMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Well done! You have won!')
                gamePlaying = False
            else:
                if fullBoard(theBoard):
                    drawBoard(theBoard)
                    print('Its a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = computerTurn(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You lose! Better luck next time.')
                gamePlaying = False
            else:
                if fullBoard(theBoard):
                    drawBoard(theBoard)
                    print('Its a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break