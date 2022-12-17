import torch
import torch.nn as nn
import torch.optim as optim


from models.Net import Net
from player import Player
from ticTacToeGame import TicTacToe


def get_reward(player1, player2, winner):
    if winner == player1.marker:
        return 1
    elif winner == player2.marker:
        return -1
    else:
        return 0.1
    
def play_game(player1, player2):
    game = TicTacToe(player1, player2)
    winner = game.play()
    reward1 = get_reward(player1, player2, winner)
    reward2 = get_reward(player2, player1, winner)
    return reward1, reward2

def train(player1, player2, num_iterations):
    optimizer1 = optim.SGD(p1.model.parameters(), lr=0.01)
    optimizer2 = optim.SGD(p2.model.parameters(), lr=0.01)
    for i in range(num_iterations):
        # Play a game and get the rewards
        reward1, reward2 = play_game(player1, player2)
        # Compute the loss and gradient
        loss1 = -reward1
        loss2 = -reward2
        optimizer1.zero_grad()
        optimizer2.zero_grad()
        loss1.backward()
        loss2.backward()
        # Update the weights
        optimizer1.step()
        optimizer2.step()

if __name__ == "__main__":

    player1 = Net()
    player2 = Net()
    
    p1 = Player('X', player1)
    p2 = Player('O', player2)
    

    game = TicTacToe(p1, p2)
    train(p1, p2, num_iterations=1000)