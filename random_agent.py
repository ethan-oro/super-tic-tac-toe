'''

This random_agent.py is a random choosing agent that will choose a move with
uniform random probability given a set of possible moves

'''

import random

class RandomAgent:

    def __init__(seed = 221):
        self.rand = random.seed(seed)

    def start(self):
        return (self.rand.randint(0, 9), self.rand.randint(0, 9))

    def chooseMove(self, actions):
        move = actions[self.rand.randint(0, len(actions))]
        return move[0], move[1]
