'''

This game.py file is intended to contain all of the relevant machinery
in order for anybody to play a game of suepr tic tac toe.

'''



import math
import os.path


class SuperTicTacToe:

    def __init__(self, rows = 3, cols = 3, numPlayers = 2, verbose = 2):
        self.size = rows * cols
        self.grid = [ SubBoard() for col in range(rows * cols) ]
        self.numPlayers = numPlayers
        self.turn = 0
        self.currBigBoard = 0
        self.is_first = True
        self.verbose = 2
        self.winners = [ -1 for col in range(rows * cols) ]


    def get_user_action(self, boardName, is_open):
        while True:
            print("Which " +  boardName + " tile do you want to play in (1-9)?")
            action = raw_input(':')
            num = int(action)
            if (num != None and num <= 9 and num >= 1):
                    num -= 1
                    if (is_open(num)):
                        return num
                    else:
                        print ("Error! Spot already taken")
            else:
                print("Error! Please enter an integer (1-9)")

    # def get_actions(self):
    #     actions = [ (self.currBigBoard, move) for move in self.grid[self.currBigBoard].get_actions() ]
    #     #if no moves, check to see why:
    #     #case 1: can move anywhere
    #     #case 2: is a tie
    #     if (len(actions) == 0):
    #         for i in range(len(self.grid)):
    #             new_moves = self.grid[i].get_actions()
    #             actions = actions + [ (i, new_move) for new_move in new_moves]
    #     return actions

    def initial_actions(self):
        self.is_first = False
        actions = []
        for i in range(0,3):
            for j in range(0,3):
                actions.append((i,j))
        return actions

    def get_actions(self):
        if self.is_first == True:
            return self.initial_actions()
        actions = []
        if (self.winners[self.currBigBoard] == -1):
            actions = [ (self.currBigBoard, move) for move in self.grid[self.currBigBoard].get_actions() ]
        #if no moves, check to see why:
        #case 1: can move anywhere
        #case 2: is a tie
        if (len(actions) == 0):
            for i in range(len(self.grid)):
                if (self.winners[i] == -1):
                    new_moves = self.grid[i].get_actions()
                    actions = actions + [ (i, new_move) for new_move in new_moves]
        return actions

    def start(self):
        #ask for which big board, which small board
        print("Welcome to SuperTicTacToe!")
        big_val = self.get_user_action("Big Board", lambda x : x)
        small_val = self.get_user_action("Small Board", lambda x : x)
        self.update(big_val, small_val)

    def play(self):
        while (self.is_end() != True):
            self.move()

    #updates the state of the board based on the last move
    def update(self, big_val, small_val):
        response = self.grid[big_val].update(self.turn, small_val)
        if (response == False):
            print ("ERROR")
            self.printBoard()
            print ('big_val' + str(big_val) + ' ' + 'small_val' + str(small_val))
            raise ValueError('Tried to overwrite a space that already exists')
        self.turn = 0 if self.turn == 1 else 1
        result = self.grid[big_val].get_winner()
        self.winners[big_val] = -1 if (result == False) else result
        self.currBigBoard = small_val
        return self
        #update self.winners

    #prompts for a move and
    def move(self):
        if (self.versbose == 2):
            self.printBoard()
        small_board = self.grid[self.currBigBoard]
        print("You need to play in square "+ str(self.currBigBoard + 1) + " of the big board")
        small_val = self.get_user_action("Small Board", small_board.is_open)
        self.update(self.currBigBoard, small_val)


    def is_end(self):
        return self.is_tie() == True or self.get_winner() != False

    def get_winner(self):
        winners = self.winners
        if winners[0] == winners[3] == winners[6] != -1 : return winners[0]
        if winners[1] == winners[4] == winners[7] != -1 : return winners[1]
        if winners[2] == winners[5] == winners[8] != -1 : return winners[2]
        if winners[0] == winners[1] == winners[2] != -1 : return winners[0]
        if winners[3] == winners[4] == winners[5] != -1 : return winners[3]
        if winners[6] == winners[7] == winners[8] != -1 : return winners[6]
        if winners[0] == winners[4] == winners[8] != -1 : return winners[4]
        if winners[2] == winners[4] == winners[6] != -1 : return winners[4]
        return False

    def get_reward(self):
        winner = self.get_winner()
        #if tie, 'reward' is 0
        if winner == False: return 0
        #if we won, reward is 1!
        if (winner == 'x'): return 1
        #if we lost, reward is 0
        return -1

    #if board is full
    def is_tie(self):
        return len(self.get_actions()) == 0

    def printBoard(self):
        ver = ' || '
        hor = ' = '
        board = [ '' for i in range (0, 18) ]
        for k in range(0, 3):
            p = 0
            for i in range(k*6, k*6+5):
                if (i % 2 == 0):
                    for j in range(0,3):
                        row = self.grid[k*3+j].getRow(p)
                        board[i] += row[0] + '|' + row[1] + '|' + row[2]
                        if (j != 2):
                            board[i] += ver
                    p += 1
                else:
                    board[i] += '-+-+- || -+-+- || -+-+- '
            if k!= 2:
                board[k*6+5] +=  '======================='

        for b in board:
            print (b)

    def printWinner(self):
        winner = self.get_winner()
        if (winner == False):
            print ("tie!")
        else:
            print (winner + ' won!')


