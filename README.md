# Adversarial Agents: Using Novel Machine Learning Strategies to Win SuperTicTacToe
Mortaza Moradi (mortaza@stanford.edu), Faraz Abassi (faraz13@stanford.edu) and Ethan Oro (eoro@stanford.edu)

## Summary of Files

- play.py is a class intended to call simulate or allow for a user to play
- agent.py is an abstract agent class that outlines functions that each agent needs
- game.py file is intended to contain all of the relevant machinery
in order for anybody to play a game of super tic tac toe.
- random_agent.py is a random choosing agent that will choose a move with
uniform random probability given a set of possible moves
- simulate.py is a class that, given two agents, will simulate a game of
supertictactoe between two agents
- minimax.py is a file that implements a minimax agent
- minimax_alphabeta.py is a minimax agent that uses alpha-beta pruning in order to increase runtime
- learning.h5 saves the weights from the neural network model
- mcts.py is a file that implements monte carlo tree search agent
- util.py contains various utility functions used throughout the game framework
- expectimax.py is a file that implements the expectimax agent
- heurisitc.py is a file that contains all of the different heuristic functions that we use throughout various agents
- deep_q_learning.py is a file that implements a neural network model that tries to estimate the best action at each game state
- run_nn.py is a file that helps simulates a neural network's training

## Instructions

In order to run these simulations, go into play.py. In this file, you can specify (1) the agents you want to play, (2) the number of games and (3) the verbosity (1-3) for how much you would want printed out after each game.
