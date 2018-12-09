#sys imports
import json
import os
import random
import copy

#nn imports
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.utils import plot_model

#lib imports
import numpy as np

#class imports
from agent import Agent
from game import *


class DeepQLearning(Agent):

    def __init__(self):
        self.vals = {}
        self.INPUTS = {' ' : 0, 'x' :1, 'o' : -1}

    #defines our nn that has an input for each board square
    def define_model(self):
        self.model = Sequential()
        self.model.add(Dense(81, input_dim=81, activation='relu'))
        self.model.add(Dense(1, activation='linear', kernel_initializer='glorot_uniform'))
        self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
        #uses keras.utils plot_model function
        # plot_model(self.model, to_file='model.png')

    def learn_previous_model(self, file):
        if os.path.isfile(file):
            self.vals = json.load(open(file, 'r'))
            self.update()

    def train(self, x, y):
        x = np.asarray(x)
        y = np.asarray(y)
        self.model.fit(x, y, epochs = 10, verbose=0)

    def board_to_input(self, state):
        board = [ x for sub in state.grid for x in sub.grid ]
        return list(map(lambda x : self.INPUTS.get(x), board))

    def predict(self, x):
        asdf = np.array(self.board_to_input(x)).reshape(1,-1)
        return self.model.predict(asdf)[0]

    def update(self):
        x = []
        y = []
        for k,v in self.vals.items():
            x.append(self.board_to_input(k))
            y.append(v)
        self.train(x, y)

    def reset(self):
        self.vals = {}

    def get_pred(self, player, board, state):
        winner = state.get_winner()
        if winner == 0: #x won
            y = 1.0 if player == 0 else 0.0
            self.vals[state] = y
        elif winner == 1: #o won
            y = 1.0 if player == 1 else 0.0
            self.vals[state] = y
        elif state.is_tie(): #is a tie
            y = 0.5
            self.vals[state] = y
        else:
            y = self.predict(state)
        return y


    def learn(self, player, state, last_state):
        board = state.get_grid()
        prediction = self.get_pred(player, board, state)
        prev_value = self.predict(last_state)
        self.vals[last_state] = prev_value + 0.2 * (prediction - prev_value)

    def start(self, state):
        return (2,2)

    def makeMove(self, state, action):
        new_state = copy.deepcopy(state)
        new_state.update(action[0], action[1])
        return new_state

    def pickMove(self, state):
        return self.pickMoveNoGuess(state)
        actions = state.get_actions()
        if (random.uniform(0,1) < 0.8):
            moves = {}
            for action in actions:
                next_state = self.makeMove(state, action)
                moves[action] = self.get_pred(0, next_state.grid, next_state)
            # print(moves)
            move = max(moves, key=moves.get)
        else:
            move = actions[random.randint(0, len(actions) - 1)]
        return move[0], move[1]

    def pickMoveNoGuess(self, state):
        actions = state.get_actions()
        moves = {}
        for action in actions:
            next_state = self.makeMove(state, action)
            moves[action] = self.get_pred(0, next_state.grid, next_state)
        # print(moves)
        move = max(moves, key=moves.get)
        return move[0], move[1]

    def chooseMove(self, actions):
        pass

    def saveLearning(self, filename):
        self.model.save_weights(filename)

    def loadLearning(self, filename):
        self.model.load_weights(filename, by_name=False)
