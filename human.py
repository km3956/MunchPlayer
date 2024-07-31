import game

class HumanPlayer(game.Player):
    def choose_action(self, state):
        lstOfActions = state.actions(self.char)
        for i in range(len(lstOfActions)):
            print(str(i)+": ", lstOfActions[i])
        optionChosen = int(input("Please choose an action: "))
        return lstOfActions[optionChosen]
