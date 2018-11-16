'''

This game.py file is intended to contain all of the relevant machinery
in order for anybody to play a game of suepr tic tac toe.

'''



import math
import os.path


class SuperTicTacToe:

    def __init__(self, rows = 3, cols = 3, numPlayers = 2):
        self.size = rows * cols
        self.grid = [ SubBoard() for col in range(rows * cols) ]
        self.numPlayers = numPlayers
        self.turn = 0


    def get_user_action(self, boardName):
        while True:
            print("Which " +  boardName + " tile do you want to play in (1-9)?")
            action = raw_input(':')
            num = int(action)
            if (num =< 9 and num <= 1):
                return num
            else:
                print ("Error! Please enter an integer (1-9)")

    def start(self):
        #ask for which big board, which small board
        print("Welcome to SuperTicTacToe!")
        big_val = self.get_user_action("Big Board")
        small_val = self.get_user_action("Small Board")
        small_board = self.grid[big_val]
        small_board.update(0, small_val)
        self.update(big_val, small_board)

    def update(self):
        #updates the state of the board based on the last move
        return ''

    def move(self, move):
        return ''

    def print(self):
        for index in range(self.size):
            self.grid[index].print()

# class BigBoard:
#
#     def __init__(self, rows = 3, cols = 3):
#         self.grid = [ SmallBoard() for col in range(rows * cols)]
#
#     def get_big_board(self):
#         return self.grid


class SubBoard:

    def __init__(self, rows = 3, cols = 3, characters = ['x', 'o']):
        self.size = rows * cols
        self.grid = [ ' ' for col in range(self.size)]
        self.characters = characters

    def get_small_board(self):
        return self.grid

    def get_actions(self):
        moves = []
        for index in range(self.size):
                if self.grid[index] == ' ':
                    moves.append(index)
        return moves

    def print(self):
        for index in range(self.size):
            print(self.grid[index])

    #function to return if a square is not occupied
    def is_open(self, location):
        self.grid[location] == ' '

    def get_chacter(self, location):
        return self.grid[location]

    #function to update the small board value, returning a boolean of success
    def update(self, characterIndex, location):
        character = self.grid[location]
        if (character == ' '):
            return False
        else:
            self.grid[location] = self.characters[characterIndex]
            return True
