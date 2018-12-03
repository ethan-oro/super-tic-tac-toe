'''
    minimax.py implements a minimax agent
'''

from agent import Agent
import copy

class Expectimax(Agent):
    
    def __init__(self, depth = 3):
        self.depth = depth
    
    def start(self, state):
        # move = self.pickMove(state)
        # return move
        return (2,2)
    
    def evaluationFunction(self,state):
        return 0
    
    def pickMove(self, state):
        new_state = copy.deepcopy(state)
        utility, action = self.recurse(state, self.depth)
        return action
    
    def recurse(self, state, depth):
        print (depth)
        actions = state.get_actions()
        if (state.is_end()): #isEnd(s)?
            return (state.get_reward(), None)
        
        
        elif (depth == 0): #d=0?
            return (self.evaluationFunction(state), None)
        
        
        list = (
                ((self.recurse(new_state.update(action[0], action[1]), depth))[0], action) for action in actions)

        if (state.turn == 0): #Player(s) = agent?
            return max(list)


        
        else: #Player(s) = agent is last last?
            total = 0
            count = 0
            for reward,action in list:
                total += reward
                count++
            avg = total/count
            
            return (avg , action)
