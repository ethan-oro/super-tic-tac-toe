'''

play.py is a class intded to call simulate or allow for a user to play


'''

import simulate
import collections
import random_agent
import game as g
import mcts

def main():
    # g = game.SuperTicTacToe()
    # g.start()
    # g.play()
    wins = collections.defaultdict(int)
    numTrials = 1000
    print ('out of ' + str(numTrials) + ' games....')
    for i in range(0, numTrials):
        game = simulate.Simulate(agent1 = mcts.MonteCarloTreeSearch(g.SuperTicTacToe(verbose = 0)), agent2 = random_agent.RandomAgent(), game = g.SuperTicTacToe(verbose = 0), verbose = 0)
        result = game.run()
        wins[str(result)] += 1
    print ('x won ' + str(wins['x'] / float(numTrials)) + '% of the time')
    print ('o won ' + str(wins['o'] / float(numTrials)) + '% of the time')
    print ('tie ' + str(wins['False'] / float(numTrials)) + '% of the time')

if __name__ == '__main__':
    main()
