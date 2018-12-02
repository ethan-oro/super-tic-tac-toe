'''

minimax.py implements a minimax agent

'''

from agent import Agent
import copy

class MiniMax(Agent):

    def __init__(self, depth = 3):
        self.depth = depth

    def start(self, state):
        # move = self.pickMove(state)
        # return move
        return (2,2)

    def evaluationFunction(self,state):
        return 0

    def pickMove(self, state):
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth)
        return action

    def recurse(self, state, depth):
        print (depth)
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
