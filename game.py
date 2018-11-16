'''

This game.py file is intended to contain all of the relevant machinery
in order for anybody to play a game of suepr tic tac toe.

'''



import math
import os.path


class SuperTicTacToe:

    def __init__(self, num_rows = 3, num_cols = 3, numPlayers = 2):
        self.grid = [ [ None for col in range(cols)] for row in range(rows)]
        self.numPlayers = numPlayers
        self.turn = 0
        self.currBigBoard = None


    def start(self):
        #ask for which big board, which small board
        print("Welcome to SuperTicTacToe!")
        print("which square would you like")
        return ''

    def update(self):
        #updates the state of the board based on the last move
        return ''

    def move(self, move):
        return ''

class BigBoard:

    def __init__(self, ):
        self.grid = [ [ SmallBoard() for col in range(cols)] for row in range(rows)]

    def get_big_board(self):
        return self.grid


class SmallBoard:

    def __init__(self, rows = 3, cols = 3, characters = ['x', 'o']):
        self.rows = rows
        self.cols = cols
        self.grid = [ [ ' ' for col in range(cols)] for row in range(rows)]
        self.characters = []

    def get_small_board(self):
        return self.grid

    def get_actions(self):
        moves = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == ' ':
                    moves.append((row, col))
        return moves

    #function to return if a square is not occupied
    def is_open(self, location):
        self.grid[location[0]][location[1]] == ' '

    def get_chacter(self, location):
        return self.grid[location[0]][location[1]]

    #function to update the small board value, returning a boolean of success
    def update(self, characterIndex, location):
        character = self.grid[location[0]][location[1]]
        if (character == ' '):
            return False
        else:
            self.grid[location[0]][location[1]] = self.characters[characterIndex]
            return True
