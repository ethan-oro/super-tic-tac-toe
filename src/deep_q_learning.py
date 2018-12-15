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
        self.INPUTS = {' ' : 0, 'x' :1, 'o' : -3}

    #defines our nn that has an input for each board square
    def define_model(self):
        self.model = Sequential()
        self.model.add(Dense(81, input_dim=81, activation='relu'))
        self.model.add(Dense(9, activation='relu'))
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
        hist = self.model.fit(x, y, verbose=0)

    def board_to_input(self, state):
        board = [ x for sub in state.grid for x in sub.grid ]
        return list(map(lambda x : self.INPUTS.get(x), board))

    def board_to_output(self, state):
        board = [ x for sub in state.grid for x in sub.grid ]
        return list(map(lambda x : str(self.INPUTS.get(x)), board))


    def predict(self, x):
        asdf = np.array(self.board_to_input(x)).reshape(1,-1)
        return self.model.predict(asdf)[0]

    def update(self, state):
        self.get_pred(0, state.grid, state)
        return
        x = []
        y = []
        for k,v in self.vals.items():
            x.append(self.board_to_input(k))
            y.append(v)
        if len(x) == 0:
            return
        self.train(x, y)

    def reset(self):
        self.vals = {}

    def save(self, state, label):
        l = self.board_to_output(state)
        l.append(str(label))
        with open("data.txt", "a") as myfile:
            myfile.write(' '.join(l) + '\n')

    def get_pred(self, player, board, state):
        winner = state.get_winner()
        if winner == False:
            z = self.predict(state)
            if(isinstance(z, int)):
                y = z
            else:
                y = z[0]
        else:
            # print (winner)
            # print (state.printBoard())
            if winner == 'x': #x won
                y = 1.0
                # print (y)
                self.save(state, y)
                self.vals[state] = y
            elif winner == 'o': #o won
                y = -1.0
                # print (y)
                self.save(state, y)
                self.vals[state] = y
            elif state.is_tie(): #is a tie
                y = 0.5
                # print (y)
                self.save(state, y)
                self.vals[state] = y
            else:
                raise ValueError('This should never happen')
        return y

    def trainLearning(self):
        x = []
        y = []
        c = 0
        with open ('data.txt', 'r') as file:
            for c, line in enumerate(file):
                x.append([ int(x) for x in line.split(' ')[:81] ])
                q = float(line.split(' ')[81:][0])
                # print (q)
                if q == 0.5:
                    q = 0.0
                    print('e')
                y.append(q)
                c+=1
                if c % 1000 == 0:
                    print (c)
        print ('training....')
        self.train(x, y)

    def learn(self, player, state, last_state):
        board = state.get_grid()
        prediction = self.get_pred(player, board, state)
        prev_value = self.predict(last_state)
        self.vals[last_state] = prev_value + 0.2 * (prediction - prev_value)

    def start(self, state):
        a, b = self.pickMove(state)
        return (a,b)

    def makeMove(self, state, action):
        new_state = copy.deepcopy(state)
        new_state.update(action[0], action[1])
        return new_state

    def pickMove(self, state):
        # return self.pickMoveNoExplore(state)
        actions = state.get_actions()
        if (random.uniform(0,1) < 0.75):
            moves = {}
            for action in actions:
                next_state = self.makeMove(state, action)
                moves[action] = self.get_pred(0, next_state.grid, next_state)
            # print(moves)
            move = max(moves, key=moves.get)
        else:
            move = actions[random.randint(0, len(actions) - 1)]
        return move[0], move[1]

    def pickMoveNoExplore(self, state):
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
        # self.model.load_weights(filename, by_name=False)
        self.trainLearning()
