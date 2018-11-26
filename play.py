import simulate
import collections
import random_agent
import game as g


def main():
    # g = game.SuperTicTacToe()
    # g.start()
    # g.play()
    wins = collections.defaultdict(int)
    numTrials = 10000
    print ('out of ' + str(numTrials) + ' games....')
    for i in range(0, numTrials):
        game = simulate.Simulate(agent1 = random_agent.RandomAgent(), agent2 = random_agent.RandomAgent(), game = g.SuperTicTacToe(verbose = 0), verbose = 0)
        result = game.run()
        wins[str(result)] += 1
    print ('x won ' + str(wins['x'] / float(numTrials)) + '% of the time')
    print ('o won ' + str(wins['o'] / float(numTrials)) + '% of the time')
    print ('tie ' + str(wins['False'] / float(numTrials)) + '% of the time')

if __name__ == '__main__':
    main()
