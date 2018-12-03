'''

minimax.py implements a minimax agent

'''
#sys imports
import copy
import time

#class imports
from agent import Agent
import heuristic

class MiniMax(Agent):

    def __init__(self, depth = 1):
        self.depth = depth

    def start(self, state):
        # move = self.pickMove(state)
        # return move
        return (2,2)

    def evaluationFunction(self, state):
        self.heuristic = heuristic.Heuristics(state, state.grid)
        static = self.heuristic.calcTotValueForAgent('x')
        dynamic = self.heuristic.agentCanWin(0)
        return static + dynamic

    def pickMove(self, state):
        start_time = time.time()
        self.count = 0
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth)
        # print (self.count)
        # print (time.time() - start_time)
        return action[0], action[1]

    def recurse(self, state, depth):
        self.count += 1
        # print (depth)
        actions = state.get_actions()
        if (state.is_end()): #isEnd(s)?
            return (state.get_reward(), None)
        elif (depth == 0): #d=0?
            return (self.evaluationFunction(state), None)
        elif (state.turn == 0): #Player(s) = agent?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                new_state.update(action[0], action[1])
                vals.append((self.recurse(new_state, depth)[0], action))
            return max(vals)
        else: #Player(s) = agent is last last?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                new_state.update(action[0], action[1])
                vals.append((self.recurse(new_state, depth - 1)[0], action))
            return min(vals)
