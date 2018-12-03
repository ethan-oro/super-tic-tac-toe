'''

The heuristic functions will encapsulate the

'''

class Heuristics(game, grid):
    def __init__(self):
        self.board = grid
        self.game = game

    def calcTotValueForAgent(self, agent):
        #Loop through the board, and calculate the total value of the board for the agent
        values = [1, 2, 3]
        valueScalars = [1, 2, 3]

        totVal = 0
        for k in range(0, 3):
            for j in range(0, 3):
                for p in range(0, 3):
                    row = self.board[k*3+j].getRow(p)
                    for r in range(0, 3):
                        if row[i] == agent:
                            #k*3 + j is the board index, and r is the row number in the subgrid
                            if (k*3+j) == 4:
                                totVal += values[1-r] * valuesScalars[1-p] * valuesScalars[2]
                            else:
                                totVal += values[1-r] * valuesScalars[1-p] * valuesScalars[1 - (k*3 + j) % 3]

        return totVal

    def agentCanWinSquare(self, subGrid, subGridIndex, characterIndex, actions):
        #We want to calculate if any actions could give the player the square
        if not subGrid.is_end():
            wins = 0
            for action in actions:
                if (action[0] == subGridIndex):
                    copy = subGrid.deepCopy()
                    copy.update(characterIndex, action[1])
                    if copy.get_winner == characterIndex:
                        wins += 1
            return wins
        return 0

    #Another one would be if the agent can win the whole game
    def agentCanWin(self, agent):
        #We want to go through all the grids and see if this agent can win the whole game
        winners = [(space == agent) for space in self.grid]

        for k in range(0, 3):
            for j in range(0, 3):
                subGrid = self.board[k*3+j]
                if not subGrid.get_winner():
                    if agentCanWinSquare(subGrid, k*3+j, characterIndex, actions) > 0:
                        #See if the agent can win the whole board with this square
                        haveWon[k*3+j] == True

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
                    haveWon[k*3+j] == False
