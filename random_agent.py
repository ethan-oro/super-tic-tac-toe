'''

This random_agent.py is a random choosing agent that will choose a move with
uniform random probability given a set of possible moves

'''

import random

class RandomAgent:

    def __init__(seed = 221):
        self.rand = random.seed(seed)

    def chooseMove(self, actions):
        return actions[self.rand.randint(0, len(actions))