class SubBoard:

    def __init__(self, rows = 3, cols = 3, characters = ['x', 'o']):
        self.size = rows * cols
        self.grid = [ ' ' for col in range(self.size) ]
        self.characters = characters
        self.winner = -1

    def get_small_board(self):
        return self.grid

    def get_actions(self):
        moves = []
        for index in range(self.size):
                if self.grid[index] == ' ':
                    moves.append(index)
        return moves

    def printBoard(self):
        for index in range(self.size):
            print(self.grid[index])

    #for printing purposes
    def getRow(self, row):
        return self.grid[3*row:3*row+3]

    #function to return if a square is not occupied
    def is_open(self, location):
        return self.grid[location] == ' '

    def get_chacter(self, location):
        return self.grid[location]

    def is_end(self):
        winners = [ space for space in self.grid ]
        if winners[0] == winners[3] == winners[6] != ' ' : return True
        if winners[1] == winners[4] == winners[7] != ' ' : return True
        if winners[2] == winners[5] == winners[8] != ' ' : return True
        if winners[0] == winners[1] == winners[2] != ' ' : return True
        if winners[3] == winners[4] == winners[5] != ' ' : return True
        if winners[6] == winners[7] == winners[8] != ' ' : return True
        if winners[0] == winners[4] == winners[8] != ' ' : return True
        if winners[2] == winners[4] == winners[6] != ' ' : return True
        return False

    def get_winner(self):
        winners = [ space for space in self.grid ]
        if winners[0] == winners[3] == winners[6] != ' ' : return winners[0]
        if winners[1] == winners[4] == winners[7] != ' ' : return winners[1]
        if winners[2] == winners[5] == winners[8] != ' ' : return winners[2]
        if winners[0] == winners[1] == winners[2] != ' ' : return winners[0]
        if winners[3] == winners[4] == winners[5] != ' ' : return winners[3]
        if winners[6] == winners[7] == winners[8] != ' ' : return winners[6]
        if winners[0] == winners[4] == winners[8] != ' ' : return winners[4]
        if winners[2] == winners[4] == winners[6] != ' ' : return winners[4]
        return False

    #function to update the small board value, returning a boolean of success
    def update(self, characterIndex, location):
        character = self.grid[location]
        if (character != ' '):
            return False
        else:
            self.grid[location] = self.characters[characterIndex]
            if (self.is_end() and self.winner == -1):
                self.winner = self.characters.index(self.get_winner())
            return True
