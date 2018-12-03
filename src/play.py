'''

play.py is a class intded to call simulate or allow for a user to play


'''
#class imports
import simulate
import collections
import random_agent
import game as g
import mcts
import minimax
import minimax_alphabeta
import deep_q_learning

def main():
    # g = game.SuperTicTacToe()
    # g.start()
    # g.play()
    wins = collections.defaultdict(int)
    numTrials = 100
    print ('out of ' + str(numTrials) + ' games....')
    for i in range(0, numTrials):
        # game = simulate.Simulate(agent1 = mcts.MonteCarloTreeSearch(g.SuperTicTacToe(verbose = 0)), agent2 = random_agent.RandomAgent(), game = g.SuperTicTacToe(verbose = 0), verbose = 0)
        # result = game.run(trial)
        game = simulate.Simulate(\
            # agent1 = deep_q_learning.DeepQLearning(),\
            agent1 = minimax.MiniMax(), \
            agent2 = random_agent.RandomAgent(),\
            game = g.SuperTicTacToe(verbose = 0),\
            verbose = 1\
        )
        result = game.run(i)
        wins[str(result)] += 1
    print ('x won ' + str(wins['x'] / float(numTrials)) + '% of the time')
    print ('o won ' + str(wins['o'] / float(numTrials)) + '% of the time')
    print ('tie ' + str(wins['False'] / float(numTrials)) + '% of the time')

def main2():
    # g = game.SuperTicTacToe()
    # g.start()
    # g.play()
    wins = collections.defaultdict(int)
    numTrials = 100
    print ('out of ' + str(numTrials) + ' games....')
    for i in range(0, numTrials):
        # game = simulate.Simulate(agent1 = mcts.MonteCarloTreeSearch(g.SuperTicTacToe(verbose = 0)), agent2 = random_agent.RandomAgent(), game = g.SuperTicTacToe(verbose = 0), verbose = 0)
        # result = game.run(trial)
        game = simulate.Simulate(\
            # agent1 = deep_q_learning.DeepQLearning(),\
            agent1 = minimax.MiniMax(depth = 2), \
            agent2 = random_agent.RandomAgent(),\
            game = g.SuperTicTacToe(verbose = 0),\
            verbose = 1\
        )
        result = game.run(i)
        wins[str(result)] += 1
    print ('x won ' + str(wins['x'] / float(numTrials)) + '% of the time')
    print ('o won ' + str(wins['o'] / float(numTrials)) + '% of the time')
    print ('tie ' + str(wins['False'] / float(numTrials)) + '% of the time')

if __name__ == '__main__':
    main2()
