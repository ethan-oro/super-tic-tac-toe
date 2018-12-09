'''

minimax.py implements a minimax agent

'''

from agent import Agent
import heuristic
import copy
import time

class MiniMax(Agent):

    def __init__(self, depth = 3):
        self.depth = depth
        self.times = []

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
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth, -10000000, 100000000)
        self.times.append(time.time() - start_time)
        return action

    def recurse(self, state, depth, alpha, beta):
        actions = state.get_actions()
        if (state.is_end()): #isEnd(s)?
            return (state.get_new_reward(), None)
        elif (depth == 0): #d=0?
            val = self.evaluationFunction(state)
            return (val, None)
        elif (state.turn == 0): #Player(s) = agent?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                score = (self.recurse(new_state.update(action[0], action[1]), depth, alpha, beta))[0]
                vals.append((score, action))
                if score > alpha:
                    alpha = score
                if alpha >= beta:
                    break
            return max(vals)

        else: #Player(s) = agent is last last?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                score = (self.recurse(new_state.update(action[0], action[1]), depth - 1, alpha, beta))[0]
                vals.append((score, action))
                if score < beta:
                    beta = score
                if alpha >= beta:
                    break

            return min(vals)
