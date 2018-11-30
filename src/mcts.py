'''

mcts.py implements monte carlo tree search for super tic tac toe


'''
from agent import Agent
from game import *
from collections import defaultdict
import random
import copy
import math
import time

class MonteCarloTreeSearch(Agent):

    def __init__(self, root):
        self.root = Node(root, parent = None)

    def start(self, state):
        move = self.pickMove(state)
        # print (move)
        return move

    def chooseMove(self, actions):
        return ''

    def pickMove(self, state):
        self.root = Node(state, parent = None)
        count = 0
        while (count < 1000):
            next = self.get_next()
            reward = next.finish_game()
            next.backpropogate(reward)
            count += 1
        return self.root.best_child(c = 0).action

    def get_next(self):
        curr = self.root
        while (curr.state.is_end() is not True):
            if (curr.has_more_actions()):
                return curr.generate_child()
            else:
                curr = curr.best_child()
        return curr


class Node:

    def __init__(self, state, parent, action = None):
        self.num_vists = 0
        self.results = defaultdict(int)
        self.state = state
        self.parent = parent
        self.children = []
        self.actions = state.get_actions()
        self.action = action
        random.seed(time.time())

    #simulates a random game to completion
    def finish_game(self):
        state = self.state
        while(state.is_end() is not True):
            moves = state.get_actions()
            big, small = moves[random.randint(0, len(moves) - 1)]
            state.update(big, small)
        return state.get_reward()

    #generates new child
    def generate_child(self):
        big, small = self.actions.pop()
        new_state = copy.deepcopy(self.state)
        new_state.update(big, small)
        child = Node(new_state, parent = self, action = (big, small))
        self.children.append(child)
        return child

    #generates the q value for a child
    def q(self):
        wins = self.results[1]
        losses = self.results[-1]
        return wins - losses

    def get_score(self):
        return (self.q() / (self.parent.num_vists)) + c * math.sqrt((2 * math.log(self.parent.num_vists) / (self.num_vists)))

    #finds best child based on defined formula
    def best_child(self, c = 1.4):
        scores = [ (child.q() / (child.num_vists)) + c * math.sqrt((2 * math.log(self.num_vists) / (child.num_vists))) for child in self.children ]
        # print ('scores', scores)
        return self.children[scores.index(max(scores))]

    #updates win/loss ratio for self, and then all parents
    def backpropogate(self, result):
        self.num_vists += 1
        self.results[result] += 1
        if self.parent:
            self.parent.backpropogate(result)

    #chekcs to see if we have any more actions
    def has_more_actions(self):
        return len(self.actions) != 0
