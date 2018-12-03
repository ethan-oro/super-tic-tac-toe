#sys imports
import json
import os

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
        self.define_model()

    #defines our nn that has an input for each board square
    def define_model(self):
        self.model = Sequential()
        self.model.add(Dense(81, input_dim=81, activation='relu'))
        self.model.add(Dense(1, activation='linear', kernel_initializer='glorot_uniform'))
        self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
        #uses keras.utils plot_model function
        plot_model(self.model, to_file='model.png')


    def learn_previous_model(self, file):
        if os.path.isfile(file):
            self.vals = json.load(open(file, 'r'))
            self.update()

    def train(self, x, y):
        self.model.fit(np.asarray(x), np.asarray(y), verbose=0)

    def board_to_input(self, state):
        return [ lambda x : {' ' : 0, 'x' :1, 'o' : -1}.get(x) for x in state ]

    def predict(self, x):
        self.model.predict(np.asarray(self.board_to_input(x)))

    def update(self):
        x = []
        y = []
        for k,v in self.vals.iteritems():
            x.append(self.convertBoardStateToInput(k))
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

    def start(self):
        return (2,2)

    def chooseMove(self, actions):
        pass
