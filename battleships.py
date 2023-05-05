from random import randint
l=1
while l==1:
    board=[]
    for x in range(5):
        board.append(["O"] * 5)

    def draw_board(board):
        for row in board:
            print((" ").join(row))

    print("Let's play Battleship!")
    draw_board(board)

    def random_row(board):
        return randint(0, len(board) - 1)
    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(9):
        print ("Turn", turn+1)
        guess_row = int(input("Guess Row:"))
        guess_col = int( input("Guess Col:"))
    
        if guess_row == ship_row and guess_col == ship_col:
            print("CONGRATULATIONS! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even close.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            elif ((guess_row+1==ship_row) or (guess_row-1==ship_row)) and ((guess_col+1==ship_col) or (guess_col-1==ship_col)):
                print('You are very close!!\n')
                board[guess_row][guess_col]='X'
            elif ((guess_row+1==ship_row) or (guess_row-1==ship_row)) or ((guess_col+1==ship_col) or (guess_col-1==ship_col)):
                print('You are close!\n')
                board[guess_row][guess_col] = "X"
                
            else:
                print("You missed my battleship!\n")
                board[guess_row][guess_col] = "X"
        if turn == 8:
            print("GAME OVER")
            print('THE BATTLESHIP WAS AT: \n ROW = ',ship_row, '\n COLUMN = ',ship_col,'\n\n')
        turn =+ 1
        draw_board(board)
    l=int(input('PRESS 1 TO PLAY AGAIN: \n IF NOT PRESS 2: \n'))

