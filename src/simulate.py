'''

simulate.py is a class that, given two agents, will simulate a game of
supertictactoe between two agents


'''
import random_agent
import game as g


class Simulate:

    def __init__(self, agent1, agent2, game, verbose = 1):
        self.agent1 = agent1
        self.agent2 = agent2
        self.game = game
        self.verbose = verbose

    def run(self, trial):
        if (self.verbose == 2):
            print ('game: ' + str(trial))
        if (self.verbose == 2):
            print ("agnet 1 moved")
        big, small = self.agent1.start(self.game)
        self.game.update(big, small)
        while (True):
            if (self.game.is_end() == True):
                break
            actions = self.game.get_actions()
            if (len(actions) == 0):
                print ("ERROR :: ")
                print ('is_end() : ' + str(self.game.is_end()))
                print ('is_tie : ' + str(self.game.is_tie()))
            big, small = self.agent2.chooseMove(actions)
            self.game.update(big,small)
            if (self.game.is_end() == True):
                break
            if (self.verbose == 2):
                print ("agent 2 moved")
            actions = self.game.get_actions()
            if (len(actions) == 0):
                print ("ERROR :: ")
                print ('is_end() : ' + str(self.game.is_end()))
            big, small = self.agent1.pickMove(self.game)
            self.game.update(big,small)
            if (self.verbose == 2):
                print ("agent 1 moved")
        if (self.verbose != 0):
            self.game.printWinner()
            if (self.verbose == 2):
                self.game.printBoard()
        return self.game.get_winner()
