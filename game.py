import munch

class Player():
    def __init__(self, char):
        self.char = char

    def choose_action(state):
        pass

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.state = munch.State()
    
    def play(self):
        statesVisited = []
        while not self.state.game_over():
            player1action = self.player1.choose_action(self.state)
            self.state.execute(player1action)
            print(self.state.pprint_string())
            print()
            statesVisited.append(self.state.clone())
            if not self.state.game_over():
                player2action = self.player2.choose_action(self.state)
                self.state.execute(player2action)
                print(self.state.pprint_string())
                print()
                statesVisited.append(self.state.clone())
        return (self.state.loser(), statesVisited)