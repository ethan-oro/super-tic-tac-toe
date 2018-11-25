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
        verbose = 2


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

    def get_actions(self):
        actions = [ (self.currBigBoard, move) for move in self.grid[self.currBigBoard].get_actions() ]
        #if no moves, check to see why:
        #case 1: can move anywhere
        #case 2: is a tie
        if (len(moves) == 0):
            for board in grid:
                new_moves = board.get_actions()
                new_actions = new_actions + [ (i, new_move) for new_move in new_moves]
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
        val = self.grid[big_val].update(self.turn, small_val)
        if (val == False):
            print ("ERROR")
        self.turn = 0 if self.turn == 1 else 1
        self.currBigBoard = small_val

    #prompts for a move and
    def move(self):
        if (versbose == 2):
            self.printBoard()
        small_board = self.grid[self.currBigBoard]
        print("You need to play in square "+ str(self.currBigBoard + 1) + " of the big board")
        small_val = self.get_user_action("Small Board", small_board.is_open)
        self.update(self.currBigBoard, small_val)


    def is_end(self):
        if (self.get_actions() == 0): return True
        winners = [ board.winner for board in self.grid ]
        if winners[0] == winners[3] == winners[6] != -1 : return True
        if winners[1] == winners[4] == winners[7] != -1 : return True
        if winners[2] == winners[5] == winners[8] != -1 : return True
        if winners[0] == winners[1] == winners[2] != -1 : return True
        if winners[3] == winners[4] == winners[5] != -1 : return True
        if winners[6] == winners[7] == winners[8] != -1 : return True
        if winners[0] == winners[4] == winners[8] != -1 : return True
        if winners[2] == winners[4] == winners[6] != -1 : return True
        return False

    def get_winner(self):
        winners = [ board.winner for board in self.grid ]
        if winners[0] == winners[3] == winners[6] != -1 : return winners[0]
        if winners[1] == winners[4] == winners[7] != -1 : return winners[1]
        if winners[2] == winners[5] == winners[8] != -1 : return winners[2]
        if winners[0] == winners[1] == winners[2] != -1 : return winners[0]
        if winners[3] == winners[4] == winners[5] != -1 : return winners[3]
        if winners[6] == winners[7] == winners[8] != -1 : return winners[6]
        if winners[0] == winners[4] == winners[8] != -1 : return winners[4]
        if winners[2] == winners[4] == winners[6] != -1 : return winners[4]
        return False


    def printBoard(self):
        ver = ' || '
        hor = ' = '
        board = [ '' for i in range (0, 22) ]
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
            if (self.is_end()):
                self.winner = self.characters.index(self.get_winner())
            return True
