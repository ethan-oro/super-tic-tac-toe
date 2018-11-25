'''

simulate.py is a class that, given two agents, will simulate a game of
supertictactoe between two agents


'''
import random_agent
import game as g


class Simulate:

    def __init__(self, agent1 = random_agent.RandomAgent(), agent2 = random_agent.RandomAgent(), game = g.SuperTicTacToe(verbose = 0)):
        self.agent1 = agent1
        self.agent2 = agent2
        self.game = game

    def run(self):
        big, small = self.agent1.start()
        self.game.update(big, small)
        while (True):
            if (self.game.is_end() == True):
                break
            big, small = self.agent2.chooseMove(self.game.get_actions())
            self.game.update(big,small)
            if (self.game.is_end() == True):
                break
            big, small = self.agent1.chooseMove(self.game.get_actions())
            self.game.update(big,small)
        self.game.printBoard()
        self.game.printWinner()
