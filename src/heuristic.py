'''

The heuristic functions will encapsulate the

'''


class Heuristics(grid):
    def __init__(self):
        self.board = grid
        self.actions = actions

    def calcTotValueForAgent(self, agent):
        #Loop through the board, and calculate the total value of the board for the agent
        values = [1, 2, 3]
        valueScalars = [1, 2, 3]

        totVal = 0
        for k in range(0, 3):
            for j in range(0, 3):
                for p in range(0, 3):
                    row = self.grid[k*3+j].getRow(p)
                    for r in range(0, 3):
                        if row[i] == agent:
                            #k*3 + j is the board index, and r is the row number in the subgrid
                            if (k*3+j) == 4:
                                totVal += values[1-r] * valuesScalars[1-p] * valuesScalars[2]
                            else:
                                totVal += values[1-r] * valuesScalars[1-p] * valuesScalars[1 - (k*3 + j) % 3]

        return totVal

    def agentCanWinSquare(self, subGrid, characterIndex, actions):
        #We want to calculate if any actions could give the player the square
        if not subGrid.is_end():
            wins = 0
            for action in actions:
                copy = subGrid.deepCopy()
                copy.update(characterIndex, action)
                if copy.is_end():
                    wins += 1
            return wins
        return 0
