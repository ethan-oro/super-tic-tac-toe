'''

simulate.py is a class that, given two agents, will simulate a game of
supertictactoe against themsevles


'''
import random_agent
import game


class Simulate:

    def __init__(agent1 = RandomAgent(), agent2 = RandomAgent(), game = game.SuperTicTacToe()):
        self.agent1 = agent1
        self.agent2 = agent2
        self.game = game

    def run(self):
        
