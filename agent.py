import game
import random
from munch import Action

class RandomPlayer(game.Player):
    def choose_action(self, state):
        lstOfActions = state.actions(self.char)
        index_ = random.randint(0, len(lstOfActions)-1)
        action_taken = lstOfActions[index_]
        return action_taken
    

class MinimaxPlayer(game.Player):

    def __init__(self, char):
        super().__init__(char)
        self.opponent_char = 'O' if char == 'X' else 'X'

    def choose_action(self, state):
        return self.minimax_decision(state)

    def minimax_decision(self, state):
        best_action = None
        best_value = float('-inf')

        for action in state.actions(self.char):
            cloned_state = state.clone()
            cloned_state.execute(action) 

            value = self.min_value(cloned_state, 1)
            if value > best_value:
                best_action = action
                best_value = value

        return best_action

    def min_value(self, state, depth):
        if state.game_over():
            return self.utility(state) / depth
        
        v = float('inf')
        for action in state.actions(self.opponent_char): 
            cloned_state = state.clone()
            cloned_state.execute(action)

            v = min(v, self.max_value(cloned_state, depth + 1))
        return v

    def max_value(self, state, depth):
        if state.game_over():
            return self.utility(state) / depth
        
        v = float('-inf')
        for action in state.actions(self.char):
            cloned_state = state.clone() 
            cloned_state.execute(action)  

            v = max(v, self.min_value(cloned_state, depth + 1))
        return v

    def utility(self, state):
        if state.game_over():
            if self.char == state.loser():
                return -1
            return 1