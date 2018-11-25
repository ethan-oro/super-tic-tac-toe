'''

simulate.py is a class that, given two agents, will simulate a game of
supertictactoe between two agents


'''
import random_agent
import game


class Simulate:

    def __init__(self, agent1 = random_agent.RandomAgent(), agent2 = random_agent.RandomAgent(), game = game.SuperTicTacToe(verbose = 0)):
        self.agent1 = agent1
        self.agent2 = agent2
        self.game = game

    def run(self):
        big, small = self.agent1.start()
        self.game.update(big, small)
        while (True):
            if (game.is_end() == True):
                break
            big, small = self.agent2(self.game.get_actions())
            self.game.update(big,small)
            if (game.is_end() == True):
                break
            big, small = self.agent1(self.game.get_actions())
            self.game.update(big,small)
        print (self.game.printBoard())
