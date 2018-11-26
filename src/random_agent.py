'''

This random_agent.py is a random choosing agent that will choose a move with
uniform random probability given a set of possible moves

'''

import random
import time

class RandomAgent:

    def __init__(self):
        random.seed(time.time())

    def start(self):
        return (random.randint(0, 8), random.randint(0, 8))

    def chooseMove(self, actions):
        if (len(actions) == 1):
            move = actions[0]
        else:
            move = actions[random.randint(0, len(actions) - 1)]
        return move[0], move[1]
