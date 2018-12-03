'''

The heuristic functions will encapsulate the

'''

import copy

class Heuristics:
    def __init__(self, game, grid):
        self.board = grid
        self.game = game

    #agent is who you are playing as
    def calcTotValueForAgent(self, agent):
        #Loop through the board, and calculate the total value of the board for the agent
        values = [2, 1, 2, 1, 3, 1, 2, 1, 2]

        totVal = 0
        for k in range(0, 9):
            row = self.board[k]
            for j in range(0, 9):
                if row.grid[j] == agent:
                    totVal += values[j] * values[j]


            #
            #
            #
            #
            # for j in range(0, 3):
            #     for p in range(0, 3):
            #         row = self.board[k*3+j].getRow(p)
            #         for r in range(0, 3):
            #             if row[r] == agent:
            #                 #k*3 + j is the board index, and r is the row number in the subgrid
            #                 if (k*3+j) == 4:
            #                     totVal += values[1-r] * valueScalars[1-p] * valueScalars[2]
            #                 else:
            #                     totVal += values[1-r] * valueScalars[1-p] * valueScalars[1 - (k*3 + j) % 3]
            #
            #
            #                 print (k, j, p, k*3+j, r,  values[1-r] * valueScalars[1-p] * valueScalars[1 - (k*3 + j) % 3], values[1-r] * valueScalars[1-p] * valueScalars[2], agent)
        # print (totVal)
        return totVal

    def agentCanWinSquare(self, subGrid, subGridIndex, characterIndex, actions):
        #We want to calculate if any actions could give the player the square
        if not subGrid.is_end():
            wins = 0
            for action in actions:
                if (action[0] == subGridIndex):
                    new_board = copy.deepcopy(subGrid)
                    new_board.update(characterIndex, action[1])
                    if new_board.get_winner() == characterIndex:
                        wins += 1
            return wins
        return 0

    #Another one would be if the agent can win the whole game
    def agentCanWin(self, agent):
        #We want to go through all the grids and see if this agent can win the whole game
        # winners = [(space == agent) for space in self.grid]
        # winners = [ winner for winner in self.game.winners if winner == agent ]
        winners = self.game.winners
        for k in range(0, 3):
            for j in range(0, 3):
                subGrid = self.board[k*3+j]
                if not subGrid.get_winner():
                    actions = [(k*3+j, action) for action in subGrid.get_actions()]
                    if self.agentCanWinSquare(subGrid, k*3+j, agent, actions) > 0:
                        #See if the agent can win the whole board with this square
                        winners[k*3+j] = True

                    #See if the agent has won now
                    if winners[0] == winners[3] == winners[6] != ' ' : return 1000
                    if winners[1] == winners[4] == winners[7] != ' ' : return 1000
                    if winners[2] == winners[5] == winners[8] != ' ' : return 1000
                    if winners[0] == winners[1] == winners[2] != ' ' : return 1000
                    if winners[3] == winners[4] == winners[5] != ' ' : return 1000
                    if winners[6] == winners[7] == winners[8] != ' ' : return 1000
                    if winners[0] == winners[4] == winners[8] != ' ' : return 1000
                    if winners[2] == winners[4] == winners[6] != ' ' : return 1000

                    #else move on to the next board
                    winners[k*3+j] = False
        return 0
