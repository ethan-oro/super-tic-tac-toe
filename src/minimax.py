'''

minimax.py implements a minimax agent

'''

from agent import Agent
import copy

class MiniMax(Agent):

    def __init__(self, depth = 2):
        self.depth = depth

    def start(self, state):
        # move = self.pickMove(state)
        # return move
        return (2,2)

    def evaluationFunction(self, state):
        val = 0
        for big_index in range(len(state.grid)):
            factor = 2 if big_index % 2 == 0 else 1
            for small_index in range(len(state.grid[big_index].grid)):
                val += factor * (2 if small_index % 2 == 0 else 1)
        return val

    def pickMove(self, state):
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth)
        return action

    def recurse(self, state, depth):
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
                vals.append((self.recurse(new_state.update(action[0], action[1]), depth)[0], action))
            return max(vals)
        else: #Player(s) = agent is last last?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                vals.append((self.recurse(new_state.update(action[0], action[1]), depth - 1)[0], action))
            return min(vals)
