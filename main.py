import util
import game
import agent
import human
import math

if __name__ == '__main__':

    cmd = util.get_arg(0)
    if cmd:
        player1 = util.get_arg(1)
        player2 = util.get_arg(2)
        if player1 == 'human':
            player1 = human.HumanPlayer('X')
        elif player1 == 'random':
            player1 = agent.RandomPlayer('X')
        elif player1 == 'minimax':
            player1 = agent.MinimaxPlayer('X')
        
        if player2 == 'human':
            player2 = human.HumanPlayer('O')
        elif player2 == 'random':
            player2 = agent.RandomPlayer('O')
        elif player2 == 'minimax':
            player2 = agent.MinimaxPlayer('O')
        game_state = game.Game(player1, player2)
        loser, statesVisited = game_state.play()
        print(loser, "loses")
        #Used for print formatting
        numOfRows = math.floor(math.sqrt(len(str(statesVisited[0]))))
        for i in range(numOfRows):
            for state in statesVisited:
                elements = str(state).split('|')
                print(elements[i], end = "   ")
            print("\n", end = "")
