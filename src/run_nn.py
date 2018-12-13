import game as g
import deep_q_learning
import random_agent
import simulate
import collections
import os


LEARNING_FILE = 'learning.h5'
WIN_PCT_FILE = 'win_pct_player_1.csv'

def main():
    agent1 = deep_q_learning.DeepQLearning()
    agent1.define_model()
    print (agent1.model.summary())
    print (agent1.model.inputs)
    agent2 = random_agent.RandomAgent()
    wins = collections.defaultdict(int)
    numberOfSetsOfGames = 1000
    if os.path.isfile(LEARNING_FILE):
        agent1.loadLearning(LEARNING_FILE)
        print('loaded learning')
    print(agent1.model.get_weights())
    print ('running....')
    for i in range(numberOfSetsOfGames):
        agent1.reset()
        sim = simulate.Simulate(agent1, agent2, g.SuperTicTacToe(verbose = 0), verbose = 2)
        result = sim.run(i)
        agent1.update()
        wins[str(result)] += 1
        if (i % 100 == 0):
            print (i)
    print ('x won ' + str(wins['x'] / float(numberOfSetsOfGames)) + '% of the time')
    print ('o won ' + str(wins['o'] / float(numberOfSetsOfGames)) + '% of the time')
    print ('tie ' + str(wins['False'] / float(numberOfSetsOfGames)) + '% of the time')
    agent1.saveLearning(LEARNING_FILE)
    # plotValues = {'X Win Fraction': zip(range(numberOfSetsOfGames), map(lambda x: x[0], results)),
    #               'O Win Fraction': zip(range(numberOfSetsOfGames), map(lambda x: x[1], results)),
    #               'Draw Fraction': zip(range(numberOfSetsOfGames), map(lambda x: x[2], results))}
    # drawXYPlotByFactor(plotValues, 'Number of Sets (of 100 Games)', 'Fraction',title='RL Player (O) vs. Random Player (X)')


if __name__ == "__main__":
    main()
