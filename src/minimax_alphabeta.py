'''

minimax.py implements a minimax agent

'''

from agent import Agent
from hueristic
import copy

class MiniMax(Agent):

    def __init__(self, depth = 3):
        self.depth = depth

    def start(self, state):
        # move = self.pickMove(state)
        # return move
        return (2,2)

    def evaluationFunction(self, state):
        pass

    def pickMove(self, state):
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth)
        return action

    def recurse(self, state, depth, alpha, beta):
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
                score = (self.recurse(new_state.update(action[0], action[1]), depth)[0]

                vals.append(score, action))

                if score > alpha:
                    alpha = score_next
                    action = next_action

                if alpha >= beta
                    break


            return max(vals)

        else: #Player(s) = agent is last last?
            vals = []
            for action in actions:
                new_state = copy.deepcopy(state)
                score = (self.recurse(new_state.update(action[0], action[1]), depth - 1)[0]

                vals.append(score, action))


                if score < beta:
                    beta = score
                    action = next_action

                if alpha >= beta:
                    break

            return min(vals)
